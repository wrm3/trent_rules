# Cursor Architecture

**Last Updated**: 2026-03-03
**Official Website**: https://cursor.com
**Version Documented**: Cursor IDE 2.5+ (Standalone IDE based on VSCode)

## Overview
Cursor is an AI-first IDE built as a fork of VSCode. It uses **rules** (`.mdc` files) for AI behavior customization, supports Skills, SubAgents, MCP integration, and provides AI-powered code editing with context awareness.

## Directory Structure

```
.cursor/
├── rules/                     # AI behavior rules (.mdc files)
│   ├── 00_always.mdc          # Universal guidelines
│   ├── 01_documentation.mdc   # Doc standards
│   ├── 02_git_workflow.mdc    # Git conventions
│   ├── 03_code_review.mdc     # Code review
│   ├── 04_code_reusability.mdc
│   ├── 10a_trent_tasks.mdc    # trent task management
│   ├── 10b_trent_enforcement.mdc
│   ├── 10c_trent_files.mdc
│   ├── 10d_trent_platform.mdc
│   ├── 11a_trent_prd_phases.mdc
│   ├── 11b_trent_subsystems.mdc
│   ├── 11c_trent_questionnaire.mdc
│   ├── 12_trent_qa.mdc
│   ├── 13_trent_workflow.mdc
│   ├── 14_trent_index.mdc
│   ├── 30_powershell.mdc
│   ├── silicon_valley_*.mdc
│   └── ...
├── skills/                    # 16 AI Skills
│   └── skill-name/
│       └── SKILL.md
├── agents/                    # 22 Specialized agents
│   └── agent-name.md
├── commands/                  # 22 @trent-* commands
│   └── command-name.md
└── hooks/                     # PowerShell automation hooks
    └── *.ps1
```

## Rules System

### .mdc File Format
```yaml
---
description: Brief description of what this rule does
globs:                         # Optional file patterns
  - "**/*.ts"
  - "**/*.tsx"
alwaysApply: true             # Apply to all conversations (optional)
---

# Rule Title

## Rule Content
[Markdown content with instructions, examples, and guidelines]
```

### Key Features
- **File Type**: `.mdc` (Markdown Cursor) — **UNIQUE TO CURSOR**
- **YAML Frontmatter**: Required for metadata
- **Glob Patterns**: Target specific file types
- **alwaysApply**: Make rule global across project
- **Subfolder Support**: Yes (but flat numbered structure preferred)

### Rule Types

1. **Global Rules** (`alwaysApply: true`) — Applied to all AI interactions
2. **File-Specific Rules** (with `globs`) — Applied only to matching files
3. **On-Demand Rules** (`alwaysApply: false`) — Loaded when relevant

## Skills System

Cursor supports Skills — reusable knowledge modules:
- Located in `.cursor/skills/skill-name/SKILL.md`
- YAML frontmatter with `name`, `description`, `triggers`
- Loaded on relevance (lazy-loaded, not always-on)
- Format is identical to Claude Code skills

## SubAgents

Cursor supports SubAgents — specialized AI assistants:
- Located in `.cursor/agents/agent-name.md`
- 22 agents covering development, AI/ML, IDE config, and specialized tasks
- Multi-agent orchestration support

## Commands

- **Invocation**: Use `@` prefix (e.g., `@trent-task-new`)
- **Format**: Plain markdown (.md files)
- **Location**: `.cursor/commands/`
- 22 `@trent-*` commands available

## MCP (Model Context Protocol)

Cursor has built-in MCP support:
- Configured via `.cursor/mcp.json`
- Supports stdio and SSE transports
- Tools accessible via `CallMcpTool`
- Resource access via `FetchMcpResource`

```json
{
  "mcpServers": {
    "trent_rules_docker": {
      "command": "node",
      "args": ["/path/to/server/index.js"]
    }
  }
}
```

## Hooks

Cursor supports lifecycle hooks:
- Located in `.cursor/hooks/`
- Pre/post tool use hooks
- Session start/stop hooks for memory capture

## Cross-Platform Compatibility

### Cursor ↔ Claude Code

| Feature | Cursor | Claude Code |
|---------|--------|-------------|
| Rule extension | `.mdc` | `.md` |
| Command prefix | `@command` | `/command` |
| Rules directory | `.cursor/rules/` | `.claude/rules/` |
| Skills | `.cursor/skills/` | `.claude/skills/` |
| Agents | `.cursor/agents/` | `.claude/agents/` |
| MCP config | `.cursor/mcp.json` | `settings.local.json` |

Content is identical between platforms; only extensions and invocation syntax differ.

### Migration: Cursor → Claude Code
1. Copy `.cursor/agents/` → `.claude/agents/` (no changes needed)
2. Copy `.cursor/skills/` → `.claude/skills/` (no changes needed)
3. Copy `.cursor/commands/` → `.claude/commands/` (no changes needed)
4. Copy `.cursor/rules/*.mdc` → `.claude/rules/*.md` (rename extension)

## Official Resources

- **Website**: https://cursor.com
- **Docs**: https://docs.cursor.com
- **Discord**: Cursor community Discord
- **Forum**: https://forum.cursor.com

---

**Critical Notes**:
1. **MUST use .mdc extension** for rules in Cursor (not .md)
2. **Use @ prefix** for commands (not /)
3. **YAML frontmatter required** for all rules
4. Skills and Agents are fully supported (same format as Claude Code)
