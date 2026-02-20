---
name: trent-task-management
description: "Manage project tasks using the trent system. Use when creating, updating, tracking, or viewing tasks in .trent/ folder. Handles task files, TASKS.md updates, status management, and task queries."
---

# trent Task Management Skill

## Overview

The trent system stores all task data in `.trent/`. This skill provides the procedures for managing tasks correctly.

## Core Files

- `.trent/TASKS.md` — Master task checklist (source of truth)
- `.trent/tasks/task{NNN}_{name}.md` — Individual task files
- `.trent/phases/phase{N}_{name}.md` — Phase documentation
- `.trent/PLAN.md` — Product Requirements Document
- `.trent/PROJECT_CONTEXT.md` — Project mission

## Task Status Flow

```
[ ] (no file) → [📋] (file created) → [🔄] (in progress) → [✅] (done)
```

**CRITICAL**: Never skip `[📋]`. Always create the task file BEFORE starting work.

## Creating a Task

1. Read `.trent/TASKS.md` to find next available ID for current phase
2. Create `.trent/tasks/task{NNN}_{name}.md` with complete YAML:

```yaml
---
id: {NNN}
title: 'Task Title'
status: pending
priority: medium
phase: {N}
subsystems: [affected]
project_context: Brief connection to project goal
dependencies: []
---

# Task: {Title}

## Objective
[Goal]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

3. Add to TASKS.md as `[📋] Task {NNN}: {Title}`

## Updating Task Status

Update BOTH files atomically (in same response):
- Task file YAML `status:` field
- TASKS.md `[indicator]`

| YAML Status | TASKS.md |
|-------------|----------|
| `pending` | `[📋]` |
| `in-progress` | `[🔄]` |
| `completed` | `[✅]` |
| `failed` | `[❌]` |

## Phase-Based Numbering

| Phase | Task IDs |
|-------|----------|
| 0 | 1-99 |
| 1 | 100-199 |
| 2 | 200-299 |
| N | N×100 to N×100+99 |

## Workflows to Use

- `/trent-task-new` — Create a new task
- `/trent-task-update` — Update task status
- `/trent-status` — View project status
