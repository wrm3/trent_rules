# PRD: trent vNext — Autonomous Multi-Agent Workflow Engine

**Version**: 1.0
**Created**: 2026-03-05
**Status**: Active Planning

---

## 1. Product Overview

### 1.1 Summary

trent vNext is the next evolution of the trent AI-assisted task management system. The
current system (v5.x) is optimized for human-supervised single-agent work. vNext is
designed for **autonomous multi-agent operation** — agents working on scheduled sprints,
without a human present, on multiple projects simultaneously.

The core insight from analyzing real projects (Maestro2: 725-task delivery project;
VisionLang: sequential research experiments): the failure modes of large projects are
not organizational — they are **structural gaps in the task system itself**. Tasks get
stuck invisibly, agents lie about completion, specs go stale, dead agents hold locks
forever, and a single failing subsystem blocks everything else with no visibility.

vNext addresses these gaps while remaining backward-compatible with existing projects.

### 1.2 The Design Document
All 42 proposed improvements are documented with full rationale in:
`potential_changes.md` — read this before implementing any task in this project.

---

## 2. Goals

### 2.1 Business Goals
- Enable solo developer to run autonomous agents on multiple projects overnight/while at day job
- Reduce $3-4K/month AI spend through cost-per-task visibility and escalation ladders
- Race China on VisionLang compression technology by multiplying output via automation
- Create a system sellable/deployable to other developers (MCP + template install)

### 2.2 Technical Goals
- Tasks cannot get invisibly stuck (TTL lease system)
- Agents cannot self-report completion without cross-verification
- Specs stay current (living docs + spec freshness)
- Failure is data, not just a status flag (failure taxonomy)
- Platform docs stay current automatically (Firecrawl + RAG)

### 2.3 Non-Goals
- Database-driven backend (deferred post-Maestro2)
- Real-time agent orchestration UI (Maestro2 provides this)
- Replacing `.cursor/`, `.claude/`, `.agent/` live configs (additive only)

---

## 3. Phases

### Phase 0: Template v2 Foundation (Tasks 001-099)
Build the complete improved template in `template_v2/`. This is the primary deliverable.

**Subsystems**:
- `template-core` — `.trent/` structure, YAML schemas, status system
- `platform-docs` — Firecrawl integration, living docs automation
- `agent-rules` — Updated rules for `.cursor/`, `.claude/`, `.agent/`
- `verification` — Cross-agent review workflow, [🔍] status
- `resilience` — TTL leases, checkpointing, failure taxonomy
- `autonomous` — SPRINT.md, cleanup agent spec, health scores

### Phase 1: Docker Integration (Tasks 100-199)
Add new MCP tools to the trent Docker server:
- `platform_docs_search` — query living platform docs
- `trent_health_report` — generate project health score
- Firecrawl crawl scheduler

### Phase 2: Installation & Deployment (Tasks 200-299)
- Update `trent_install` to deploy from `template_v2/`
- Migration guide from template v1 to v2
- Update `_trent_shared.py` manifests

---

## 4. Key Design Decisions

### 4.1 New Task Status Values
```
[ ]  = Pending (no file yet) — same as v1
[📋] = Ready (file created) — same as v1
[🔄] = In Progress — same as v1, now has TTL
[🔍] = Awaiting Verification — NEW: impl done, reviewer not yet run
[✅] = Completed — same as v1, now requires verified_by
[❌] = Failed/Cancelled — same as v1
[⏳] = Resource-Gated — NEW: ready but blocked on storage/compute
[🌾] = Harvested — NEW: done but approach abandoned, kept as reference
[⏸️] = Paused — same as v1
```

### 4.2 New Task YAML Fields
```yaml
# Autonomy
ai_safe: true | false
requires_solo_agent: true | false
blast_radius: low | medium | high

# Resilience
claimed_by: agent-id
claimed_at: ISO-timestamp
claim_ttl_minutes: 120
claim_expires_at: ISO-timestamp
estimated_duration_minutes: 60

# Verification
requires_verification: true
verified_by: agent-id (different from implementing agent)
evidence_of_completion:
  type: test_output | compile_log | runtime_log
  path: .trent/logs/task001_test.log

# Failure
failure_history:
  - attempt: 1
    agent: cursor-agent-01
    failure_reason: compilation_error | test_failure | spec_outdated | approach_wrong | resource_unavailable | escalation_needed | timeout | agent_timeout
    failure_note: human-readable description
    failure_log: path-to-log

# Spec management
spec_version: 1
spec_last_verified: YYYY-MM-DD
allow_spec_update: true | false
spec_dependencies:
  - name: library-name
    pinned_version: "1.2.3"
    last_verified: YYYY-MM-DD

# Progress (for checkpointing)
execution_progress:
  last_checkpoint: step_N_of_M
  checkpoint_date: ISO-timestamp
  completed_steps: []
  remaining_steps: []

# Cost tracking
execution_cost:
  model_used: model-name
  input_tokens: 0
  output_tokens: 0
  estimated_cost_usd: 0.00
```

### 4.3 New Template Files
```
template_v2/.trent/
├── ARCHITECTURE_CONSTRAINTS.md  ← NEW: non-negotiable constraints
├── SPRINT.md                    ← NEW: active work queue (≤15 tasks)
├── SYSTEM_EXPERIMENTS.md        ← NEW: system evolution log
├── PRD.md                       ← RENAMED from PLAN.md
├── TASKS.md                     ← UPDATED: new statuses + subsystem headers
├── BUGS.md                      ← same
├── PROJECT_CONTEXT.md           ← UPDATED: includes health score section
├── PROJECT_GOALS.md             ← same
├── SUBSYSTEMS.md                ← same
├── FILE_REGISTRY.md             ← same
├── IDEA_BOARD.md                ← UPDATED: AI-generated ideas section
├── tasks/                       ← task files with new YAML schema
├── phases/                      ← phase files with purpose/hypothesis fields
└── logs/                        ← NEW: execution evidence logs
```

### 4.4 Project Types
At `@trent-setup`, the system asks: **Delivery or Research project?**

| Behavior | Delivery | Research |
|----------|----------|----------|
| Default template | PRD.md + phases | HYPOTHESIS.md + EXPERIMENT.md |
| Task failure | Problem to fix | Data to learn from |
| Phase purpose | milestone delivery | hypothesis validation |
| TASKS.md headers | Subsystem | Experiment batch |

---

## 5. Firecrawl Integration

### Architecture
```
docker/firecrawl/          ← NEW Docker service
├── Dockerfile
├── crawler.py             ← Firecrawl-based crawler
├── scheduler.py           ← Cron scheduler
└── config.yaml            ← Targets, schedule, output paths

Weekly schedule:
  → crawl cursor docs → .platforms/cursor/YYYY-MM-DD/
  → crawl claude docs → .platforms/claude/YYYY-MM-DD/
  → crawl gemini docs → .platforms/gemini/YYYY-MM-DD/
  → diff against last crawl
  → commit changed pages
  → ingest changed pages into pgvector RAG
  → write .platforms/CHANGELOG.md

New MCP tool: platform_docs_search(query, platform)
  → semantic search over indexed platform docs
  → returns current relevant pages
```

---

## 6. Success Metrics
- Tasks can never be invisibly stuck (TTL + cleanup agent)
- No task marked [✅] without a different agent's verified_by
- Platform docs updated weekly without manual intervention
- Cost per task tracked and visible in health reports
- template_v2 fully installable via trent_install

---

**Reference**: `potential_changes.md` — 42-item roadmap with full rationale
**Baseline**: `template/` — current v1 template
