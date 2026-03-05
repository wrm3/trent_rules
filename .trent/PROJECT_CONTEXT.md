# Project Context: trent_rules

## Mission
Build the next evolution of the trent AI task management system — an autonomous, resilient,
multi-agent workflow engine that works even when the developer isn't at the keyboard.

## Current Phase
**Phase 0: trent vNext Planning & Template v2**

Capture all lessons learned from project analyses (Maestro2, VisionLang), design the
next version of the trent system, and build it out in `template_v2/` without disrupting
the live system in `.cursor/`, `.claude/`, `.agent/`.

## Architecture Principles

### Non-Negotiable Constraints
1. **Do NOT modify** `.agent/`, `.cursor/`, `.claude/`, `.platforms/`, `agents.md`,
   `CLAUDE.md`, `GEMINI.md`, `GUARDRAILS.md` in the project root — these keep the live
   system running during development.
2. **Do NOT disrupt** the Docker trent server — it is in active use.
3. All new template work goes in `template_v2/`.
4. The live `template/` folder is the reference baseline — copy and improve, don't replace.

### Design Philosophy
- Autonomous-first: every workflow must work without a human present
- Resilient by default: task claims expire, checkpoints are written, failures are data
- Verified not assumed: tasks require cross-agent verification before closing
- Living not static: specs can update, docs stay current, memory is captured
- Research-aware: delivery and research projects get different default behaviors

## Success Criteria

### Primary Objectives
- [ ] template_v2 contains complete, improved trent system
- [ ] All 42 improvements from potential_changes.md implemented or explicitly deferred
- [ ] Firecrawl automation integrated for living platform documentation
- [ ] Task spec files created for all Phase 0 tasks
- [ ] template_v2 installable via updated trent_install MCP tool

### Quality Standards
- Each new rule file has a clear purpose, no overlap with others
- All new YAML fields have examples in task templates
- New status values have visual indicators (Windows-safe)
- Breaking changes from template/ to template_v2/ are documented

## Scope Boundaries

### In Scope (template_v2/)
- New and updated `.trent/` templates and rules
- New `.cursor/rules/`, `.claude/rules/`, `.agent/rules/` content
- Firecrawl Docker integration
- New MCP tools for platform doc search
- Updated task/phase YAML schemas

### Out of Scope (this phase)
- Modifying live `.cursor/`, `.claude/`, `.agent/` configs
- Modifying Docker trent server internals
- Database-driven version (post-Maestro2)
- Changes to existing template/ folder

## Key References
- `potential_changes.md` — Full 42-item improvement roadmap (the design document)
- `template/` — Current v1 template (reference baseline)
- `docker/` — Live MCP server (do not disrupt)

---

**Last Updated**: 2026-03-05
**Project Status**: Active — Phase 0
**Current Phase**: Phase 0 - trent vNext Planning & Template v2
