---
id: 401
title: 'Write GEMINI.md session rule'
type: task
status: completed
priority: medium
phase: 4
subsystems: [rules]
project_context: Rule file to instruct Gemini AI to self-report session memory.
dependencies: [400]
completed_date: '2026-03-01'
---

# Task 401: Gemini Session Rule

## Delivered
Created `20_agent_memory_gemini.mdc` with:
- Mandatory capture triggers (goodbye, done, 10+ tools, token limit)
- Template for memory_capture_session call
- Summary content guidelines
- Fallback to .trent/memory_fallback.md
- Deployed to .cursor/rules/, .claude/rules/, .agent/rules/
