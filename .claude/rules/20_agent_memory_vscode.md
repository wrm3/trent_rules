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
- `20_agent_memory_gemini.mdc` — same approach for Gemini
- `10a_trent_tasks.mdc` — Task management
- `00_always.mdc` — Response format
