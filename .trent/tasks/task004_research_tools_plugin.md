---
id: 4
title: 'Create deep research tools plugin (no DuckDuckGo)'
type: task
status: pending
priority: high
phase: 0
subsystems: [mcp, research, web]
project_context: 'Integrate deep research capabilities WITHOUT DuckDuckGo - use Perplexity and Google instead'
dependencies: [2]
estimated_effort: '2 hours'
---

# Task 004: Create Deep Research Tools Plugin

## Objective
Create plugin tools for deep research using Perplexity and Google APIs. **CRITICAL: NO DuckDuckGo.**

## Sources
- `mcps/fstrent_mcp_deep_research/tools/deep_researcher.py`
- `mcps/fstrent_mcp_mediawiki/tools/deep_researcher.py` (compare, use better one)

## Tools to Create

### research_query.py
```python
@tool
async def research_query(
    query: str,
    depth: str = "standard",  # "quick", "standard", "deep"
    sources: list[str] = ["perplexity", "google"]
) -> ResearchResult:
    """Execute research query across configured sources (NO DuckDuckGo)"""
```

### research_summarize.py
```python
@tool
async def research_summarize(
    content: str,
    style: str = "concise"  # "concise", "detailed", "bullets"
) -> SummaryResult:
    """Summarize research content"""
```

### web_fetch.py
```python
@tool
async def web_fetch(
    url: str,
    extract_type: str = "text"  # "text", "html", "pdf"
) -> FetchResult:
    """Fetch and extract content from URL"""
```

## Configuration Required
```env
PERPLEXITY_API_KEY=
GOOGLE_SEARCH_API_KEY=
GOOGLE_SEARCH_ENGINE_ID=
SERPAPI_KEY=  # Optional alternative
```

## Dependencies
- `openai>=1.75.0` (for Perplexity)
- `beautifulsoup4>=4.12.0`
- `aiohttp>=3.12.15`
- `requests>=2.32.5`
- `pymupdf>=1.26.4` (PDF extraction)

## EXPLICITLY EXCLUDED
- `duckduckgo-search` - **DO NOT INCLUDE**
- Any DuckDuckGo API calls

## Acceptance Criteria
- [ ] Plugin loads via plugin_loader
- [ ] Perplexity search works
- [ ] Google search works (if API keys provided)
- [ ] URL fetching and extraction works
- [ ] NO DuckDuckGo imports or calls
- [ ] Graceful fallback if API key missing

## Notes
- Compare deep_researcher.py from both mediawiki and deep_research MCPs
- Use the better implementation as base
- Remove ALL DuckDuckGo references
