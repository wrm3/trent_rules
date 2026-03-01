---
phase: 8
name: 'Final Cleanup & Release'
status: planning
subsystems: [all]
task_range: '800-899'
prerequisites: [0, 1, 2, 3, 4, 5, 6, 7]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 8: Final Cleanup & Release

## Overview
The feature is complete. This phase resets .trent/ to the pristine template state
(so the trent_rules repo ships a clean task management template, not a development
history), then makes the final commit and push.

## CRITICAL: .trent Reset Process

The .trent/ folder in this repo is a TEMPLATE that gets deployed to new projects.
It must not ship with this project's development history.

```powershell
# Step 1: Verify all code is complete and tested
# Step 2: Remove current .trent/ contents (preserve the folder)
Remove-Item G:\trent_rules\.trent\* -Recurse -Force
# Step 3: Copy pristine template back from backup
Copy-Item G:\trent_rules\.trent_bk\* G:\trent_rules\.trent\ -Recurse
# Step 4: Verify .trent/ looks like a clean template
# Step 5: Proceed with final commit
```

## Deliverables
- [ ] All Phase 0-7 tasks completed and verified
- [ ] .trent/ reset to pristine template state from .trent_bk/
- [ ] Final git status shows only intended changes (code, no dev .trent history)
- [ ] Committed and pushed to main

## Acceptance Criteria
- [ ] git diff shows only: new SQL file, new Python files, updated hooks, updated docs
- [ ] .trent/ contents match .trent_bk/ (the pristine template)
- [ ] All 4 adapters confirmed working
- [ ] AGENTS.md and CLAUDE.md updated
- [ ] Push succeeded
