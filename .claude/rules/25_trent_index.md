---
description: "Trent system overview, directory structure, command list"
globs:
alwaysApply: true
---

# trent System Overview

## Session Start Protocol (MANDATORY)

**When user mentions tasks, phases, or project status, FIRST run sync validation:**

```
📋 TRENT SYNC VALIDATION
Task Sync: Comparing .trent/tasks/ against TASKS.md... [X synced, Y mismatches]
Phase Sync: Comparing .trent/phases/ against TASKS.md headers... [X synced, Y mismatches]
Status: [ALL SYNCED ✅ / ISSUES FOUND ⚠️]
```

**If issues found: FIX BEFORE proceeding.**

---

## Directory Structure
```
.trent/
├── tasks/              # Task files (taskNNN_name.md)
├── phases/             # Phase files (phaseN_name.md)
├── TASKS.md            # Master task list (source of truth)
├── PLAN.md             # Product Requirements Document
├── PROJECT_CONTEXT.md  # Project mission
├── BUGS.md             # Bug tracking
├── SUBSYSTEMS.md       # Component registry
├── IDEA_BOARD.md       # Ideas parking lot
└── PROJECT_GOALS.md    # Strategic goals

docs/                   # All documentation (NOT .trent/)
temp_scripts/           # Test and utility scripts
```

---

## Trent Rule Files

| File | Purpose |
|------|---------|
| `20_trent_tasks.md` | Task management, status, sync, completion |
| `21_trent_infrastructure.md` | File organization, scope control |
| `22_trent_planning.md` | PRD, phase management, phase sync |
| `23_trent_qa.md` | Bug tracking, zero-tolerance, quality |
| `24_trent_workflow.md` | Task expansion, complexity, story points |
| `25_trent_index.md` | System overview (this file) |
| `26_trent_agents_multi.md` | Parallel agent execution |
| `27_trent_self_improvement.md` | System issue detection |
| `28_trent_project_files.md` | agents.md/CLAUDE.md management |
| `29_trent_codebase_analysis.md` | Codebase integration analysis |
| `30_trent_ideas_goals.md` | IDEA_BOARD and PROJECT_GOALS |

---

## Commands (`@trent-` prefix)

| Command | Description |
|---------|-------------|
| `trent-setup` | Initialize system |
| `trent-status` | Project status overview |
| `trent-task-new` | Create a new task |
| `trent-task-update` | Update task status |
| `trent-task-sync-check` | Validate task sync |
| `trent-plan` | Project planning |
| `trent-review` | Code review |
| `trent-qa` / `trent-qa-report` | Quality assurance |
| `trent-bug-report` / `trent-bug-fix` | Bug tracking |
| `trent-git-commit` | Create commits |
| `trent-issue-fix` | Fix GitHub issue |
| `trent-phase-add` / `trent-phase-pivot` | Phase management |
| `trent-phase-sync-check` | Validate phase sync |
| `trent-workflow` | Task expansion |
| `trent-idea-capture` / `trent-idea-review` | Idea management |
| `trent-goal-update` | Update project goals |
