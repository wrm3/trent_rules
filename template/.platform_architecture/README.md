# AI Platform Architecture Documentation

**Purpose**: Source of truth for AI coding platform setup, features, and cross-platform compatibility.

## Overview

This folder documents the architecture, features, and setup requirements for major AI coding platforms.

### Primary Platforms for This Project

1. **Cursor IDE** — `.cursor/` with `.mdc` rules, `@` command prefix, Skills, Agents
2. **Claude Code** — `.claude/` with `.md` rules, `/` command prefix, Skills, Agents
3. **Google Antigravity** — `.agent/` with `.md` rules, `/workflow-name`, Skills, Workflows

All three share agents, skills, and commands. Content is identical; file extensions and invocation syntax differ.

## Documentation Files

| File | Description | Status |
|------|-------------|--------|
| [Claude/CLAUDE_CODE.md](Claude/CLAUDE_CODE.md) | Claude Code architecture and config guide | Updated 2026-02 |
| [Gemini/ANTIGRAVITY.md](Gemini/ANTIGRAVITY.md) | Google Antigravity architecture and config guide | Updated 2026-02 |
| [Cursor/CURSOR.md](Cursor/CURSOR.md) | Cursor IDE architecture | Updated 2026-03 |
| [PLATFORM_ARCHITECTURE.md](PLATFORM_ARCHITECTURE.md) | Cross-platform comparison and migration guides | Updated 2026-03 |

## Quick Start

### For Platform-Specific Users

- **Using Claude Code?** → [Claude/CLAUDE_CODE.md](Claude/CLAUDE_CODE.md)
- **Using Google Antigravity?** → [Gemini/ANTIGRAVITY.md](Gemini/ANTIGRAVITY.md)
- **Using Cursor?** → [Cursor/CURSOR.md](Cursor/CURSOR.md)

## Architecture Patterns

**Pattern 1: Claude Code + Cursor (Shared Architecture)**
```
✅ Skills system - Reusable knowledge modules (16 skills)
✅ SubAgents - Specialized AI assistants (22 agents)
✅ Commands - 22 trent-* commands
✅ Rules - Numbered, flat directory structure
✅ Hooks - PowerShell automation hooks
   Only difference: .md vs .mdc extension, / vs @ prefix
```

**Pattern 2: Google Antigravity**
```
✅ Skills - Same format as Claude Code/Cursor
✅ Workflows - Slash commands (/workflow-name)
✅ Artifacts - task.md, implementation_plan.md, walkthrough.md
✅ Knowledge Items - Auto-generated persistent memory
✅ GUARDRAILS.md - Learned failure constraints
✅ Multi-model - Gemini + Claude + GPT
```

### The ONLY Real Difference Between Cursor and Claude Code

| | Cursor | Claude Code |
|--|--------|-------------|
| **Rule extension** | `.mdc` | `.md` |
| **Command prefix** | `@command` | `/command` |
| **Config** | `.cursor/mcp.json` | `settings.local.json` |
| Everything else | Identical | Identical |

## Verification Status

| Platform | Directory | File Format | Commands | MCP | Skills/Agents |
|----------|-----------|-------------|----------|-----|---------------|
| Claude Code | `.claude/` | `.md` | `/command` | Built-in | 16 skills, 22 agents |
| Cursor | `.cursor/` | `.mdc` | `@command` | `.cursor/mcp.json` | 16 skills, 22 agents |
| Antigravity | `.agent/` | `.md` | `/workflow-name` | `mcp_config.json` | Skills yes, no agents |

## Maintenance Schedule

### Quarterly Review (Every 3 Months)
- [ ] Check all platform official docs for updates
- [ ] Test template on each platform
- [ ] Update architecture docs
- [ ] Update comparison table

## Official Resources

- **Claude Code**: https://docs.anthropic.com/en/docs/claude-code
- **Google Antigravity**: https://antigravity.google/docs
- **Cursor**: https://docs.cursor.com
- **MCP Protocol**: https://modelcontextprotocol.io/

---

**Last Review**: 2026-03-03
**Status**: Active documentation
