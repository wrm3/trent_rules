---
id: 20
title: 'Implement Task Claim TTL System'
type: feature
status: pending
priority: critical
phase: 0
subsystem: resilience
ai_safe: true
requires_solo_agent: false
blast_radius: low
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 45
claim_ttl_minutes: 90
dependencies: [3]
---

# Task 020: Implement Task Claim TTL System

## Objective
Add task claim lease/TTL to the trent rules so that tasks claimed by agents that die
(bluescreen, power loss, rate limit, token limit) are automatically recoverable by the
cleanup agent. A task in `[🔄]` must never be permanently stuck.

## Background
From `potential_changes.md` Idea #6 (resilience): Any system where workers can die mid-task
needs either a heartbeat or a lease expiry. This is distributed systems 101.
Currently `[🔄]` is permanent — a dead agent holds the lock forever.

## Acceptance Criteria
- [ ] TTL fields added to task YAML schema in template (task003 must complete first)
- [ ] Rule added to `template_v2/.cursor/rules/20_trent_tasks.mdc` (and .claude and .agent equivalents)
- [ ] Cleanup agent spec references TTL check as mandatory step
- [ ] Rule clearly states: claimed_at + claim_ttl_minutes = claim_expires_at
- [ ] Rule clearly states: if claim_expires_at < now → reset to [📋] + log failure_reason: agent_timeout
- [ ] Default TTL formula documented: estimated_duration_minutes * 1.5
- [ ] Short task TTL: 30-45 min minimum (even if estimate is very short)
- [ ] Long task TTL: up to 8 hours for compute-heavy tasks
- [ ] Heartbeat field (last_heartbeat) documented for long-running tasks
- [ ] Git commit: `feat(template-v2): implement task claim TTL resilience system`

## Rule Text to Add (to 20_trent_tasks)

```markdown
### Task Claim TTL (Resilience)

Every [🔄] task MUST have a claim expiry. When an agent claims a task:

1. Set claimed_by: {agent-id}
2. Set claimed_at: {ISO-8601 timestamp}
3. Set claim_ttl_minutes: {estimated_duration_minutes * 1.5, min 30}
4. Set claim_expires_at: {claimed_at + claim_ttl_minutes}
5. Commit: "claim: task{id} claimed by {agent} [expires: {claim_expires_at}]"

**On task completion**: Clear claimed_by, claimed_at, claim_expires_at

**Cleanup agent MUST**:
- Check all [🔄] tasks for expired claims (claim_expires_at < now)
- Reset expired tasks to [📋]
- Add to failure_history: failure_reason: agent_timeout
- Commit: "cleanup: task{id} claim expired, reset to ready"

**Long-running tasks** (>60 min estimate):
- Agent writes last_heartbeat every 15 minutes
- Cleanup considers claim dead if last_heartbeat is stale by 2x heartbeat interval
```

## When Stuck
This is a rules/template task — write markdown rule text, no code execution needed.
Reference `potential_changes.md` TTL section for full design rationale.
