# Claude Code Architecture

**Last Updated**: 2026-02-19
**Official Website**: https://docs.anthropic.com/en/docs/claude-code
**Version Documented**: Claude Code (VSCode Extension + CLI)

## Overview

Claude Code is Anthropic's official CLI and VSCode extension for AI-assisted development. It uses a rich project configuration system with skills, agents, commands, rules, and hooks stored in the `.claude/` directory.

## Directory Structure

```
.claude/
├── CLAUDE.md                  # Project instructions (auto-loaded every conversation)
├── settings.local.json        # MCP servers, permissions, env vars
├── hooks.json                 # Hook event configuration
├── agents/                    # Specialized agent definitions
│   ├── agent-name.md          # Agent definition file
│   └── README.md              # Agent index
├── commands/                  # Slash commands (/)
│   ├── command-name.md        # Command definition
│   └── ...
├── hooks/                     # Hook scripts (PowerShell/Bash)
│   ├── audit.ps1
│   ├── session-start.ps1
│   ├── agent-complete.ps1
│   └── validate-shell.ps1
├── rules/                     # Context rules (.md files)
│   ├── 00_always.md           # Always-apply rules
│   ├── 10_trent_core.md       # trent system rules
│   └── ...
├── skills/                    # Skill definitions
│   └── skill-name/
│       ├── SKILL.md           # Main skill definition
│       ├── reference/         # Reference documentation
│       ├── examples/          # Usage examples
│       ├── scripts/           # Executable scripts
│       └── templates/         # File templates
└── memory/                    # Auto-memory (persists across sessions)
    └── MEMORY.md              # Auto-loaded memory file
```

## Key Configuration Files

### CLAUDE.md (Project Root)
The primary project instruction file. Auto-loaded at the start of every conversation.
- Contains project overview, conventions, task management rules
- Equivalent to `.cursor/rules/` combined for Claude Code

### .claude/CLAUDE.md
Additional Claude Code-specific instructions. Also auto-loaded.
- Rate limit protocol, agent coordination rules
- Supplements the root CLAUDE.md

### settings.local.json
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENTS_TEAMS": "true"
  },
  "permissions": {
    "allow": ["Bash(git diff:*)", "mcp__server__tool_name"]
  },
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["trent_rules_docker", "blender"],
  "defaultMode": "bypassPermissions"
}
```

### hooks.json
```json
{
  "version": 1,
  "hooks": {
    "sessionStart": [{"command": "powershell -File .claude/hooks/session-start.ps1"}],
    "stop": [{"command": "powershell -File .claude/hooks/agent-complete.ps1"}],
    "afterFileEdit": [{"command": "powershell -File .claude/hooks/audit.ps1"}],
    "beforeShellExecution": [{"command": "powershell -File .claude/hooks/validate-shell.ps1"}],
    "preToolUse": [{"command": "powershell -File .claude/hooks/audit.ps1"}],
    "postToolUse": [{"command": "powershell -File .claude/hooks/audit.ps1"}]
  }
}
```

## Rules System

### File Format: .md (Standard Markdown)
```yaml
---
description: 'Brief description of the rule purpose'
globs:
  - '**/*.py'
alwaysApply: false
---

# Rule Content
Markdown content with instructions and examples.
```

### Key Differences from Cursor
| Feature | Claude Code | Cursor |
|---------|-------------|--------|
| Rule extension | `.md` | `.mdc` |
| Command prefix | `/command` | `@command` |
| Rules directory | `.claude/rules/` | `.cursor/rules/` |
| Skills | `.claude/skills/` | `.cursor/skills/` |
| Agents | `.claude/agents/` | `.cursor/agents/` |
| Config | `settings.local.json` | `.cursor/mcp.json` |

## Skills System

Skills are reusable knowledge modules with structured directories:

```yaml
# SKILL.md frontmatter
---
name: skill-name
description: What this skill does
triggers: [keyword1, keyword2]
---
```

Skills are lazy-loaded when triggered by matching keywords in conversation.

## Agent System

Agents are specialized AI assistants defined in markdown:

```yaml
---
name: agent-name
description: What this agent specializes in
tools: Read, Edit, Write, Bash, Grep, Glob
model: sonnet|opus|haiku
---

# Agent Name

## Role
Description of the agent's specialization.

## Instructions
Detailed instructions for the agent.
```

Agents are invoked via the Task tool with `subagent_type` parameter.

## Commands System

Commands are slash-invocable prompts:

```markdown
# /command-name

Description of what this command does.

## Prompt
The actual prompt that gets executed when the command is invoked.
```

## Hook Events

| Event | When |
|-------|------|
| `sessionStart` | New conversation created |
| `sessionEnd` | Conversation ends |
| `stop` | Agent loop ends |
| `afterFileEdit` | After any file edit |
| `beforeShellExecution` | Before shell command runs |
| `preToolUse` | Before any tool use |
| `postToolUse` | After any tool use |

## MCP Integration

Claude Code has built-in MCP (Model Context Protocol) support:
- Configure via `settings.local.json` or `claude mcp add` CLI
- Supports stdio, SSE, and streamable-http transports
- MCP tools appear as `mcp__servername__toolname`

## Cross-Platform Compatibility with Cursor

This project maintains full parity between `.claude/` and `.cursor/`:
- **Agents**: Identical files in both directories
- **Skills**: Identical directories and SKILL.md files
- **Commands**: Same commands, different prefix (`/` vs `@`)
- **Rules**: Same content, different extension (`.md` vs `.mdc`)
- **Hooks**: Same scripts, adjusted paths for each system

### Migration: Claude Code -> Cursor
1. Copy `.claude/agents/` to `.cursor/agents/`
2. Copy `.claude/skills/` to `.cursor/skills/`
3. Copy `.claude/commands/` to `.cursor/commands/`
4. Copy `.claude/rules/*.md` to `.cursor/rules/*.mdc` (rename extension)

### Migration: Cursor -> Claude Code
1. Copy `.cursor/agents/` to `.claude/agents/`
2. Copy `.cursor/skills/` to `.claude/skills/`
3. Copy `.cursor/commands/` to `.claude/commands/`
4. Copy `.cursor/rules/*.mdc` to `.claude/rules/*.md` (rename extension)

## Official Resources

- **Docs**: https://docs.anthropic.com/en/docs/claude-code
- **GitHub**: https://github.com/anthropics/claude-code
- **Changelog**: https://docs.anthropic.com/en/docs/claude-code/changelog

---

**Last Updated**: 2026-02-19
