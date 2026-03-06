---
id: 13
title: 'Create HYPOTHESIS.md and EXPERIMENT.md templates for research projects'
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
project_context: 'Research projects need structured hypothesis and experiment tracking — VisionLang had informal experiment logs that lost context between POC iterations; these templates formalize that process'
---

# Task 013: Create HYPOTHESIS.md and EXPERIMENT.md templates for research projects

## Objective
Create two templates in `template_v2/.trent/` for research-type projects:
1. `HYPOTHESIS.md` — tracks active hypotheses and their validation status
2. `EXPERIMENT.md` — a per-experiment spec for individual research runs

## Context
VisionLang's `POC018_TASK_REFINEMENT_SUMMARY.md` and `POC019_PREFLIGHT_CHECKLIST.md` were informal versions of these concepts. By formalizing them, future research projects get:
- Clear hypothesis tracking (so we know what we're trying to prove, not just what we're building)
- Preflight checklists built into experiment specs
- Explicit "carry forward" and "abandon" decisions instead of accidental drift

## HYPOTHESIS.md Template

```markdown
# HYPOTHESIS.md — Research Hypothesis Registry

This file tracks all active and resolved hypotheses for this research project.
A hypothesis is a testable belief about what will solve the core problem.

**Project**: {project_name}
**Core Problem**: {one sentence — what are we trying to solve?}

---

## Active Hypotheses

### H-001: {Hypothesis Title}
**Status**: untested | testing | validated | invalidated | inconclusive
**Proposed**: {YYYY-MM-DD} by {human | AI | agent_id}
**Statement**: "We believe {X} because {Y}. We'll know we're right when {Z}."
**Test Plan**: {How we'll test this — experiment, POC, benchmark}
**Experiment Reference**: {EXP-NNN from SYSTEM_EXPERIMENTS.md if applicable}
**Risk**: {What happens if this is wrong — how much work is wasted?}

---

## Validated Hypotheses (Carry Forward)

### H-000: {Example Validated}
**Validated**: {YYYY-MM-DD}
**Evidence**: {What proved it}
**Incorporated In**: {Which POC/phase captured this}

---

## Invalidated Hypotheses (Do Not Retry)

### H-000: {Example Invalidated}
**Invalidated**: {YYYY-MM-DD}
**Evidence**: {What disproved it}
**Why Abandoned**: {Brief reason — prevents re-trying same approach}
**Alternative Explored**: {What we tried instead}

---

## Hypothesis ID Registry
Last H ID: H-000
```

## EXPERIMENT.md Template (per-experiment spec)

```markdown
# EXPERIMENT: {EXP-NAME}
<!-- One file per experiment run — place in .trent/experiments/ -->

## Experiment Metadata
**ID**: EXP-NNN
**Hypothesis**: H-NNN (from HYPOTHESIS.md)
**Started**: {YYYY-MM-DD}
**Completed**: {YYYY-MM-DD}
**Status**: planning | running | completed | abandoned

## Objective
{What this experiment is trying to prove or measure}

## Prerequisites / Preflight Checklist
- [ ] Data: {required datasets or inputs}
- [ ] Environment: {GPU, storage, software, versions}
- [ ] Baseline: {what we're comparing against}
- [ ] Success Metric: {how we measure success — specific and measurable}

## Configuration
```yaml
# Exact parameters used in this experiment
parameter_name: value
```

## Results
**Outcome**: success | failed | partial | inconclusive
**Metrics Achieved**: {what we measured}
**vs Baseline**: {comparison}
**Notes**: {what happened that wasn't expected}

## Carry Forward
- {Specific finding #1 to use in next experiment}
- {Specific finding #2}

## Abandon
- {Approach #1 that doesn't work — do not retry}
- {Why it doesn't work}

## Resource Log
**Compute Used**: {GPU hours, cost}
**Data Processed**: {volume}
**Wall Clock Time**: {duration}
```

## Acceptance Criteria
- [ ] `template_v2/.trent/HYPOTHESIS.md` exists with H-NNN format
- [ ] `template_v2/.trent/experiments/` directory exists (for per-experiment files)
- [ ] `template_v2/.trent/experiments/EXPERIMENT_TEMPLATE.md` exists
- [ ] Both templates have preflight checklist sections
- [ ] HYPOTHESIS.md has active/validated/invalidated sections
- [ ] "Do Not Retry" section in invalidated hypotheses (prevents VisionLang-style re-attempts)

## Verification Steps
- [ ] Both files exist at correct paths
- [ ] Experiments directory exists (with .gitkeep)
- [ ] HYPOTHESIS.md has the three-section structure
- [ ] EXPERIMENT.md has preflight checklist

## When Stuck
- These are pure markdown templates
- The key innovation is the explicit "Invalidated / Do Not Retry" section — make sure it's prominent
