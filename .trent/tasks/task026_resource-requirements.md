---
id: 26
title: 'Add resource_requirements to task YAML (storage_gb, compute_hours, vram_gb)'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [resilience]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [3, 7]
project_context: 'Research projects hit resource gates constantly (GPU, storage, API credits) — resource_requirements lets agents and cleanup agent detect and properly status tasks as [⏳] instead of leaving them stuck at [📋]'
---

# Task 026: Add resource_requirements to task YAML

## Objective
Add a `resource_requirements` section to the task YAML schema in `template_v2/`, allowing task authors to declare what external resources are needed and allowing agents to auto-detect resource-gating situations and apply the `[⏳]` status.

## Context
VisionLang tasks were repeatedly blocked by: missing GPU compute, insufficient storage for training data, data quality issues, and API rate limits. These tasks sat at `[📋]` looking like normal "ready to start" tasks — but they were actually resource-gated. The cleanup agent had no way to distinguish them. `resource_requirements` solves this.

## YAML Fields to Add

```yaml
resource_requirements:
  # ALL OPTIONAL — only specify what's needed
  vram_gb: 0           # GPU VRAM required (0 = no GPU needed)
  storage_gb: 0        # Disk space required
  compute_hours: 0     # Estimated GPU/CPU hours
  api_credits: ''      # API service + estimated cost (e.g., "OpenAI: ~$5", "Meshy: ~50 credits")
  external_services:   # Services that must be available
    - ''               # e.g., "PostgreSQL", "Redis", "Meshy API", "HuggingFace"
  data_requirements:   # Datasets or data files needed
    - path: ''         # Where the data should be
      size_gb: 0       # Size of required data
      source: ''       # Where to get it
      status: missing | present | partial  # Current availability
  estimated_available: ''  # YYYY-MM-DD — when resources expected to be available
  notes: ''            # Freeform notes about resource situation
```

## Resource Gate Detection (for agents)

When an agent claims a task and checks prerequisites:
1. Read `resource_requirements`
2. If any required resource is missing/unavailable:
   - Update task YAML: `status: resource_gated`
   - Update TASKS.md: change `[📋]` to `[⏳]`
   - Fill in `resource_requirements.estimated_available` if known
   - Git commit: `"gate(task-{id}): resource-gated — {reason}"`
   - DO NOT attempt to work on the task

## Cleanup Agent Behavior

During nightly cleanup scan:
1. For each `[⏳]` task, check if `estimated_available` date has passed
2. If date passed: attempt to verify resource now available
   - If available: move back to `[📋]`, update status to `pending`
   - If still unavailable: extend `estimated_available` + add AI-IDEA to IDEA_BOARD
3. Report all resource-gated tasks in CLEANUP_REPORT.md

## Acceptance Criteria
- [ ] `resource_requirements:` YAML block added to task003 (YAML schema)
- [ ] Resource gate detection protocol documented in task file template
- [ ] Cleanup agent resource-gate checking behavior added to task040 (cleanup spec)
- [ ] `[⏳]` status transitions defined (📋 → ⏳ when gated, ⏳ → 📋 when available)
- [ ] Example task with resource requirements shown in schema documentation

## Verification Steps
- [ ] task003 schema has `resource_requirements` block with all fields
- [ ] Resource gate detection protocol is in the task file template
- [ ] task040 cleanup spec references resource_gated task handling

## When Stuck
- Pure schema + documentation task
- Cross-reference task007 (⏳ status) — this task provides the YAML fields that drive that status
