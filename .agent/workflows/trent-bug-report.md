---
description: "Report and document a bug with proper tracking in BUGS.md and TASKS.md"
---

# Workflow: trent-bug-report

Report and document a bug with full tracking integration.

## Steps

### Step 1: Read Current Bugs

// turbo
Read `.trent/BUGS.md` to determine the next BUG-{N} number and `.trent/TASKS.md` to determine the next task ID.

### Step 2: Gather Bug Information

Ask the user for (if not already provided):
- **What happened**: Actual behavior observed
- **What should happen**: Expected behavior
- **Steps to reproduce**: How to trigger the bug
- **Severity**: Critical, High, Medium, or Low
- **Environment**: OS, version, configuration

### Step 3: Create BUGS.md Entry

Add to `.trent/BUGS.md`:

```markdown
### Bug ID: BUG-{N}
- **Title**: {Brief description}
- **Severity**: {Critical/High/Medium/Low}
- **Source**: {User Reported/Development/Testing/Production}
- **Status**: Open
- **Task Reference**: Task {task_id}
- **Created**: {date}
- **Description**: {what's wrong}
- **Steps to Reproduce**:
  1. {step}
- **Expected**: {expected behavior}
- **Actual**: {actual behavior}
```

### Step 4: Create Bug Task

Create `.trent/tasks/task{NNN}_bug_{description}.md` with:

```yaml
---
id: {NNN}
title: '[BUG] {Brief description}'
type: bug_fix
status: pending
priority: {severity}
phase: {affected_phase}
subsystems: [{affected_subsystems}]
bug_reference: BUG-{N}
severity: critical|high|medium|low
---
```

### Step 5: Update TASKS.md

Add under the appropriate phase section:
```
- [ ] Task {NNN}: [BUG] {Brief description}
```

Then update to `[📋]` after creating the task file.

### Step 6: Confirm

Report the bug ID, task ID, and next recommended action (start investigation or fix).
