---
id: 51
title: 'Add agent identity in git commit footer convention'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [50]
project_context: 'When 5 agents work overnight, git log must show WHICH agent made each commit — agent identity in commit footer enables post-hoc debugging, cost attribution, and identifying which agent produced good vs bad work'
---

# Task 051: Add agent identity in git commit footer convention

## Objective
Define the agent identity footer convention for all git commits made by autonomous agents in `template_v2/` — a standardized multi-line commit message footer that identifies the agent, model, task, and context.

## The Agent Identity Footer

All commits made by autonomous agents MUST include a footer:

```
feat(task-042): implement @trent-sprint command spec

[implementation summary — what was done]

---
Agent: cursor-agent-session-abc123
Model: claude-sonnet-4-5
Task: 042
Phase: 0
Subsystem: autonomous
Cost: ~$0.08
Tokens: 45,230 input / 2,100 output
Rules-Version: v5.0.0
Sprint: 2026-03-07T02:00:00Z
```

## Footer Fields

| Field | Format | Required | Description |
|-------|--------|----------|-------------|
| `Agent` | `{ide}-{type}-session-{hash}` | ✅ | Unique agent identifier |
| `Model` | `{model-name}` | ✅ | Exact model used |
| `Task` | `{numeric id}` | ✅ | Task being worked on |
| `Phase` | `{phase number}` | ✅ | Current project phase |
| `Subsystem` | `{subsystem name}` | ✅ | Primary subsystem affected |
| `Cost` | `~${amount}` | ⬜ | Estimated API cost |
| `Tokens` | `{in} input / {out} output` | ⬜ | Token usage |
| `Rules-Version` | `{version}` | ✅ | trent rules version used |
| `Sprint` | `{ISO timestamp}` | ⬜ | Sprint window this was in |

## Agent ID Format

```
{ide}-{agent-type}-session-{short-hash}

Examples:
cursor-sprint-session-a1b2c3
claude-cleanup-session-d4e5f6
cursor-verifier-session-g7h8i9
gemini-sprint-session-j1k2l3
```

The `{short-hash}` is a 6-char random string generated at session start, stable for the life of that session.

## Human Commits (distinguishing from agent commits)

Human commits do NOT need the footer. This allows git log analysis to distinguish:
```bash
# Find only agent commits
git log --grep="^Agent:" -10

# Find commits from a specific agent
git log --grep="Agent: cursor-sprint" -5

# Find all commits for a task by any agent
git log --grep="Task: 042" -10
```

## Acceptance Criteria
- [ ] Agent identity footer format documented in `template_v2/` rules
- [ ] Footer fields table with required/optional markers
- [ ] Agent ID format convention defined
- [ ] Git log query patterns for finding agent commits documented
- [ ] Human commits distinguished (no footer required)

## Verification Steps
- [ ] Footer format is documented in template_v2 agent rules
- [ ] All required fields listed
- [ ] Agent ID format is consistent and parseable

## When Stuck
- Pure documentation task
- Cross-reference task050 (commit formats) — footer appended to those commit messages
