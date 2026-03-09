---
name: trent-task-update
description: Step-by-step workflow for updating task status, both in task file and TASKS.md atomically.
---
# trent-task-update

## When to Use
Changing task status (start working, mark complete, pause, fail).

## Status Transitions
```
[ ] → [📋] → [🔄] → [🔍] → [✅]
              ↓         ↓
             [⏸️]       [📋] (verification failed — reset)
             [❌]
```

## Steps

1. **Read current state** (both files):
   - `.trent/tasks/taskNNN_*.md` → current YAML `status:`
   - `.trent/TASKS.md` → current indicator for task NNN
   - Verify they match — if not, fix mismatch first (file is source of truth)

2. **Apply transition**:

| Action | File YAML | TASKS.md |
|---|---|---|
| Start working | `status: in-progress` | `[🔄]` |
| Submit for verification | `status: awaiting-verification` | `[🔍]` |
| Mark complete (verifier only) | `status: completed` | `[✅]` |
| Pause | `status: paused` | `[⏸️]` |
| Mark failed | `status: failed` | `[❌]` |

3. **For in-progress**: also set:
```yaml
claimed_by: "{agent_id}"
claimed_at: "YYYY-MM-DDTHH:MM:SSZ"
claim_ttl_minutes: {estimated * 1.5}
claim_expires_at: "YYYY-MM-DDTHH:MM:SSZ"
```

4. **For completed**: run full completion workflow (see trent-task-manager):
   - Validate acceptance criteria
   - Offer git commit
   - Check project files impact

5. **Print sync confirmation**:
```
Task Sync Confirmation:
- Task {ID} file: status: {new_status} ✅
- TASKS.md entry: [{indicator}] ✅
- Sync verified: ✅
```
