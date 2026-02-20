---
description: "Add a new project phase to TASKS.md and create the corresponding phase file"
---

# Workflow: trent-phase-add

Add a new project phase with atomic creation of both TASKS.md header and phase file.

## Steps

### Step 1: Read Current Phases

// turbo
Read `.trent/TASKS.md` to see existing phases and determine the next phase number.

### Step 2: Gather Phase Information

Ask the user for (if not already provided):
- **Phase Name**: Descriptive name
- **Phase Number**: Which phase (or suggest next available)
- **Objectives**: What this phase accomplishes
- **Deliverables**: Tangible outputs
- **Acceptance Criteria**: How we know it's done
- **Affected Subsystems**: Which components

### Step 3: ATOMIC CREATION — Both Files in This Response

**3a. Add Phase Header to TASKS.md**

Add under the appropriate location:
```markdown
### Phase {N}: {Phase Name}

- [ ] Task {N×100}: {First task for this phase}
```

**3b. Create Phase File**

Create `.trent/phases/phase{N}_{kebab-case-name}.md`:

```yaml
---
phase: {N}
name: '{Phase Name}'
status: planning
subsystems: [{subsystems}]
task_range: '{N×100}-{N×100+99}'
prerequisites: [{prior_phase_numbers}]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase {N}: {Phase Name}

## Overview
{Brief description}

## Objectives
- {Objective 1}
- {Objective 2}

## Deliverables
- [ ] {Deliverable 1}
- [ ] {Deliverable 2}

## Acceptance Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}
```

### Step 4: Validate Sync

Confirm BOTH were created:
```
✅ Phase Sync Confirmation:
- TASKS.md header: ### Phase {N}: {Name} ✅
- Phase file: .trent/phases/phase{N}_{name}.md ✅
- Sync verified: ✅
```

### Step 5: Suggest Next Steps

Recommend using `/trent-task-new` to populate this phase with initial tasks.
