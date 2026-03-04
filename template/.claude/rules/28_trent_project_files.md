---
description: agents.md and CLAUDE.md management, section ownership, update triggers
globs:
alwaysApply: true
---

# Project Instruction Files Management

## File Purposes

| File | Primary Use | Read By |
|------|-------------|---------|
| `agents.md` | Universal AI agent instructions | Cursor, Windsurf, Copilot, Codex, Aider, Zed, 15+ others |
| `CLAUDE.md` | Claude-specific project context | Claude Code |

## Key Principle: Coexistence (MANDATORY)

These files are read by MULTIPLE AI systems. The trent system MUST NOT:
- Override or conflict with other systems' usage
- Remove sections added by other tools
- Assume exclusive ownership of these files

## Protected Sections

Use HTML comment markers for trent-managed content:

**agents.md**: `<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->` ... `<!-- END TRENT SYSTEM SECTION -->`
**CLAUDE.md**: `<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->` ... `<!-- END TRENT SYSTEM CONTEXT -->`

Everything outside markers is preserved during trent updates.

## Update Triggers

### agents.md (update trent section when):

| Task Type | Update? |
|-----------|---------|
| Added MCP tool | YES |
| Added command/skill/agent | YES |
| New user-facing feature | MAYBE |
| Bug fix / Refactor / Docs | NO |

**Process**: Read → locate markers → replace ONLY between markers → preserve all other content → update version/date.

### CLAUDE.md (update trent section when):

| Event | Update? |
|-------|---------|
| Phase created/pivoted/completed | YES |
| Project structure changes | YES |
| Tech stack / conventions change | YES |
| New directories added | YES |

**Process**: Read → locate markers → replace ONLY between markers → preserve all other content. For phase changes, also update "Current Phase" section outside markers.

## Creation Rules

**agents.md**: If exists → update trent section only. If missing → create with full template from `trent-planning` skill.
**CLAUDE.md**: If exists → update trent section only. If missing → create with template (optional).

## Conflict Resolution

- **Other tools modified trent section**: Ask user — restore standard, keep modified, or merge manually.
- **Markers missing**: Wrap existing trent content with markers, notify user.
- **Incompatible format**: Append trent section at end, do not modify existing content.

## Templates

Full templates for agents.md and CLAUDE.md structure are in the `trent-planning` skill.
Installation templates: `docker/templates/agents.md`, `docker/templates/CLAUDE.md`.
