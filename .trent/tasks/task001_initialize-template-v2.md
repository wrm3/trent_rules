---
id: 1
title: 'Initialize template_v2 Folder Structure'
type: feature
status: pending
priority: critical
phase: 0
subsystem: template-core
ai_safe: true
requires_solo_agent: false
blast_radius: low
blast_radius_reason: "Creates new folder only — no existing files modified"
requires_verification: true
verified_by: null
spec_version: 1
spec_last_verified: "2026-03-05"
allow_spec_update: false
estimated_duration_minutes: 45
claim_ttl_minutes: 90
dependencies: []
---

# Task 001: Initialize template_v2 Folder Structure

## Objective
Create the complete directory structure for `template_v2/` by copying the current
`template/` baseline and adding all new directories and placeholder files needed
for the vNext system. This is the foundation task — all other Phase 0 tasks build on it.

## Context
- `template/` is the current v1 baseline — READ ONLY reference
- `template_v2/` is the build target — starts empty
- Do NOT modify `.agent/`, `.cursor/`, `.claude/` in the project root
- The docker server is live — do not touch `docker/`
- Full spec in `potential_changes.md` and `.trent/PRD.md`

## Acceptance Criteria
- [ ] `template_v2/` mirrors `template/` structure as baseline
- [ ] New directories added: `template_v2/.trent/logs/`
- [ ] New placeholder files created (with TODO comments):
  - `template_v2/.trent/ARCHITECTURE_CONSTRAINTS.md`
  - `template_v2/.trent/SPRINT.md`
  - `template_v2/.trent/SYSTEM_EXPERIMENTS.md`
  - `template_v2/.trent/PRD.md` (copied from PLAN.md, renamed)
- [ ] `template_v2/.trent/PLAN.md` → `template_v2/.trent/PRD.md` (rename only, content next task)
- [ ] All existing template files copied faithfully (no content changes yet)
- [ ] `template_v2/.gitkeep` files in empty directories (docs, research, temp_scripts)
- [ ] `template_v2/.trent/.project_id` placeholder created
- [ ] Git commit: `chore(template-v2): initialize folder structure from template v1 baseline`

## Implementation Notes

### Step 1: Copy baseline
```powershell
# Copy entire template/ to template_v2/
Copy-Item -Recurse -Force G:\trent_rules\template\* G:\trent_rules\template_v2\
```

### Step 2: Add new directories
```powershell
New-Item -ItemType Directory -Force G:\trent_rules\template_v2\.trent\logs
New-Item -ItemType Directory -Force G:\trent_rules\template_v2\.trent\phases
```

### Step 3: Rename PLAN.md → PRD.md
```powershell
Rename-Item G:\trent_rules\template_v2\.trent\PLAN.md PRD.md
```

### Step 4: Create new placeholder files
Create stub files for ARCHITECTURE_CONSTRAINTS.md, SPRINT.md, SYSTEM_EXPERIMENTS.md
with a clear `# TODO: Implement in Task 002/003/005` header.

### Step 5: Verify structure
```powershell
Get-ChildItem G:\trent_rules\template_v2 -Recurse | Select-Object FullName
```

## Verification
- [ ] `Get-ChildItem template_v2 -Recurse` shows complete structure
- [ ] No files in `template/` were modified (git diff shows no changes to template/)
- [ ] No files in `.cursor/`, `.claude/`, `.agent/` were modified
- [ ] `template_v2/.trent/PRD.md` exists (renamed from PLAN.md)
- [ ] `template_v2/.trent/ARCHITECTURE_CONSTRAINTS.md` exists (stub)
- [ ] `template_v2/.trent/SPRINT.md` exists (stub)
- [ ] `template_v2/.trent/SYSTEM_EXPERIMENTS.md` exists (stub)
- [ ] `template_v2/.trent/logs/` directory exists

## When Stuck
### If Copy-Item fails:
Use manual file-by-file copy. Check for locked files.
### If directory already has partial content:
Check what's there first with `Get-ChildItem template_v2 -Recurse`. Don't overwrite.
### Escalation trigger:
If template/ contains unexpected new files not accounted for in this spec, stop and
update spec before proceeding.
