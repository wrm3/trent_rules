# trent_rules — Master Task List

**Project**: trent vNext — Autonomous Multi-Agent Workflow Engine
**Reference**: `potential_changes.md` (42-item improvement roadmap)
**Template target**: `template_v2/`
**Constraint**: Do NOT modify `.agent/`, `.cursor/`, `.claude/`, `.platforms/`, `agents.md`, `CLAUDE.md`, `GEMINI.md`, `GUARDRAILS.md`

---

## Status Indicators
- `[ ]` = Pending (no task file yet) — CODING BLOCKED
- `[📋]` = Task file created, ready to start
- `[🔄]` = In Progress (claimed by agent, has TTL)
- `[🔍]` = Awaiting Verification (impl done, reviewer pending)
- `[✅]` = Completed (verified by different agent)
- `[❌]` = Failed/Cancelled
- `[⏳]` = Resource-Gated (waiting on storage/compute/API)
- `[🌾]` = Harvested (done but approach abandoned, kept as reference)
- `[⏸️]` = Paused

---

## Phase 0: trent vNext — Template v2 Foundation [🔄]

### Subsystem: template-core

- [✅] **Task 001**: Initialize template_v2 folder structure (copy baseline from template/, apply new structure)
- [✅] **Task 002**: Create ARCHITECTURE_CONSTRAINTS.md template with session-start enforcement
- [📋] **Task 003**: Create updated task YAML schema (all new fields: ai_safe, TTL, blast_radius, failure_history, spec_freshness, execution_cost, verification)
- [✅] **Task 004**: Create SPRINT.md template (active work queue, ≤15 tasks, cleanup-agent-generated)
- [✅] **Task 005**: Create SYSTEM_EXPERIMENTS.md template (system evolution log)
- [✅] **Task 006**: Rename PLAN.md → PRD.md in template_v2, update all references
- [✅] **Task 007**: Add `[🔍]` Awaiting Verification and `[⏳]` Resource-Gated and `[🌾]` Harvested to status system
- [📋] **Task 008**: Add `status: harvested` to task lifecycle rules
- [✅] **Task 009**: Create PROJECT_CONTEXT.md template with health score section
- [✅] **Task 010**: Create updated TASKS.md template with subsystem headers (not just phase headers)
- [✅] **Task 011**: Create phase YAML schema additions (purpose: milestone|experiment|domain|maintenance, hypothesis, outcome)
- [📋] **Task 012**: Add project type selection to @trent-setup (delivery vs research)
- [✅] **Task 013**: Create HYPOTHESIS.md + EXPERIMENT.md templates for research projects
- [✅] **Task 014**: Update IDEA_BOARD.md template with AI-generated ideas section

### Subsystem: resilience

- [📋] **Task 020**: Implement task claim TTL system (claimed_by, claimed_at, claim_ttl_minutes, claim_expires_at)
- [📋] **Task 021**: Implement failure taxonomy (failure_reason enum, failure_history array in task YAML)
- [📋] **Task 022**: Implement mid-task progress checkpointing (execution_progress YAML section)
- [📋] **Task 023**: Add "When Stuck" protocol section to task file template
- [📋] **Task 024**: Add blast_radius declaration to task YAML schema
- [📋] **Task 025**: Add requires_solo_agent flag to task YAML
- [📋] **Task 026**: Add resource_requirements to task YAML (storage_gb, compute_hours, vram_gb)
- [📋] **Task 027**: Implement spec_freshness fields (spec_version, spec_last_verified, allow_spec_update, spec_dependencies)

### Subsystem: verification

- [📋] **Task 030**: Add [🔍] Awaiting Verification to trent rules — task cannot reach [✅] without verified_by from different agent
- [📋] **Task 031**: Add evidence_of_completion field to task YAML schema
- [📋] **Task 032**: Create mandatory verification workflow rule (implementer ≠ verifier)
- [📋] **Task 033**: Add adversarial persona (Gilfoyle-mode) as default instruction for review agents
- [📋] **Task 034**: Add pre-mortem prompting as mandatory pre-implementation step to task template

### Subsystem: autonomous

