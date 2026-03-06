---
id: 103
title: 'Update server.py instructions for new tools'
type: documentation
status: pending
priority: medium
phase: 1
subsystem: autonomous
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: [100, 101]
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "The server instructions string is what AI IDEs display as tool descriptions at session start"
---

# Task 103: Update server.py instructions for new tools

## Objective
Update the `instructions=` string in `docker/trent/server.py` FastMCP constructor to document `platform_docs_search` and `trent_health_report`.

## Acceptance Criteria
- [ ] `platform_docs_search` listed under a new `**Platform Documentation:**` section
- [ ] `trent_health_report` listed under a new `**Project Health:**` section
- [ ] Existing sections unchanged
- [ ] No functional code changes — instructions string only

## Implementation Notes
Find the `mcp = FastMCP(...)` block in `server.py`. Add two new sections to the `instructions=` string after `**Utilities:**`:

```
**Platform Documentation:**
- platform_docs_search - Semantic search over weekly-crawled Cursor/Claude/Gemini docs

**Project Health:**
- trent_health_report - Compute health score for a trent-managed project
```
