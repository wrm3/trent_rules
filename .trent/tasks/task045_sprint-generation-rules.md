---
id: 45
title: 'Create SPRINT.md generation rules (cleanup agent populates from tasks)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [4, 40, 44]
project_context: 'Rules for HOW the cleanup agent selects and ranks tasks into SPRINT.md — the selection algorithm determines what gets done autonomously overnight, needs to be deterministic and auditable'
---

# Task 045: Create SPRINT.md generation rules

## Objective
Document the SPRINT.md task selection algorithm in `template_v2/` — the rules the cleanup agent follows when deciding which tasks to include in the next sprint queue.

## The Selection Algorithm

### Step 1: Eligibility Filter (MUST pass ALL)
A task is eligible for SPRINT.md if and only if:
- `ai_safe: true`
- `status: pending` (task file exists, not started)
- TASKS.md shows `[📋]` (not `[ ]` — file must exist)
- All `dependencies` are in `status: completed`
- `blast_radius: low` or `medium` (never high/critical)
- `requires_solo_agent: false` OR (true AND no other tasks in sprint)
- NOT `resource_gated` (status: pending, not resource_gated)
- spec_last_verified < staleness_days old (or allow_spec_update: true)

### Step 2: Ranking (sort eligible tasks)
Sort by the following criteria in order:
1. **Priority**: critical > high > medium > low
2. **Blocking factor**: tasks that are blocking other tasks rank higher
3. **Age**: older pending tasks rank higher (prevent starvation)
4. **Blast radius**: low > medium (prefer safer within same priority)
5. **Effort**: shorter tasks (≤2h) rank higher than longer ones (prefer completing over starting)

### Step 3: Solo Task Handling
If a `requires_solo_agent: true` task is #1 in the ranked list:
- Include it as the ONLY task (sprint max = 1)
- Add ⚠️ SOLO SPRINT warning to SPRINT.md header

### Step 4: Capacity Fill
Fill up to `max_sprint_tasks` slots (default: 15) from the ranked eligible list.

### Step 5: Exclusion Summary
For every ineligible task, categorize the exclusion reason:
- `not_ai_safe` — ai_safe: false
- `no_task_file` — status `[ ]` in TASKS.md
- `dependency_blocked` — dependency not completed
- `resource_gated` — resource unavailable
- `blast_radius_excluded` — high or critical
- `stale_spec` — spec too old and allow_spec_update: false
- `already_claimed` — another agent has it

### Step 6: Write SPRINT.md
Overwrite `.trent/SPRINT.md` with:
- Metadata header (generated_at, valid_until = +2h, generating_agent)
- Ranked task table
- Exclusion summary table
- Sprint Rules (from template)

## Acceptance Criteria
- [ ] Selection algorithm (5 steps) documented in cleanup agent rule/command
- [ ] Eligibility criteria (all-must-pass) listed
- [ ] Ranking criteria (order-of-priority) listed
- [ ] Solo task handling documented
- [ ] Exclusion categories listed
- [ ] SPRINT.md overwrite behavior documented (overwrites, not appends)

## Verification Steps
- [ ] All 6 algorithm steps present
- [ ] Eligibility is all-must-pass (not any-one)
- [ ] 6 exclusion categories defined
- [ ] Solo sprint override behavior documented

## When Stuck
- Cross-reference task040 (cleanup spec) and task004 (SPRINT.md template)
- This task is specifically about the ALGORITHM — how cleanup agent DECIDES what goes in the sprint
