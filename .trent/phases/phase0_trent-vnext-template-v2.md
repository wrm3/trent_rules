---
phase: 0
name: 'trent vNext — Template v2 Foundation'
status: in_progress
purpose: delivery
subsystems: [template-core, resilience, verification, autonomous, platform-docs, agent-rules, memory]
task_range: '001-099'
prerequisites: []
started_date: '2026-03-05'
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 0: trent vNext — Template v2 Foundation

## Overview
Build the complete improved trent system template in `template_v2/`. This is a delivery phase
(not experimental) — the deliverables are clear, the design is documented in `potential_changes.md`.

## Objectives
- All 42 improvements from `potential_changes.md` implemented or explicitly deferred with reason
- `template_v2/` is a complete, installable trent template
- Firecrawl automation integrated and documented
- All new YAML schemas, rules, and commands created and verified

## Constraints (Non-Negotiable)
- DO NOT modify `.agent/`, `.cursor/`, `.claude/`, `.platforms/` in project root
- DO NOT modify `agents.md`, `CLAUDE.md`, `GEMINI.md`, `GUARDRAILS.md` in project root
- DO NOT disrupt the live Docker trent server
- All work in `template_v2/` and `docker/firecrawl/` (new service only)

## Deliverables
- [ ] `template_v2/` — complete installable template with all vNext improvements
- [ ] `template_v2/.trent/` — updated schemas, templates, and new files
- [ ] `template_v2/.cursor/rules/` — updated rules with all vNext behaviors
- [ ] `template_v2/.claude/rules/` — parity with cursor rules
- [ ] `template_v2/.agent/rules/` — parity with cursor rules
- [ ] `docker/firecrawl/` — Firecrawl service design and implementation
- [ ] New MCP tool: `platform_docs_search`

## Acceptance Criteria
- [ ] Task 001 complete: template_v2 initialized
- [ ] ARCHITECTURE_CONSTRAINTS.md template exists and is referenced in session-start rules
- [ ] Task claim TTL system implemented in rules
- [ ] [🔍] Awaiting Verification status exists in all rule files
- [ ] verified_by enforcement rule exists
- [ ] Firecrawl architecture documented and service created
- [ ] Platform parity: .cursor/ .claude/ .agent/ rules are identical in content
- [ ] @trent-cleanup command fully specced
- [ ] SPRINT.md template exists

## Notes
Design document: `potential_changes.md` (42-item roadmap, full rationale for every change)
Reference baseline: `template/` (current v1 — read only)
