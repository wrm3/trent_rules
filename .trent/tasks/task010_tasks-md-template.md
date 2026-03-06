---
id: 10
title: 'Create updated TASKS.md template with subsystem headers'
type: feature
status: pending
priority: high
phase: 0
subsystems: [template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1, 7]
project_context: 'TASKS.md template needs subsystem-based organization headers alongside phases — key structural change from trent v1 based on lessons from Maestro2 (phases alone become junk drawers)'
---

# Task 010: Create updated TASKS.md template with subsystem headers

## Objective
Create `template_v2/.trent/TASKS.md` template that supports BOTH phase-based organization AND subsystem-based grouping within phases. Tasks should be grouped by subsystem under each phase header, not just listed sequentially.

## Context
The Maestro2 analysis revealed that flat phase headers with 50-100+ tasks become unsearchable "junk drawers." The fix: within each phase, tasks are grouped by subsystem. This gives agents two dimensions to filter by: "What phase?" and "What subsystem am I working in?"

## Template Content

```markdown
# {PROJECT_NAME} — Master Task List

**Project**: {project_name}
**Type**: delivery | research  (set during @trent-setup)
**PRD**: `.trent/PRD.md`
**Subsystems**: `.trent/SUBSYSTEMS.md`
**Architecture Constraints**: `.trent/ARCHITECTURE_CONSTRAINTS.md`

---

## Status Indicators
- `[ ]` = Pending (no task file yet) — CODING BLOCKED
- `[📋]` = Task file created, ready to start
- `[📝]` = Spec being written (TTL: 1 hour)
- `[🔄]` = In Progress (claimed by agent, has TTL)
- `[🔍]` = Awaiting Verification (impl done, reviewer pending)
- `[⏳]` = Resource-Gated (waiting on storage/compute/API)
- `[✅]` = Completed (verified by different agent)
- `[❌]` = Failed/Cancelled
- `[⏸️]` = Paused
- `[🌾]` = Harvested (done but approach superseded — preserved as reference)

---

## Phase 0: {Phase Name} [ ]

### Subsystem: {subsystem-name-1}
- [ ] **Task 001**: {Task description} — {brief acceptance criteria}
- [ ] **Task 002**: {Task description} — {brief acceptance criteria}

### Subsystem: {subsystem-name-2}
- [ ] **Task 010**: {Task description} — {brief acceptance criteria}

---

## Phase 1: {Phase Name} [ ]

### Subsystem: {subsystem-name-1}
- [ ] **Task 100**: {Task description}

---

## Bugs
[See `.trent/BUGS.md` for full bug list]

- [ ] **BUG-001**: {Bug description} — {severity}

---

## Completed Tasks
[Tasks moved here when fully verified]

---

## Harvested Tasks
[Tasks that were completed but whose approach was superseded]

---

**Last Updated**: {YYYY-MM-DD}
**Phase 0 Progress**: 0/{n} tasks
**Overall Progress**: 0/{total} tasks
```

## Key Structural Changes vs v1
1. **Subsystem headers within phases** — `### Subsystem: {name}` grouping
2. **New status indicators** in legend (🔍, ⏳, 🌾)
3. **Bugs section** inline with link to BUGS.md
4. **Harvested section** at bottom for superseded work
5. **Project type field** in header (delivery | research)
6. **Architecture Constraints reference** in header

## Acceptance Criteria
- [ ] File exists at `template_v2/.trent/TASKS.md`
- [ ] Subsystem headers (`### Subsystem:`) used within phase sections
- [ ] All 10 status indicators present in legend
- [ ] Harvested section present at bottom
- [ ] Project type field in header
- [ ] Architecture Constraints reference in header

## Verification Steps
- [ ] Template has both Phase and Subsystem header levels
- [ ] Status legend is complete (all 10 values)
- [ ] `{PROJECT_NAME}` and other placeholders in curly braces

## When Stuck
- This is a markdown template — no logic needed
- The key innovation is `### Subsystem:` headers INSIDE `## Phase` sections
