"""
Firecrawl Platform Documentation Crawler
Crawls Cursor, Claude, and Gemini docs and saves them as markdown snapshots.
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import requests

logger = logging.getLogger(__name__)

PLATFORMS_DIR = Path(os.environ.get("PLATFORMS_DIR", str(Path(__file__).parent / "platforms")))

# ---------------------------------------------------------------------------
# Crawl target definitions
# ---------------------------------------------------------------------------

@dataclass
class CrawlTarget:
    name: str
    base_url: str
    platform_dir: str
    max_pages: int = 500
    exclude_patterns: list[str] = field(default_factory=list)
    include_patterns: list[str] = field(default_factory=list)
    sitemap: str = "include"  # v2: "include" | "skip" | "only"
    max_discovery_depth: Optional[int] = None  # v2: 1 = start URL + links on that page; None = API default
    crawl_entire_domain: bool = False  # v2: if True, follow sibling/parent links, not just deeper paths


CRAWL_TARGETS: list[CrawlTarget] = [
    # -----------------------------------------------------------------------
    # Cursor IDE docs  →  saved under Cursor/docs/
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="cursor",
        base_url="https://cursor.com/en-US/docs",
        platform_dir="Cursor/docs",
        max_pages=300,
        exclude_patterns=["/changelog/", "/blog/", "/es/", "/ja/", "/fr/", "/de/", "/ko/", "/zh/"],
        include_patterns=["/docs/", "/en-US/docs/"],
        sitemap="skip",           # cursor.com/llms.txt exists — link crawl is better
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    # -----------------------------------------------------------------------
    # Anthropic / Claude docs  →  all saved under Claude/
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="claude",
        base_url="https://docs.anthropic.com/en/docs",
        platform_dir="Claude/docs",
        max_pages=300,
        exclude_patterns=["/release-notes/"],
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    CrawlTarget(
        name="claude-api",
        base_url="https://docs.anthropic.com/en/api",
        platform_dir="Claude/api",
        max_pages=300,
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    CrawlTarget(
        name="claude-platform",
        base_url="https://platform.claude.com/docs/en/home",
        platform_dir="Claude/platform",
        max_pages=300,
        include_patterns=["/docs/"],
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    CrawlTarget(
        name="claude-code",
        base_url="https://code.claude.com/docs/en/overview",
        platform_dir="Claude/code",
        max_pages=300,
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    # -----------------------------------------------------------------------
    # Google Gemini API docs  →  saved under Gemini/
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="gemini",
        base_url="https://ai.google.dev/gemini-api/docs",
        platform_dir="Gemini/api",
        max_pages=300,
        exclude_patterns=["/samples/"],
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    # -----------------------------------------------------------------------
    # Google Antigravity (Gemini agent IDE)  →  saved under Gemini/antigravity
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="antigravity",
        base_url="https://antigravity.google/docs/get-started",
        platform_dir="Gemini/antigravity",
        max_pages=300,
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
    # -----------------------------------------------------------------------
    # OpenAI Codex docs  →  saved under OpenAI/codex
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="openai-codex",
        base_url="https://developers.openai.com/codex/",
        platform_dir="OpenAI/codex",
        max_pages=300,
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=False,  # stay within /codex/ subtree only
        include_patterns=["/codex/"],
    ),
    # -----------------------------------------------------------------------
    # OpenCode docs
    # -----------------------------------------------------------------------
    CrawlTarget(
        name="opencode",
        base_url="https://opencode.ai/docs/",
        platform_dir="opencode",
        max_pages=300,
        sitemap="skip",
        max_discovery_depth=4,
        crawl_entire_domain=True,
    ),
]


# ---------------------------------------------------------------------------
# Page result dataclass
# ---------------------------------------------------------------------------

@dataclass
class PageResult:
    url: str
    platform: str
    title: str
    markdown: str
    content_hash: str
    metadata: dict


# ---------------------------------------------------------------------------
# Crawler
# ---------------------------------------------------------------------------

class PlatformDocsCrawler:
    """
    Crawls platform documentation using either Firecrawl.dev API (if API key set)
    or falls back to a simple requests-based scraper.
    """

    def __init__(self):
        self.api_key = os.environ.get("FIRECRAWL_API_KEY", "")
        # Use v2 API: supports sitemap "include"|"skip"|"only", better defaults, recommended over v1
        self.firecrawl_base = "https://api.firecrawl.dev/v2"
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "trent-docs-crawler/1.0"})

    def crawl_target(self, target: CrawlTarget) -> list[PageResult]:
        """Crawl a single target. Uses Firecrawl API if key available, else basic scraper."""
        if self.api_key:
            return self._crawl_with_firecrawl(target)
        else:
            return self._crawl_basic(target)

    def crawl_all(self, targets: Optional[list[str]] = None) -> dict[str, list[PageResult]]:
        """Crawl all configured targets. Filter by name if targets list provided."""
        results: dict[str, list[PageResult]] = {}
        crawl_list = [t for t in CRAWL_TARGETS if targets is None or t.name in targets]
        for target in crawl_list:
            logger.info(f"Crawling {target.name} ({target.base_url})...")
            try:
                pages = self.crawl_target(target)
                results[target.name] = pages
                logger.info(f"  {len(pages)} pages retrieved from {target.name}")
            except Exception as e:
                logger.error(f"  FAILED to crawl {target.name}: {e}")
                results[target.name] = []
        return results

    # ------------------------------------------------------------------
    # Firecrawl API path
    # ------------------------------------------------------------------

    def _crawl_with_firecrawl(self, target: CrawlTarget) -> list[PageResult]:
        """Use Firecrawl.dev API for high-quality markdown extraction."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "url": target.base_url,
            "limit": target.max_pages,
            "scrapeOptions": {"formats": ["markdown"]},
            "sitemap": target.sitemap,  # v2: "include" | "skip" | "only"
        }
        if target.max_discovery_depth is not None:
            payload["maxDiscoveryDepth"] = target.max_discovery_depth
        if target.crawl_entire_domain:
            payload["crawlEntireDomain"] = True
        if target.exclude_patterns:
            payload["excludePaths"] = target.exclude_patterns
        if target.include_patterns:
            payload["includePaths"] = target.include_patterns

        resp = self.session.post(f"{self.firecrawl_base}/crawl", headers=headers, json=payload, timeout=30)
        resp.raise_for_status()

        job_id = resp.json().get("id")
        if not job_id:
            raise ValueError(f"Firecrawl returned no job ID: {resp.text}")

        return self._poll_firecrawl_job(job_id, target, headers)

    def _poll_firecrawl_job(self, job_id: str, target: CrawlTarget, headers: dict) -> list[PageResult]:
        """Poll Firecrawl for job completion, return pages when done."""
        max_polls = 120
        for attempt in range(max_polls):
            resp = self.session.get(f"{self.firecrawl_base}/crawl/{job_id}", headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            status = data.get("status", "unknown")
            logger.debug(f"  Job {job_id}: {status} ({attempt+1}/{max_polls})")

            if status == "completed":
                return self._parse_firecrawl_response(data, target)
            elif status == "failed":
                raise RuntimeError(f"Firecrawl job {job_id} failed: {data.get('error')}")

            time.sleep(10)

        raise TimeoutError(f"Firecrawl job {job_id} did not complete after {max_polls} polls")

    def _parse_firecrawl_response(self, data: dict, target: CrawlTarget) -> list[PageResult]:
        pages = []
        for item in data.get("data", []):
            markdown = item.get("markdown", "")
            url = item.get("metadata", {}).get("url", "")
            title = item.get("metadata", {}).get("title", url)
            if not markdown:
                continue
            pages.append(PageResult(
                url=url,
                platform=target.name,
                title=title,
                markdown=markdown,
                content_hash=hashlib.sha256(markdown.encode()).hexdigest()[:12],
                metadata=item.get("metadata", {}),
            ))
        return pages

    # ------------------------------------------------------------------
    # Basic fallback scraper (no Firecrawl API key required)
    # ------------------------------------------------------------------

    def _crawl_basic(self, target: CrawlTarget) -> list[PageResult]:
        """
        Simple fallback: fetch the base URL and extract visible text as pseudo-markdown.
        Not as clean as Firecrawl but works without an API key.
        """
        try:
            from html.parser import HTMLParser

            class TextExtractor(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.text_parts: list[str] = []
                    self._skip_tags = {"script", "style", "nav", "footer"}
                    self._current_skip = 0

                def handle_starttag(self, tag, attrs):
                    if tag in self._skip_tags:
                        self._current_skip += 1

                def handle_endtag(self, tag):
                    if tag in self._skip_tags and self._current_skip > 0:
                        self._current_skip -= 1

                def handle_data(self, data):
                    if self._current_skip == 0:
                        stripped = data.strip()
                        if stripped:
                            self.text_parts.append(stripped)

            resp = self.session.get(target.base_url, timeout=20)
            resp.raise_for_status()
            extractor = TextExtractor()
            extractor.feed(resp.text)
            markdown = "\n\n".join(extractor.text_parts)
            return [PageResult(
                url=target.base_url,
                platform=target.name,
                title=f"{target.name} docs (basic crawl)",
                markdown=markdown,
                content_hash=hashlib.sha256(markdown.encode()).hexdigest()[:12],
                metadata={"url": target.base_url, "crawl_method": "basic"},
            )]
        except Exception as e:
            logger.warning(f"Basic crawl failed for {target.name}: {e}")
            return []


# ---------------------------------------------------------------------------
# Snapshot manager
# ---------------------------------------------------------------------------

class SnapshotManager:
    """
    Persists page snapshots to disk under platforms/ and detects changes.
    Each page is stored as a .md file with a JSON sidecar for metadata.
    """

    def __init__(self, base_dir: Path = PLATFORMS_DIR):
        self.base_dir = base_dir

    def _page_path(self, platform: str, url: str) -> Path:
        safe_name = url.replace("https://", "").replace("/", "_").replace("?", "_")[:200]
        return self.base_dir / platform / f"{safe_name}.md"

    def _meta_path(self, page_path: Path) -> Path:
        return page_path.with_suffix(".json")

    def load_snapshot(self, platform: str, url: str) -> Optional[PageResult]:
        path = self._page_path(platform, url)
        if not path.exists():
            return None
        meta_path = self._meta_path(path)
        metadata = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
        markdown = path.read_text(encoding="utf-8")
        return PageResult(
            url=url,
            platform=platform,
            title=metadata.get("title", ""),
            markdown=markdown,
            content_hash=hashlib.sha256(markdown.encode()).hexdigest()[:12],
            metadata=metadata,
        )

    def save_snapshot(self, page: PageResult) -> bool:
        """Save page. Returns True if content changed (or is new)."""
        path = self._page_path(page.platform, page.url)
        path.parent.mkdir(parents=True, exist_ok=True)

        existing = self.load_snapshot(page.platform, page.url)
        if existing and existing.content_hash == page.content_hash:
            return False  # unchanged

        path.write_text(page.markdown, encoding="utf-8")
        self._meta_path(path).write_text(
            json.dumps({
                "url": page.url,
                "title": page.title,
                "content_hash": page.content_hash,
                **page.metadata,
            }, indent=2),
            encoding="utf-8",
        )
        return True  # changed

    def diff_summary(self, new_pages: list[PageResult]) -> dict[str, list[str]]:
        """Return dict with 'new', 'updated', 'unchanged' URL lists."""
        result: dict[str, list[str]] = {"new": [], "updated": [], "unchanged": []}
        for page in new_pages:
            existing = self.load_snapshot(page.platform, page.url)
            if existing is None:
                result["new"].append(page.url)
            elif existing.content_hash != page.content_hash:
                result["updated"].append(page.url)
            else:
                result["unchanged"].append(page.url)
        return result

    def load_all(self, platform_dir: Path) -> list[PageResult]:
        """Load all .md snapshots from a platform directory (for backfill ingest).
        Uses rglob to support nested subdirectories (e.g. Claude/docs/, Claude/api/)."""
        pages = []
        if not platform_dir.exists():
            return pages
        for md_path in sorted(platform_dir.rglob("*.md")):
            meta_path = md_path.with_suffix(".json")
            try:
                markdown = md_path.read_text(encoding="utf-8")
                metadata = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
                url = metadata.get("url", str(md_path))
                title = metadata.get("title", md_path.stem)
                pages.append(PageResult(
                    url=url,
                    platform=platform_dir.name,
                    title=title,
                    markdown=markdown,
                    content_hash=hashlib.sha256(markdown.encode()).hexdigest()[:12],
                    metadata=metadata,
                ))
            except Exception as e:
                logger.warning(f"  Could not load snapshot {md_path}: {e}")
        return pages


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    parser = argparse.ArgumentParser(description="Crawl platform docs")
    parser.add_argument("--platform", help="Platform name to crawl (default: all)")
    parser.add_argument("--diff-only", action="store_true", help="Show diff without saving")
    args = parser.parse_args()

    crawler = PlatformDocsCrawler()
    snapshots = SnapshotManager()

    platforms = [args.platform] if args.platform else None
    all_results = crawler.crawl_all(targets=platforms)

    for platform_name, pages in all_results.items():
        diff = snapshots.diff_summary(pages)
        print(f"\n{platform_name}: {len(diff['new'])} new, {len(diff['updated'])} updated, {len(diff['unchanged'])} unchanged")
        if not args.diff_only:
            for page in pages:
                changed = snapshots.save_snapshot(page)
                if changed:
                    print(f"  SAVED: {page.url}")
