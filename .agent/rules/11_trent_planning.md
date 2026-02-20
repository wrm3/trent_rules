---
description: "trent planning system - PRD creation, phase management, subsystems registry, and scope validation"
activation: "always_on"
---

# trent Planning System

## Phase Management

### Phase Structure

- **Master Location**: `.trent/TASKS.md` — phase headers with task lists
- **Detail Files**: `.trent/phases/phase{N}_{name}.md`
- **Sync Required**: TASKS.md headers ↔ phase files MUST match

### Phase File Format

```yaml
---
phase: 0
name: 'Setup & Infrastructure'
status: planning|in_progress|completed|cancelled|paused
subsystems: [database, api]
task_range: '1-99'
prerequisites: []
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase {N}: {Phase Name}

## Overview
## Objectives
## Deliverables
## Acceptance Criteria
```

### MANDATORY: Atomic Phase Creation

When adding a new phase, create BOTH in the SAME response:
1. Add header to TASKS.md: `### Phase 2: Core Development`
2. Create file: `.trent/phases/phase2_core-development.md`

```
✅ CORRECT: Both created in same response
❌ WRONG: Create TASKS.md header now, file later
```

### Phase Status Mapping

| TASKS.md Header | Phase File YAML |
|-----------------|-----------------|
| `### Phase N: Name` | `status: planning` |
| `### Phase N: Name [🔄]` | `status: in_progress` |
| `### Phase N: Name [✅]` | `status: completed` |
| `### Phase N: Name [❌]` | `status: cancelled` |
| `### Phase N: Name [⏸️]` | `status: paused` |

## PRD Generation

Location: `.trent/PLAN.md`

### PRD Template

```markdown
# PRD: [Project/Feature Title]

## 1. Product Overview
### 1.1 Document title and version
### 1.2 Product summary

## 2. Goals
### 2.1 Business goals
### 2.2 User goals
### 2.3 Non-goals

## 3. User Personas
### 3.1 Key user types
### 3.2 Persona details
### 3.3 Role-based access

## 4. Phases (high-level — detail in TASKS.md)
## 5. User Experience
## 6. Narrative
## 7. Success Metrics
## 8. Technical Considerations
### 8.1 Affected subsystems
### 8.2 Integration points
### 8.3 Data storage & privacy
### 8.4 Scalability & performance
### 8.5 Potential challenges

## 9. Milestones & Sequencing
## 10. User Stories
```

## Scope Validation Questions

Before creating any PRD, ask:

1. **User Context**: Personal use, small team, or broader deployment?
2. **Security**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration**: Standalone, basic, standard, or enterprise?

## Subsystems Registry

Location: `.trent/SUBSYSTEMS.md`

Track major project components. Subsystem types:
- `core` — Essential business logic
- `support` — Infrastructure, utilities
- `integration` — External system connections

Tasks should reference affected subsystems in YAML: `subsystems: [SS-01, SS-03]`

## Session Start Protocol

When user mentions tasks, phases, or project status:

1. Validate `.trent/tasks/` files against TASKS.md entries
2. Validate `.trent/phases/` files against TASKS.md headers
3. Fix any mismatches BEFORE proceeding

```
📋 TRENT SYNC VALIDATION
Task Sync: X synced, Y mismatches, Z orphans
Phase Sync: X synced, Y mismatches, Z orphans
Status: ALL SYNCED ✅ / ISSUES FOUND ⚠️
```
