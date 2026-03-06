---
id: 202
title: 'Create migration guide template_v1 to template_v2'
type: documentation
status: pending
priority: medium
phase: 2
subsystem: installation
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: [200, 201]
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "Existing trent projects need clear guidance on what changes and what stays the same"
---

# Task 202: Create migration guide template_v1 to template_v2

## Objective
Write `docs/MIGRATION_V1_TO_V2.md` — a clear, actionable guide for upgrading existing trent projects from v1 to vNext (template_v2).

## Acceptance Criteria
- [ ] File created at `docs/MIGRATION_V1_TO_V2.md`
- [ ] Covers: what's new, what changed, what's backward compatible
- [ ] Step-by-step upgrade process
- [ ] Notes on TASKS.md changes (new status indicators)
- [ ] Notes on PRD.md rename (was PLAN.md)
- [ ] Notes on new files required (ARCHITECTURE_CONSTRAINTS.md, SPRINT.md, etc.)
- [ ] One-command upgrade path via `trent_install`

## Content Outline
1. **What's New in vNext** — bulleted summary of major features
2. **Backward Compatibility** — what works without any changes
3. **Breaking Changes** — PLAN.md → PRD.md rename, new status indicators
4. **Upgrade Steps** — run trent_install, verify files, add ARCHITECTURE_CONSTRAINTS.md
5. **New Files to Create** — ARCHITECTURE_CONSTRAINTS.md template walkthrough
6. **Optional: Enable Autonomous Agents** — how to configure PROJECT_CONTEXT.md for unattended runs
