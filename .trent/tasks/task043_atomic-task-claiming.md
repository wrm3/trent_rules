---
id: 43
title: 'Implement atomic task claiming protocol (git-commit-based claim)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, resilience]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 20]
project_context: 'Without atomic claiming, two agents on the same project at the same time will both claim the same task and overwrite each others work — git commit as the claim lock is the simplest reliable coordination mechanism when there is no central database'
---

# Task 043: Implement atomic task claiming protocol

## Objective
Document and formalize the git-commit-based atomic task claiming protocol in `template_v2/` — the mechanism that prevents two agents from claiming the same task simultaneously when running in parallel without a central coordination server.

## Context
The trent system is file-based (no database in v2). When multiple agents run simultaneously (scheduled or ad-hoc), they could collide on the same task. The solution: use git commits as a distributed lock. An agent that successfully commits a claim "wins" — another agent that pulls and sees the claim already set knows to choose a different task.

## The Atomic Claim Protocol

### Step 1: Pre-Claim Read
```bash
git pull  # always sync before claiming
```
Read the task YAML. Confirm `claimed_by` is null/empty and `status` is `pending`.

### Step 2: Write the Claim (local)
Update the task YAML file ONLY:
```yaml
claimed_by: "{agent_id}"
claimed_at: "{ISO timestamp}"
claim_ttl_minutes: {N}
claim_expires_at: "{claimed_at + ttl}"
status: in_progress
```
Update TASKS.md: `[📋]` → `[🔄]`

### Step 3: Commit Immediately (no other files)
```bash
git add .trent/tasks/task{ID}_*.md .trent/TASKS.md
git commit -m "claim(task-{id}): {agent_id} starting work
TTL: {N} minutes
Expires: {claim_expires_at}"
git push
```

### Step 4: Handle Collision
If `git push` fails (someone else pushed first):
```bash
git pull  # get their changes
# Read the task again — is it now claimed by someone else?
# If yes: select a different task (this one is taken)
# If no: try the commit again (transient failure)
```
Maximum 3 retry attempts. After 3 failures: skip task, log collision, move on.

### Why This Works
Git push is atomic — only one agent can push a commit that claims a given task. The second agent's push will fail with a merge conflict or rejection. The "check after pull" step confirms whether it was a real collision or a transient error.

### Limitations
- Not 100% guaranteed under extreme concurrent load (millisecond-level race)
- Acceptable for 2-10 agents with 1-2 second operations
- For higher parallelism: need database-backed claiming (future v3)

## Heartbeat Protocol (for long tasks)

To keep a claim alive beyond its TTL:
```yaml
# Every 10 minutes during active work, update task YAML:
last_heartbeat: "{ISO timestamp}"
# And commit:
git commit -m "heartbeat(task-{id}): {agent_id} still active ({percent_complete}%)"
git push
```
Cleanup agent: if `now > claim_expires_at` AND `last_heartbeat` is recent (< ttl/2): extend claim by 1 TTL period. If `last_heartbeat` is old: reset claim.

## Acceptance Criteria
- [ ] Atomic claiming protocol documented in task file template or rule files
- [ ] 4-step protocol (read, write, commit, handle collision) documented
- [ ] Heartbeat protocol documented
- [ ] Collision handling (3 retry max) documented
- [ ] Limitations acknowledged in documentation

## Verification Steps
- [ ] Protocol documented in template_v2 rules
- [ ] All 4 steps present
- [ ] Heartbeat mechanism present
- [ ] Collision retry limit defined

## When Stuck
- Pure documentation task — the protocol is defined above, just document it clearly
- The git commit format MUST match the pattern in other claim commits for cleanup agent detection
