---
id: 74
title: 'Update 27_trent_self_improvement rule with SYSTEM_EXPERIMENTS.md'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [5]
project_context: 'Rule 27 detects system issues — must be updated to write accepted improvements to SYSTEM_EXPERIMENTS.md and check that file before re-proposing ideas that were already tried or rejected'
---

# Task 074: Update 27_trent_self_improvement rule with SYSTEM_EXPERIMENTS.md

## Objective
Create updated `27_trent_self_improvement.md` in `template_v2/` that integrates SYSTEM_EXPERIMENTS.md into the issue reporting workflow — checking for prior attempts before proposing, and logging accepted improvements.

## Key Addition: Pre-Proposal Check

Add before Step 2 (Propose Solution):

```markdown
### Step 1.5: Check SYSTEM_EXPERIMENTS.md Before Proposing

Before proposing any improvement:
1. Read `.trent/SYSTEM_EXPERIMENTS.md`
2. Check `## Rejected Ideas` — is this idea already there?
   - If yes: DO NOT re-propose. Reference the rejection: "This was rejected as REJ-{ID} on {date}: {reason}"
3. Check `## Completed Experiments` — was this tried and found successful?
   - If yes: it's already implemented — investigate why it's failing again
4. Check `## Active Experiments` — is this currently being monitored?
   - If yes: note the experiment ID in your proposal

This prevents proposing ideas that were already tried, implemented, or explicitly rejected.
```

## Key Addition: Post-Acceptance Logging

Add after user accepts a proposed improvement:

```markdown
### After User Accepts (Step 4: Log to SYSTEM_EXPERIMENTS.md)

When user accepts an improvement (responds "1" or "Accept"):
1. Add entry to `.trent/SYSTEM_EXPERIMENTS.md` under `## Active Experiments`
2. Use next available EXP-NNN ID
3. Entry format:
   ```markdown
   ### EXP-{NNN}: {Improvement Title}
   **Status**: monitoring
   **Started**: {today}
   **Proposed By**: AI
   **Hypothesis**: This change will improve {metric} because {reason}
   **Change Made**: {specific files/rules changed}
   **Monitoring**: {how we'll know in 2-4 weeks if it worked}
   ```
4. After 4 weeks (cleanup agent moves to Completed with outcome)
```

## Key Addition: Post-Rejection Logging

When user declines (responds "2" or "Decline"):
```markdown
### After User Declines (Log to SYSTEM_EXPERIMENTS.md)

Add to `## Rejected Ideas`:
### REJ-{NNN}: {Idea Title}
**Date**: {today}
**Proposed By**: AI
**Summary**: {what was proposed}
**Why Rejected**: {user's reason if given, or "User declined without reason"}
**Do Not Re-Propose**: true
```

## Acceptance Criteria
- [ ] Rule file updated in template_v2 (all 3 IDEs)
- [ ] Pre-proposal check against SYSTEM_EXPERIMENTS.md documented
- [ ] Post-acceptance EXP logging documented
- [ ] Post-rejection REJ logging documented

## Verification Steps
- [ ] Pre-proposal check is before "Propose Solution" step
- [ ] Both EXP and REJ logging paths documented

## When Stuck
- Start from existing 27_trent_self_improvement rule, add 3 new sections
