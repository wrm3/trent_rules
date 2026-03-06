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

from crawler import CrawlTarget, PageResult, PlatformDocsCrawler, SnapshotManager, CRAWL_TARGETS

logger = logging.getLogger(__name__)

PLATFORMS_DIR = Path(__file__).parent / "platforms"
CHANGELOG_PATH = Path(__file__).parent.parent.parent / ".platforms" / "CHANGELOG.md"
CRAWL_STATUS_PATH = Path(__file__).parent.parent.parent / ".platforms" / "CRAWL_STATUS.json"

DB_CONFIG = {
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": int(os.environ.get("POSTGRES_PORT", "5432")),
    "dbname": os.environ.get("POSTGRES_DB", "trent_memory"),
    "user": os.environ.get("POSTGRES_USER", "trent"),
    "password": os.environ.get("POSTGRES_PASSWORD", ""),
}
RAG_SUBJECT = os.environ.get("RAG_SUBJECT", "platform_docs")
GIT_AUTO_COMMIT = os.environ.get("GIT_AUTO_COMMIT", "true").lower() == "true"

# Retry configuration
MAX_CRAWL_ATTEMPTS = 3
RETRY_BASE_DELAY_SECONDS = 5   # doubles each attempt: 5 → 10 → 20


# ---------------------------------------------------------------------------
# RAG ingest
# ---------------------------------------------------------------------------

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)


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
            embedding = _get_embedding(chunk)
            cur.execute(
                """
                INSERT INTO memory_captures (subject, content, embedding, metadata, created_at)
                VALUES (%s, %s, %s, %s, NOW())
                """,
                (
                    RAG_SUBJECT,
                    chunk,
                    embedding,
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


def _chunk_markdown(text: str, max_chars: int = 2000, overlap: int = 200) -> list[str]:
    """Split markdown into overlapping chunks for embedding."""
    if len(text) <= max_chars:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        # Try to break on newline near the end
        if end < len(text):
            newline_pos = text.rfind("\n", start + max_chars // 2, end)
            if newline_pos > start:
                end = newline_pos
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def _get_embedding(text: str) -> list[float]:
    """Generate embedding vector. Uses OpenAI if key set, else zero vector fallback."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if api_key:
        import openai
        client = openai.OpenAI(api_key=api_key)
        resp = client.embeddings.create(model="text-embedding-3-small", input=text)
        return resp.data[0].embedding
    else:
        logger.warning("No OPENAI_API_KEY set — using zero embedding vector (search will not work)")
        return [0.0] * 1536


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
    repo_root = Path(__file__).parent.parent.parent

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
    snapshots = SnapshotManager()

    # Use retry-aware crawl per target
    all_results: dict[str, list[PageResult]] = {}
    dead_letter_targets: list[str] = []

    targets_to_crawl = [t for t in CRAWL_TARGETS if not platforms or t.name in platforms]
    for target in targets_to_crawl:
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


# ---------------------------------------------------------------------------
# Entry points: cron daemon and CLI
# ---------------------------------------------------------------------------

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

    parser = argparse.ArgumentParser(description="Platform docs scheduler")
    parser.add_argument("--now", action="store_true", help="Run crawl immediately and exit")
    parser.add_argument("--diff-only", action="store_true", help="Show diff without saving or ingesting")
    parser.add_argument("--platform", help="Crawl specific platform only")
    parser.add_argument("--daemon", action="store_true", help="Run as cron daemon (default behavior in Docker)")
    args = parser.parse_args()

    if args.now or args.diff_only:
        run_crawl(diff_only=args.diff_only, platforms=[args.platform] if args.platform else None)
    else:
        start_cron_daemon()
