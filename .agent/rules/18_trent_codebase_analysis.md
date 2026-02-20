---
description: "Command: trent-analyze-codebase - Analyze external codebase, map components, compare with TrentWorks, and generate integration plan"
activation: "always_on"
---

# Codebase Integration Analysis Command

## Command: `trent-analyze-codebase`

**Purpose:** Analyze an external codebase, map its architecture, compare it with TrentWorks, and generate a complete integration plan with a new phase and fully-specced tasks.

## Activation

This rule activates when:
- User invokes `trent-analyze-codebase` or `/trent-analyze-codebase`
- User asks to "analyze a codebase for integration"
- User asks to "compare a project with ours"
- User asks to "create an integration plan from a project"

## Execution

### Step 1: Read the Skill
Read the skill file at `.cursor/skills/codebase-integration-analysis/SKILL.md` and follow the 5-phase process exactly.

### Step 2: Follow the 5-Phase Process
1. Codebase Exploration (parallel)
2. Architecture Document
3. Comparison Document
4. Integration Plan (phase + tasks)
5. Deliverables Verification

### Step 3: Report Summary
- Components mapped
- Integration gaps found
- Tasks created
- Phase created
- Document links

## Output Files

| File | Location | Purpose |
|------|----------|---------|
| Architecture Map | `docs/YYYYMMDD_HHMMSS_Cursor_{PROJECT}_ARCHITECTURE_MAP.md` | Complete component mapping |
| Comparison | `docs/YYYYMMDD_HHMMSS_Cursor_{PROJECT}_VS_TRENTWORKS_COMPARISON.md` | Side-by-side comparison |
| Phase File | `.trent/phases/phase{N}_{project}-integration.md` | Phase definition |
| Tasks | `.trent/TASKS.md` (updated) | Integration tasks |

## Quality Gates

- [ ] Architecture document covers ALL directories
- [ ] Comparison document covers ALL components
- [ ] No settings/env vars missed
- [ ] Phase file and TASKS.md header synchronized
- [ ] Documents follow naming convention
