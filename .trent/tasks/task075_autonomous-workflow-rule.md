---
id: 75
title: 'Create new rule: autonomous agent workflow (cleanup + sprint agent protocols)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [agent-rules, autonomous]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [40, 42, 43, 44, 45]
project_context: 'The autonomous workflow is new enough to warrant its own rule file — consolidates all unattended execution protocols, scheduling, safety gates, and coordination into a single reference agents read before running unattended'
---

# Task 075: Create new rule: autonomous agent workflow

## Objective
Create `template_v2/.cursor/rules/31_trent_autonomous.mdc` — a new rule file that consolidates all autonomous agent protocols: cleanup agent responsibilities, sprint agent workflow, safety gates, and coordination between multiple agents.

## Rule Content Summary

```markdown
# Autonomous Agent Workflow

## Purpose
This rule governs how trent agents operate unattended — without a human at the keyboard.
All agents running on schedule MUST read and follow this rule.

## The Autonomous Architecture

### Cleanup Agent (midnight, @trent-cleanup)
- Runs once per project per night
- Reads: TASKS.md, all task files, git log
- Writes: SPRINT.md, CLEANUP_REPORT.md, health scores, IDEA_BOARD AI-ideas
- Does NOT implement any tasks — analysis and curation only
- Schedule: 00:00 UTC or configured time in PROJECT_CONTEXT.md

### Sprint Agent (every 2 hours, @trent-sprint)
- Reads: SPRINT.md (must be valid — not expired)
- Claims tasks atomically (see atomic claiming protocol)
- Implements tasks (one at a time within sprint)
- Sets tasks to [🔍] — never [✅]
- Commits after every acceptance criterion
- Respects all safety gates (ai_safe, blast_radius, requires_solo_agent)

### Verification Agent (triggered after [🔍])
- Activated when a task moves to [🔍] (Awaiting Verification)
- MUST be a different agent than the implementer
- Applies adversarial review persona
- Approves ([✅]) or returns ([🔄]) based on evidence_of_completion

## Safety Gates (all agents check these)
[reference task044 ai_safe rules]
[reference task024 blast_radius rules]
[reference task025 requires_solo_agent rules]
[reference task047 Ralph Wiggum rules]
[reference task023 When Stuck protocol]

## Coordination (multiple agents running simultaneously)
[reference task043 atomic claiming protocol]
[reference task050 mandatory commit points]
[reference task051 agent identity in commits]

## What Autonomous Agents MUST NOT Do
- Mark tasks [✅] without verification
- Modify ARCHITECTURE_CONSTRAINTS.md
- Execute tasks with ai_safe: false
- Execute tasks with blast_radius: critical
- Modify other projects' .trent/ folders
- Ignore claim_expires_at — expired claims must be reset before re-claiming
```

## Acceptance Criteria
- [ ] New rule file `31_trent_autonomous.mdc` created in template_v2
- [ ] Cleanup agent responsibilities documented
- [ ] Sprint agent workflow documented
- [ ] Verification agent role documented
- [ ] All safety gate cross-references present
- [ ] MUST NOT list present
- [ ] Parity: .claude/rules/31_trent_autonomous.md and .agent/rules/31_trent_autonomous.md

## Verification Steps
- [ ] Rule file exists in all 3 IDE directories
- [ ] Three agent types (cleanup, sprint, verification) documented
- [ ] Safety gate references present
- [ ] MUST NOT list present

## When Stuck
- This is an assembly task — pulls content from tasks 040, 042, 043, 044, 045, 047, 050
- Write the rule structure first, then fill in references to the detailed task specs
