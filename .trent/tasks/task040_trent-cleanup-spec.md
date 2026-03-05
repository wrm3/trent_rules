---
id: 40
title: 'Create @trent-cleanup Command Spec'
type: feature
status: pending
priority: high
phase: 0
subsystem: autonomous
ai_safe: true
requires_solo_agent: false
blast_radius: low
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 60
claim_ttl_minutes: 120
dependencies: [3, 20, 21]
---

# Task 040: Create @trent-cleanup Command Spec

## Objective
Create the complete specification for the `@trent-cleanup` command — the midnight agent
that maintains project health, resets expired claims, curates task lists, generates health
scores, and prepares SPRINT.md for the next autonomous sprint.

## Background
From `potential_changes.md` Idea P: The cleanup agent is the janitor that makes autonomous
operation sustainable. Without it, stale claims accumulate, orphan tasks pile up, and the
queue becomes unworkable. It runs on a schedule (cron), requires no human input, and
produces a CLEANUP_REPORT.md that becomes the morning briefing.

## Acceptance Criteria
- [ ] @trent-cleanup command created in template_v2/.cursor/commands/ and .claude/commands/
- [ ] CLEANUP_REPORT.md template created in template_v2/.trent/templates/
- [ ] Cleanup agent responsibilities fully documented
- [ ] Health score formula defined (per-project and per-subsystem)
- [ ] Squeaky wheel detection logic defined (which subsystem is blocking)
- [ ] TTL expiry reset logic documented (from task020)
- [ ] Orphan/phantom task detection logic documented
- [ ] SPRINT.md population logic documented (how it selects tasks)
- [ ] ai_safe filter documented (only ai_safe: true tasks in unattended sprint)
- [ ] Git commit convention for cleanup runs documented
- [ ] Git commit: `feat(template-v2): add trent-cleanup command and spec`

## Cleanup Agent Responsibilities (to document)

### Step 1: Sync Validation
- Check TASKS.md vs task files (existing sync check)
- Check phase files vs TASKS.md headers

### Step 2: TTL Expiry Check
- Find all [🔄] tasks where claim_expires_at < now
- Reset to [📋], add failure_reason: agent_timeout to failure_history
- Commit: "cleanup: reset N expired task claims"

### Step 3: Orphan/Phantom Detection
- Orphans: task files with no TASKS.md entry → flag for human
- Phantoms: TASKS.md entries with no task file → flag or create stub

### Step 4: Health Score Generation
```
Per subsystem:
  complete_pct = completed / total
  blocked_count = [❌] + [⏳] tasks
  stale_count = [🔄] tasks with expired claims
  awaiting_verification_count = [🔍] tasks
  health = green if complete_pct > 80% and blocked_count == 0
           yellow if blocked_count > 0 or complete_pct < 60%
           red if stale_count > 2 or awaiting_verification_count > 5

Project health = weighted average of subsystem healths
```

### Step 5: SPRINT.md Population
```
Select up to 15 tasks:
  Priority 1: [🔍] awaiting verification (route to review agent)
  Priority 2: blocked tasks that became unblocked (dependencies complete)
  Priority 3: ai_safe: true tasks with no unresolved failure_history
  Priority 4: oldest pending tasks with no blockers
Filter: exclude requires_solo_agent: true if any other [🔄] tasks in same subsystem
```

### Step 6: CLEANUP_REPORT.md Generation
```markdown
# Cleanup Report — YYYY-MM-DD HH:MM UTC

## Health Summary
[per-project and per-subsystem health table]

## Actions Taken
- Reset N expired claims
- [other actions]

## Requires Human Attention
- [tasks with approach_wrong failures]
- [tasks escalation_needed]
- [high blast_radius tasks needing human approval]

## Sprint Ready
N tasks queued in SPRINT.md for next autonomous sprint
```

### Step 7: Git Commit
```
cleanup(project): midnight run YYYY-MM-DD
- Reset N stale claims
- Health: {overall score}
- Sprint: N tasks queued
- Attention needed: N items
```

## When Stuck
This is a specification/rules writing task. Reference `potential_changes.md` Ideas P and S.
The cleanup agent does NOT fix code — it manages task state and generates reports only.
