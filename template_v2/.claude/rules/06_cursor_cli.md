# Cursor CLI Quick Reference

Cursor CLI (`agent` command) — terminal-based AI coding. Docs: https://cursor.com/docs/cli/overview

## Commands
```bash
agent                          # Interactive session
agent "prompt here"            # With initial prompt
agent --mode=plan "prompt"     # Plan mode (no code changes)
agent --mode=ask "prompt"      # Ask mode (read-only)
agent -p "prompt" --output-format json  # Non-interactive (CI/CD)
agent ls                       # List conversations
agent resume                   # Resume last conversation
```

## Modes
- **Agent** (default): Full tool access — implementation, refactoring, fixes
- **Plan** (`Shift+Tab`): Design approach before coding
- **Ask**: Read-only exploration
- **Debug** (`/debug`): Hypothesis generation

## Key Shortcuts
`Shift+Tab` rotate modes | `Shift+Enter` newline | `Ctrl+R` review | `Ctrl+D` x2 exit

## Cloud Agent
Prepend `&` to hand off long tasks: `& implement auth module with tests`

## Windows Note
Use `;` not `&&` for chaining. Set UTF-8 encoding before running.
