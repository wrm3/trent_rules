# agents.md - trent Template

> **Task Management System for Cursor IDE**

## Quick Start

This project uses **trent** for task management.

### Core Data Location
All task data is in `.trent/`:
- `PLAN.md` - Product Requirements Document
- `TASKS.md` - Master task list
- `PROJECT_CONTEXT.md` - Project mission
- `tasks/` - Individual task files

### Task Status Indicators
- `[ ]` Pending
- `[📋]` Ready
- `[🔄]` In Progress
- `[✅]` Completed
- `[❌]` Failed

### Commands (`trent-` prefix)

| Command | Description |
|---------|-------------|
| `trent-bug-report` | Report bug |
| `trent-bug-fix` | Fix bug |
| `trent-git-commit` | Git commit |
| `trent-phase-add` | Add phase |
| `trent-phase-pivot` | Pivot phase |
| `trent-plan` | Project planning |
| `trent-qa` | Quality assurance |
| `trent-review` | Code review |
| `trent-setup` | Initialize system |
| `trent-status` | Project status |
| `trent-task-new` | Create task |
| `trent-task-update` | Update task |
| `trent-workflow` | Workflow management |

**Usage:** `@trent-setup`, `@trent-task-new`, etc.

### Direct Edit Policy
Edit `.trent/` files directly without confirmation prompts.

---

For full documentation, see the main trent repository.
