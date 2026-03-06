---
id: 11
title: 'Create phase YAML schema additions for research vs delivery'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1, 12]
project_context: 'Phases in research projects need hypothesis/outcome fields; phases in delivery projects need milestone/acceptance criteria — same structure, different required fields based on project type'
---

# Task 011: Create phase YAML schema additions (research vs delivery)

## Objective
Update the phase file YAML frontmatter schema in `template_v2/` to support two project types — `delivery` and `research` — with appropriate required fields for each. Add `purpose`, `hypothesis`, `outcome`, and `experiment_type` fields.

## Context
VisionLang POC analysis showed that research phases need to capture: "What did we hypothesize? What happened? What do we carry forward?" Delivery phases need: "What's the milestone? What are the acceptance criteria?" A single schema must accommodate both with conditional required fields.

## Updated Phase YAML Schema

```yaml
---
# COMMON FIELDS (all project types)
phase: 0
name: 'Phase Name'
status: planning | in_progress | completed | cancelled | paused
purpose: milestone | experiment | domain | maintenance
subsystems: [subsystem1, subsystem2]
task_range: '0-99'
prerequisites: []
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''

# DELIVERY FIELDS (purpose: milestone | maintenance)
milestone_name: ''          # Name of the delivery milestone
acceptance_criteria:        # What must be true to call this phase done
  - ''
definition_of_done: ''      # Single sentence summary of completion

# RESEARCH FIELDS (purpose: experiment | domain)  
experiment_type: ''         # poc | spike | ab_test | exploration
hypothesis: ''              # "We believe X because Y. We'll know we're right when Z."
outcome: ''                 # Populated at end: success | failed | partial | invalidated
outcome_notes: ''           # What actually happened
lessons_learned: []         # Key takeaways for next experiment
carry_forward: []           # Specific things to preserve in next experiment
abandoned_approaches: []    # What didn't work (prevents re-trying)
---
```

## Purpose Values
- `milestone` — Delivery phase with concrete acceptance criteria
- `experiment` — Research phase with hypothesis and outcome tracking
- `domain` — Exploratory phase (learning a new technology/domain)
- `maintenance` — Ongoing maintenance work (no specific end milestone)

## Acceptance Criteria
- [ ] Schema documented in `template_v2/.trent/phases/phase_template.md`
- [ ] Example delivery phase file created: `template_v2/.trent/phases/phase0_example-delivery.md`
- [ ] Example research phase file created: `template_v2/.trent/phases/phase0_example-research.md`
- [ ] `purpose:` field values documented with descriptions
- [ ] Research-only fields clearly marked in schema comments

## Verification Steps
- [ ] Both example phase files exist and are valid YAML
- [ ] Delivery example has `milestone_name` and `acceptance_criteria`
- [ ] Research example has `hypothesis`, `outcome`, `carry_forward`
- [ ] Schema comments indicate which fields are type-conditional

## When Stuck
- Task012 (project type selection) sets the project-level type
- Phase-level `purpose:` is more granular — a delivery project can still have experimental phases
