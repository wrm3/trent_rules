---
id: 49
title: 'Add git log as mandatory pre-task context to agent pre-flight checklist'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1, 34]
project_context: 'Git history is free context — an agent that reads the last 10-20 commits before starting work knows what was recently changed, avoids undoing completed work, and understands the project trajectory without a human briefing'
---

# Task 049: Add git log as mandatory pre-task context

## Objective
Add `git log` reading to the mandatory pre-flight checklist in `template_v2/` task templates and sprint agent rules — agents MUST review recent git history before starting any task.

## Context
Git history is the only reliable source of "what actually happened" on the project. An agent without this context may:
- Re-implement something just completed
- Undo a recent fix without knowing it was a fix
- Miss the current trajectory of the codebase
- Repeat an approach that was recently tried and reverted

## Pre-Flight Git Context Protocol

Add to both the task template `## Pre-Mortem > Pre-Implementation Checks` (task034) and the sprint agent pre-task step:

```markdown
### Git Context Check (Mandatory)

Before starting implementation, run and review:

```bash
# Last 20 commits (project history)
git log --oneline -20

# Recent changes to files this task will touch
git log --oneline -10 -- {affected_files}

# What changed in the last 48 hours
git log --oneline --since="48 hours ago"

# Any open claims by other agents
git log --oneline --grep="^claim(" -5
```

**What to look for:**
- Any recent commits to files I'm about to touch (don't undo their work)
- Any recent `revert(` commits — indicates an approach that didn't work
- Any `fail(task-{this_id})` commits — prior failures on THIS task
- Any `claim(` commits — active agents to avoid colliding with
- Any `spec(` commits — spec was recently updated, my local copy might be current

**If you find relevant history:** Add a note to `execution_progress.notes` summarizing what you found.
```

## Git Commit Message Conventions (for context extraction)

Add to rules: commit message prefixes that agents should use and recognize:

| Prefix | Meaning |
|--------|---------|
| `feat(task-{id})` | Feature implementation |
| `fix(task-{id})` | Bug fix |
| `spec(task-{id})` | Spec update only |
| `claim(task-{id})` | Task claim announcement |
| `heartbeat(task-{id})` | Agent still active |
| `checkpoint(task-{id})` | Progress save |
| `impl(task-{id})` | Implementation complete, awaiting verification |
| `verify(task-{id})` | Verification result |
| `fail(task-{id})` | Task failure |
| `escalate(task-{id})` | Model tier escalation |
| `solo-claim(task-{id})` | Exclusive solo claim |
| `solo-release(task-{id})` | Solo claim release |
| `revert(task-{id})` | Reverting task work |

## Acceptance Criteria
- [ ] Git context check added to Pre-Mortem pre-implementation checklist (task034 template)
- [ ] Git context check in sprint agent pre-task step (task042)
- [ ] 4 git log commands documented with explanations
- [ ] "What to look for" list documented
- [ ] Commit message prefix conventions table documented

## Verification Steps
- [ ] Pre-flight checklist in task template has git log steps
- [ ] Sprint agent workflow has git log step
- [ ] Commit prefix table is complete (all patterns agents should recognize)

## When Stuck
- Pure documentation task
- The commit prefix table is essential — it's what makes git history human AND machine readable
