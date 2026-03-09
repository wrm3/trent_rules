"""
Firecrawl Scheduler
Weekly cron job that crawls platform docs, detects diffs, ingests to RAG, and commits snapshots.
"""

from __future__ import annotations

import argparse
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import psycopg2
import psycopg2.extras
import psycopg2.pool

from crawler import CrawlTarget, PageResult, PlatformDocsCrawler, SnapshotManager, CRAWL_TARGETS, PLATFORMS_DIR

logger = logging.getLogger(__name__)

REPO_ROOT = Path(os.environ.get("REPO_ROOT", str(Path(__file__).resolve().parent.parent.parent)))
CHANGELOG_PATH = REPO_ROOT / ".platforms" / "CHANGELOG.md"
CRAWL_STATUS_PATH = REPO_ROOT / ".platforms" / "CRAWL_STATUS.json"

DB_CONFIG = {
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": int(os.environ.get("POSTGRES_PORT", "5432")),
    "dbname": os.environ.get("POSTGRES_DB", "rag_knowledge"),
    "user": os.environ.get("POSTGRES_USER", "trent"),
    "password": os.environ.get("POSTGRES_PASSWORD", ""),
}
RAG_SUBJECT = os.environ.get("RAG_SUBJECT", "platform_docs")
GIT_AUTO_COMMIT = os.environ.get("GIT_AUTO_COMMIT", "true").lower() == "true"

# ---------------------------------------------------------------------------
# AI Model Configuration (all controlled via .env)
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "text-embedding-3-small")
EMBEDDING_DIMENSIONS = int(os.environ.get("EMBEDDING_DIMENSIONS", "1536"))
EMBEDDING_CHUNK_MAX_CHARS = int(os.environ.get("EMBEDDING_CHUNK_MAX_CHARS", "2000"))
EMBEDDING_CHUNK_OVERLAP = int(os.environ.get("EMBEDDING_CHUNK_OVERLAP", "200"))

# Retry configuration
MAX_CRAWL_ATTEMPTS = 3
RETRY_BASE_DELAY_SECONDS = 5   # doubles each attempt: 5 → 10 → 20


# ---------------------------------------------------------------------------
# RAG ingest
# ---------------------------------------------------------------------------

def get_db_connection():
    config = {**DB_CONFIG, "connect_timeout": 10, "options": "-c statement_timeout=30000"}
    return psycopg2.connect(**config)


# ---------------------------------------------------------------------------
# Crawl registry helpers
# ---------------------------------------------------------------------------

# Canonical mapping from CRAWL_TARGETS name → registry platform key
# (CRAWL_TARGETS names come from crawler.py CrawlTarget.name values)
_PLATFORM_REGISTRY_KEY: dict[str, str] = {
    "cursor":      "cursor",
    "claude_code": "claude_code",
    "gemini":      "gemini",
    # common aliases used in some CRAWL_TARGETS definitions
    "claude":      "claude_code",
    "claude-code": "claude_code",
}

REGISTRY_MAX_AGE_DAYS = int(os.environ.get("CRAWL_REGISTRY_MAX_AGE_DAYS", "30"))


def check_registry_freshness(conn, platform_name: str) -> bool:
    """
    Return True if the platform was crawled within REGISTRY_MAX_AGE_DAYS.
    Logs and returns False if the table doesn't exist (graceful degradation).
    """
    registry_key = _PLATFORM_REGISTRY_KEY.get(platform_name.lower())
    if not registry_key:
        return False  # unknown platform — don't skip, crawl it

    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute(
                """
                SELECT last_crawled_at, pages_count, crawl_status
                FROM platform_docs_crawl_registry
                WHERE platform = %s
                """,
                (registry_key,),
            )
            row = cur.fetchone()
    except Exception as e:
        logger.warning(f"Registry check failed for {platform_name}: {e} — proceeding with crawl")
        return False

    if not row or not row["last_crawled_at"] or row["crawl_status"] == "never":
        return False

    from datetime import timezone
    last = row["last_crawled_at"]
    if last.tzinfo is None:
        last = last.replace(tzinfo=timezone.utc)
    age_days = (datetime.now(timezone.utc) - last).days
    fresh = age_days <= REGISTRY_MAX_AGE_DAYS

    if fresh:
        logger.info(
            f"  REGISTRY: {platform_name} is fresh ({age_days}d old, "
            f"threshold={REGISTRY_MAX_AGE_DAYS}d, pages={row['pages_count']}) — skipping crawl"
        )
    return fresh


