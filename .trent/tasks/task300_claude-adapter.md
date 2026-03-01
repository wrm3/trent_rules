---
id: 300
title: 'Implement claude_adapter.py (~/.claude/projects/*.jsonl reader)'
type: task
status: in-progress
priority: high
phase: 3
subsystems: [claude_adapter, memory_rest]
project_context: >
  Claude Code stores sessions as JSONL files in ~/.claude/projects/<encoded-path>/.
  This adapter reads those files and ingests them to the memory system.
dependencies: [108]
---

# Task 300: Claude Code Adapter

## Objective
Parse Claude Code JSONL session files and POST turns to /memory/ingest.

## JSONL Format
- type="user": user message, message.content[{type:"text"}]
- type="assistant" with stop_reason set: final assistant message
- type="progress": intermediate streaming chunks (SKIP)
- Thinking blocks (type="thinking") must be excluded from agent_response text

## Path Mapping
G:\trent_rules → g--trent-rules (lowercase drive, : and \ and _ → -)

## Acceptance Criteria
- [ ] Finds project dir without hardcoded paths
- [ ] Reads most recent JSONL (or specific session_id)
- [ ] Extracts user/assistant turn pairs correctly
- [ ] Skips thinking blocks in assistant content
- [ ] POSTs to /memory/ingest successfully
- [ ] Deduplication works (content hash)
