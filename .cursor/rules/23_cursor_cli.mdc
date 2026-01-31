# Cursor CLI Integration Guide

## Overview

Cursor CLI (`agent` command) enables AI-powered coding assistance directly from the terminal. It provides the same capabilities as the Cursor IDE agent but accessible from any terminal window.

**Documentation**: https://cursor.com/docs/cli/overview

## When to Use Cursor CLI

### Ideal Use Cases
- **Parallel Development**: Run a separate agent in a terminal while the IDE agent handles another task
- **CI/CD Pipelines**: Automated code review, linting fixes, and test generation in pipelines
- **Remote/SSH Sessions**: When working on a remote server without GUI access
- **Scripting & Automation**: Non-interactive mode for batch processing
- **Long-Running Tasks**: Hand off to Cloud Agent for tasks that take time
- **Team Collaboration**: Share conversations via Cloud Agent web interface

### When NOT to Use CLI
- When you're already in the IDE and the task is simple
- For complex multi-file refactoring where visual diff review is important
- When you need the full IDE context (open tabs, cursor position, etc.)

## CLI Commands

### Starting Sessions

```bash
# Start interactive session (default)
agent

# Start with initial prompt
agent "refactor the auth module to use JWT tokens"

# Start in specific mode
agent --mode=plan "design a caching strategy"
agent --mode=ask "how does the auth flow work?"
```

### Session Management

```bash
# List previous conversations
agent ls

# Resume most recent conversation
agent resume

# Resume specific conversation by ID
agent --resume="chat-id-here"
```

### Non-Interactive Mode (CI/Pipelines)

```bash
# Run with specific prompt
agent -p "find and fix linting issues" --output-format text

# Run with JSON output for parsing
agent -p "analyze this code for security issues" --output-format json

# Specify model
agent -p "review these changes" --model "gpt-5"
```

## CLI Modes

| Mode | Command/Shortcut | Description |
|------|-----------------|-------------|
| **Agent** | Default | Full access to all tools for complex tasks |
| **Plan** | `Shift+Tab`, `/plan`, `--mode=plan` | Design approach before coding, asks clarifying questions |
| **Ask** | `/ask`, `--mode=ask` | Read-only exploration, no file changes |
| **Debug** | `/debug` | Hypothesis generation, log instrumentation |

### Mode Selection Guidelines

- **Use Agent Mode** for: Implementation, refactoring, bug fixes
- **Use Plan Mode** for: Complex features, architectural decisions, multi-file changes
- **Use Ask Mode** for: Understanding code, learning, exploration without changes
- **Use Debug Mode** for: Tricky bugs, race conditions, performance issues

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Shift+Tab` | Rotate between modes (Agent → Plan → Ask) |
| `Shift+Enter` | Insert newline (multi-line prompts) |
| `Ctrl+R` | Review changes |
| `Ctrl+D` (twice) | Exit CLI |
| `Arrow Up/Down` | Cycle through previous messages |
| `i` (in review) | Add follow-up instructions |

## Cloud Agent Handoff

Hand off long-running tasks to Cloud Agent by prepending `&` to your message:

```bash
# Send to Cloud Agent
& implement the complete authentication module with tests

# Pick up at cursor.com/agents
```

## MCP Integration

The CLI automatically respects your `mcp.json` configuration. All MCP servers configured for the IDE are available in CLI mode.

## Rules Integration

The CLI loads rules from:
- `.cursor/rules/*.mdc` files
- `AGENTS.md` at project root
- `CLAUDE.md` at project root

Rules are automatically applied based on their glob patterns and configuration.

## Best Practices for CLI Usage

### 1. Clear Intent Statements
State your intent clearly. For planning without code:
```
agent "analyze the payment flow - do not write any code"
```

### 2. Context Selection
Use `@` to include specific files/folders:
```
agent "refactor @src/auth to use the new token format"
```

### 3. Compress Context
Use `/compress` to free up context window space during long sessions.

### 4. Command Approval
CLI asks for approval before running terminal commands. You can:
- Press `y` to approve
- Press `n` to reject
- Press `Tab` to add to allowlist

### 5. Shell Mode Limitations
- Commands timeout after 30 seconds
- No interactive prompts supported
- No long-running servers
- Use `cd dir && command` for different directories

## PowerShell-Specific Notes (Windows)

When using Cursor CLI on Windows PowerShell:
- Use semicolons (`;`) instead of `&&` for command chaining
- Ensure UTF-8 encoding is set before running
- Avoid multi-line strings in prompts

```powershell
# Windows example
agent "review the changes in src/auth"
```

## Integration with trent

When using Cursor CLI with this project's task management:

1. **Reference Tasks**: Include task context in prompts
   ```bash
   agent "implement task 720 - monitoring dashboards"
   ```

2. **Update Task Files**: CLI can edit task files directly
   ```bash
   agent "mark task 720 as completed in TASKS.md"
   ```

3. **Create Task Files**: Use CLI for batch task creation
   ```bash
   agent -p "create task files for phase 8 based on PLAN.md" --mode=plan
   ```

## Troubleshooting

### Command Hangs
Press `Ctrl+C` to cancel, add non-interactive flags to commands.

### Permission Issues
Approve commands with `y` or add to allowlist with `Tab`.

### Truncated Output
Press `Ctrl+O` to expand truncated output.

### Terminal Compatibility
Run `/setup-terminal` to configure `Option+Enter`/`Alt+Enter` for newlines in:
- Apple Terminal
- Alacritty
- VS Code integrated terminal

## Related Resources

- [CLI Overview](https://cursor.com/docs/cli/overview)
- [Using Agent in CLI](https://cursor.com/docs/cli/using)
- [Shell Mode](https://cursor.com/docs/cli/shell-mode)
- [Agent Modes](https://cursor.com/docs/agent/modes)
- [Cloud Agent](https://cursor.com/docs/cloud-agent)
