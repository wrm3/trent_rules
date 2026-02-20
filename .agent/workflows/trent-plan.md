---
description: "Activate trent planning system - create PRD, define phases, validate scope"
---

# Workflow: trent-plan

Activate the trent planning system to create or update project plans.

## Steps

### Step 1: Load Project Context

Read:
- `.trent/PROJECT_CONTEXT.md` (if exists)
- `.trent/PLAN.md` (if exists)
- `.trent/SUBSYSTEMS.md` (if exists)

### Step 2: Scope Validation Questions

Ask the user these essential scoping questions before creating PRD:

1. **User Context**: Personal use, small team (2-10), or broader deployment (10+)?
2. **Security**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration**: Standalone, basic, standard, or enterprise?
6. **Timeline**: What's the delivery preference (quick prototype, phased, complete)?

### Step 3: Create/Update PRD

Create or update `.trent/PLAN.md` following the PRD template:

```markdown
# PRD: [Title]

## 1. Product Overview
## 2. Goals (Business, User, Non-goals)
## 3. User Personas
## 4. Phases (high-level)
## 5. User Experience
## 6. Narrative
## 7. Success Metrics
## 8. Technical Considerations
## 9. Milestones & Sequencing
## 10. User Stories
```

### Step 4: Define Phases

For each project phase:
1. Add phase header to TASKS.md: `### Phase N: Name`
2. Create phase file: `.trent/phases/phase{N}_{name}.md`
3. **BOTH must be created in this same response**

### Step 5: Create Initial Tasks

Create initial task files for Phase 0 (setup) and Phase 1 (foundation) based on the PRD.

### Step 6: Update AGENTS.md

Check if AGENTS.md exists. Update the trent section between markers with new phase and planning information.

### Step 7: Summary

Present a summary of:
- Created PRD highlights
- Phases defined
- Initial tasks created
- Recommended next workflow: `/trent-task-new` to add more tasks
