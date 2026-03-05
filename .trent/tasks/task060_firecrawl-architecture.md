---
id: 60
title: 'Design Firecrawl Docker Service Architecture'
type: feature
status: pending
priority: high
phase: 0
subsystem: platform-docs
ai_safe: true
requires_solo_agent: false
blast_radius: low
blast_radius_reason: "Creates new docker service — does not modify existing docker services"
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: true
estimated_duration_minutes: 60
claim_ttl_minutes: 120
dependencies: [1]
spec_dependencies:
  - name: firecrawl-py
    pinned_version: "latest"
    last_verified: "2026-03-05"
    reference_url: "https://github.com/mendableai/firecrawl"
---

# Task 060: Design Firecrawl Docker Service Architecture

## Objective
Design and document the complete Firecrawl Docker service that will automatically crawl
platform documentation sites weekly, commit changes to `.platforms/`, and ingest updated
pages into the pgvector RAG system. This is the architecture/design task — implementation
is Tasks 061-065.

## Background
From `potential_changes.md` Part 6: The `.platforms/` folder is currently a manually-maintained
dead snapshot. Platform docs (Cursor, Claude, Gemini) change weekly. Firecrawl is an open-source
tool that crawls docs sites and converts to clean markdown. Combined with the existing RAG
system (pgvector), agents can query current platform docs via MCP tool.

Key insight: agents are blind to adjacent docs pages. Given one URL, they don't know about
related pages. Crawling the full site solves this structurally.

## Acceptance Criteria
- [ ] Architecture diagram documented (ASCII or mermaid) showing data flow
- [ ] Crawl targets defined with base URLs and scope
- [ ] Output structure defined (.platforms/cursor/YYYY-MM-DD/, etc.)
- [ ] Diff strategy defined (how to detect changes from last crawl)
- [ ] RAG ingestion pipeline defined (which subject/namespace in pgvector)
- [ ] CHANGELOG.md format defined for .platforms/
- [ ] Docker service spec defined (service name, resource limits, volume mounts)
- [ ] Schedule defined (weekly, specific day/time, configurable)
- [ ] Fallback behavior defined (if crawl fails, keep last known good)
- [ ] New MCP tool interface defined: platform_docs_search(query, platform, limit)
- [ ] Design document saved to `template_v2/docs/FIRECRAWL_ARCHITECTURE.md`
- [ ] Git commit: `docs(template-v2): firecrawl architecture design`

## Architecture Design

### Data Flow
```
Weekly cron (Sunday 02:00 UTC):
  firecrawl crawler.py
    → crawl https://docs.cursor.com/
    → crawl https://platform.claude.com/docs/
    → crawl https://ai.google.dev/gemini-api/docs/
    → crawl https://docs.anthropic.com/en/
    ↓
  For each crawled page:
    → Compare to .platforms/{platform}/latest/{path}.md
    → If changed: write to .platforms/{platform}/YYYY-MM-DD/{path}.md
    → Collect list of changed pages
    ↓
  diff_and_commit.py
    → Git add changed pages
    → Update .platforms/{platform}/latest/ symlinks (or copies)
    → Write .platforms/CHANGELOG.md entry
    → Git commit: "docs(platforms): weekly crawl YYYY-MM-DD — N pages updated"
    ↓
  rag_ingest.py
    → For each changed page: rag_ingest_text(content, subject="platform-docs-{platform}")
    → Log ingestion results
```

### Crawl Targets
| Platform | Base URL | Scope | Subject |
|----------|----------|-------|---------|
| cursor | https://docs.cursor.com/ | full | platform-docs-cursor |
| claude | https://platform.claude.com/docs/ | full | platform-docs-claude |
| claude-api | https://docs.anthropic.com/en/ | full | platform-docs-anthropic |
| gemini | https://ai.google.dev/gemini-api/docs/ | full | platform-docs-gemini |

### Docker Service Spec
```yaml
# In docker-compose.yml additions:
firecrawl-crawler:
  build: ./docker/firecrawl
  volumes:
    - ./.platforms:/app/platforms
    - ./:/app/repo  # for git operations
  environment:
    - CRAWL_SCHEDULE=0 2 * * 0  # Sunday 02:00 UTC
    - GIT_USER_EMAIL=agent@trent.local
    - GIT_USER_NAME=firecrawl-agent
  depends_on:
    - trent  # needs RAG MCP tools
```

### MCP Tool Interface
```python
def platform_docs_search(
    query: str,
    platform: str = None,  # "cursor" | "claude" | "gemini" | None (all)
    limit: int = 5
) -> list[dict]:
    """
    Search current platform documentation using semantic search.
    Returns relevant pages with title, url, content excerpt, last_updated.
    """
```

## When Stuck
### If firecrawl-py API is unclear:
Check https://github.com/mendableai/firecrawl for Python SDK docs.
allow_spec_update is true — update this spec if the API differs from design.
### Escalation trigger:
If the RAG pgvector system can't handle the volume of platform docs, escalate —
we may need a separate pgvector collection or chunking strategy.
