---
id: 50
title: 'Add frequent git commit enforcement (every state transition)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, agent-rules, resilience]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [43, 49]
project_context: 'Frequent commits = frequent checkpoints = crash recovery — an agent that commits after every acceptance criterion means at most that criterion is lost on crash, not the whole task'
---

# Task 050: Add frequent git commit enforcement

## Objective
Add explicit git commit frequency rules to `template_v2/` — mandating commits at every meaningful state transition so that crashes, rate limits, and disconnections lose at most one checkpoint of work.

## The Mandatory Commit Points

Add to task rules and sprint agent spec:

```markdown
## Mandatory Git Commits

**Rule**: Every state transition MUST be committed to git immediately.
**Why**: Git commits are your crash recovery checkpoints.

### Required commit points (in order):

1. **Task Claim** (always):
   ```bash
   git commit -m "claim(task-{id}): {agent_id} starting work"
   ```

2. **Pre-Mortem Complete** (after filling pre-mortem):
   ```bash
   git commit -m "premortem(task-{id}): pre-implementation analysis complete"
   ```

3. **Spec Updated** (if spec_freshness update needed):
   ```bash
   git commit -m "spec(task-{id}): update spec v{old} → v{new} — {reason}"
   ```

4. **Each Acceptance Criterion Met** (after each ✅):
   ```bash
   git commit -m "progress(task-{id}): criterion N/{total} — {brief description}"
   ```

5. **Before Any Destructive Operation**:
   ```bash
   git commit -m "checkpoint(task-{id}): pre-{operation} state saved"
   ```

6. **Every ~15 Minutes** (heartbeat during long criteria):
   ```bash
   git commit -m "heartbeat(task-{id}): {agent_id} — {percent}% complete"
   ```

7. **Implementation Complete** (before setting awaiting_verification):
   ```bash
   git commit -m "impl(task-{id}): complete — {summary of what was done}"
   ```

8. **Clean Exit** (if stopping before completion):
   ```bash
   git commit -m "checkpoint(task-{id}): stopping — {reason} — resumable from {next_step}"
   ```
```

## What NOT to Batch

The temptation is to batch all changes into one big commit. This is WRONG for autonomous operation.

Each of the above commit points must be its own commit because:
- Another agent reading `git log` needs to see the granular history
- If a crash occurs, the last commit is the recovery point — granular = less work lost
- The cleanup agent uses commit patterns to detect stuck/expired claims

## Push Frequency

After every commit: `git push` immediately.
If push fails: retry 3 times, then log failure and continue (working commits are still local).

## Acceptance Criteria
- [ ] 8 mandatory commit points documented in task rules
- [ ] "What NOT to batch" explanation included
- [ ] Push frequency rule documented
- [ ] Commit message format for each checkpoint type defined
- [ ] Parity: rules in .cursor, .claude, .agent templates

## Verification Steps
- [ ] All 8 commit points listed
- [ ] Push-after-commit rule documented
- [ ] Formats consistent with task049 commit prefix table

## When Stuck
- Pure documentation task
- Cross-reference task049 (commit prefix table) — formats must match
