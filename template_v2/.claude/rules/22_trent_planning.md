---
description: "PRD structure, phase management, phase sync enforcement, pivot workflow"
globs:
alwaysApply: true
---

# Planning System

## PRD (Product Requirements Document)

**Location**: `.trent/PRD.md` (single mandatory file)

**Required Sections** (see `trent-planning` skill for full template):
1. Product overview
2. Goals (business, user, non-goals)
3. User personas
4. Phases (overview + references to TASKS.md)
5. User experience
6. Narrative
7. Success metrics
8. Technical considerations (including 8.6: shared modules & reusability)
9. Milestones & sequencing
10. User stories

**Before creating a PRD**: Ask scope validation questions (see `21_trent_infrastructure.md`).

---

## Phase Management

### Key Principle
TASKS.md is the master file for phases. Each phase header in TASKS.md MUST have a corresponding phase file. See `20_trent_tasks.md` for phase numbering.

### Phase File Format

**Filename**: `phase{N}_{kebab-case-name}.md` (e.g., `phase0_setup.md`)

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
```

Phase file body: Overview, Objectives, Deliverables (checklist), Acceptance Criteria (checklist).

---

## Phase Sync Enforcement (MANDATORY)

### Atomic Phase Creation

**When adding a phase, MUST create BOTH in the SAME response:**
1. Add phase header to TASKS.md
2. Create phase file in `.trent/phases/`

**Split across responses = VIOLATION.**

### Status Mapping (MUST Match)

| TASKS.md Header | Phase File YAML |
|-----------------|-----------------|
| `### Phase N: Name` | `status: planning` |
| `### Phase N: Name [🔄]` | `status: in_progress` |
| `### Phase N: Name [✅]` | `status: completed` |
| `### Phase N: Name [❌]` | `status: cancelled` |
| `### Phase N: Name [⏸️]` | `status: paused` |

**If mismatch detected: FIX IT FIRST before any other operation.**

### Orphan & Phantom Detection

- **Orphan**: Phase file exists but no TASKS.md header → Add header or delete file
- **Phantom**: TASKS.md header exists but no phase file → Create file or remove header

---

## Pivot Workflow

1. Update old phase file: `status: paused` or `cancelled`
2. Update TASKS.md: Add `[⏸️]` or `[❌]` to old phase header
3. Create new phase file with `pivoted_from` and `pivot_reason`
4. Add new header to TASKS.md
5. Update CLAUDE.md with new phase context

**All 5 steps in the SAME response. No split operations.**

---

## Subsystems Registry

**Location**: `.trent/SUBSYSTEMS.md`

**Purpose**: Track project components/modules for impact analysis and planning.

**Subsystem Types**: core (business logic), support (infrastructure), integration (external APIs)

**Task Integration**: Tasks reference affected subsystems in YAML: `subsystems: [SS-01, SS-03]`

See `trent-planning` skill for full SUBSYSTEMS.md template and auto-discovery process.
