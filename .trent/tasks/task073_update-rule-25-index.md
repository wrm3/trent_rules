---
id: 73
title: 'Update 25_trent_index rule with session-start ARCHITECTURE_CONSTRAINTS load'
type: feature
status: pending
priority: medium
phase: 0
subsystems: [agent-rules]
ai_safe: true
blast_radius: low
requires_verification: false
requires_solo_agent: false
dependencies: [2, 70, 71, 72]
project_context: 'Rule 25 is the system index — session-start protocol must explicitly include loading ARCHITECTURE_CONSTRAINTS.md, checking SPRINT.md validity, and loading PROJECT_CONTEXT.md health score'
---

# Task 073: Update 25_trent_index rule

## Objective
Create updated `25_trent_index.md` in `template_v2/` with the enhanced session-start protocol that loads architecture constraints, sprint status, and project health on every session.

## Updated Session Start Protocol

```markdown
## 🚨 SESSION START PROTOCOL (MANDATORY)

When user mentions tasks, phases, project status, or any trent-related operation:

### Step 1: Load Context
- [ ] Read `PROJECT_CONTEXT.md` — note mission, health score, autonomous config
- [ ] Read `ARCHITECTURE_CONSTRAINTS.md` — commit ALL constraints to memory
- [ ] Read `SPRINT.md` — is it valid? (valid_until not expired)

### Step 2: Sync Validation
- [ ] Validate TASKS.md ↔ task files sync
- [ ] Validate TASKS.md phase headers ↔ phase files sync
- [ ] If issues found: FIX before proceeding

### Step 3: Health Check
Display: PROJECT CONTEXT OVERVIEW
📌 Mission: [from PROJECT_CONTEXT.md]
🎯 Phase: [current phase]
🏥 Health: [overall score]/100 ([healthy|degraded|critical])
📋 Active Sprint: [n] tasks | Valid until: [time]
⚠️ Active Constraints: [top 3 from ARCHITECTURE_CONSTRAINTS.md]
💡 Ideas: [n] active on IDEA_BOARD.md

### Step 4: Architecture Constraint Acknowledgment
State explicitly: "Architecture constraints loaded. I will not [top constraint] under any circumstance."

This step cannot be skipped. Constraint amnesia is a system failure.
```

## Updated Command Table

Add new commands to the index:
- `@trent-cleanup` — Nightly cleanup agent
- `@trent-sprint` — 2-hour sprint agent  
- `@trent-review` — Code review (adversarial mode)

## Acceptance Criteria
- [ ] Updated 25_trent_index.md in template_v2 (all 3 IDEs)
- [ ] Session start protocol includes ARCHITECTURE_CONSTRAINTS step
- [ ] Session start protocol includes SPRINT.md validity check
- [ ] Health score display in session context
- [ ] New commands in command table

## Verification Steps
- [ ] ARCHITECTURE_CONSTRAINTS step is in session start protocol
- [ ] Step 4 (acknowledgment) is explicit
- [ ] New commands listed

## When Stuck
- Start from existing 25_trent_index rule, update session start section and command table
