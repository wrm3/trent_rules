---
id: 21
title: 'Implement Failure Taxonomy (failure_reason enum)'
type: feature
status: pending
priority: critical
phase: 0
subsystem: resilience
ai_safe: true
requires_solo_agent: false
blast_radius: low
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 45
claim_ttl_minutes: 90
dependencies: [3]
---

# Task 021: Implement Failure Taxonomy

## Objective
Add a standardized failure taxonomy to the trent system so that failed tasks carry
actionable diagnostic information. "Why did this fail?" must be answerable from the
task file without reading logs. This powers the escalation ladder and Ralph Wiggum
prevention.

## Background
From `potential_changes.md` Idea O: Without a failure taxonomy, a pile of [❌] tasks
gives no signal about what kind of help is needed. With it, the cleanup agent can route:
- `spec_outdated` → refresh spec before retry
- `escalation_needed` → promote to better model
- `approach_wrong` → flag for human, don't auto-retry
- `agent_timeout` → reset claim, retry with fresh agent

## Acceptance Criteria
- [ ] failure_reason enum defined in rules with all values and their meanings
- [ ] failure_history YAML structure defined in task template (task003)
- [ ] Each failure_reason maps to a recommended next action
- [ ] Rule added: before attempting a task with failure_history, agent MUST read prior failures
- [ ] Rule added: agent MUST explicitly acknowledge prior failures and state different approach
- [ ] Ralph Wiggum prevention rule added (after N failures with same failure_reason → escalate)
- [ ] approach_history YAML structure defined (what was tried, what worked)
- [ ] Git commit: `feat(template-v2): add failure taxonomy and Ralph Wiggum prevention`

## Failure Taxonomy (to implement in rules)

| failure_reason | Meaning | Recommended Next Action |
|----------------|---------|------------------------|
| `compilation_error` | Code doesn't compile/parse | Run lint/compile check first, fix errors |
| `test_failure` | Tests ran but failed | Read test output, fix specific failures |
| `resource_unavailable` | Storage/compute/API not available | Use [⏳] status, wait for resource |
| `spec_outdated` | Spec references old API/library/approach | Update spec (allow_spec_update: true) |
| `approach_wrong` | Method fundamentally won't work | Flag for human review, don't auto-retry |
| `dependencies_missing` | Other tasks must complete first | Check dependencies, wait |
| `escalation_needed` | Beyond this model's capability | Promote to better model |
| `timeout` | Ran out of time/tokens mid-task | Use checkpointing, resume |
| `agent_timeout` | Agent died (bluescreen/disconnect) | Reset claim, fresh agent starts |

## Ralph Wiggum Prevention Rule (to add)

```markdown
### Ralph Wiggum Loop Prevention

If a task has 2+ failures with the same failure_reason:
- 3rd attempt MUST include failure logs from all prior attempts
- 3rd attempt MUST explicitly state: "Previous approaches failed due to [reason].
  I will try [different specific approach] instead."
- If failure_reason is approach_wrong: DO NOT auto-retry, flag for human review
- If same failure_reason persists after 3 attempts: set failure_reason: escalation_needed
```

## When Stuck
Rules/template writing task. Reference `potential_changes.md` Idea O for full rationale.
