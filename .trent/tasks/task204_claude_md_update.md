---
id: 204
title: 'Update CLAUDE.md trent section for vNext'
type: documentation
status: pending
priority: high
phase: 2
subsystem: installation
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: [201]
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "CLAUDE.md is the primary context file for Claude Code — must be current for accurate tool/command descriptions"
---

# Task 204: Update CLAUDE.md trent section for vNext

## Objective
Update the trent section in `CLAUDE.md` (between `<!-- TRENT SYSTEM CONTEXT -->` markers) to reflect vNext features: new commands, new file structure, new status indicators, rules version 5.1.

## Acceptance Criteria
- [ ] `@trent-cleanup` and `@trent-sprint` mentioned
- [ ] New trent files listed (ARCHITECTURE_CONSTRAINTS.md, SPRINT.md, CLEANUP_REPORT.md, SYSTEM_EXPERIMENTS.md)
- [ ] Status flow updated to include `[🔍]`
- [ ] Rules version updated to 5.1.0
- [ ] Version/date updated at bottom of CLAUDE.md
- [ ] Content outside markers unchanged

## Implementation Notes
Find markers `<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->` and `<!-- END TRENT SYSTEM CONTEXT -->` in `CLAUDE.md`. Replace section content only.
