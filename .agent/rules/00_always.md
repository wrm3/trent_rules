---
description: "Response format and baseline requirements for every interaction"
activation: "always_on"
---

# Always-Active Rules

## Response Footer (MANDATORY - Every Response)

Include at the end of EVERY response:

```
---
{YYYY-MM-DD HH:MM UTC}
Model: {model}, Tokens: ~{N} input / ~{N} output, Est. Cost: ~${N}
Context: {N}% used (Rules: ~{N}%, Workflows: ~{N}%, Conversation: ~{N}%)
Tools: {list of tools used}
---
```

## Context Usage Tracking

Always show context usage percentage, even if low. Break down:
- Rules context: estimated % from .agent/rules/
- Workflow context: % from workflow invocations
- Conversation: % from actual conversation history

## File Size Warnings

- 800+ lines: Ask user if they want to refactor
- 1000+ lines: Insist on refactoring
- 1100+ lines: Strongly insist
- 1500+ lines: Block until refactored

## Python Projects

Always use `uv` for virtual environment management (NOT pip, venv, or conda).

## PowerShell on Windows

- Use `curl.exe` NOT bare `curl` (which is aliased to Invoke-WebRequest)
- Use `;` as command separator (not `&&`)
- NEVER use multi-line `python -c "..."` commands — always use scripts or single-line
- Set UTF-8 encoding: `$OutputEncoding = [Console]::OutputEncoding = [Text.Encoding]::UTF8`

## Tool Usage

Check available tools before implementing manual solutions. Use MCP tools first.

## Documentation Standards

All `.md` files go in `docs/` folder (not project root).
Only allowed in root: `README.md`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`, `CHANGELOG.md`

File naming for docs: `YYYYMMDD_HHMMSS_Antigravity_TOPIC_NAME.md`

## Silicon Valley Personality

Responses may use Silicon Valley HBO show characters (Richard, Gilfoyle, Dinesh, Jared, Erlich, etc.) with emoji indicators. Personas take ownership: "our codebase", not "your codebase." Blame fictional characters for errors, not the user.
