---
id: 52
title: 'Add spec-vs-implementation separate commit convention'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [autonomous, agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [50, 27]
project_context: 'Separating spec updates from code changes in git history means you can always diff "what was the spec when code was written" vs "what was implemented" — crucial for debugging why an implementation diverged from the spec'
---

# Task 052: Add spec-vs-implementation separate commit convention

## Objective
Document the spec-vs-implementation commit separation convention in `template_v2/` — the rule that spec updates and code changes MUST be separate commits, never mixed.

## Context
When a task spec is updated mid-implementation (due to staleness, pivot, or discovery), mixing the spec update with code changes in a single commit makes it impossible to:
1. Know what spec version the code was written against
2. Identify whether a bug was in the spec or the implementation
3. Review the spec change independently of the code change

The solution: always commit spec changes separately.

## The Convention

### Rule: Two Separate Commits, Always

When updating a spec AND changing code in the same task:

```bash
# Commit 1: Spec update ONLY (no .py, .ts, .js files)
git add .trent/tasks/task{id}_*.md
git commit -m "spec(task-{id}): update spec v{old} → v{new}
Reason: {specific reason — e.g., 'Cursor changed OAuth flow', 'pivot to different approach'}
Updated sections: {acceptance criteria | implementation notes | dependencies}

---
Agent: {agent_id}
Model: {model}
Task: {id}
Rules-Version: {version}"

# Commit 2: Implementation ONLY (no .trent task files)
git add src/... lib/... template_v2/...
git commit -m "feat(task-{id}): implement {title} [spec v{new}]
[summary of what was implemented]

---
Agent: {agent_id}
Model: {model}
Task: {id}
Rules-Version: {version}"
```

### The `[spec v{N}]` Tag in Implementation Commits

The implementation commit message MUST include `[spec v{N}]` — the spec version it was written against.

This allows future agents to:
```bash
# Find all implementations and their spec versions
git log --grep="\[spec v" --oneline

# Check if implementation is based on current spec
# Task says spec_version: 1.2 — is there an impl commit with [spec v1.2]?
git log --grep="\[spec v1.2\]" --oneline -- src/myfile.py
```

### When to Update a Spec Mid-Implementation

Permitted reasons:
- Platform API changed (with evidence)
- Dependency task used a different approach than spec assumed
- Discovered the spec is technically incorrect/impossible as written
- Project pivot changed requirements

NOT permitted reasons:
- "I think this is a better way" (if not in acceptance criteria, don't change spec)
- Convenience — spec update to match what you already implemented

## Acceptance Criteria
- [ ] Spec-vs-implementation convention documented in template_v2 rules
- [ ] Two separate commit format examples documented
- [ ] `[spec v{N}]` tag in implementation commit messages mandatory
- [ ] Permitted vs not-permitted spec update reasons listed
- [ ] Cross-reference to task027 (spec_freshness) for `spec_version` field

## Verification Steps
- [ ] Convention documented in template_v2 rules
- [ ] Both commit formats present (spec commit, impl commit)
- [ ] `[spec v{N}]` tag rule explicitly stated

## When Stuck
- Pure documentation task
- Cross-reference task027 (spec_freshness) for the `spec_version` YAML field
- Cross-reference task050 (commit formats) for footer convention
