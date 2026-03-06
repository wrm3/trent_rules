---
id: 70
title: 'Update 20_trent_tasks rule with new status values, YAML fields, verification workflow'
type: feature
status: pending
priority: high
phase: 0
subsystems: [agent-rules]
ai_safe: true
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [3, 7, 30, 32, 47, 50]
project_context: 'Rule 20 is the core task management rule — must be updated to include all new vNext features: new statuses, YAML fields, verification workflow, Ralph Wiggum rule, commit enforcement'
---

# Task 070: Update 20_trent_tasks rule with vNext features

## Objective
Create updated `20_trent_tasks.md` rule in `template_v2/` that incorporates all new vNext task management features. This is the primary rule that agents read for task operations.

## Changes From v1 to v2

### New Status Values (add to Status Indicators section)
```
[🔍] = Awaiting Verification (impl done, reviewer pending)
[⏳] = Resource-Gated (blocked on GPU/storage/API)
[🌾] = Harvested (done but approach superseded)
[📝] = Spec Being Written (TTL: 1 hour) — already exists in some versions, formalize
```

### New YAML Fields (document in Task File Format section)
Add to the YAML example:
```yaml
# Resilience fields
ai_safe: false
blast_radius: low | medium | high | critical
requires_solo_agent: false
model_tier: 1
claimed_by: null
claimed_at: null
claim_ttl_minutes: 60
claim_expires_at: null
last_heartbeat: null
spec_version: "1.0"
spec_last_verified: null
spec_staleness_days: 30
allow_spec_update: true

# Verification fields
verified_by: null
verified_at: null
evidence_of_completion: {}

# Cost tracking
execution_cost: {}

# History
failure_history: []
execution_progress: {}
```

### New Workflow Sections to Add
1. **Task Claiming Protocol** → reference task043 (atomic claiming)
2. **Verification Workflow** → reference task032 (implementer ≠ verifier)
3. **Ralph Wiggum Prevention** → reference task047 (3-strike rule)
4. **Mandatory Commit Points** → reference task050 (8 commit points)
5. **Pre-Mortem Protocol** → reference task034
6. **When Stuck Protocol** → reference task023
7. **Blast Radius Enforcement** → reference task024
8. **ai_safe Enforcement** → reference task044

## Acceptance Criteria
- [ ] Rule file created at `template_v2/.cursor/rules/20_trent_tasks.mdc`
- [ ] All 9 status values documented (including 3 new ones)
- [ ] Updated YAML frontmatter example with all new fields
- [ ] 8 new workflow sections added
- [ ] Task completion self-check updated (includes verification, ai_safe, blast_radius)
- [ ] Parity: `.claude/rules/20_trent_tasks.md` and `.agent/rules/20_trent_tasks.md` identical

## Verification Steps
- [ ] Rule file exists in template_v2 (all 3 IDE directories)
- [ ] All 9 status values in legend
- [ ] YAML example has all new fields
- [ ] All 8 workflow sections referenced

## When Stuck
- Prerequisite tasks (003, 007, 030, 032, 047, 050) provide the content for each section
- This task ASSEMBLES those pieces into a coherent rule file
- Start from the existing 20_trent_tasks.mdc and add/update sections
