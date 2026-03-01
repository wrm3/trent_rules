---
phase: 6
name: 'trent_install Integration'
status: completed
subsystems: [trent_install, hooks, rules]
task_range: '600-699'
prerequisites: [0, 1, 2, 3, 4, 5]
started_date: '2026-03-01'
completed_date: '2026-03-01'
pivoted_from: null
pivot_reason: ''
---

# Phase 6: trent_install Integration

## Overview
Ensure the memory system is automatically deployed when `trent_install` runs
on a new project.

## What Was Already in Place
The hook files, rules, and adapters are already part of the existing manifests:
- `.cursor/hooks/` → deployed by CURSOR_MANIFEST
- `.claude/hooks/` → deployed by CLAUDE_MANIFEST
- `.agent/rules/` → deployed by GEMINI_MANIFEST
- `~/.trent/user_config.json` → auto-created by adapters on first run

## New Changes
- `trent_install.py`: Phase 3 post-install step generates `.trent/.project_id`
  - Format: `proj-<name>-<hash8>` (human-readable + unique)
  - Only created if not already present (preserves existing IDs)
- AGENTS.md: 5 new memory MCP tools documented in the tools table

## Acceptance Criteria
- [x] trent_install creates .trent/.project_id on fresh installs
- [x] Existing .project_id files are never overwritten
- [x] All hooks deployed via manifest
- [x] Memory tools documented in AGENTS.md
