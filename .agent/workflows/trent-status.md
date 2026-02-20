---
description: "Show current project status - tasks, phases, and progress overview"
---

# Workflow: trent-status

Show current project status with tasks, phases, and progress.

## Steps

### Step 1: Read Core Files

// turbo
Read:
- `.trent/TASKS.md`
- `.trent/PROJECT_CONTEXT.md`

### Step 2: Run Sync Validation

Check that task files match TASKS.md entries:

```
📋 TRENT SYNC VALIDATION

Task Sync Check:
- Compare .trent/tasks/ files against TASKS.md entries
- Report: X synced, Y mismatches, Z orphans

Phase Sync Check:
- Compare .trent/phases/ files against TASKS.md headers
- Report: X synced, Y mismatches, Z orphans

Status: ALL SYNCED ✅ / ISSUES FOUND ⚠️
```

Fix any sync issues found.

### Step 3: Display Status Report

Show a comprehensive status report:

```
📋 PROJECT CONTEXT
🎯 Mission: {from PROJECT_CONTEXT.md}

📊 PHASE OVERVIEW
Phase 0: {name} [{status}]
Phase 1: {name} [{status}]
...

📈 TASK SUMMARY
Total Tasks: {N}
✅ Completed: {N}
🔄 In Progress: {N}
📋 Ready: {N}
⬜ Pending: {N}
❌ Failed: {N}

🔄 ACTIVE TASKS (In Progress)
{list of [🔄] tasks}

📋 NEXT UP (Ready to Start)
{list of [📋] tasks}

🐛 ACTIVE BUGS
{list from BUGS.md if any}
```
