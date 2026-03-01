---
phase: 5
name: 'VS Code + Claude Extension Adapter'
status: planning
subsystems: [vscode_adapter, hooks]
task_range: '500-599'
prerequisites: [0, 1, 2, 3]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 5: VS Code + Claude Extension Adapter

## Overview
Fourth adapter. VS Code + Anthropic Claude extension. Storage likely follows VS Code's
globalStorage pattern (similar to Cursor since Cursor is a VS Code fork).

## Blocked On
Phase 0 Task 002: Research VS Code + Claude extension session storage.

## Hypothesis (to verify in Phase 0)
VS Code stores extension data at:
- Windows: %APPDATA%\Code\User\globalStorage\{extension-id}\
- macOS: ~/Library/Application Support/Code/User/globalStorage/{extension-id}/
- Linux: ~/.config/Code/User/globalStorage/{extension-id}/

The Claude extension ID is: anthropic.claude-ai (unverified — needs research)
If it follows Cursor's pattern, there may be a state.vscdb with similar structure.
The cursor_adapter.py may be reusable with a different path.

## Deliverables (once unblocked)
- [ ] docker/trent/adapters/vscode_adapter.py
- [ ] VS Code hook mechanism (extension event bridge or external watcher)
- [ ] End-to-end verification: VS Code Claude session → PostgreSQL turns

## Notes
VS Code extensions have an activation event system — may be able to register a
deactivation handler or use an external file watcher instead of a hook.
Will update after Phase 0 research.