def update_registry_after_crawl(conn, platform_name: str, pages_count: int, status: str) -> None:
    """
    Upsert the crawl registry for a platform after a completed crawl.
    Silently skips if the table doesn't exist.
    """
    registry_key = _PLATFORM_REGISTRY_KEY.get(platform_name.lower())
    if not registry_key:
        return

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO platform_docs_crawl_registry
                    (platform, last_crawled_at, pages_count, crawl_status)
                VALUES (%s, NOW(), %s, %s)
                ON CONFLICT (platform) DO UPDATE SET
                    last_crawled_at = NOW(),
                    pages_count     = EXCLUDED.pages_count,
                    crawl_status    = EXCLUDED.crawl_status,
                    updated_at      = NOW()
                """,
                (registry_key, pages_count, status),
            )
        conn.commit()
        logger.info(f"  REGISTRY: Updated {platform_name} → {pages_count} pages, status={status}")
    except Exception as e:
        logger.warning(f"Registry update failed for {platform_name}: {e} (non-fatal)")


def rag_ingest_page(conn, page: PageResult, changed_type: str) -> None:
    """Ingest a single page to the RAG knowledge base."""
    chunks = _chunk_markdown(page.markdown)
    with conn.cursor() as cur:
        # Delete existing embeddings for this URL to avoid duplicates
        cur.execute(
            "DELETE FROM memory_captures WHERE subject = %s AND metadata->>'url' = %s",
            (RAG_SUBJECT, page.url),
        )
        for i, chunk in enumerate(chunks):
            logger.debug(f"  Embedding chunk {i+1}/{len(chunks)} for {page.url}")
            embedding = _get_embedding(chunk)
            # pgvector expects embedding as a string "[0.1,0.2,...]" — psycopg2 can't adapt a raw list
            embedding_str = "[" + ",".join(str(v) for v in embedding) + "]"
            cur.execute(
                """
                INSERT INTO memory_captures (subject, content, embedding, metadata, created_at)
                VALUES (%s, %s, %s, %s, NOW())
                """,
                (
                    RAG_SUBJECT,
                    chunk,
                    embedding_str,
                    psycopg2.extras.Json({
                        "url": page.url,
                        "title": page.title,
                        "platform": page.platform,
                        "chunk_index": i,
                        "content_hash": page.content_hash,
                        "change_type": changed_type,
                    }),
                ),
            )
    conn.commit()


def _chunk_markdown(text: str, max_chars: int = EMBEDDING_CHUNK_MAX_CHARS, overlap: int = EMBEDDING_CHUNK_OVERLAP) -> list[str]:
    """Split markdown into overlapping chunks for embedding."""
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        # Try to break on newline near the end (but only in the last 25% of the window)
        if end < len(text):
            search_from = start + (max_chars * 3 // 4)  # only look in last 25%
            newline_pos = text.rfind("\n", search_from, end)
            if newline_pos > start:
                end = newline_pos
        chunks.append(text[start:end])
        # Always advance by at least (max_chars - overlap) to prevent crawling/infinite loops
        min_advance = max(1, max_chars - overlap)
        start = start + min_advance
    return chunks


def _get_embedding(text: str) -> list[float]:
    """Generate embedding vector using the model configured in EMBEDDING_MODEL env var."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if api_key:
        import openai
        client = openai.OpenAI(api_key=api_key, timeout=30.0)
        resp = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=text[:8000],
        )
        vec = resp.data[0].embedding
        if len(vec) != EMBEDDING_DIMENSIONS:
            logger.warning(
                f"Embedding dimension mismatch: model returned {len(vec)}, "
                f"EMBEDDING_DIMENSIONS={EMBEDDING_DIMENSIONS}. Update DB schema or fix .env."
            )
        return vec
    else:
        logger.warning(
            f"No OPENAI_API_KEY set — using zero vector ({EMBEDDING_DIMENSIONS}d). Search will not work."
        )
        return [0.0] * EMBEDDING_DIMENSIONS


