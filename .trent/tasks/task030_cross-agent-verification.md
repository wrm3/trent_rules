---
id: 30
title: 'Implement Cross-Agent Verification Workflow ([🔍] status)'
type: feature
status: pending
priority: critical
phase: 0
subsystem: verification
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
dependencies: [3, 7]
---

# Task 030: Implement Cross-Agent Verification Workflow

## Objective
Add the mandatory cross-agent verification workflow to trent rules. No task can reach
[✅] without a verified_by field populated by a DIFFERENT agent than the implementer.
This is the structural solution to agent self-reporting lies.

## Background
From `potential_changes.md` Part 5: The proven workflow — Cursor plans/specs, Claude Code
implements, Cursor reviews. The reviewer has no stake in the implementation being correct.
A task is never complete until a different agent context verifies it.

This is the trent equivalent of the Monty Hall insight: always get a second opinion from
an agent that doesn't share context with the first.

## Acceptance Criteria
- [ ] [🔍] Awaiting Verification added as new task status in rules
- [ ] Status progression updated: [🔄] → [🔍] → [✅] (implementer cannot skip [🔍])
- [ ] verified_by field must be populated by different agent (rule enforced, not just documented)
- [ ] evidence_of_completion field required before [🔍] transition
- [ ] Rule: reviewer reads spec FIRST (not implementation), then implementation
- [ ] Rule: reviewer runs tests independently
- [ ] Rule: reviewer produces structured review (required/recommended/minor)
- [ ] Rule: adversarial persona (Gilfoyle-mode) recommended for review agents
- [ ] Verification workflow documented as mandatory — not optional
- [ ] TASKS.md status legend updated with [🔍]
- [ ] Git commit: `feat(template-v2): implement mandatory cross-agent verification workflow`

## Verification Workflow Rule (to implement)

```markdown
### Mandatory Cross-Agent Verification

Every task that modifies code REQUIRES verification by a different agent.

**Status flow**:
[ ] → [📋] → [🔄] → [🔍] → [✅]
                     ↑
            Implementer done, awaiting reviewer

**Implementer responsibilities** (before setting [🔍]):
1. Attach execution evidence (test output, compile log)
2. Set evidence_of_completion.path
3. Commit: "impl: task{id} complete, awaiting verification"
4. Set status: awaiting-verification

**Reviewer responsibilities** (to set [✅]):
1. Read the task SPEC first (not the code)
2. Read the implementation
3. Run tests independently
4. Produce structured review (required/recommended/minor)
5. If PASS: set verified_by (your agent ID), set verified_date, transition [✅]
6. If FAIL: set failure_reason, return to implementer with specific issues

**CRITICAL**: The implementer CANNOT populate verified_by.
A task with verified_by = same agent as implementing agent is a VIOLATION.

**Recommended**: Reviewer agent uses adversarial persona (Gilfoyle-mode):
"I read every line. Here's the verdict."
```

## When Stuck
Rules/template writing task. See `potential_changes.md` Part 5 for full design rationale
and the Meshy API code review example (shows exactly how this workflow should function).
