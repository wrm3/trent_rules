# Migration Guide: trent v1 → trent vNext (template_v2)

**Date**: 2026-03-06
**From**: trent v1 (`template/`)
**To**: trent vNext (`template_v2/`)

---

## What's New in vNext

| Feature | v1 | vNext |
|---|---|---|
| Autonomous cleanup agent | ❌ | ✅ `@trent-cleanup` |
| Sprint agent | ❌ | ✅ `@trent-sprint` |
| Architecture constraints file | ❌ | ✅ `ARCHITECTURE_CONSTRAINTS.md` |
| Cross-agent verification | ❌ | ✅ Mandatory (rule 32) |
| Task claim TTL | ❌ | ✅ `claim_ttl_minutes` in YAML |
| Blast radius flags | ❌ | ✅ `blast_radius`, `ai_safe` |
| Failure taxonomy | ❌ | ✅ `FAILURE_TAXONOMY` enum |
| Ralph Wiggum prevention | ❌ | ✅ Enforced (rule 31) |
| System experiments | ❌ | ✅ `SYSTEM_EXPERIMENTS.md` |
| Platform parity enforcement | ❌ | ✅ Rule 66 + cleanup audit |
| Dependency graph | ❌ | ✅ `DEPENDENCY_GRAPH.md` |
| SPRINT.md | ❌ | ✅ Weekly sprint planning file |
| Project types | ❌ | ✅ `delivery` vs `research` |
| Health score | ❌ | ✅ Via `trent_health_report` MCP tool |

---

## Backward Compatibility

The following **work unchanged** with vNext — no action required:

- `.trent/TASKS.md` — same format, new status indicators are additive
- `.trent/tasks/task*.md` — YAML fields are additive; old files are valid
- `.trent/phases/` — same structure
- `.trent/BUGS.md`, `PLAN.md`, `PROJECT_CONTEXT.md` — all preserved
- All existing `@trent-` commands — fully supported
- `trent_install` MCP tool — detects and preserves `.trent/` data

---

## Breaking Changes

### 1. `PLAN.md` → `PRD.md`

The Product Requirements Document is now named `PRD.md` instead of `PLAN.md`.

**Impact**: Low — `PLAN.md` still works but is considered legacy. Planning commands now write to `PRD.md`.

**Action**: Rename manually if desired:
```powershell
Rename-Item .trent\PLAN.md .trent\PRD.md
```

### 2. New Status Indicators

vNext adds status indicators. Old indicators still work.

| Indicator | Meaning | New in vNext? |
|---|---|---|
| `[ ]` | Pending | No |
| `[📋]` | Ready (file created) | No |
| `[🔄]` | In Progress | No |
| `[✅]` | Completed | No |
| `[❌]` | Failed | No |
| `[⏸️]` | Paused | No |
| `[📝]` | Speccing (TTL: 1hr) | **Yes** |
| `[🔍]` | Under verification | **Yes** |
| `[⏳]` | Waiting on dependency | **Yes** |
| `[🌾]` | Harvested | **Yes** |

### 3. Task YAML — New Optional Fields

vNext task files support new YAML fields. Old task files without these fields continue to work.

```yaml
# vNext additions (all optional for existing tasks)
blast_radius: low          # low | medium | high
ai_safe: true              # false = requires human review
requires_solo_agent: false # true = no parallel agents
claimed_by: null           # agent ID claiming the task
claimed_at: null           # ISO timestamp of claim
claim_ttl_minutes: 120     # lease duration
failure_count: 0           # times failed (Ralph Wiggum check)
failure_history: []        # list of failure reason codes
rules_version: "5.1.0"     # version of rules when task was created
```

---

## Upgrade Steps

### Option A: One-Command Upgrade (Recommended)

Run the `trent_install` MCP tool from your IDE:

```
@trent-install target_path="<your-project-path>" use_v2=true
```

This will:
1. Overwrite all `.cursor/`, `.claude/`, `.agent/` rules with vNext versions
2. Add any **missing** `.trent/` files (existing files preserved)
3. Create a `.trent_backup_*.zip` if you have uncommitted task data

### Option B: Manual Upgrade

1. **Back up your .trent/ data**:
   ```powershell
   Compress-Archive -Path .trent -DestinationPath .trent_backup_$(Get-Date -Format 'yyyyMMdd').zip
   ```

2. **Copy new rules** from `template_v2/` into your project's `.cursor/`, `.claude/`, `.agent/`:
   ```powershell
   # From the trent_rules repo root:
   Copy-Item -Recurse template_v2/.cursor <your-project>/.cursor -Force
   Copy-Item -Recurse template_v2/.claude <your-project>/.claude -Force
   Copy-Item -Recurse template_v2/.agent  <your-project>/.agent  -Force
   ```

3. **Add new .trent/ files** (do NOT overwrite existing):
   ```powershell
   # Only copy files that don't already exist
   Copy-Item template_v2/.trent/ARCHITECTURE_CONSTRAINTS.md <your-project>/.trent/ -ErrorAction SilentlyContinue
   Copy-Item template_v2/.trent/SPRINT.md                   <your-project>/.trent/ -ErrorAction SilentlyContinue
   Copy-Item template_v2/.trent/CLEANUP_REPORT.md           <your-project>/.trent/ -ErrorAction SilentlyContinue
   Copy-Item template_v2/.trent/SYSTEM_EXPERIMENTS.md       <your-project>/.trent/ -ErrorAction SilentlyContinue
   ```

---

## New Files to Create After Upgrade

### `ARCHITECTURE_CONSTRAINTS.md` (Required for autonomous agents)

This is the most important vNext file. It tells autonomous agents what they must never do.

Create `.trent/ARCHITECTURE_CONSTRAINTS.md`:

```markdown
# Architecture Constraints

> Non-negotiable technical constraints. Autonomous agents MUST read this before
> starting any task. Violations require human review.

## Core Constraints

| ID | Constraint | Enforcement |
|---|---|---|
| C-01 | Never modify production database directly | ai_safe: false on DB tasks |
| C-02 | All secrets via environment variables | Pre-commit hook check |
| C-03 | No direct commits to main/master | Branch protection + CI |

## Technology Constraints

- **Language**: [e.g., Python 3.11+, TypeScript 5+]
- **Package Manager**: [e.g., UV for Python, pnpm for JS]
- **Database**: [e.g., PostgreSQL 15+]

## Deployment Constraints

- **Environment**: [e.g., Docker on Linux only]
- **CI/CD**: [e.g., GitHub Actions]

## Data Constraints

- [e.g., No PII in log files]
- [e.g., All user data encrypted at rest]

## Agent-Specific Rules

- Tasks with `blast_radius: high` require solo agent execution
- Tasks touching `ai_safe: false` paths require human approval before commit
```

---

## Optional: Enable Autonomous Agents

To allow the cleanup and sprint agents to run unattended:

1. **Set project type in `PROJECT_CONTEXT.md`**:
   ```markdown
   ## Project Type
   delivery   # or: research
   ```

2. **Configure sprint schedule in `SPRINT.md`**:
   ```markdown
   ## Sprint Configuration
   duration_hours: 2
   max_parallel_agents: 3
   ```

3. **Grant agent permissions** — ensure your IDE allows background agent execution
   (Cursor: Background Agents setting; Claude Code: headless mode)

---

## Verification After Upgrade

Run the health report to confirm everything is working:

```
@trent-health-report target_path="<your-project>"
```

Expected output: `status: healthy` with updated rule count.

---

*Generated by trent vNext — 2026-03-06*
