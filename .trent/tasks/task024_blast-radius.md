---
id: 24
title: 'Add blast_radius declaration to task YAML schema'
type: feature
status: pending
priority: high
phase: 0
subsystems: [resilience, template-core]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3]
project_context: 'blast_radius tells the autonomous agent and cleanup agent how dangerous a task is — low means safe to run unattended, high means stop and get human approval first'
---

# Task 024: Add blast_radius declaration to task YAML schema

## Objective
Add `blast_radius`, `affected_files_estimate`, and `actual_files_changed` fields to the task YAML schema in `template_v2/`, and document the blast_radius enforcement rules for autonomous agents.

## Context
Not all tasks are equal risk. A task that creates a new template file is safe to run at 2am. A task that refactors the database migration system touches dozens of files and could break everything. `blast_radius` gives agents the vocabulary to self-assess risk and gives the cleanup agent the ability to exclude high-blast tasks from unattended sprints.

## YAML Fields to Add

```yaml
# In task YAML frontmatter:
blast_radius: low | medium | high | critical
affected_files_estimate: 1-3  # rough count of files this task will touch
actual_files_changed: 0       # updated by agent after completion (for accuracy tracking)

# blast_radius definitions:
# low      — 1-5 files, isolated change, easily reversible
# medium   — 6-20 files, affects 1 subsystem, git revert recovers
# high     — 20+ files, affects multiple subsystems, hard to reverse cleanly
# critical — schema changes, deletions, external API calls with side effects, data migrations
```

## Blast Radius Enforcement Rules

### For autonomous sprint agents (unattended):
- `low` → run freely
- `medium` → run if `ai_safe: true` AND no other `medium+` task is in progress by another agent
- `high` → NEVER run unattended — requires `requires_solo_agent: true` AND human approval flag
- `critical` → NEVER run unattended — always requires human at keyboard

### For cleanup agent (sprint population):
- Exclude `high` and `critical` blast_radius tasks from SPRINT.md unless `human_approved: true`
- Include in Exclusion Summary: `blast_radius_excluded: {count}, task IDs: {ids}`

### For implementing agents (self-assessment):
Before starting any task, the agent should:
1. Read `blast_radius` from YAML
2. If `high` or `critical` and no human is present: stop, add to SPRINT exclusions, log reason
3. If `medium` and another medium+ task is active: wait or claim different task

## Acceptance Criteria
- [ ] `blast_radius:` field added to task003 YAML schema
- [ ] `affected_files_estimate:` and `actual_files_changed:` fields in schema
- [ ] Four blast_radius values defined with clear criteria
- [ ] Enforcement rules documented in resilience rule template
- [ ] Cleanup agent spec (task040) updated to reference blast_radius in exclusion logic
- [ ] SPRINT.md template (task004) exclusion table includes blast_radius as exclusion reason

## Verification Steps
- [ ] task003 schema has all three blast_radius-related fields
- [ ] Four blast_radius levels defined with file count ranges
- [ ] Enforcement matrix (low/medium/high/critical × unattended) documented
- [ ] Cleanup agent exclusion logic references blast_radius

## When Stuck
- Pure schema + documentation task
- Cross-reference task003 (YAML schema) — add fields there
- Cross-reference task040 (cleanup spec) — add blast_radius to exclusion logic
