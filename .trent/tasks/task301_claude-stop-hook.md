---
id: 301
title: 'Create Claude Code stop hook'
type: task
status: completed
priority: high
phase: 3
subsystems: [claude_adapter, hooks]
project_context: >
  Claude Code fires a Stop hook when a session ends. This hook calls
  claude_adapter.py to ingest the session into trent memory.
dependencies: [300]
completed_date: '2026-03-01'
---

# Task 301: Claude Code Stop Hook

## Deliverables
- `.claude/hooks/stop.sh` — cross-platform bash script (Linux/Mac)
- `.claude/hooks/agent-complete.ps1` — updated with memory capture (Windows)

## Implementation
Both hooks call claude_adapter.py in background mode so Claude Code proceeds
immediately without waiting for ingestion.

The hooks.json already had stop hooked to agent-complete.ps1; we extended it
with the memory capture block following the same pattern as Cursor's hook.
