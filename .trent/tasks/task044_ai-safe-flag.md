---
id: 44
title: 'Add ai_safe flag to task YAML + rules for unattended execution'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 24]
project_context: 'ai_safe is the human-controlled gate for autonomous execution — the human explicitly marks which tasks are safe to run without supervision, nothing runs unattended without this flag'
---

# Task 044: Add ai_safe flag to task YAML + rules for unattended execution

## Objective
Add `ai_safe: true/false` field to the task YAML schema in `template_v2/`, define what makes a task ai_safe, and document the enforcement rules for unattended agent execution.

## Context
The human needs an explicit veto mechanism for autonomous agents: "Do NOT work on this without me." Without this, autonomous agents might tackle risky work while the human is unavailable. The `ai_safe` flag is the human's explicit authorization for unattended execution.

## YAML Field to Add

```yaml
ai_safe: false           # default: false — requires human to explicitly set true
ai_safe_reason: ''       # Why this task is/isn't safe for unattended execution
ai_safe_set_by: ''       # Who set this flag (human | {agent_id})
ai_safe_set_at: ''       # When it was set
```

## What Makes a Task ai_safe

### ai_safe: true (safe for unattended execution)
All of these must be true:
- `blast_radius: low` or `blast_radius: medium` (NOT high or critical)
- Task does NOT touch external paid APIs (no Meshy, OpenAI API calls)
- Task does NOT modify database schemas or run migrations
- Task does NOT delete files (only creates/updates)
- Task has clear, verifiable acceptance criteria
- Task has no unresolved spec dependencies
- Task has been reviewed by human at least once (or is a template/doc task)

### ai_safe: false (requires human at keyboard)
Any of these makes a task NOT safe:
- `blast_radius: high` or `critical`
- Touches production data or external paid services
- Has ambiguous acceptance criteria
- Has `requires_solo_agent: true` (solo + unattended = high risk)
- Human explicitly set `ai_safe: false` (human veto, always honored)
- Task is in a subsystem with health score < 40 (too many recent failures)

## Enforcement Rules

### For cleanup agent (sprint population):
- NEVER include `ai_safe: false` tasks in SPRINT.md
- If no `ai_safe: true` tasks exist: generate empty SPRINT.md with note "No safe tasks available for autonomous execution"

### For sprint agents:
- MUST check `ai_safe` before claiming ANY task
- If `ai_safe: false`: do NOT claim, add to exclusion summary
- Sprint agents cannot set `ai_safe: true` — only humans can

### Who can set ai_safe: true
- **Human only** — via direct file edit or IDE
- AI agents can SUGGEST tasks should be ai_safe (via AI-IDEA on IDEA_BOARD)
- AI agents CAN set `ai_safe: false` (they can revoke safety, not grant it)

## Default Behavior

New tasks created by agents: `ai_safe: false` (conservative default)
New tasks created during `@trent-setup`: `ai_safe: false` (human reviews and sets)
Template tasks (creating files, writing docs): human should set `ai_safe: true` after reviewing

## Acceptance Criteria
- [ ] `ai_safe:` field added to task003 YAML schema (with ai_safe_reason, ai_safe_set_by, ai_safe_set_at)
- [ ] Criteria for ai_safe: true vs false documented
- [ ] "Human only can grant" rule explicitly stated
- [ ] Cleanup agent exclusion rule documented
- [ ] Default: false rule documented

## Verification Steps
- [ ] task003 schema has all 4 ai_safe fields
- [ ] Criteria list (what makes safe/unsafe) documented
- [ ] "Human only grants" rule is explicit
- [ ] Default value is false

## When Stuck
- Pure schema + documentation task
- The critical design principle: AI agents can revoke safety but cannot grant it
