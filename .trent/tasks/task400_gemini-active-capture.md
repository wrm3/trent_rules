---
id: 400
title: 'Gemini/Antigravity active MCP capture — rule + identity'
type: task
status: completed
priority: medium
phase: 4
subsystems: [memory_capture_session, rules]
project_context: >
  Gemini/Antigravity encrypts conversation files (.pb). Passive reading is
  impossible. Solution: AI self-reports via memory_capture_session MCP tool.
dependencies: [103]
completed_date: '2026-03-01'
---

# Task 400: Gemini Active Capture

## Deliverables
- `.cursor/rules/20_agent_memory_gemini.mdc` — instructs AI to call memory_capture_session
- `.claude/rules/20_agent_memory_gemini.md` — same rule for Claude Code
- `.agent/rules/20_agent_memory_gemini.md` — same rule for other agents
- Updated `_get_machine_id()` in both adapters to check Antigravity installation_id

## Antigravity identity
- `installation_id` found at `~/.gemini/antigravity/installation_id`
- Value: 4bedca94-6e04-448a-9c8d-fe221fdc7302
- Now used as machine_id fallback across all adapters

## Rule Content
The rule instructs Gemini sessions to:
1. Call memory_capture_session before ending any session
2. Include summary, key_decisions, files_changed
3. Fall back to .trent/memory_fallback.md if MCP unavailable
