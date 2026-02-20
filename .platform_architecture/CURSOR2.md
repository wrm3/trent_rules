# Cursor IDE Architecture

**trent** - Cursor Implementation Guide

## Overview

Cursor IDE provides full support for trent with unique features like `.mdc` rule files and `@` command prefix.

## File Structure

```
.cursor/
├── rules/
│   └── trent/
│       ├── rules/
│       │   ├── rules.mdc
│       │   ├── plans.mdc
│       │   ├── qa.mdc
│       │   └── workflow.mdc
│       └── _index.mdc
├── skills/
│   └── fstrent-task-management/
│       └── SKILL.md
├── agents/
│   ├── backend-developer.md
│   ├── frontend-developer.md
│   └── ... (18+ agents)
└── commands/
    └── (command definitions)
```

## Rule Files (.mdc)

### Format Requirements

```yaml
---
description: Brief description of the rule
globs: ["**/*.py", "**/*.js"]  # Optional: file patterns
alwaysApply: true  # or false
---

# Rule Content
```

### Key Points
- **Extension**: Must use `.mdc` (not `.md`)
- **Location**: `.cursor/rules/` or subdirectories
- **YAML Frontmatter**: Required with `description` and `alwaysApply`

## Commands

### Syntax
```bash
@trent-task-new
@trent-status
@trent-plan
@trent-qa
@trent-workflow
```

### Command Definition
Commands are defined in `.cursor/rules/*/commands/` directories.

## Skills

Cursor supports Skills:
- Skills in `.cursor/skills/` directory
- `SKILL.md` format with YAML frontmatter
- Organized by capability

## SubAgents

Cursor supports SubAgents:
- SubAgents in `.cursor/agents/` directory
- Agent definitions in Markdown format
- Multi-agent orchestration support

## MCP Integration

Cursor has full MCP (Model Context Protocol) support:
- MCP servers configured in settings
- Tools accessible via `CallMcpTool`
- Resource access via `FetchMcpResource`

## Hooks

Cursor supports lifecycle hooks:
- Pre/post tool use hooks
- Session hooks
- Located in `.cursor/hooks/`

## Best Practices

1. **Use `.mdc` for rules** - Required for Cursor
2. **Test commands** - Verify `@` prefix works
3. **Leverage Skills** - Use Skills for complex workflows
4. **MCP Tools** - Prefer MCP tools over manual implementation
5. **Organize by capability** - Group related skills/agents

## Resources

- **Official Docs**: https://docs.cursor.com
- **Skills Guide**: See `.cursor/skills/` examples
- **MCP Docs**: Cursor MCP integration guide

## Last Updated

**Date**: 2026-01-29  
**Cursor Version**: 2.4.21+
