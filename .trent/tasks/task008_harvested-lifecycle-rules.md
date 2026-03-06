---
id: 8
title: 'Add status: harvested to task lifecycle rules'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [template-core, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [7]
project_context: 'Harvested status preserves completed-but-superseded work for future reference — critical for research projects like VisionLang where approaches get abandoned mid-experiment'
---

# Task 008: Add harvested status to task lifecycle rules

## Objective
Add the `harvested` status to the formal task lifecycle documentation in `template_v2/` — specifically the rule files that define allowed status transitions, completion workflows, and the cleanup agent behavior when it encounters harvested tasks.

## Context
Task007 adds the status values to the schema and templates. This task ensures the *rules* (the behavioral guides for agents) properly define what `harvested` means, when it's used, and how agents should interact with harvested tasks during cleanup and planning sessions.

## Acceptance Criteria
- [ ] Rule template for `20_trent_tasks` in `template_v2/` documents `harvested` in status transition section
- [ ] Harvested tasks are explicitly excluded from SPRINT.md population
- [ ] Cleanup agent rule mentions harvested tasks should be included in phase SWOT (as "work done but abandoned — why?")
- [ ] `[🌾]` appears in TASKS.md master status table in template_v2
- [ ] Agents instructed: "Do NOT delete harvested task files — they are reference material"
- [ ] Rule states: harvested tasks count toward project history, not toward completion metrics

## Lifecycle Addition

Add to the task lifecycle section:

```
CORRECT lifecycle for pivoted work:
[📋] → [🔄] → [✅] → [🌾]  (completed, then approach superseded)

WRONG:
[✅] → deleted  ← loses institutional memory of what was tried
[✅] → [❌]     ← implies failure, which is incorrect
```

## Cleanup Agent Behavior

When cleanup agent scans for harvested tasks:
1. Count total harvested per subsystem
2. Include in health score: `{subsystem}.harvested_count`
3. In SWOT Weaknesses section: list subsystems with high harvest rate (signals frequent pivoting)
4. Do NOT re-queue harvested tasks for sprint

## Implementation Notes
- This is a rules documentation task — write the behavioral guidance
- Primary file to update: `template_v2/.cursor/rules/20_trent_tasks.mdc` template
- Also update `template_v2/.claude/rules/20_trent_tasks.md` for parity
- Also update `template_v2/.agent/rules/20_trent_tasks.md` for parity

## Verification Steps
- [ ] Harvested lifecycle shows `[✅] → [🌾]` in rules
- [ ] SPRINT.md exclusion explicitly stated
- [ ] Cleanup agent behavior for harvested tasks documented
- [ ] Parity: .cursor, .claude, .agent rule files all updated

## When Stuck
- Depends on task007 being completed first
- Just document the behavioral rules — no code needed