def crawl_with_retry(
    crawler: "PlatformDocsCrawler",
    target: "CrawlTarget",
    max_attempts: int = MAX_CRAWL_ATTEMPTS,
    base_delay: float = RETRY_BASE_DELAY_SECONDS,
) -> list["PageResult"]:
    """
    Crawl a single target with exponential backoff retry.
    Returns pages on success, empty list after all attempts fail (dead-letter).
    Delays: base, base*2, base*4, ...
    """
    for attempt in range(1, max_attempts + 1):
        try:
            pages = crawler.crawl_target(target)
            if pages:
                return pages
            # Got zero pages — could be a transient empty response, retry
            logger.warning(f"  Zero pages returned for {target.name} (attempt {attempt}/{max_attempts})")
        except Exception as e:
            logger.warning(f"  Crawl error for {target.name} attempt {attempt}/{max_attempts}: {e}")

        if attempt < max_attempts:
            delay = base_delay * (2 ** (attempt - 1))
            logger.info(f"  Retrying {target.name} in {delay:.0f}s...")
            time.sleep(delay)

    logger.error(f"  DEAD-LETTER: {target.name} failed after {max_attempts} attempts — skipping")
    return []


def write_crawl_status(
    crawl_date: str,
    pages_crawled: int,
    pages_failed: int,
    dead_letter_targets: list[str],
    status: str,
) -> None:
    """Write CRAWL_STATUS.json so trent_health_report can surface stale crawls."""
    import json

    CRAWL_STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    status_data = {
        "last_crawl_date": crawl_date,
        "pages_crawled": pages_crawled,
        "pages_failed": pages_failed,
        "dead_letter_targets": dead_letter_targets,
        "status": status,   # "success" | "partial" | "failed"
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    CRAWL_STATUS_PATH.write_text(
        json.dumps(status_data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info(f"Crawl status written: {CRAWL_STATUS_PATH} [{status}]")


# ---------------------------------------------------------------------------
# Changelog update
# ---------------------------------------------------------------------------

def update_changelog(changes: dict[str, dict[str, list[str]]], crawl_date: str) -> None:
    """Prepend a changelog entry to .platforms/CHANGELOG.md."""
    CHANGELOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    entry_lines = [f"## {crawl_date}\n"]
    total_new = sum(len(v["new"]) for v in changes.values())
    total_updated = sum(len(v["updated"]) for v in changes.values())

    if total_new == 0 and total_updated == 0:
        entry_lines.append("No changes detected in any platform docs.\n")
    else:
        for platform, diff in changes.items():
            if diff["new"] or diff["updated"]:
                entry_lines.append(f"\n### {platform}\n")
                for url in diff["new"]:
                    entry_lines.append(f"- **NEW**: {url}\n")
                for url in diff["updated"]:
                    entry_lines.append(f"- **UPDATED**: {url}\n")

    entry_lines.append("\n---\n\n")
    new_entry = "".join(entry_lines)

    if CHANGELOG_PATH.exists():
        existing = CHANGELOG_PATH.read_text(encoding="utf-8")
        # Insert after the header (first H1)
        header_end = existing.find("\n\n")
        if header_end > 0:
            updated = existing[: header_end + 2] + new_entry + existing[header_end + 2 :]
        else:
            updated = new_entry + existing
    else:
        header = "# Platform Documentation Changelog\n\nChanges detected by the weekly Firecrawl crawler.\n\n---\n\n"
        updated = header + new_entry

    CHANGELOG_PATH.write_text(updated, encoding="utf-8")
    logger.info(f"Changelog updated: {CHANGELOG_PATH}")


# ---------------------------------------------------------------------------
# Git operations
# ---------------------------------------------------------------------------

def git_commit_snapshots(crawl_date: str, changes: dict[str, dict[str, list[str]]]) -> None:
    """Commit updated snapshots and changelog to git."""
    repo_root = REPO_ROOT

    try:
        subprocess.run(["git", "add", str(PLATFORMS_DIR), str(CHANGELOG_PATH)], cwd=repo_root, check=True)

        total_new = sum(len(v["new"]) for v in changes.values())
        total_updated = sum(len(v["updated"]) for v in changes.values())
        if total_new == 0 and total_updated == 0:
            logger.info("No changes to commit")
            return

        msg = (
            f"platform-docs(update): {crawl_date} crawl\n\n"
            + "\n".join(
                f"{p}: {len(d['new'])} new, {len(d['updated'])} updated"
                for p, d in changes.items()
                if d["new"] or d["updated"]
            )
            + f"\n\nAgent: firecrawl-scheduler\nRules-Version: 5.1.0"
        )
        subprocess.run(["git", "commit", "-m", msg], cwd=repo_root, check=True)
        logger.info("Committed platform doc snapshots")

        subprocess.run(["git", "push"], cwd=repo_root, check=True)
        logger.info("Pushed to remote")
    except subprocess.CalledProcessError as e:
        logger.error(f"Git operation failed: {e}")


# ---------------------------------------------------------------------------
# Main scheduler logic
# ---------------------------------------------------------------------------

def run_crawl(diff_only: bool = False, platforms: Optional[list[str]] = None) -> None:
    crawl_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    logger.info(f"Starting platform docs crawl — {crawl_date}")

    crawler = PlatformDocsCrawler()
    snapshots = SnapshotManager(base_dir=PLATFORMS_DIR)

    # Use retry-aware crawl per target
    all_results: dict[str, list[PageResult]] = {}
    dead_letter_targets: list[str] = []

    # Open a registry connection (non-fatal if unavailable)
    registry_conn = None
    try:
        registry_conn = get_db_connection()
    except Exception as e:
        logger.warning(f"Registry DB unavailable — will crawl all platforms: {e}")

    targets_to_crawl = [t for t in CRAWL_TARGETS if not platforms or t.name in platforms]
    for target in targets_to_crawl:
        # Check registry freshness before crawling (skip if already fresh)
        if registry_conn and not diff_only:
            if check_registry_freshness(registry_conn, target.name):
                all_results[target.name] = []  # mark as skipped (not failed)
                continue

        pages = crawl_with_retry(crawler, target)
        if pages:
            all_results[target.name] = pages
        else:
            dead_letter_targets.append(target.name)
            all_results[target.name] = []

    total_pages_crawled = sum(len(p) for p in all_results.values())
    if total_pages_crawled == 0:
        logger.error(
            "ZERO pages crawled across all targets — platform knowledge base NOT updated. "
            "Check Firecrawl API key, network connectivity, and target URLs."
        )
        write_crawl_status(crawl_date, 0, len(dead_letter_targets), dead_letter_targets, "failed")
        return

    all_changes: dict[str, dict[str, list[str]]] = {}
    changed_pages: list[PageResult] = []

    for platform_name, pages in all_results.items():
        diff = snapshots.diff_summary(pages)
        all_changes[platform_name] = diff

        if not diff_only:
            for page in pages:
                changed = snapshots.save_snapshot(page)
                if changed:
                    change_type = "new" if page.url in diff["new"] else "updated"
                    changed_pages.append(page)
                    logger.info(f"  [{change_type.upper()}] {page.url}")

    total_new = sum(len(v["new"]) for v in all_changes.values())
    total_updated = sum(len(v["updated"]) for v in all_changes.values())
    logger.info(f"Crawl complete: {total_pages_crawled} pages, {total_new} new, {total_updated} updated")

    if diff_only:
        return

    pages_failed = len(dead_letter_targets)
    crawl_status = "partial" if dead_letter_targets else "success"

    if changed_pages:
        logger.info("Ingesting changed pages to RAG...")
        try:
            conn = get_db_connection()
            for page in changed_pages:
                change_type = "new" if page.url in all_changes.get(page.platform, {}).get("new", []) else "updated"
                rag_ingest_page(conn, page, change_type)
                logger.info(f"  RAG ingested: {page.url}")

            # Update the crawl registry per platform after successful ingest
            if registry_conn:
                for platform_name, pages_list in all_results.items():
                    if pages_list:  # only update platforms that were actually crawled
                        platform_status = "partial" if platform_name in dead_letter_targets else "success"
                        update_registry_after_crawl(
                            registry_conn, platform_name, len(pages_list), platform_status
                        )

            conn.close()
        except Exception as e:
            logger.error(f"RAG ingest failed (continuing): {e}")
            crawl_status = "partial"

    update_changelog(all_changes, crawl_date)
    write_crawl_status(crawl_date, total_pages_crawled, pages_failed, dead_letter_targets, crawl_status)

    if dead_letter_targets:
        logger.warning(f"Dead-letter targets (crawl failed): {dead_letter_targets}")

    if GIT_AUTO_COMMIT:
        git_commit_snapshots(crawl_date, all_changes)

    if registry_conn:
        try:
            registry_conn.close()
        except Exception:
            pass

def ingest_snapshots(platforms: Optional[list[str]] = None) -> None:
    """
    Read all existing .md snapshot files from PLATFORMS_DIR and ingest them to RAG.
    Useful for backfilling the DB after snapshots already exist on disk.
    """
    snapshots = SnapshotManager(base_dir=PLATFORMS_DIR)

    # Collect snapshot dirs: filter by platform name (target name = subdir name)
    if platforms:
        dirs_to_scan = [PLATFORMS_DIR / p for p in platforms if (PLATFORMS_DIR / p).exists()]
    else:
        dirs_to_scan = [d for d in PLATFORMS_DIR.iterdir() if d.is_dir()]

    if not dirs_to_scan:
        logger.warning(f"No snapshot dirs found under {PLATFORMS_DIR} for platforms={platforms}")
        return

    all_pages: list[PageResult] = []
    for platform_dir in dirs_to_scan:
        pages = snapshots.load_all(platform_dir)
        logger.info(f"  {platform_dir.name}: {len(pages)} snapshots found")
        all_pages.extend(pages)

    if not all_pages:
        logger.warning("No snapshots found to ingest.")
        return

    logger.info(f"Ingesting {len(all_pages)} pages to RAG (subject={RAG_SUBJECT})...")
    try:
        conn = get_db_connection()
        ingested = 0
        for page in all_pages:
            if "sitemap" in page.url.lower() or len(page.markdown.strip()) < 200:
                logger.info(f"  SKIP (low value): {page.url}")
                continue
            logger.info(f"  Ingesting: {page.url}")
            try:
                rag_ingest_page(conn, page, "backfill")
                ingested += 1
                logger.info(f"  OK ({ingested}): {page.url}")
            except Exception as e:
                logger.error(f"  FAILED: {page.url}: {e}")
                conn.rollback()
        conn.close()
        logger.info(f"Backfill ingest complete: {ingested}/{len(all_pages)} pages ingested.")
    except Exception as e:
        logger.error(f"RAG ingest failed: {e}")



def start_cron_daemon() -> None:
    """Start a blocking cron-style loop using the CRAWL_SCHEDULE env var."""
    try:
        from croniter import croniter
    except ImportError:
        logger.error("croniter not installed. pip install croniter")
        sys.exit(1)

    schedule = os.environ.get("CRAWL_SCHEDULE", "0 2 * * 0")
    logger.info(f"Starting scheduler with cron: {schedule}")

    import time as _time
    cron = croniter(schedule, datetime.now(timezone.utc))
    while True:
        next_run = cron.get_next(datetime)
        sleep_seconds = (next_run - datetime.now(timezone.utc)).total_seconds()
        logger.info(f"Next crawl at {next_run.isoformat()} (in {sleep_seconds/3600:.1f}h)")
        _time.sleep(max(0, sleep_seconds))
        try:
            run_crawl()
        except Exception as e:
            logger.error(f"Crawl failed: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    logger.info(
        f"AI Model Config — Embedding: {EMBEDDING_MODEL} ({EMBEDDING_DIMENSIONS}d), "
        f"chunk={EMBEDDING_CHUNK_MAX_CHARS}chars/overlap={EMBEDDING_CHUNK_OVERLAP}"
    )

    parser = argparse.ArgumentParser(description="Platform docs scheduler")
    parser.add_argument("--now", action="store_true", help="Run crawl immediately and exit")
    parser.add_argument("--diff-only", action="store_true", help="Show diff without saving or ingesting")
    parser.add_argument("--platform", help="Crawl specific platform only (e.g. claude-platform)")
    parser.add_argument("--daemon", action="store_true", help="Run as cron daemon (default behavior in Docker)")
    parser.add_argument("--ingest-snapshots", action="store_true", help="Ingest existing on-disk snapshots to RAG (backfill, no crawl)")
    args = parser.parse_args()

    if args.ingest_snapshots:
        ingest_snapshots(platforms=[args.platform] if args.platform else None)
    elif args.now or args.diff_only:
        run_crawl(diff_only=args.diff_only, platforms=[args.platform] if args.platform else None)
    else:
        start_cron_daemon()
