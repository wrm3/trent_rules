---
id: 101
title: 'trent_health_report MCP tool'
type: feature
status: pending
priority: high
phase: 1
subsystem: autonomous
blast_radius: low
ai_safe: true
requires_solo_agent: false
claimed_by: null
claimed_at: null
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "Exposes project health scoring via the MCP server so IDEs can query task status without reading the file system directly"
---

# Task 101: trent_health_report MCP tool

## Objective
Create a `trent_health_report` MCP plugin that computes a project's Phase 0 / overall health score by reading `.trent/TASKS.md` and `.trent/tasks/` files in a target directory.

## Acceptance Criteria
- [ ] Plugin file: `docker/trent/tools/plugins/trent_health_report.py`
- [ ] Follows standard plugin pattern (`TOOL_NAME`, `TOOL_DESCRIPTION`, `TOOL_PARAMS`, `setup()`, `execute()`)
- [ ] Accepts `target_path` parameter (the project to report on)
- [ ] Returns: overall health score (0-100), per-subsystem breakdown, stale claims count, blocked tasks list
- [ ] Gracefully handles missing `.trent/` directory
- [ ] Server instructions updated (Task 103)

## Implementation Notes
Read `.trent/TASKS.md` at the target path. Count tasks by status indicator (`[✅]`, `[🔄]`, `[📋]`, `[ ]`, `[❌]`). Compute score:
```
score = (completed / total_non_cancelled) * 100
```
Parse per-subsystem from `### Subsystem:` headers in TASKS.md.
Check `.trent/tasks/` for YAML `claimed_at` + `claim_ttl_minutes` to detect stale claims.

Return structure:
```python
{
  "success": True,
  "project": target_path,
  "overall_health": 72,
  "status": "degraded",   # healthy>=80, degraded 50-79, critical<50
  "task_counts": {"completed": 45, "in_progress": 2, "pending": 8, "failed": 1, "total": 56},
  "subsystems": [
    {"name": "template-core", "completed": 14, "total": 14, "health": 100},
  ],
  "stale_claims": [],
  "blocked_tasks": []
}
```

## Verification
- Call with a real project path and verify counts match TASKS.md
- Call with missing path → should return `{"success": False, "error": "..."}`
