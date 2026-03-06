---
id: 12
title: 'Add project type selection to @trent-setup (delivery vs research)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [template-core, agent-rules]
ai_safe: true
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [1, 9]
project_context: 'Project type (delivery vs research) fundamentally changes which templates, workflows, and validation rules are active — must be captured at setup time to configure the whole system appropriately'
---

# Task 012: Add project type selection to @trent-setup

## Objective
Update the `@trent-setup` command template in `template_v2/` to ask the user to select a project type at initialization — `delivery` or `research` — and configure the generated `.trent/` files appropriately based on the selection.

## Context
Delivery projects (Maestro2) and research projects (VisionLang) have fundamentally different failure modes and need different tooling:
- **Delivery**: milestone tracking, definition of done, blast radius enforcement, cross-agent verification mandatory
- **Research**: hypothesis tracking, experiment logging, abandoned approach memory, flexible scope, harvest-first mentality

## Project Type Definitions

### `delivery` — Building a defined product
- Has a clear MVP/feature set
- Phases have acceptance criteria
- Tasks have definition_of_done
- Cross-agent verification mandatory
- Blast radius enforcement active
- ARCHITECTURE_CONSTRAINTS.md mandatory

### `research` — Exploring unknown solutions
- Goal is learning, not shipping
- Phases have hypothesis + outcome
- Tasks may be exploratory (no fixed deliverable)
- HYPOTHESIS.md and EXPERIMENT.md templates activated
- Harvest mentality: preserve and learn, don't just fail
- Scope pivots are expected and tracked, not failures

## @trent-setup Additions

Add to the setup questionnaire:

```markdown
## Project Type Selection

**Q: What type of project is this?**

1. **delivery** — You're building a defined product/feature with known requirements
   - Examples: SaaS app, API, internal tool, game, automation script
   - Activates: milestone tracking, blast radius enforcement, cross-agent verification
   
2. **research** — You're exploring an unknown solution space
   - Examples: ML model experiments, algorithm exploration, new tech evaluation, POCs
   - Activates: hypothesis tracking, experiment log, harvest workflow, flexible scope

Your choice sets `project_type:` in PROJECT_CONTEXT.md and activates the appropriate templates.
```

## FILES AFFECTED IN template_v2

### PROJECT_CONTEXT.md
Add `project_type: delivery | research` field to header.

### TASKS.md
- Delivery: add `## Acceptance Criteria` subsection to phase headers
- Research: add `## Hypothesis` and `## Outcome` subsection to phase headers

### Setup command template
Add the type selection question after project name, before tech stack questions.

## Acceptance Criteria
- [ ] `@trent-setup` command template in template_v2 includes project type question
- [ ] Selection saves `project_type:` to `PROJECT_CONTEXT.md`
- [ ] Delivery path: activates ARCHITECTURE_CONSTRAINTS.md, verification workflow
- [ ] Research path: activates HYPOTHESIS.md, EXPERIMENT.md, SYSTEM_EXPERIMENTS.md
- [ ] Both paths still create the same core `.trent/` structure

## Verification Steps
- [ ] Setup command template has the type selection question
- [ ] Both `delivery` and `research` options are documented with examples
- [ ] PROJECT_CONTEXT.md template shows `project_type:` field
- [ ] Task013 (HYPOTHESIS.md template) is correctly listed as research-only

## When Stuck
- This is primarily documentation/template work for the command
- The actual conditional logic in @trent-setup is executed by the AI agent reading the command — it doesn't need to be code, just clear enough instructions that an agent follows the right path
