---
id: 27
title: 'Implement spec_freshness fields (spec_version, spec_last_verified, allow_spec_update)'
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
project_context: 'Specs go stale when the platform evolves or the project pivots — spec_freshness lets agents flag outdated specs before blindly implementing them, preventing wasted work on superseded approaches'
---

# Task 027: Implement spec_freshness fields

## Objective
Add `spec_version`, `spec_last_verified`, `allow_spec_update`, and `spec_dependencies` fields to the task YAML schema in `template_v2/`, enabling agents to detect and flag stale specifications before implementing them.

## Context
One of the major failure modes identified across projects: an agent implements a task spec faithfully, but the spec itself is outdated — either because the project pivoted, or because the underlying platform (Cursor, Claude, Gemini APIs) released breaking changes, or because an earlier task changed the architecture the spec assumed. `spec_freshness` gives agents explicit permission to flag and update stale specs before wasting implementation effort.

## YAML Fields to Add

```yaml
# In task YAML frontmatter:
spec_version: "1.0"              # Increment when spec is updated
spec_created: ''                 # YYYY-MM-DD — when spec was written
spec_last_verified: ''           # YYYY-MM-DD — when spec was last reviewed for accuracy
spec_staleness_days: 30          # How many days before spec is considered potentially stale (default: 30)
allow_spec_update: true          # Can agents update this spec if they find it's outdated? (default: true)
spec_dependencies:               # Other tasks/specs this spec assumes are complete/current
  - task_id: 1
    dependency_type: 'must_be_complete'  # or 'assumes_approach_from'
```

## Spec Freshness Protocol

### When agent picks up a task:
1. Check: `spec_last_verified` — is it more than `spec_staleness_days` old?
2. Check: `spec_dependencies` — are all dependency tasks completed? Do the approaches still match what this spec assumes?
3. If either check fails AND `allow_spec_update: true`:
   - Update the spec (acceptance criteria, implementation notes) to reflect current reality
   - Increment `spec_version` (e.g., "1.0" → "1.1")
   - Update `spec_last_verified` to today
   - Git commit: `"spec(task-{id}): update spec to v{version} — {brief reason}"`
   - Then proceed with implementation
4. If `allow_spec_update: false`:
   - Flag the staleness: add to `failure_history` with `failure_reason: spec_outdated`
   - Set `status: failed`, update TASKS.md
   - Add AI-IDEA: "Task {id} spec is stale and locked — needs human review"

### What makes a spec stale:
- Platform/library API changed (check with web search if >30 days old)
- Dependent task used a different approach than this spec assumed
- Project pivot changed the requirements
- File paths or folder structures referenced no longer exist

## Cleanup Agent Behavior

During nightly cleanup:
1. For each `[📋]` and `[ ]` task: check `spec_last_verified`
2. If staleness detected (>30 days) AND task not yet started: add to CLEANUP_REPORT.md as warning
3. Count: `stale_specs_detected: {n}` in health report

## Acceptance Criteria
- [ ] `spec_version`, `spec_last_verified`, `spec_staleness_days`, `allow_spec_update`, `spec_dependencies` added to task003 YAML schema
- [ ] Spec freshness protocol documented in task file template
- [ ] `failure_reason: spec_outdated` in task021 failure taxonomy
- [ ] Cleanup agent spec (task040) includes stale spec detection in nightly scan
- [ ] `spec-vs-implementation` commit convention documented (separate commits for spec updates vs code)

## Spec vs Implementation Commit Convention

When updating a spec:
```bash
git commit -m "spec(task-{id}): update spec v{old} → v{new}
Reason: {brief — e.g., 'Cursor API changed authentication flow'}
Updated sections: {acceptance criteria | implementation notes | dependencies}
allow_spec_update: true (confirmed)"
```

When implementing (separate commit from spec update):
```bash
git commit -m "feat(task-{id}): implement {title}
Based on spec v{version}
Agent: {agent_id}"
```

## Verification Steps
- [ ] task003 schema has all 5 spec_freshness fields
- [ ] task021 failure taxonomy has `spec_outdated`
- [ ] task040 cleanup spec includes stale spec detection
- [ ] Commit convention for spec-vs-implementation documented

## When Stuck
- Pure schema + documentation task
- The key design principle: specs are living documents that agents can update, not locked contracts
