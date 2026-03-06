---
id: 61
title: 'Create Firecrawl crawler.py (crawl targets: Cursor, Claude, Gemini docs)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [platform-docs]
ai_safe: false
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [60]
project_context: 'crawler.py is the core of the Firecrawl service — fetches and converts platform documentation to markdown, performs diff against last crawl, and outputs structured data for RAG ingestion'
---

# Task 061: Create Firecrawl crawler.py

## Objective
Create `template_v2/docker/firecrawl/crawler.py` — the Python script that crawls configured platform documentation sites using Firecrawl's API, computes diffs against the last crawl, and saves structured output for RAG ingestion.

## Crawl Targets (default configuration)

```yaml
# In docker/firecrawl/config.yaml
targets:
  - id: cursor
    name: "Cursor IDE"
    base_url: "https://docs.cursor.com"
    crawl_depth: 3
    include_patterns:
      - "/docs/*"
    output_dir: "crawled/cursor"
    
  - id: claude
    name: "Claude / Anthropic"
    base_url: "https://docs.anthropic.com"
    crawl_depth: 3
    output_dir: "crawled/claude"
    
  - id: claude_platform
    name: "Claude Platform (beta APIs)"
    base_url: "https://platform.claude.com/docs"
    crawl_depth: 2
    output_dir: "crawled/claude_platform"

  - id: gemini
    name: "Google Gemini API"
    base_url: "https://ai.google.dev/gemini-api/docs"
    crawl_depth: 3
    output_dir: "crawled/gemini"
```

## crawler.py Structure

```python
"""
Firecrawl Platform Documentation Crawler
Crawls platform docs sites → converts to markdown → diffs → saves for RAG ingestion
"""

from firecrawl import FirecrawlApp
import hashlib, json, os
from datetime import datetime
from pathlib import Path

class PlatformDocCrawler:
    def __init__(self, config_path: str, output_base: str):
        ...
    
    def crawl_target(self, target: dict) -> CrawlResult:
        """Crawl a single documentation target using Firecrawl API"""
        ...
    
    def compute_diff(self, target_id: str, new_content: dict) -> DiffResult:
        """Compare new crawl with previous crawl — return changed/new/removed pages"""
        ...
    
    def save_crawl(self, target_id: str, result: CrawlResult):
        """Save crawl output: markdown files + metadata + diff"""
        ...
    
    def prepare_rag_input(self, target_id: str, diff: DiffResult) -> list[dict]:
        """Convert changed pages to RAG-ready chunks"""
        ...

class CrawlResult:
    target_id: str
    crawled_at: str
    page_count: int
    pages: list[CrawlPage]  # {url, title, markdown, hash}
    
class DiffResult:
    target_id: str
    new_pages: list[str]    # URLs of new pages
    changed_pages: list[str]  # URLs of changed pages
    removed_pages: list[str]  # URLs no longer found
    unchanged_count: int
```

## Output Structure

```
docker/firecrawl/
├── crawled/
│   ├── cursor/
│   │   ├── latest/          # Current crawl markdown files
│   │   │   ├── docs_cursor_com_docs_overview.md
│   │   │   └── ...
│   │   ├── previous/        # Last crawl (for diff)
│   │   └── metadata.json    # Crawl metadata (timestamps, page hashes)
│   ├── claude/
│   └── gemini/
├── diffs/
│   └── YYYY-MM-DD/
│       ├── cursor_diff.md   # Human-readable diff summary
│       └── claude_diff.md
└── rag_pending/             # Ready for RAG ingestion
    └── YYYY-MM-DD/
        └── {target_id}_chunks.json
```

## Acceptance Criteria
- [ ] `template_v2/docker/firecrawl/crawler.py` exists
- [ ] `PlatformDocCrawler` class with 4 methods implemented
- [ ] `config.yaml` with 4 default crawl targets
- [ ] Diff logic: compares page hashes, identifies changed/new/removed
- [ ] Output structure created (crawled/, diffs/, rag_pending/)
- [ ] Firecrawl API key read from environment variable `FIRECRAWL_API_KEY`
- [ ] Error handling: if target unreachable, log and continue (don't fail whole crawl)

## Verification Steps
- [ ] File exists at correct path
- [ ] `from firecrawl import FirecrawlApp` import present
- [ ] PlatformDocCrawler class has all 4 methods
- [ ] config.yaml has 4 targets
- [ ] Output directories are created if not exist
- [ ] FIRECRAWL_API_KEY env var used (not hardcoded)

## When Stuck
- Firecrawl Python SDK: `pip install firecrawl-py`
- Firecrawl docs: https://docs.firecrawl.dev/
- Start with basic `app.crawl_url()` — don't over-engineer the diff first
- task060 (architecture) has the full design context
