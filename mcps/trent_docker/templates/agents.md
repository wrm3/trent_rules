# agents.md - {Project Name}

> {Brief project description}

---

## 📋 Project Overview

**{Project Name}** - {One-line description}

**Purpose**: {What this project does and why}

**Core Features**:
- {Feature 1}
- {Feature 2}
- {Feature 3}

---

## 📁 Project Structure

```
{project}/
├── src/                    # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── .trent/                 # Task management
│   ├── PLAN.md            # Product Requirements
│   ├── TASKS.md           # Master task list
│   ├── PROJECT_CONTEXT.md # Project mission
│   └── tasks/             # Individual task files
└── {other directories}
```

---

## 🔧 Development Commands

```bash
# Install dependencies
{install_command}

# Run development server
{dev_command}

# Run tests
{test_command}

# Build for production
{build_command}
```

---

## 📝 Code Style Guidelines

### {Primary Language}
- {Style guide or linter}
- {Formatting tool}
- {Key conventions}

---

## 🔒 Security

- Never commit API keys, tokens, or passwords
- Use environment variables for secrets
- {Project-specific security requirements}

---

## 📋 Quick Reference

### When Starting Work
1. Read `.trent/PROJECT_CONTEXT.md` for project goals
2. Check `.trent/TASKS.md` for current tasks
3. Create task file before starting work

### When Completing Work
1. Update task file status to `completed`
2. Update TASKS.md status to `[✅]`
3. Commit changes with descriptive message

---

<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->
## 🗂️ Trent Task Management

This project uses **trent** for task management.

### Task Location
All task data is in `.trent/`:
- `PLAN.md` - Product Requirements Document
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
| `trent-task-sync-check` | Validate sync |
| `trent-status` | Project status |
| `trent-plan` | Project planning |
| `trent-review` | Code review |
| `trent-git-commit` | Git commit |

### Direct Edit Policy
Edit `.trent/` files directly without confirmation prompts.

### Synchronization
- TASKS.md ↔ task files must stay in sync
- Phase headers ↔ phase files must stay in sync
- Use `@trent-task-sync-check` to validate
<!-- END TRENT SYSTEM SECTION -->

---

<!-- CUSTOM SECTIONS BELOW - Safe for other tools and manual editing -->

---

**Version**: 1.0.0
**Last Updated**: {YYYY-MM-DD}
