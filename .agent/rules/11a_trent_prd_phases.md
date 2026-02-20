---
description: "PRD generation templates and phase management system"
activation: "always_on"
---

# Planning System

This rule provides comprehensive planning functionality including PRD creation, phase management, subsystems registry, scope validation, and requirements gathering.

## PRD Generation

### PRD Structure
**Location**: `.trent/PLAN.md` (single mandatory file)

### PRD Template
```markdown
# PRD: [Project/Feature Title]

## 1. Product overview
### 1.1 Document title and version
- PRD: [Project/Feature Title]
- Version: 1.0

### 1.2 Product summary
[2-3 short paragraphs providing an overview of the project or feature.]

## 2. Goals
### 2.1 Business goals
- [Bullet list of business objectives]

### 2.2 User goals
- [Bullet list of what users aim to achieve]

### 2.3 Non-goals
- [Bullet list of explicitly out-of-scope items]

## 3. User personas
### 3.1 Key user types
- [Bullet list of primary user categories]

### 3.2 Basic persona details
- **[Persona Name 1]**: [Brief description]
- **[Persona Name 2]**: [Brief description]

### 3.3 Role-based access
- **[Role Name 1]**: [Description of permissions/access]
- **[Role Name 2]**: [Description of permissions/access]

## 4. Phases
*Note: Detailed phase management is in TASKS.md. This section provides high-level overview only.*

### 4.1 Phase Overview
- **Phase 0: Setup & Infrastructure** - [Brief description]
- **Phase 1: Foundation** - [Brief description]
- **Phase 2: Core Development** - [Brief description]

### 4.2 Phase References
- **Master Location**: TASKS.md (phase headers with task lists)
- **Detail Files**: `.trent/phases/phase{N}_{name}.md`
- **Template**: `.trent/templates/phase_template.md`

## 5. User experience
### 5.1 Entry points & first-time user flow
- [How users access this feature/product initially]

### 5.2 Core experience
- **[Step 1]**: [Explanation of the step]
- **[Step 2]**: [Explanation of the step]

### 5.3 Advanced features & edge cases
- [Bullet list of less common scenarios or advanced capabilities]

### 5.4 UI/UX highlights
- [Key design principles or user interface elements]

## 6. Narrative
[A single paragraph describing the user's journey and the benefit they receive.]

## 7. Success metrics
### 7.1 User-centric metrics
- [e.g., Task completion rate, user satisfaction]

### 7.2 Business metrics
- [e.g., Conversion rate, revenue impact]

### 7.3 Technical metrics
- [e.g., Page load time, error rate]

## 8. Technical considerations
### 8.1 Affected subsystems
- **Primary subsystems** (directly modified/extended):
  - [Subsystem Name 1]: [Impact description]
  - [Subsystem Name 2]: [Impact description]
- **Secondary subsystems** (indirectly affected):
  - [Subsystem Name 3]: [Dependency/integration description]

### 8.2 Integration points
- [Interaction with other systems/services]

### 8.3 Data storage & privacy
- [How data is handled, GDPR/CCPA compliance etc.]

### 8.4 Scalability & performance
- [Anticipated load, performance targets]

### 8.5 Potential challenges
- [Risks or technical hurdles]

## 9. Milestones & sequencing
### 9.1 Project estimate
- [Small/Medium/Large]: [Rough time estimate, e.g., 2-4 weeks]

### 9.2 Team size & composition
- [e.g., Small Team: 1-2 people (1 PM, 1 Eng)]

### 9.3 Suggested phases
- **[Phase 1]**: [Description] ([Time estimate])
  - Key deliverables: [List]
- **[Phase 2]**: [Description] ([Time estimate])
  - Key deliverables: [List]

## 10. User stories
### 10.1 [User Story Title 1]
- **ID**: US-001
- **Description**: As a [persona], I want to [action] so that [benefit].
- **Acceptance Criteria**:
  - [Criterion 1.1]
  - [Criterion 1.2]

### 10.2 [User Story Title 2]
- **ID**: US-002
- **Description**: As a [persona], I want to [action] so that [benefit].
- **Acceptance Criteria**:
  - [Criterion 2.1]
  - [Criterion 2.2]
```

## Phase Management

### Phase System Overview
**Purpose**: Phases provide logical groupings of tasks within the overall project plan, allowing for iterative development, pivoting, and clear milestone tracking.

**Key Principle**: TASKS.md is the master file for phases. Each phase header in TASKS.md MUST have a corresponding phase file.

### Phase Structure
- **Master Location**: TASKS.md contains phase headers with task lists
- **Detail Files**: `.trent/phases/phase{N}_{name}.md` for detailed phase info
- **Sync Required**: Phase headers in TASKS.md ↔ Phase files MUST match

