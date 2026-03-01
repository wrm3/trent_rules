---
phase: 5
name: 'VS Code + Claude Extension Adapter'
status: completed
subsystems: [memory_capture_session, rules, claude_adapter]
task_range: '500-599'
prerequisites: [0, 1, 2, 3, 4]
started_date: '2026-03-01'
completed_date: '2026-03-01'
pivoted_from: null
pivot_reason: ''
---

# Phase 5: VS Code + Claude Extension Adapter

## Overview
VS Code chat sessions (Claude extension) use Tier-2 active self-reporting.
The rule `20_agent_memory_vscode.mdc` instructs the AI to call
`memory_capture_session` before ending sessions.

## Technical Approach
- Active Tier-2: AI calls memory_capture_session
- VS Code devDeviceId added as machine_id source
- Rule deployed to all IDE directories

## Identity
VS Code/Cursor `%APPDATA%\Cursor\User\globalStorage\storage.json`:
- `telemetry.devDeviceId`: 87869a1d-24a1-4ebf-a9e9-f00a0d491951

## Deliverables
- [x] `20_agent_memory_vscode.mdc` → deployed to all rule dirs
- [x] claude_adapter.py: devDeviceId added to machine_id detection chain
- [x] Rule defines capture triggers (same pattern as Gemini)