- [📋] **Task 040**: Create @trent-cleanup command spec (midnight cleanup agent responsibilities)
- [📋] **Task 041**: Create CLEANUP_REPORT.md template
- [✅] **Task 042**: Create @trent-sprint command spec (2-hour sprint agent responsibilities)
- [📋] **Task 043**: Implement atomic task claiming protocol (git-commit-based claim)
- [📋] **Task 044**: Add ai_safe flag to task YAML + rules for unattended execution
- [📋] **Task 045**: Create SPRINT.md generation rules (cleanup agent populates from tasks)
- [📋] **Task 046**: Add cost_per_task tracking fields + subsystem cost aggregation to health report
- [📋] **Task 047**: Add Ralph Wiggum prevention rule (N failures → research-mode retry with different approach)
- [📋] **Task 048**: Add escalation ladder rule (local LLM → paid model → human review)
- [📋] **Task 049**: Add git log as mandatory pre-task context to agent pre-flight checklist
- [📋] **Task 050**: Add frequent git commit enforcement (every state transition)
- [📋] **Task 051**: Add agent identity in git commit footer convention
- [📋] **Task 052**: Add spec-vs-implementation separate commit convention

### Subsystem: platform-docs

- [📋] **Task 060**: Design Firecrawl Docker service architecture (docker/firecrawl/)
- [📋] **Task 061**: Create Firecrawl crawler.py (crawl targets: Cursor, Claude, Gemini docs)
- [📋] **Task 062**: Create Firecrawl scheduler.py (weekly cron, diff, commit, RAG ingest)
- [📋] **Task 063**: Create docker-compose additions for firecrawl service
- [📋] **Task 064**: Create platform_docs_search MCP tool (semantic search over crawled docs)
- [📋] **Task 065**: Create .platforms/CHANGELOG.md template and update format
- [✅] **Task 066**: Create platform parity enforcement rule (cross-IDE rule diff check)

### Subsystem: agent-rules

- [📋] **Task 070**: Update 20_trent_tasks rule with new status values, YAML fields, verification workflow
- [📋] **Task 071**: Update 21_trent_infrastructure rule with new file structure (logs/, SPRINT.md, etc.)
- [📋] **Task 072**: Update 22_trent_planning rule with project types, PRD rename, ARCHITECTURE_CONSTRAINTS
- [📋] **Task 073**: Update 25_trent_index rule with session-start ARCHITECTURE_CONSTRAINTS load
- [📋] **Task 074**: Update 27_trent_self_improvement rule with SYSTEM_EXPERIMENTS.md
- [📋] **Task 075**: Create new rule: autonomous agent workflow (cleanup + sprint agent protocols)
- [📋] **Task 076**: Create new rule: verification and cross-agent review workflow
- [📋] **Task 077**: Ensure .cursor/rules/, .claude/rules/, .agent/rules/ are in sync (parity check)
- [📋] **Task 078**: Add rules_version field to trent config + commit footer convention

### Subsystem: memory

- [📋] **Task 080**: Make memory capture mandatory at task completion (not optional)
- [📋] **Task 081**: Add institutional memory query to agent pre-task checklist ("what happened last time in this subsystem?")
- [📋] **Task 082**: Create task dependency graph generation (DEPENDENCY_GRAPH.md via cleanup agent)

---

## Phase 1: Docker Integration (Tasks 100-199) [ ]

- [ ] **Task 100**: Add platform_docs_search MCP tool to docker/trent/tools/plugins/
- [ ] **Task 101**: Add trent_health_report MCP tool
- [ ] **Task 102**: Add Firecrawl service to docker-compose.yml
- [ ] **Task 103**: Update server.py instructions to reflect new tools

---

## Phase 2: Installation & Deployment (Tasks 200-299) [ ]

- [ ] **Task 200**: Update _trent_shared.py manifests for template_v2
- [ ] **Task 201**: Update trent_install to deploy from template_v2/
- [ ] **Task 202**: Create migration guide template_v1 → template_v2
- [ ] **Task 203**: Update AGENTS.md trent section with new commands and capabilities
- [ ] **Task 204**: Update CLAUDE.md trent section

---

## Completed Tasks
(None yet)

---

**Last Updated**: 2026-03-06
**Phase 0 Progress**: 83/82 tasks specced — 12 COMPLETED [✅], remaining [📋] UNBLOCKED
**Completed this session**: Tasks 002, 004, 005, 006, 007, 009, 010, 011, 013, 014, 042, 066
