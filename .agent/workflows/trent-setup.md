---
description: "Initialize the trent task management system for this project"
---

# Workflow: trent-setup

Initialize the trent task management system for this project.

## Steps

### Step 1: Check Existing Structure

Check if `.trent/` folder already exists and read current state.

### Step 2: Create Required Directories

// turbo
Create the following directories if they don't exist:
- `.trent/`
- `.trent/tasks/`
- `.trent/phases/`
- `docs/`
- `temp_scripts/`

### Step 3: Create Core Files

Create these files if they don't exist (with blank templates):
- `.trent/PLAN.md` — Product Requirements Document
- `.trent/TASKS.md` — Master task checklist
- `.trent/PROJECT_CONTEXT.md` — Project mission and goals
- `.trent/SUBSYSTEMS.md` — Component registry
- `.trent/BUGS.md` — Bug tracking
- `.trent/FILE_REGISTRY.md` — File documentation

### Step 4: Analyze Existing Codebase

If this is an existing project:
1. Scan directory structure for major components
2. Identify tech stack from config files (package.json, requirements.txt, etc.)
3. Populate `.trent/SUBSYSTEMS.md` with discovered components
4. Create Phase 0 (Setup/Infrastructure) in TASKS.md

### Step 5: Create AGENTS.md

Check if `AGENTS.md` exists. If not, create it with:
- Project name and description
- Directory structure overview
- Development commands
- trent task management section (between markers)

### Step 6: Report

Report what was created and next steps for the user.
