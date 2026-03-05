---
id: 2
title: 'Create ARCHITECTURE_CONSTRAINTS.md Template'
type: feature
status: pending
priority: critical
phase: 0
subsystem: template-core
ai_safe: true
requires_solo_agent: false
blast_radius: low
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 30
claim_ttl_minutes: 60
dependencies: [1]
---

# Task 002: Create ARCHITECTURE_CONSTRAINTS.md Template

## Objective
Create the `ARCHITECTURE_CONSTRAINTS.md` template in `template_v2/.trent/`. This is
the #1 priority improvement from `potential_changes.md` — the file that prevents
"constraint amnesia" (AI forgetting hard architectural rules between sessions).

## Background
From analysis of Maestro2: the user created this file out of necessity because the AI
kept suggesting Docker-first architecture violations. Phase 14 was entirely cancelled
because an agent forgot the constraint. This template ensures every future project
starts with this protection.

The session-start protocol (`25_trent_index.mdc`) must also be updated (Task 073) to
load this file's constraint names at session start.

## Acceptance Criteria
- [ ] `template_v2/.trent/ARCHITECTURE_CONSTRAINTS.md` created with full template
- [ ] Template includes change authority section (only user can approve changes)
- [ ] Template includes example constraint format with all required fields
- [ ] Template includes change log section
- [ ] Template includes violation examples section
- [ ] Constraint format clearly distinguishes non-negotiable vs user-overridable
- [ ] Git commit: `feat(template-v2): add ARCHITECTURE_CONSTRAINTS template`

## Template to Create

```markdown
# ARCHITECTURE_CONSTRAINTS.md

> **ALWAYS load this file at session start.**
> Read before suggesting any changes to infrastructure, deployment, or service boundaries.
> These constraints are non-negotiable without explicit user approval.

---

## Change Authority

**The user has ultimate authority over architectural constraints.**

- The AI MAY suggest changes but MUST present them as an explicit standalone question
- The user MUST explicitly agree (e.g., "yes", "approved", "change it")
- **Silence, "sounds good", "ok", or inferred agreement is NOT approval**
- Every constraint change MUST be logged in the Change Log below

---

## Active Constraints

### Constraint 1: [Name]
**Non-negotiable**: Yes
**Rationale**: [Why this constraint exists]
**Applies to**: [Which parts of the system]

**What this means in practice**:
- [Specific behavior required]
- [Specific behavior required]

**Violation examples** (AI must never suggest these):
- [Specific thing that would violate this constraint]
- [Specific thing that would violate this constraint]

**Change authority**: User-only, requires explicit approval

---

## Change Log

| Date | Constraint | Change | Approved By |
|------|------------|--------|-------------|
| YYYY-MM-DD | Constraint N | Description | User |

---

## Session Start Summary

When loading this file at session start, display:
```
⚠️ ACTIVE CONSTRAINTS:
  C1: [Constraint 1 name] — [one line]
  C2: [Constraint 2 name] — [one line]
Full constraints: .trent/ARCHITECTURE_CONSTRAINTS.md
```
```

## When Stuck
This is a template creation task — write the file, no execution needed.
If the template structure seems wrong, check potential_changes.md section on
ARCHITECTURE_CONSTRAINTS (Idea C and Idea H).
