---
id: 5
title: 'Create SYSTEM_EXPERIMENTS.md template'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1]
project_context: 'System evolution log — captures what the trent system tried, what worked, what failed, so the next AI context or project can learn from it without re-reading the whole session history'
---

# Task 005: Create SYSTEM_EXPERIMENTS.md template

## Objective
Create `template_v2/.trent/SYSTEM_EXPERIMENTS.md` — a living log of system-level experiments, rule changes, and AI-initiated improvements. This is the trent system's own equivalent of the VisionLang `experiment_log.txt` — a record of what was tried on the *system itself*, not on project features.

## Context
The self-improvement protocol (rule 27) detects issues but has no persistent memory of what was already tried. When a new AI session starts, it may re-propose ideas that were already rejected or already implemented. SYSTEM_EXPERIMENTS.md solves this by logging every significant rule change, workflow experiment, or AI suggestion with its outcome.

## Acceptance Criteria
- [ ] File exists at `template_v2/.trent/SYSTEM_EXPERIMENTS.md`
- [ ] Contains an `Active Experiments` section for ongoing changes being monitored
- [ ] Contains a `Completed Experiments` section with outcome (success/failed/partial)
- [ ] Contains a `Rejected Ideas` section so AI doesn't re-propose them
- [ ] Each entry has: date, proposed_by (human/AI/agent_id), description, hypothesis, outcome, lessons_learned
- [ ] Header clearly states this is for *system-level* experiments, not feature work
- [ ] Cross-references IDEA_BOARD.md (promoted system ideas land here)

## Template Content

```markdown
# SYSTEM_EXPERIMENTS.md
## trent System Evolution Log

This file tracks changes and experiments made to the trent system itself —
rule modifications, workflow changes, template updates, and AI-initiated
improvements. It prevents re-proposing rejected ideas and captures lessons
for future AI sessions.

**Scope**: System-level changes only. Feature work goes in TASKS.md.
**Updated By**: Cleanup agent (nightly) + human + AI during sessions

---

## Active Experiments

### EXP-001: [Experiment Title]
**Status**: monitoring
**Started**: YYYY-MM-DD
**Proposed By**: human | AI | {agent_id}
**Hypothesis**: [What we expect this change to improve]
**Change Made**: [What was actually changed — file, rule, template]
**Monitoring**: [How we'll know if it worked — metric, observation, timeframe]

---

## Completed Experiments

### EXP-000: [Example Completed Experiment]
**Status**: success | failed | partial
**Completed**: YYYY-MM-DD
**Proposed By**: human
**Hypothesis**: Cross-agent verification would reduce false completions
**Change Made**: Added `[🔍]` status and `verified_by` field to task YAML
**Outcome**: [What actually happened]
**Lessons Learned**: [What future sessions should know]
**Reference**: task030_cross-agent-verification.md

---

## Rejected Ideas

### REJ-001: [Idea That Was Considered But Rejected]
**Date**: YYYY-MM-DD
**Proposed By**: AI
**Summary**: [What was proposed]
**Why Rejected**: [Reason — too complex, not needed, conflicts with X, user declined]
**Do Not Re-Propose**: true

---

## Experiment ID Registry
Last EXP ID: EXP-000
Last REJ ID: REJ-000
```

## Implementation Notes
- IDs use `EXP-NNN` for experiments and `REJ-NNN` for rejections
- Cleanup agent should scan self-improvement rule outputs and auto-add `Active Experiments` entries for any accepted changes
- This file is the memory layer for the trent system's own evolution — treat it like TASKS.md treats project tasks

## Verification Steps
- [ ] File exists at correct path
- [ ] All three sections present (Active, Completed, Rejected)
- [ ] ID registry section at bottom
- [ ] Clear scope statement in header

## When Stuck
- Pure template task — no logic required
- Keep it simple; the AI writing to this file later will add the actual entries
