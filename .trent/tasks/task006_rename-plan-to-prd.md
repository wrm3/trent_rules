---
id: 6
title: 'Rename PLAN.md to PRD.md in template_v2, update all references'
type: refactor
status: pending
priority: high
phase: 0
subsystems: [template-core, agent-rules]
ai_safe: true
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [1]
project_context: 'PRD.md is the industry-standard term for Product Requirements Document in spec-driven development — aligning terminology improves cross-team and cross-agent communication'
---

# Task 006: Rename PLAN.md → PRD.md in template_v2

## Objective
In `template_v2/`, rename the planning document from `PLAN.md` to `PRD.md` and update every reference to it across all template files, rule templates, and command templates. Do NOT touch the live `template/` folder or any `.cursor/`, `.claude/`, `.agent/` rules.

## Context
The industry has converged on "PRD" (Product Requirements Document) as the standard name for spec-driven development documents. Using `PLAN.md` creates confusion when developers familiar with PRD workflows interact with trent. This is a pure rename — the content and structure of the document does not change.

## Acceptance Criteria
- [ ] `template_v2/.trent/PRD.md` exists (was `PLAN.md`)
- [ ] `template_v2/.trent/PLAN.md` does NOT exist
- [ ] All references to `PLAN.md` in `template_v2/` are updated to `PRD.md`
- [ ] `.trent/` directory listing section in any template files updated
- [ ] Rule template files that reference `PLAN.md` updated to `PRD.md`
- [ ] `agents.md` trent section in template_v2 updated
- [ ] `CLAUDE.md` trent section in template_v2 updated
- [ ] No references to `PLAN.md` remain anywhere in `template_v2/`

## Files to Update

After running the rename, grep for `PLAN.md` in `template_v2/` and update every hit:

```
grep -r "PLAN.md" template_v2/
```

Expected files needing updates:
- `template_v2/.trent/PLAN.md` → rename to `template_v2/.trent/PRD.md`
- `template_v2/.trent/PROJECT_CONTEXT.md` → update reference
- `template_v2/agents.md` → update trent section directory listing
- `template_v2/CLAUDE.md` → update trent section directory listing
- `template_v2/.cursor/rules/*.mdc` → update any PLAN.md references
- `template_v2/.claude/rules/*.md` → update any PLAN.md references
- `template_v2/.agent/rules/*.md` → update any PLAN.md references

## Implementation Notes
- This is a find-and-replace + rename operation — no logic changes
- The PRD.md content/structure is identical to PLAN.md — only the filename changes
- Do NOT update the live `template/` folder — that's a separate migration task (task202)
- Do NOT update `.cursor/rules/22_trent_planning.mdc` — that's task072

## Verification Steps
- [ ] `grep -r "PLAN.md" template_v2/` returns zero results
- [ ] `template_v2/.trent/PRD.md` exists
- [ ] `template_v2/.trent/PLAN.md` does not exist
- [ ] Template directory listings correctly show `PRD.md`

## When Stuck
- This is purely mechanical — rename + find/replace
- If grep finds unexpected files, update them too
- When in doubt: update the reference, never leave a PLAN.md reference behind
