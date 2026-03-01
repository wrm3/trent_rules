---
phase: 2
name: 'Cursor Adapter'
status: completed
subsystems: [cursor_adapter, hooks, mcp_server]
task_range: '200-299'
prerequisites: [0, 1]
started_date: '2026-03-01'
completed_date: '2026-03-01'
pivoted_from: null
pivot_reason: ''
---

# Phase 2: Cursor Adapter

## Overview
First production adapter. Cursor storage is fully understood (cursor_chat_commander_ext).
End state: a real Cursor session completes → agent-complete.ps1 fires → turns appear
in PostgreSQL with LLM summaries.

## Technical Approach
- Python reads state.vscdb via sqlite3 (stdlib)
- Key lookup: composerData:{conversationId} → fullConversationHeadersOnly headers
- Per-header lookup: bubbleId:{conversationId}:{bubbleId} → message content
- Opened read-only to avoid SQLite lock conflicts with running Cursor

## Deliverables
- [ ] docker/trent/adapters/cursor_adapter.py
- [ ] Extended .cursor/hooks/agent-complete.ps1 (background HTTP call)
- [ ] Extended .cursor/hooks/session-start.ps1 (memory_context injection)
- [ ] End-to-end verification: Cursor session → PostgreSQL turns

## Acceptance Criteria
- [ ] cursor_adapter.py reads a real state.vscdb without errors
- [ ] Extracted turns have correct user/assistant roles
- [ ] agent-complete.ps1 hook exits in < 500ms (fire-and-forget)
- [ ] memory_context() output appears in session-start context injection
- [ ] Duplicate conversations not re-ingested (content hash deduplication)
