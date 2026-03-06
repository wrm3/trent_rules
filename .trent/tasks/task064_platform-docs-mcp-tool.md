---
id: 64
title: 'Create platform_docs_search MCP tool (semantic search over crawled docs)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [platform-docs]
ai_safe: false
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [61, 62, 100]
project_context: 'The platform_docs_search MCP tool gives agents semantic search over all crawled platform documentation — instead of relying on training data cutoffs, agents query the live crawled docs'
---

# Task 064: Create platform_docs_search MCP tool

## Objective
Create the `platform_docs_search` MCP tool in `template_v2/docker/trent/tools/plugins/` — a FastMCP tool that provides semantic search over all platform documentation ingested by the Firecrawl service.

## Tool Interface

```python
@mcp.tool()
async def platform_docs_search(
    query: str,
    platform: str = "all",
    limit: int = 5,
    include_url: bool = True,
) -> str:
    """
    Search platform documentation (Cursor, Claude, Gemini) for current information.
    
    Use this tool when you need current documentation about:
    - Cursor IDE features, APIs, or configuration
    - Claude/Anthropic API, models, or capabilities  
    - Gemini API, models, or capabilities
    - Any platform that may have changed since training cutoff
    
    Args:
        query: What you want to know about the platform
        platform: Filter by platform - "cursor", "claude", "gemini", "all" (default: "all")
        limit: Maximum number of results to return (default: 5)
        include_url: Include source URL in results (default: True)
    
    Returns:
        Relevant documentation excerpts with source URLs
    
    Example:
        platform_docs_search("cursor agent commands", platform="cursor")
        platform_docs_search("claude tool use beta", platform="claude")
    """
    ...
```

## Implementation

```python
async def platform_docs_search(query, platform="all", limit=5, include_url=True):
    # Map platform to RAG subjects
    subject_map = {
        "cursor": "platform_docs_cursor",
        "claude": "platform_docs_claude",
        "gemini": "platform_docs_gemini", 
        "all": None  # Search across all platform_docs_* subjects
    }
    
    subject = subject_map.get(platform)
    
    # Query RAG with subject filter
    results = await rag_search(
        query=query,
        subject_prefix="platform_docs_" if not subject else subject,
        limit=limit
    )
    
    if not results:
        return f"No documentation found for '{query}' in {platform} docs. The docs may not have been crawled yet."
    
    output = f"## Platform Documentation: {query}\n\n"
    for i, result in enumerate(results, 1):
        output += f"### Result {i}: {result['title']}\n"
        if include_url:
            output += f"**Source**: {result['url']}\n"
        output += f"**Platform**: {result['platform']}\n\n"
        output += result['content'] + "\n\n---\n\n"
    
    return output
```

## Acceptance Criteria
- [ ] `platform_docs_search` tool created in template_v2 plugin directory
- [ ] Query, platform, limit, include_url parameters
- [ ] Platform filter maps to correct RAG subjects
- [ ] Clear error message when no results found
- [ ] Docstring explains when to use this tool (replaces stale training data)
- [ ] Tool registered in server.py tool list

## Verification Steps
- [ ] Tool file exists in plugin directory
- [ ] @mcp.tool() decorator present
- [ ] All 4 parameters defined
- [ ] subject_map covers all 4 platform options
- [ ] Error case handled (no results)

## When Stuck
- Look at existing rag_search tool in `docker/trent/tools/plugins/` for pattern
- task100 (Phase 1) adds this to the live docker — this task creates the template_v2 version
- If RAG isn't running, tool should return a helpful error, not crash
