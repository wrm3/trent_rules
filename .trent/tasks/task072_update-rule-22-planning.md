---
id: 72
title: 'Update 22_trent_planning rule with project types, PRD rename, ARCHITECTURE_CONSTRAINTS'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [6, 11, 12, 13]
project_context: 'Rule 22 governs planning — needs project type awareness (delivery vs research), PRD rename, and ARCHITECTURE_CONSTRAINTS enforcement added to the session-start and planning protocols'
---

# Task 072: Update 22_trent_planning rule

## Objective
Create updated `22_trent_planning.md` in `template_v2/` incorporating project types (delivery vs research), PRD.md rename from PLAN.md, ARCHITECTURE_CONSTRAINTS enforcement, and phase YAML schema additions.

## Key Additions

### 1. PRD.md Rename
Update all references: `PLAN.md` → `PRD.md` throughout the rule.

### 2. Project Type Section (add after PRD structure)
```markdown
## Project Types

### Delivery Projects
- Phases: milestone + maintenance types
- Required: ARCHITECTURE_CONSTRAINTS.md
- Phase YAML: acceptance_criteria, definition_of_done fields

### Research Projects  
- Phases: experiment + domain types
- Required: HYPOTHESIS.md, experiments/ directory
- Phase YAML: hypothesis, outcome, carry_forward, abandoned_approaches fields
- Scope pivots are expected — document, not fail
```

### 3. ARCHITECTURE_CONSTRAINTS Enforcement
Add to Session Start Protocol:
```markdown
### MANDATORY at Session Start
1. Read PROJECT_CONTEXT.md
2. Read ARCHITECTURE_CONSTRAINTS.md → commit to memory
3. Refuse any task that violates constraints, regardless of who asks
```

### 4. Phase YAML Schema Update
Update the phase YAML example to include new fields (purpose, hypothesis, outcome, etc.)

### 5. @trent-setup Updates
Add project type selection question to setup questionnaire reference.

## Acceptance Criteria
- [ ] Rule file created in template_v2 (all 3 IDEs)
- [ ] All PLAN.md → PRD.md references updated
- [ ] Project type section added
- [ ] ARCHITECTURE_CONSTRAINTS enforcement in session start
- [ ] Updated phase YAML schema

## Verification Steps
- [ ] No PLAN.md references remain in the rule
- [ ] Project type section present
- [ ] ARCHITECTURE_CONSTRAINTS in session start protocol

## When Stuck
- Tasks 006, 011, 012, 013 provide all content needed — this task assembles them into rule 22
