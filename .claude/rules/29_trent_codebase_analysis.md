---
description: 'Command: trent-analyze-codebase — map external codebase and generate integration plan'
globs: []
alwaysApply: false
---

# Codebase Integration Analysis Command

## Command: `trent-analyze-codebase`

**Purpose**: Analyze an external codebase, map architecture, compare with this project, and generate integration plan with phase + tasks.

## Activation

- User invokes `trent-analyze-codebase`
- User asks to "analyze a codebase for integration" or "compare a project with ours"

## Execution

1. Read `.cursor/skills/codebase-integration-analysis/SKILL.md` and follow the 5-phase process
2. Codebase Exploration (parallel) → Architecture Document → Comparison Document → Integration Plan (phase + tasks) → Deliverables Verification

## Output Files

| File | Location |
|------|----------|
| Architecture Map | `docs/YYYYMMDD_HHMMSS_Cursor_{PROJECT}_ARCHITECTURE_MAP.md` |
| Comparison | `docs/YYYYMMDD_HHMMSS_Cursor_{PROJECT}_VS_TRENTWORKS_COMPARISON.md` |
| Phase File | `.trent/phases/phase{N}_{project}-integration.md` |
| Tasks | `.trent/TASKS.md` (updated) |

## Quality Gates (ALL MUST pass)

- [ ] Architecture document covers ALL directories
- [ ] Comparison document covers ALL components
- [ ] No settings/env vars missed
- [ ] Phase file and TASKS.md header synchronized
- [ ] Documents follow naming convention
