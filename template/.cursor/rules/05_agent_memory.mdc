---
description: "Gemini/Antigravity memory capture rule — call memory_capture_session before ending"
globs: []
alwaysApply: false
---

# Gemini/Antigravity Memory Capture Protocol

## Why This Rule Exists

Gemini CLI (Antigravity) stores conversations as **encrypted `.pb` files** in
`~/.gemini/antigravity/conversations/`. These files cannot be passively read.

Instead, this rule instructs the AI to **actively capture** session memory by
calling the `memory_capture_session` MCP tool before ending each session.

This is the Tier-2 (active self-reporting) path of the trent memory system.

## MANDATORY: Before Ending Any Gemini Session

**Before your final response in any Gemini/Antigravity session, you MUST:**

1. Generate a session summary covering:
   - What was accomplished
   - Key decisions made
   - Files changed
   - Problems solved

2. Call `memory_capture_session` with the summary

3. Only then provide your final response

### Tool Call Template

```
memory_capture_session(
    project_id    = <read from .trent/.project_id or derive from cwd>,
    conversation_id = <Antigravity session ID if available, else generate UUID>,
    platform      = "gemini_antigravity",
    summary       = "<2-3 paragraph summary of the session>",
    key_decisions = ["decision 1", "decision 2", ...],
    files_changed = ["path/to/file.py", "path/to/other.ts", ...],
    status        = "completed"
)
```

## Capture Triggers

Capture when ANY of these occur:
- User says "goodbye", "done", "that's all", "thanks", "exit"
- User asks to wrap up or summarize
- Session reaches token limit
- Task is fully completed
- After 10+ tool calls in a session (checkpoint capture)

## What to Include in Summary

**Do include:**
- What the user was trying to accomplish
- What was built, fixed, or changed
- Key technical decisions and their rationale
- Errors encountered and how they were resolved
- Current status (completed/partial/in-progress)

**Do NOT include:**
- Sensitive data (API keys, passwords, personal info)
- Large code blocks (reference file paths instead)
- Boilerplate or routine tool call logs

## Identity

Antigravity installation_id is available at:
`~/.gemini/antigravity/installation_id`

This should be used as `machine_id` when the trent user_config.json is
created on a Gemini/Antigravity system.

## Fallback

If `memory_capture_session` is unavailable (MCP server offline):
- Log the summary to `.trent/memory_fallback.md` with timestamp
- The next session will see this file and can ingest it manually

## Integration

This rule works alongside:
- `20_trent_tasks.md` — Task management
- `25_trent_index.md` — Session start context loading
- `00_always.md` — Response format requirements


---

---
description: "VS Code + Claude Extension memory capture rule"
globs: []
alwaysApply: false
---

# VS Code + Claude Extension Memory Capture Protocol

## Why This Rule Exists

VS Code chat sessions (via the Claude extension) are stored in VS Code's
workspace storage as JSON. The format can vary between extension versions
and the storage may not be easily accessible from outside VS Code.

This rule uses the same **Tier-2 active self-reporting** strategy as the
Gemini rule: the AI calls `memory_capture_session` before ending each session.

## MANDATORY: Before Ending Any VS Code Claude Session

**Before your final response in any VS Code session, you MUST:**

1. Generate a session summary
2. Call `memory_capture_session`
3. Then provide your final response

### Tool Call Template

```
memory_capture_session(
    project_id    = <read from .trent/.project_id or derive from workspace path>,
    conversation_id = <VS Code session ID if available, else generate UUID>,
    platform      = "vscode_claude",
    summary       = "<2-3 paragraph summary>",
    key_decisions = ["decision 1", ...],
    files_changed = ["path/to/file.ext", ...],
    status        = "completed"
)
```

## Capture Triggers (same as Gemini rule)

- User says "goodbye", "done", "that's all", "exit"
- Task fully completed
- Token limit approaching
- After 10+ tool calls (checkpoint)
- User asks for a summary

## VS Code Machine Identity

VS Code stores a stable device ID at:
`%APPDATA%\Cursor\User\globalStorage\storage.json`
Key: `telemetry.devDeviceId`

This can be used as `machine_id` in user_config.json when the Windows
MachineGuid or Antigravity installation_id are unavailable.

## Integration

This rule works alongside:
- `05_agent_memory.md` — Gemini + VS Code memory protocols (this file)
- `20_trent_tasks.md` — Task management
- `00_always.md` — Response format
