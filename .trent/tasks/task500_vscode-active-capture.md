---
id: 500
title: 'VS Code + Claude Extension active capture rule'
type: task
status: completed
priority: medium
phase: 5
subsystems: [memory_capture_session, rules, claude_adapter]
project_context: >
  VS Code Claude extension uses Tier-2 active capture. Rule deployed to all IDEs.
  VS Code devDeviceId added to machine_id detection chain.
dependencies: [103]
completed_date: '2026-03-01'
---

# Task 500: VS Code Active Capture

## Deliverables
- `20_agent_memory_vscode.mdc` deployed to .cursor/rules/, .claude/rules/, .agent/rules/
- claude_adapter.py `_get_machine_id()` checks VS Code/Cursor devDeviceId from storage.json

## VS Code identity
- Path: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- Key: `telemetry.devDeviceId`
- Fallback: `%APPDATA%\Code\User\globalStorage\storage.json`
