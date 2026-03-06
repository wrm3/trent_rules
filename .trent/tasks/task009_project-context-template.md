---
id: 9
title: 'Create updated PROJECT_CONTEXT.md template with health score section'
type: feature
status: pending
priority: high
phase: 0
subsystems: [template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [1]
project_context: 'PROJECT_CONTEXT.md is what agents read at session start — adding health scores and architecture constraints reference makes it the single authoritative session-start document'
---

# Task 009: Create updated PROJECT_CONTEXT.md template with health score section

## Objective
Create `template_v2/.trent/PROJECT_CONTEXT.md` with an updated template that includes:
1. Project health score section (per-project and per-subsystem)
2. Reference to ARCHITECTURE_CONSTRAINTS.md (load at session start)
3. Current sprint reference
4. Autonomous agent configuration section

## Context
The existing PROJECT_CONTEXT.md template is minimal. For autonomous agents running without humans at the keyboard, this file needs to be the complete session-start briefing — health status, constraints, active sprint, and agent behavior configuration.

## Template Content

```markdown
# PROJECT_CONTEXT.md

## Mission
[One-sentence project mission statement]

## Current Phase
**Phase {N}**: {Phase Name}
**Status**: [in_progress | planning | completed]
**Objective**: [What this phase accomplishes]

---

## Project Health Score
<!-- Updated by @trent-cleanup nightly -->

**Overall Health**: {score}/100 | {status: healthy | degraded | critical}
**Last Updated**: {YYYY-MM-DD}

| Subsystem | Health | Pending | In Progress | Blocked | Notes |
|-----------|--------|---------|-------------|---------|-------|
| {name} | {score}/100 | {n} | {n} | {n} | {note} |

**Health Calculation**: (completed / total_non_cancelled) × 100, penalized for:
- Tasks stuck in [🔄] past TTL: -5 per task
- Tasks in [🔍] > 4 hours: -3 per task
- Tasks with failure_history > 2: -10 per task
- Subsystems with 0 completed tasks: -15

---

## Architecture Constraints
**⚠️ MANDATORY: Read ARCHITECTURE_CONSTRAINTS.md before any coding.**
[List top 3 most critical constraints inline here for quick reference]
1. {Constraint 1}
2. {Constraint 2}
3. {Constraint 3}
**Full list**: `.trent/ARCHITECTURE_CONSTRAINTS.md`

---

## Active Sprint
**Sprint File**: `.trent/SPRINT.md`
**Generated**: {timestamp}
**Valid Until**: {timestamp}
**Tasks in Sprint**: {n}

---

## Autonomous Agent Configuration

### Unattended Execution Settings
```yaml
sprint_interval_hours: 2
cleanup_time: "00:00"  # UTC
max_sprint_tasks: 15
default_claim_ttl_minutes: 60
escalation_threshold_failures: 3  # Ralph Wiggum limit
escalation_ladder:
  - local_llm
  - claude_sonnet
  - claude_opus
  - human_review
```

### Human Approval Required For
- Tasks with `ai_safe: false`
- Tasks with `blast_radius: high`
- Tasks with `requires_solo_agent: true` (when multiple agents detected)
- Phase completion gates
- Architecture constraint changes

---

## Subsystem Registry
[Brief list of subsystems — full registry in SUBSYSTEMS.md]

## Key Files
- `.trent/PRD.md` — Product Requirements Document
- `.trent/TASKS.md` — Master task list
- `.trent/SPRINT.md` — Active sprint queue (auto-generated)
- `.trent/ARCHITECTURE_CONSTRAINTS.md` — Non-negotiable constraints
- `.trent/BUGS.md` — Bug tracking
- `.trent/SYSTEM_EXPERIMENTS.md` — System evolution log
```

## Acceptance Criteria
- [ ] File exists at `template_v2/.trent/PROJECT_CONTEXT.md`
- [ ] Health score section present with per-subsystem table
- [ ] Architecture constraints reference present
- [ ] Autonomous agent configuration YAML block present
- [ ] Sprint reference section present
- [ ] All placeholder values use `{curly_brace}` format

## Verification Steps
- [ ] File exists at correct path
- [ ] Health score table has correct columns
- [ ] Escalation ladder matches the agreed ladder (local → sonnet → opus → human)
- [ ] ARCHITECTURE_CONSTRAINTS.md reference is bolded/prominent

## When Stuck
- Pure template task — fill in the structure shown above
- Keep placeholders generic; project-specific values get filled in at `@trent-setup` time
