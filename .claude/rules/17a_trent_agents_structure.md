---
description: agents.md and CLAUDE.md file structure, section ownership, and update triggers
globs: 
alwaysApply: true
---

# Project Instruction Files Management

This rule governs the maintenance of `agents.md` and `CLAUDE.md` files - universal AI assistant instruction files used across multiple AI coding tools.

## Overview

### File Purposes

| File | Primary Use | Supported Tools |
|------|-------------|-----------------|
| `agents.md` | Universal AI agent instructions | Cursor, Windsurf, Copilot, Codex, Aider, Zed, 15+ others |
| `CLAUDE.md` | Claude-specific project context | Claude Code, Claude API integrations |

### Key Principle: Coexistence

**CRITICAL**: These files are read by MULTIPLE AI systems. The trent system MUST NOT:
- Override or conflict with other systems' usage
- Remove sections added by other tools
- Assume exclusive ownership of these files

## File Structure Standards

### agents.md Structure

```markdown
# agents.md - {Project Name}

> {Brief project description}

---

## 📋 Project Overview
{Project purpose and core features}

---

## 📁 Project Structure
{Directory layout with descriptions}

---

## 🔧 Development Commands
{Common commands for building, testing, running}

---

## 📝 Code Style Guidelines
{Language-specific conventions}

---

## 🔒 Security
{Security requirements and practices}

---

## 📋 Quick Reference
{Essential workflows and patterns}

---

<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->
## 🗂️ Trent Task Management

{Auto-generated trent system documentation}

<!-- END TRENT SYSTEM SECTION -->

---

<!-- CUSTOM SECTIONS BELOW - Safe for other tools -->

{Additional sections added by other systems or manually}

---

**Version**: {version}
**Last Updated**: {date}
```

### CLAUDE.md Structure

```markdown
# CLAUDE.md - {Project Name}

## Project Overview
{Brief description of what this project does}

## Tech Stack
{Technologies and versions used}

## Key Directories
{Important paths and their purposes}

## Development Commands
{Common commands Claude should know}

## Coding Conventions
{Style guidelines and patterns}

## Testing
{How to run tests, testing patterns}

## Important Notes
{Project-specific gotchas and warnings}

---

<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->
## Task Management (Trent)

{Auto-generated trent context}

<!-- END TRENT SYSTEM CONTEXT -->

---

<!-- Additional context below is safe for manual editing -->
```

## Section Ownership

### Protected Sections (Trent-Managed)

These sections are auto-generated and should not be manually edited:

**In agents.md:**
```markdown
<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->
...
<!-- END TRENT SYSTEM SECTION -->
```

**In CLAUDE.md:**
```markdown
<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->
...
<!-- END TRENT SYSTEM CONTEXT -->
```

### Open Sections (User/Other Tools)

Everything outside the protected markers is:
- Safe for manual editing
- Safe for other AI tools to modify
- Preserved during trent updates

## Update Triggers

### When to Update agents.md

**Automatic updates required when:**
- New trent commands are added
- Task status indicators change
- Phase numbering convention changes
- New agents or skills are added
- Direct edit policy changes
- **New MCP tools are added**
- **New features are implemented** (user-facing)
- **New subsystems are created**

**Task-Based Triggers** (check on task completion):
| Task Type | Update agents.md? |
|-----------|-------------------|
| Added MCP tool | ✅ YES - Add to tools section |
| Added command | ✅ YES - Add to commands table |
| Added skill | ✅ YES - Add to skills list |
| Added agent | ✅ YES - Add to agents table |
| New feature | ⚠️ MAYBE - If affects workflow |
| Bug fix | ❌ NO |
| Refactor | ❌ NO |
| Documentation | ❌ NO |

**Update process:**
1. Read current agents.md
2. Locate trent section markers
3. Replace ONLY content between markers
4. Preserve all other content
5. Update version and date at bottom

### When to Update CLAUDE.md

**Automatic updates required when:**
- Project structure changes significantly
- New development commands are added
- Tech stack changes
- Trent system conventions change
- **Phase is created or pivoted**
- **New directories are added**
- **Coding conventions change**

**Phase-Based Triggers:**
| Event | Update CLAUDE.md? |
|-------|-------------------|
| New phase created | ✅ YES - Update current phase section |
| Phase pivoted | ✅ YES - Update phase context and reason |
| Phase completed | ✅ YES - Update to next active phase |
| Subsystems changed | ✅ YES - Update key directories |

**Update process:**
1. Read current CLAUDE.md (or create if missing)
2. Locate trent section markers
3. Replace ONLY content between markers
4. Preserve all other content
5. **For phase changes**: Also update "Current Phase" section outside markers
