---
id: 48
title: 'Add escalation ladder rule (local LLM → paid model → human review)'
type: feature
status: pending
priority: high
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [47, 9]
project_context: 'Start cheap, escalate when stuck — local LLM for simple template tasks, Sonnet for standard implementation, Opus for complex/stuck tasks, human for critical decisions; saves thousands in API costs monthly'
---

# Task 048: Add escalation ladder rule

## Objective
Add the escalation ladder rule to task templates and autonomous agent rules in `template_v2/` — defining which model tier handles which task complexity, and the automatic escalation protocol when a task exceeds a tier's capability.

## The Escalation Ladder

```
Tier 0: LOCAL LLM (free)
  - Use for: template creation, file moves, simple find-replace, documentation
  - Task indicators: blast_radius: low, effort ≤ 30 min, no logic required
  - Fail threshold: 1 failure → escalate to Tier 1

Tier 1: CLAUDE SONNET (standard cost)
  - Use for: standard implementation, API integrations, moderate complexity
  - Task indicators: blast_radius: low/medium, effort 30min-4h, moderate logic
  - Fail threshold: 2 failures → escalate to Tier 2

Tier 2: CLAUDE OPUS (high cost)
  - Use for: complex algorithms, architectural decisions, debugging deep issues
  - Task indicators: blast_radius: medium/high, effort 4h+, complex logic
  - Fail threshold: 1 failure → escalate to Tier 3 (human)
  
Tier 3: HUMAN REVIEW
  - Used when: 3 total failures, blast_radius: critical, ai_safe: false, architectural pivots
  - Action: set task to [❌], add to CLEANUP_REPORT Actions Required section
  - Human decides: attempt differently, descope, redesign, or abandon
```

## YAML Fields to Add

```yaml
# In task YAML:
model_tier: 0 | 1 | 2 | 3    # Suggested starting tier (0=local, 1=sonnet, 2=opus, 3=human)
current_tier: 1               # Updated by agent on escalation
escalation_history:           # Track when escalations occurred
  - from_tier: 0
    to_tier: 1
    reason: ''
    escalated_by: ''
    escalated_at: ''
```

## Tier Assignment Heuristics

Cleanup agent or human assigns `model_tier` at task creation:

| Indicator | Suggested Tier |
|-----------|---------------|
| Pure template/file task | 0 (local) |
| blast_radius: low + effort ≤ 30min | 0 (local) |
| Standard feature implementation | 1 (sonnet) |
| blast_radius: medium, moderate complexity | 1 (sonnet) |
| Complex algorithm, debugging | 2 (opus) |
| blast_radius: high | 2 (opus) |
| ai_safe: false | 3 (human) |
| failure_history.length >= 3 | 3 (human) |

## Escalation Commit Format

```bash
git commit -m "escalate(task-{id}): tier {N} → tier {N+1}
Reason: {failure reason / exceeded capability}
Attempts at tier {N}: {count}
New model: {model_name}"
```

## Acceptance Criteria
- [ ] Escalation ladder documented in task template and rules
- [ ] 4-tier ladder with criteria for each tier
- [ ] `model_tier`, `current_tier`, `escalation_history` YAML fields
- [ ] Tier assignment heuristics table
- [ ] Escalation commit format
- [ ] Cleanup agent uses `model_tier: 0` tasks as "free sprint" priority

## Verification Steps
- [ ] 4 tiers defined with clear criteria
- [ ] YAML fields for escalation tracking
- [ ] Heuristics table present
- [ ] Escalation commit format documented

## When Stuck
- Cross-reference task047 (Ralph Wiggum) — escalation ladder is the mechanism that executes strike 3
- Cross-reference task009 (PROJECT_CONTEXT) — escalation_ladder config lives there
