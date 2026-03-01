---
phase: 3
name: 'Claude Code Adapter'
status: completed
subsystems: [claude_adapter, hooks, mcp_server]
task_range: '300-399'
prerequisites: [0, 1, 2]
started_date: '2026-03-01'
completed_date: '2026-03-01'
pivoted_from: null
pivot_reason: ''
---

# Phase 3: Claude Code Adapter

## Overview
Claude Code stores sessions as JSONL files in ~/.claude/projects/<encoded-path>/.
This phase implements passive Tier-1 capture for Claude Code sessions.

## Technical Approach
- Path encoding: G:\trent_rules → g--trent-rules (lowercase, : \ _ → -)
- JSONL parsing: type="user" for user messages, type="assistant" with stop_reason for final responses
- Thinking blocks (type="thinking") excluded from agent_response
- File locking: JSONL files are plain text, no copy needed (unlike Cursor's SQLite)
- Stop hook: .claude/hooks/stop.sh (bash) + agent-complete.ps1 (PowerShell/Windows)

## Deliverables
- [x] .cursor/hooks/claude_adapter.py — JSONL reader + REST ingestion
- [x] .claude/hooks/stop.sh — bash stop hook for Linux/Mac
- [x] .claude/hooks/agent-complete.ps1 — updated with memory capture
- [x] .trent/.project_id — stable project identity file created
- [x] End-to-end verification: 10 turns (trent-rules), 41 turns (Maestro2)

## Acceptance Criteria
- [x] claude_adapter.py reads real JSONL without errors
- [x] Turns have correct user/assistant roles
- [x] Thinking blocks excluded from captured text
- [x] agent-complete.ps1 exits immediately (background job)
- [x] Duplicate sessions not re-ingested (content hash dedup)
- [x] .trent/.project_id used as stable project identifier
