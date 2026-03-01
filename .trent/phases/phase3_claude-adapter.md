---
phase: 3
name: 'Claude Code Adapter'
status: planning
subsystems: [claude_adapter, hooks]
task_range: '300-399'
prerequisites: [0, 1, 2]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 3: Claude Code Adapter

## Overview
Second adapter. Claude Code stores JSONL files at ~/.claude/projects/{hash}/*.jsonl.
OneContext/Aline fully documented this format. End state: Claude Code session → stop hook
fires → turns in PostgreSQL.

## Technical Approach
- Claude Code stop hook: ~/.claude/hooks/ (shell script, cross-platform)
- JSONL parsing: one JSON object per line, type field distinguishes user/assistant
- Hook provides session file path directly (no discovery needed)

## Reference
- OneContext stop_hook.py: G:\git_memory\onecontext-versions\datar-fork\python\realign\claude_hooks\stop_hook.py
- Claude Code hook docs: https://docs.anthropic.com/claude-code/hooks

## Deliverables
- [ ] docker/trent/adapters/claude_adapter.py
- [ ] ~/.claude/hooks/stop_hook (shell, cross-platform)
- [ ] End-to-end verification: Claude Code session → PostgreSQL turns

## Acceptance Criteria
- [ ] claude_adapter.py parses a real .jsonl session file
- [ ] Stop hook exits < 200ms (lightweight, enqueue-and-exit pattern)
- [ ] Cross-platform: works on Windows (PowerShell) and macOS/Linux (bash)
