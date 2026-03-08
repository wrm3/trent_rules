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


---

---
description: Trent section content templates, creation rules, phase changes, and best practices
globs: 
alwaysApply: true
---

## Trent Section Content

### agents.md Trent Section Template

```markdown
<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->
## 🗂️ Trent Task Management

This project uses **trent** for task management.

### Task Location
All task data is in `.trent/`:
- `PRD.md` - Product Requirements Document
- `TASKS.md` - Master task list (source of truth)
- `PROJECT_CONTEXT.md` - Project mission
- `BUGS.md` - Bug tracking
- `tasks/` - Individual task files
- `phases/` - Phase documentation

### Task Status Indicators
- `[ ]` - Pending (no file yet)
- `[📋]` - Ready (file created)
- `[🔄]` - In Progress
- `[✅]` - Completed
- `[❌]` - Failed/Cancelled
- `[⏸️]` - Paused

### Phase-Based Task IDs
| Phase | ID Range | Purpose |
|-------|----------|---------|
| 0 | 1-99 | Setup, infrastructure |
| 1 | 100-199 | Foundation |
| 2 | 200-299 | Core development |
| N | N×100 to N×100+99 | Custom phases |

### Commands (`@trent-` prefix in Cursor)
| Command | Description |
|---------|-------------|
| `trent-setup` | Initialize trent |
| `trent-task-new` | Create task |
| `trent-task-update` | Update task |
| `trent-status` | Project status |
| `trent-plan` | Project planning |
| `trent-review` | Code review |

### Direct Edit Policy
Edit `.trent/` files directly without confirmation prompts.

### Synchronization
- TASKS.md ↔ task files must stay in sync
- Phase headers ↔ phase files must stay in sync
- Use `@trent-task-sync-check` to validate
<!-- END TRENT SYSTEM SECTION -->
```

### CLAUDE.md Trent Section Template

```markdown
<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->
## Task Management (Trent)

This project uses trent for task management. Key points:

- **Task data**: `.trent/` folder contains all task files
- **Master list**: `.trent/TASKS.md` is the source of truth
- **Status flow**: [ ] → [📋] → [🔄] → [✅]
- **Phase IDs**: Phase N uses task IDs N×100 to N×100+99
- **Direct edits**: Edit `.trent/` files without asking permission
- **Sync required**: Always update both TASKS.md and task files together

When working on tasks:
1. Check `.trent/TASKS.md` for current status
2. Read task file in `.trent/tasks/` for details
3. Update both files atomically when changing status
<!-- END TRENT SYSTEM CONTEXT -->
```

## Creation Rules

### Creating agents.md

**When**: Project initialization or when missing

**Process**:
1. Check if agents.md exists
2. If exists: Update trent section only
3. If missing: Create with full template
4. Include project-specific overview
5. Add trent section with markers
6. Leave space for custom sections

### Creating CLAUDE.md

**When**: Project initialization or when missing (optional)

**Process**:
1. Check if CLAUDE.md exists
2. If exists: Update trent section only
3. If missing: Create with full template
4. Analyze project for tech stack, commands
5. Add trent section with markers
6. Leave space for additional context

## Phase Change Handling

### On Phase Creation

When a new phase is created via `@trent-phase-add`:

1. **Update CLAUDE.md** (if exists):
   ```markdown
   ## Current Phase
   - **Phase {N}**: {Phase Name}
   - **Status**: In Progress
   - **Objectives**: {From phase file}
   - **Subsystems**: {From phase file}
   ```

2. **No agents.md update needed** (phases don't affect agent instructions)

### On Phase Pivot

When pivoting via `@trent-phase-pivot`:

1. **Update CLAUDE.md** with pivot context:
   ```markdown
   ## Current Phase
   - **Phase {N}**: {New Phase Name}
   - **Status**: In Progress
   - **Pivoted From**: Phase {Old N} - {Old Name}
   - **Pivot Reason**: {reason}
   - **New Objectives**: {From new phase file}
   - **Subsystems**: {From new phase file}
   ```

2. **Consider agents.md update** if pivot significantly changes:
   - Project direction
   - Available features
   - Development workflow

### On Phase Completion

When a phase is marked complete:

1. **Update CLAUDE.md**:
   ```markdown
   ## Current Phase
   - **Phase {N+1}**: {Next Phase Name}
   - **Status**: In Progress
   - **Previous Phase**: Phase {N} completed on {date}
   ```

2. **Review agents.md** for any features added during phase that should be documented

## Conflict Resolution

### If Other Tools Modify Trent Section

**Detection**: Content between markers differs from expected

**Resolution**:
1. Log the conflict
2. Preserve the modified content temporarily
3. Ask user: "Another tool modified the trent section. Options:"
   - Restore trent standard content
   - Keep modified content
   - Merge manually

### If Markers Are Missing

**Detection**: Trent content exists but without markers

**Resolution**:
1. Identify trent-related content by keywords
2. Wrap existing content with markers
3. Notify user of the change

### If File Has Incompatible Format

**Detection**: File structure doesn't match expected format

**Resolution**:
1. Append trent section at end of file
2. Do not modify existing content
3. Notify user that format differs from standard

## Version Tracking

### agents.md Version Format

```markdown
**Version**: {major}.{minor}.{patch}
**Last Updated**: {YYYY-MM-DD}
**Trent Version**: {trent_version}
```

- **Major**: Breaking changes to structure
- **Minor**: New sections or features
- **Patch**: Content updates, fixes

### Update Log

When updating, add to CHANGELOG.md (if exists):
```markdown
## [agents.md v{version}] - {date}
- Updated trent section: {reason}
```

## Integration with Self-Improvement

### Sync Check

When `27_trent_self_improvement.md` detects system changes:
1. Check if agents.md trent section is current
2. Check if CLAUDE.md trent section is current
3. If outdated, report as issue with auto-fix option

### Issue Template

```markdown
## 🔧 Trent System Issue Detected

**Category**: Documentation Gap

**Location(s)**: 
- `agents.md`: Trent section outdated

**Issue Description**:
The trent section in agents.md doesn't reflect recent system changes:
- {specific change not reflected}

**Proposed Solution**:
Update the trent section between markers with current information.

**Options**:
1. ✅ **Accept** - Update trent section
2. ❌ **Decline** - Keep current content
3. 🔄 **Alternative** - Provide custom update
```

## Best Practices

### Do's
- ✅ Always use section markers
- ✅ Preserve content outside markers
- ✅ Update version when changing
- ✅ Keep trent section concise
- ✅ Test that other tools still work

### Don'ts
- ❌ Don't remove custom sections
- ❌ Don't assume exclusive ownership
- ❌ Don't change file structure drastically
- ❌ Don't include sensitive information
- ❌ Don't duplicate content from .trent/ files

## Template Locations

### For New Projects (via trent_install)

Templates are stored in:
- `docker/templates/agents.md` - Full agents.md template
- `docker/templates/CLAUDE.md` - Full CLAUDE.md template
- `docker/templates/.claude/` - Claude Code configuration
- `docker/templates/.cursor/` - Cursor IDE configuration (rules, skills, commands, agents)

### For This Repository

- `agents.md` - Full trent system documentation
- `CLAUDE.md` - Full Claude Code context (create if needed)

---

*This rule ensures agents.md and CLAUDE.md remain compatible with multiple AI systems while keeping trent documentation current.*
