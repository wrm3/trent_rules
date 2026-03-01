---
phase: 0
name: 'Research & Foundation'
status: completed
subsystems: [research, identity, database]
task_range: '1-99'
prerequisites: []
started_date: '2026-03-01'
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 0: Research & Foundation

## Overview
Confirm all platform-specific unknowns before writing production code. The goal is zero guesses
entering Phase 1. Every technical question that could invalidate an architectural decision
must be answered here.

## Objectives
- Determine where Gemini CLI stores session files (path, format, schema)
- Determine where VS Code + Claude extension stores session data
- Finalize the user_config.json spec (fields, generation, storage path)
- Finalize project_uuid format and injection into .trent/
- Write and review the complete PostgreSQL schema for agent memory

## Key Research Questions

| # | Question | Answers Phase 0? | Unblocks |
|---|----------|-----------------|----------|
| 1 | Where does Gemini CLI write session files? | Task 001 | Tasks 400-403 |
| 2 | Does VS Code + Claude ext use globalStorage like Cursor? | Task 002 | Tasks 500-503 |
| 3 | What fields does user_config.json need? | Task 003 | Tasks 600-601 |
| 4 | How do we inject project_uuid without breaking existing .trent/ format? | Task 004 | Tasks 600+ |
| 5 | What indexes does the memory schema need for performance? | Task 005 | Tasks 100+ |

## Deliverables
- [ ] Research notes in docs/ for Gemini and VS Code storage
- [ ] `~/.trent/user_config.json` spec (fields, defaults, generation)
- [ ] project_uuid placement decision documented
- [ ] `docker/init_db/05_agent_memory.sql` written and reviewed

## Acceptance Criteria
- [ ] Can query Gemini CLI session file with Python (or confirmed unavailable)
- [ ] Can query VS Code + Claude ext storage with Python (or confirmed unavailable)
- [ ] user_config.json spec reviewed and approved
- [ ] 05_agent_memory.sql reviewed and approved
- [ ] No open architecture questions blocking Phase 1

## Notes
- Cursor storage: FULLY SOLVED by cursor_chat_commander_ext project
  - Path: %APPDATA%\Cursor\User\globalStorage\state.vscdb
  - Table: cursorDiskKV
  - Keys: composerData:{id} + bubbleId:{composerId}:{bubbleId}
- Claude Code storage: SOLVED by OneContext/Aline project
  - Path: ~/.claude/projects/{hash}/*.jsonl
  - Format: JSONL, one object per turn
- Two unknowns remaining: Gemini CLI, VS Code + Claude extension
