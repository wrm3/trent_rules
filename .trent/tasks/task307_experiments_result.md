---
id: 307
title: 'SYSTEM_EXPERIMENTS.md result field + memory capture wiring'
type: feature
status: pending
priority: medium
phase: 3
subsystem: memory
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "SYSTEM_EXPERIMENTS.md already tracks proposed improvements with hypothesis + expected impact. Adding an experiment_result YAML field and wiring it to memory_capture_insight enables the system to learn which rule changes actually reduced task failure rates over time."
---

# Task 307: SYSTEM_EXPERIMENTS result field + memory wiring

## Objective
1. Update SYSTEM_EXPERIMENTS.md template to add `experiment_result` field
2. Update `27_trent_self_improvement.mdc` rule: when closing an experiment, call `memory_capture_insight`
3. Add `memory_search` suggestion to experiment review flow: "check if similar experiment was tried before"

## Acceptance Criteria
- [ ] SYSTEM_EXPERIMENTS.md template (in template_v2) has `experiment_result` field
- [ ] 27_trent_self_improvement rule instructs AI to call memory_capture_insight when closing experiment
- [ ] Rule instructs AI to call memory_search at start of experiment proposal ("has this been tried?")
- [ ] Synced to .claude and .agent versions

## New experiment_result field format
```yaml
experiment_result:
  outcome: success | failed | partial | abandoned
  measured_by: [metric or observation used]
  task_failure_rate_before: N%   # optional — from trent_health_report
  task_failure_rate_after: N%    # optional
  notes: "what actually happened"
  closed_date: YYYY-MM-DD
```
