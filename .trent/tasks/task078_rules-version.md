---
id: 78
title: 'Add rules_version field to trent config + commit footer convention'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [agent-rules, autonomous]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [51, 73]
project_context: 'rules_version in every agent commit lets you correlate behavior regressions to specific rule changes — if an agent starts making errors after v5.1.0, you can diff the rules at that version boundary'
---

# Task 078: Add rules_version field to trent config

## Objective
Add `rules_version` tracking to `template_v2/` — a version field in PROJECT_CONTEXT.md and the `.trent/` configuration that agents include in every commit footer, enabling correlation between agent behavior and rule versions.

## Where rules_version Lives

### In PROJECT_CONTEXT.md (add to header):
```yaml
rules_version: "5.0.0"         # Current trent system version
rules_last_updated: "YYYY-MM-DD"  # When rules were last modified
rules_source: "https://github.com/yourusername/trent_rules"  # Optional
```

### In every agent commit footer (already in task051):
```
Rules-Version: 5.0.0
```

## Version Numbering Convention

```
{major}.{minor}.{patch}

major — Breaking changes to task workflow, status system, or YAML schema
minor — New features (new rules, new commands, new templates)
patch — Bug fixes, clarifications, documentation improvements

Examples:
5.0.0 — Initial vNext (trent v2 template)
5.1.0 — Added new autonomous rule 31_trent_autonomous
5.1.1 — Fixed typo in pre-mortem template
6.0.0 — Breaking change: YAML schema change incompatible with v5
```

## How to Update rules_version

When any template_v2 rule file is modified:
1. Update `rules_version` in `PROJECT_CONTEXT.md`
2. Update version in rule file header comment (if present)
3. Commit: `"chore(rules): bump version v{old} → v{new} — {what changed}"`

## Cleanup Agent Behavior

During nightly cleanup:
1. Compare `rules_version` in PROJECT_CONTEXT.md vs latest commit with `Rules-Version:` footer
2. If mismatch: warn in CLEANUP_REPORT.md — agent running different rules version than project expects

## Acceptance Criteria
- [ ] `rules_version` and `rules_last_updated` fields in PROJECT_CONTEXT.md template
- [ ] Version numbering convention documented
- [ ] Update process documented (when/how to bump)
- [ ] Cleanup agent mismatch detection added to task040 spec

## Verification Steps
- [ ] PROJECT_CONTEXT.md template has rules_version field
- [ ] Version numbering convention (major/minor/patch) documented

## When Stuck
- Pure documentation task
- Cross-reference task051 (agent identity commits) — `Rules-Version:` footer already planned there
