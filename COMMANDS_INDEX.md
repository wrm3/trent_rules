# Commands Index

> Quick reference for all available commands in this system.
> 
> **Location**: `.cursor/commands/`
> **Usage**: Invoke with `@command-name` in Cursor IDE.

---

## Trent Task Management Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `@trent-setup` | Initialize Trent system in a project | New project setup |
| `@trent-status` | Show project status overview | Daily check-in |
| `@trent-task-new` | Create a new task | Starting new work |
| `@trent-task-update` | Update task status | Progress tracking |
| `@trent-task-sync-check` | Verify TASKS.md ↔ task files sync | Maintenance |

## Trent Planning Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `@trent-plan` | Create/update PRD and planning docs | Project planning |
| `@trent-phase-add` | Add a new project phase | Expanding scope |
| `@trent-phase-pivot` | Pivot project direction with new phase | Changing direction |
| `@trent-phase-sync-check` | Verify phase consistency | Maintenance |
| `@trent-workflow` | Task expansion, sprint planning | Complex tasks |

## Trent Quality Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `@trent-qa` | Activate quality assurance mode | QA work |
| `@trent-qa-report` | Generate quality metrics report | Status reporting |
| `@trent-bug-report` | Report/document a bug | Bug discovery |
| `@trent-bug-fix` | Fix a reported bug | Bug resolution |
| `@trent-review` | Comprehensive code review | Before merge/commit |

## Trent Git Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `@trent-git-commit` | Create well-structured commits | After completing work |
| `@trent-issue-fix` | Fix a GitHub issue | Issue resolution |

---

## Command Count Summary

- **Total Commands**: 17
- **Task Management**: 5
- **Planning**: 5
- **Quality**: 5
- **Git**: 2

## How to Use Commands

In Cursor IDE, type `@` followed by the command name:

```
@trent-setup
@trent-task-new
@trent-status
```

## Command Categories

### Daily Workflow
```
@trent-status          → Check what's happening
@trent-task-new        → Start new work
@trent-task-update     → Update progress
@trent-git-commit      → Commit completed work
```

### Planning
```
@trent-plan            → Create/update PRD
@trent-phase-add       → Add new phase
@trent-workflow        → Break down complex tasks
```

### Quality
```
@trent-review          → Code review
@trent-bug-report      → Document bug
@trent-bug-fix         → Fix bug
@trent-qa-report       → Quality metrics
```

### Maintenance
```
@trent-task-sync-check  → Verify task sync
@trent-phase-sync-check → Verify phase sync
```

---

*Last updated: 2026-02-01*
