---
id: 7
title: 'Add new status values to trent status system (template_v2)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [template-core, agent-rules]
ai_safe: true
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [1, 3]
project_context: 'New status values [🔍] [⏳] [🌾] cover verification, resource-gating, and harvested experiments — gaps in current system that cause tasks to get stuck with no accurate status'
---

# Task 007: Add new status values to trent status system

## Objective
Add three new task status values to `template_v2/` — `[🔍]` (Awaiting Verification), `[⏳]` (Resource-Gated), and `[🌾]` (Harvested) — with corresponding YAML status values, rules, and enforcement logic. Update all template files and rule templates to include these.

## Context
Current status system gaps:
- No way to express "implementation done, waiting for another agent to verify" → causes tasks to sit at `[🔄]` past completion
- No way to express "task is ready but blocked on GPU/storage/API credits" → these look identical to dependency-blocked tasks
- No way to preserve a completed approach that was later abandoned but is worth keeping for reference → gets incorrectly deleted

## The Three New Statuses

### `[🔍]` — Awaiting Verification
- **Meaning**: Implementation complete, task file updated to `status: awaiting_verification`, waiting for a DIFFERENT agent to verify
- **YAML value**: `status: awaiting_verification`
- **Entered from**: `[🔄]` (in_progress) when implementer finishes
- **Exits to**: `[✅]` (if verifier approves) or `[🔄]` (if verifier finds issues)
- **TTL**: 4 hours (if no verifier picks it up, cleanup agent re-queues)
- **Rule**: The agent that implemented CANNOT be the one to verify

### `[⏳]` — Resource-Gated
- **Meaning**: Task is ready to execute but blocked on an external resource (GPU, storage, API credits, 3rd party service)
- **YAML value**: `status: resource_gated`
- **Fields**: `resource_requirement: {type: gpu|storage|api_credits|service, details: "...", estimated_available: "YYYY-MM-DD"}`
- **Entered from**: `[📋]` when agent determines it cannot proceed due to resource
- **Exits to**: `[📋]` when resource becomes available (cleanup agent checks)
- **Rule**: Cleanup agent checks `estimated_available` date and moves back to `[📋]` when past

### `[🌾]` — Harvested
- **Meaning**: Task was completed but the approach was later abandoned (pivot, better solution found, feature descoped). The work is preserved as reference but not in active use.
- **YAML value**: `status: harvested`
- **Fields**: `harvest_reason: "..."`, `harvest_date: "YYYY-MM-DD"`, `harvest_reference: "task_id or commit hash"`
- **Entered from**: `[✅]` when a completed task's output is superseded
- **Never exits to anything** — terminal state like `[❌]`
- **Rule**: Harvested tasks remain in TASKS.md with `[🌾]` so their work is discoverable

## Acceptance Criteria
- [ ] All three status values documented in `template_v2/.trent/TASKS.md` status legend
- [ ] `status: awaiting_verification` added to YAML schema (task003)
- [ ] `status: resource_gated` added to YAML schema with `resource_requirement` field
- [ ] `status: harvested` added to YAML schema with `harvest_reason`, `harvest_date`, `harvest_reference` fields
- [ ] Status transition diagram updated (where applicable in rule templates)
- [ ] Cleanup agent spec (task040) references `[🔍]` TTL expiry check
- [ ] `agents.md` template status table updated in `template_v2/`

## Implementation Notes
- The emoji-to-YAML mapping: `[🔍]` = `awaiting_verification`, `[⏳]` = `resource_gated`, `[🌾]` = `harvested`
- These changes go in template_v2/ ONLY — do not touch live rules
- The TASKS.md status legend in template_v2 should be the canonical reference

## Verification Steps
- [ ] `template_v2/.trent/TASKS.md` status legend shows all 9 status values
- [ ] Task YAML schema includes all 3 new `status:` values in the enum
- [ ] `resource_requirement` YAML structure is defined in schema
- [ ] `harvest_reason` + `harvest_date` + `harvest_reference` in schema
- [ ] agents.md template in template_v2 shows updated status table

## When Stuck
- Cross-reference task003 (YAML schema) — add fields there first, then update legend here