### Phase Numbering Convention
| Phase | Task ID Range | Typical Purpose |
|-------|---------------|-----------------|
| Phase 0 | 1-99 | Setup, infrastructure, environment |
| Phase 1 | 100-199 | Foundation, database, core handlers |
| Phase 2 | 200-299 | Core development, main features |
| Phase 3 | 300-399 | Enhancement, secondary features |
| Phase N | N×100 to N×100+99 | Custom phase scope |

### Phase File Format
**Filename**: `phase{N}_{kebab-case-name}.md` (e.g., `phase0_setup.md`, `phase1_foundation.md`)

**YAML Frontmatter** (required fields):
```yaml
---
phase: 0
name: 'Setup & Infrastructure'
status: planning|in_progress|completed|cancelled|paused
subsystems: [database, api, authentication]  # Affected subsystems
task_range: '1-99'
prerequisites: []  # Phase numbers that must complete first
started_date: ''
completed_date: ''
pivoted_from: null  # Phase number if this is a pivot
pivot_reason: ''    # Why the pivot occurred
---
```

**Status Values**:
- `planning` - Phase defined but not started
- `in_progress` - Actively working on phase tasks
- `completed` - All acceptance criteria met
- `cancelled` - Phase abandoned, won't resume
- `paused` - Work stopped, may resume later (often due to pivot)

### Phase Document Template
```markdown
---
phase: {N}
name: '{Phase Name}'
status: planning
subsystems: [{subsystem1}, {subsystem2}]
task_range: '{N*100}-{N*100+99}'
prerequisites: []
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase {N}: {Phase Name}

## Overview
{Brief description of the phase goals and scope}

## Objectives
- {Objective 1}
- {Objective 2}

## Deliverables
- [ ] {Deliverable 1}
- [ ] {Deliverable 2}

## Acceptance Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}

## Notes
{Additional context}
```

### 🚨 MANDATORY: Phase Synchronization Enforcement

**CRITICAL**: TASKS.md phase headers and phase files MUST always be in sync.

#### Atomic Phase Creation (BOTH OR NEITHER)

**When adding a new phase, you MUST create BOTH in the SAME response:**

```
✅ CORRECT (Atomic):
1. Add phase header to TASKS.md: "### Phase 2: Core Development"
2. Create phase file: .trent/phases/phase2_core-development.md
3. Confirm BOTH in response

❌ WRONG (Split):
Response 1: Add header to TASKS.md only
Response 2: Create phase file later  ← VIOLATION!
```

#### Status Mapping (MUST Match)

| TASKS.md Header | Phase File YAML |
|-----------------|-----------------|
| `### Phase N: Name` | `status: planning` (default) |
| `### Phase N: Name [🔄]` | `status: in_progress` |
| `### Phase N: Name [✅]` | `status: completed` |
| `### Phase N: Name [❌]` | `status: cancelled` |
| `### Phase N: Name [⏸️]` | `status: paused` |

#### Pre-Operation Validation

**Before ANY phase operation:**
1. Read TASKS.md - identify all phase headers
2. List `.trent/phases/` - identify all phase files
3. Verify each header has a matching file
4. If mismatch: FIX IT FIRST

#### Phase Sync Check

```markdown
📋 PHASE SYNC VALIDATION
Phase 0: TASKS.md header ↔ phase0_setup.md ✅ SYNCED
Phase 1: TASKS.md header ↔ phase1_foundation.md ✅ SYNCED
Phase 2: TASKS.md header ↔ (NO FILE) ⚠️ MISSING - CREATING
Sync Status: 2/3 synced, 1 created
```

#### Orphan & Phantom Detection

**Orphan Phase Files** (files without TASKS.md header):
```markdown
📋 ORPHAN: phase5_experimental.md exists but no header in TASKS.md
Action: Add header to TASKS.md or delete file
```

**Phantom Phase Headers** (headers without files):
```markdown
📋 PHANTOM: "### Phase 3: Enhancement" in TASKS.md but no file
Action: Create phase file or remove header
```

### Dynamic Phase Management

- **Adding Phases**: Create header in TASKS.md AND phase file atomically
- **Pivoting**: Mark old phase as `paused`, create new phase with `pivoted_from` field
- **Phase Gaps**: Allowed (e.g., Phase 0, 1, 2, then jump to 5)
- **Completing Phases**: Update both TASKS.md header and phase file status

### Pivot Workflow

When pivoting to a new direction:

1. **Update old phase file**: Set `status: paused` or `status: cancelled`
2. **Update TASKS.md**: Add `[⏸️]` or `[❌]` to old phase header
3. **Create new phase file**: Include `pivoted_from` and `pivot_reason`
4. **Add new header to TASKS.md**: New phase section

**Example Pivot**:
```yaml
# In phase5_new-direction.md
---
phase: 5
name: 'New Direction'
status: in_progress
subsystems: [api, frontend]
task_range: '500-599'
prerequisites: [0, 1]
pivoted_from: 2
pivot_reason: 'User requirements changed - MVP focus instead of full feature set'
---
```
