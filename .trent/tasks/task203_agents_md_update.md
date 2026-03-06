---
id: 203
title: 'Update AGENTS.md trent section with vNext commands'
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
project_context: "AGENTS.md is the universal instruction file — it must reflect new capabilities so IDEs display them correctly"
---

# Task 203: Update AGENTS.md trent section with vNext commands

## Objective
Update the trent section in `AGENTS.md` (between `<!-- TRENT SYSTEM SECTION -->` markers) to add the new `@trent-cleanup`, `@trent-sprint`, and `platform_docs_search` tool.

## Acceptance Criteria
- [ ] `@trent-cleanup` listed in commands table
- [ ] `@trent-sprint` listed in commands table
- [ ] `platform_docs_search` listed in MCP Tools table
- [ ] `trent_health_report` listed in MCP Tools table
- [ ] New status indicators (`[📝]`, `[🔍]`, `[⏳]`, `[🌾]`) added to status table
- [ ] Version/date updated at bottom of file
- [ ] Content outside markers unchanged

## Implementation Notes
Find the trent section between `<!-- TRENT SYSTEM SECTION - DO NOT EDIT MANUALLY -->` and `<!-- END TRENT SYSTEM SECTION -->` in `AGENTS.md`. Make targeted additions only.
