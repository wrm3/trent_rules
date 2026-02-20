---
description: "Update a task status. Usage: /trent-task-update [task ID] [new status: pending|ready|in-progress|completed|failed|paused]"
---

# Workflow: trent-task-update

Update a task's status with atomic sync between task file and TASKS.md.

## Steps

### Step 1: Read Current State

Read the task file at `.trent/tasks/task{ID}_*.md` and current TASKS.md entry.
Verify they are in sync before making changes.

### Step 2: Validate Transition

Check the status transition is valid:
```
[ ] → [📋] = File must be created first
[📋] → [🔄] = OK, start working
[🔄] → [✅] = Run completion validation first
[🔄] → [❌] = OK, mark as failed
Any → [⏸️] = OK, pause
```

### Step 3: Update Task File

Update the YAML frontmatter in the task file:
- Change `status:` to the new value
- Add `completed_date:` if completing
- Add any relevant notes

### Step 4: Update TASKS.md (ATOMIC)

Update the status indicator in TASKS.md to match:

| Status | TASKS.md Indicator |
|--------|-------------------|
| pending | `[ ]` |
| ready | `[📋]` |
| in-progress | `[🔄]` |
| completed | `[✅]` |
| failed | `[❌]` |
| paused | `[⏸️]` |

### Step 5: Completion Actions (if completing)

If marking as completed:
1. Run validation: code compiles, acceptance criteria met
2. Update both files atomically
3. Offer git commit
4. Check if AGENTS.md needs updating (new tools/features added?)

### Step 6: Confirm Sync

```
✅ Task Sync Confirmation:
- Task {ID} file: status: {new_status} ✅
- TASKS.md entry: [{indicator}] ✅
- Sync verified: ✅
```
