# Platform Features

**trent** - Cursor IDE Features

## Core Features

| Feature | Support |
|---------|---------|
| **Rules Format** | `.mdc` files |
| **Skills Support** | ✅ Yes |
| **SubAgents Support** | ✅ Yes |
| **Commands** | `@trent-*` |
| **Task Management** | ✅ Full |
| **MCP Tools** | ✅ Full |
| **Hooks** | ✅ Yes |
| **Memory System** | ✅ Built-in |

## File Format

### Cursor Rules
- Uses `.mdc` extension for rules (Markdown Cursor)
- Located in `.cursor/rules/` directory
- YAML frontmatter required: `description`, `globs`, `alwaysApply`

## Command Syntax

```bash
@trent-task-new
@trent-status
@trent-plan
@trent-qa
@trent-workflow
```

## Skills & SubAgents

### Skills
- Full Skills system with `SKILL.md` files
- Located in `.cursor/skills/` directory
- Organized by capability (task management, databases, DevOps, etc.)

### SubAgents
- SubAgents for specialized tasks
- Located in `.cursor/agents/` directory
- Agent orchestration support

## Task Management

**Universal Features**:
- `.trent/` folder structure
- YAML frontmatter in task files
- Phase-based task numbering
- Status indicators ([ ], [📋], [🔄], [✅])
- Markdown documentation

## Best Practices

1. **Use `.mdc` extension** for all rule files
2. **Include YAML frontmatter** in rules
3. **Leverage Skills** for complex workflows
4. **Use MCP tools** when available
5. **Follow naming conventions** for task files

## Last Updated

**Date**: 2026-01-29  
**Version**: 3.0.0
