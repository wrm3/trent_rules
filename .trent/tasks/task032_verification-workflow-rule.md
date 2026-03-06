---
id: 32
title: 'Create mandatory verification workflow rule (implementer ≠ verifier)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [verification, agent-rules]
ai_safe: true
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [30, 31]
project_context: 'The verification rule is the structural solution to AI agent self-reporting bias — formalizing that the agent who wrote the code cannot be the one who marks it complete prevents the single biggest source of false completions'
---

# Task 032: Create mandatory verification workflow rule

## Objective
Create a formal verification workflow rule in `template_v2/` rule files — the complete protocol for how tasks move from `[🔄]` → `[🔍]` → `[✅]`, with explicit enforcement that the implementing agent and verifying agent MUST be different.

## Context
This is the formalization of the user's proven Cursor-reviews-Claude-Code workflow into the system itself. The key insight: AI agents that implement code will rationalize away their own mistakes. A fresh agent with no implementation history will spot the problems the implementer rationalized. This isn't a trust issue — it's a cognitive architecture issue.

## The Complete Verification Workflow

```
IMPLEMENTER AGENT:
[ ] or [📋] → [🔄] → (work done) → fill evidence_of_completion → [🔍]
commit: "impl(task-{id}): complete — awaiting verification"

VERIFIER AGENT (different agent_id):
[🔍] → check evidence_of_completion → run verification_commands → judge

IF PASSES: [🔍] → [✅]
  - Update verified_by, verified_at
  - commit: "verify(task-{id}): verified by {agent_id} — APPROVED"

IF FAILS: [🔍] → [🔄] (back to implementer)
  - Document failure reason
  - commit: "verify(task-{id}): returned to implementer — {failure_details}"
```

## Enforcement Rules (add to trent rules in template_v2)

### MANDATORY — Cannot Be Skipped:
1. A task CANNOT reach `[✅]` without `verified_by:` being set to a different agent than `claimed_by:`
2. A task CANNOT be marked `[✅]` by the same agent that set it to `[🔍]`
3. If `verified_by == claimed_by`: this is a SYSTEM VIOLATION — revert to `[🔍]`

### For autonomous unattended runs:
- If only one agent is running (solo sprint), skip verification for `ai_safe: true, blast_radius: low` tasks only
- Solo exception MUST be logged: `solo_verification_exception: true` in YAML
- Solo exception CANNOT be used for `blast_radius: medium+` tasks

### For the human (when reviewing):
- Human approval counts as verification
- Human sets `verified_by: human`, `verified_at: {timestamp}`
- Human can override verification failure: set `human_override: true` with reason

## What Verifiers Check

Beyond evidence_of_completion, verifiers should apply:
1. **Does the code compile/run without errors?**
2. **Does it actually do what the task spec says?** (read acceptance criteria)
3. **Did it introduce anything obviously broken?** (linter, imports, syntax)
4. **Is the evidence_of_completion honest?** (spot-check 1-2 items independently)
5. **Are there any obvious security issues?** (for tasks touching auth, data, external APIs)

Verifiers should NOT:
- Rubber-stamp: "looks good" without checking
- Re-implement: their job is verify, not improve
- Scope-creep: don't fail for things not in acceptance criteria

## Acceptance Criteria
- [ ] Verification workflow rule added to `template_v2/.cursor/rules/` (and .claude, .agent)
- [ ] Workflow diagram (implementer → verifier → approved/returned) documented
- [ ] `verified_by ≠ claimed_by` enforcement rule documented
- [ ] Solo verification exception documented with constraints
- [ ] Human override documented
- [ ] What verifiers check (and don't check) documented
- [ ] Parity: .cursor, .claude, .agent rule files updated

## Verification Steps
- [ ] Rule file exists in template_v2 (all 3 IDE directories)
- [ ] `verified_by ≠ claimed_by` rule is explicit (not just implied)
- [ ] Solo exception is documented with its constraints
- [ ] Human override path documented

## When Stuck
- This is a rules documentation task — write the workflow in clear, unambiguous language
- The strictest possible language is better: "CANNOT", "MUST", "SYSTEM VIOLATION"
- Vague language like "should" gets ignored by agents
