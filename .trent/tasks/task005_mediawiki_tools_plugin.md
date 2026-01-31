---
id: 5
title: 'Create MediaWiki tools plugin'
type: task
status: pending
priority: medium
phase: 0
subsystems: [mcp, mediawiki, documentation]
project_context: 'Integrate MediaWiki page management for internal OCI VPN wiki'
dependencies: [2]
estimated_effort: '1.5 hours'
---

# Task 005: Create MediaWiki Tools Plugin

## Objective
Create plugin tools for MediaWiki page management, targeting internal wiki server on OCI VPN.

## Source
From `mcps/fstrent_mcp_mediawiki/tools/`:
- `mediawiki_api.py` - Core API wrapper

## Tools to Create

### mediawiki_get_page.py
```python
@tool
async def mediawiki_get_page(
    title: str
) -> PageResult:
    """Get MediaWiki page content by title"""
```

### mediawiki_create_page.py
```python
@tool
async def mediawiki_create_page(
    title: str,
    content: str,
    summary: str = "Created via MCP"
) -> CreateResult:
    """Create new MediaWiki page"""
```

### mediawiki_update_page.py
```python
@tool
async def mediawiki_update_page(
    title: str,
    content: str,
    summary: str = "Updated via MCP"
) -> UpdateResult:
    """Update existing MediaWiki page"""
```

### mediawiki_search.py
```python
@tool
async def mediawiki_search(
    query: str,
    limit: int = 10
) -> SearchResult:
    """Search MediaWiki pages"""
```

## Configuration Required
```env
MEDIAWIKI_URL=
MEDIAWIKI_USERNAME=
MEDIAWIKI_PASSWORD=
MEDIAWIKI_API_KEY=  # If using API key auth
```

## Dependencies
- `requests>=2.32.5`
- `beautifulsoup4>=4.12.0`

## Acceptance Criteria
- [ ] Plugin loads via plugin_loader
- [ ] Can retrieve pages by title
- [ ] Can create new pages
- [ ] Can update existing pages
- [ ] Search functionality works
- [ ] Authentication works with internal wiki

## Notes
- Wiki is internal to OCI VPN network
- May need to handle network connectivity gracefully
- Consider caching for frequently accessed pages
