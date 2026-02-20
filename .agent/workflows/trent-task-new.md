---
description: "Create a new trent task with proper file and TASKS.md entry. Usage: /trent-task-new [task title and description]"
---

# Workflow: trent-task-new

Create a new trent task with the proper file and TASKS.md entry.

## Steps

### Step 1: Read Current State

Read `.trent/TASKS.md` to:
- Determine the next available task ID for the current phase
- Identify which phase this task belongs to
- Check for any dependencies

### Step 2: Assess Complexity

Score the task complexity (1-10+):
- >2-3 developer days: +4 pts
- Multiple subsystems affected: +3 pts
- Multiple unrelated modules: +3 pts
- High uncertainty: +2 pts

**If score ≥ 7**: Expand into sub-tasks before proceeding.

### Step 3: Create Task File

Create `.trent/tasks/task{NNN}_{descriptive_name}.md` with:

```yaml
---
id: {NNN}
title: '{Task Title}'
type: feature|bug_fix|refactor|documentation
status: pending
priority: critical|high|medium|low
phase: {phase_number}
subsystems: [{affected_subsystems}]
project_context: {brief connection to project goal}
dependencies: []
---

# Task: {Title}

## Objective
{Clear, actionable goal}

## Acceptance Criteria
- [ ] {Specific outcome 1}
- [ ] {Specific outcome 2}

## Implementation Notes
{Technical details, constraints}
```

### Step 4: Update TASKS.md

Add to `.trent/TASKS.md` under the appropriate phase section:
```
- [📋] Task {NNN}: {Title}
```

### Step 5: Confirm

Report the created task ID, file path, and any sub-tasks if complexity was high.
