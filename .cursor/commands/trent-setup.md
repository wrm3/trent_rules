Initialize the trent system: $ARGUMENTS

## What This Command Does

Initializes or reinitializes the trent task management system in the current project.

## Setup Workflow

### 1. Create Directory Structure
I'll create these folders if they don't exist:
- `.trent/` - Main working directory
- `.trent/tasks/` - Individual task files
- `.trent/phases/` - Phase documentation
- `docs/` - Project documentation
- `temp_scripts/` - Test scripts

### 2. Create Core Files
I'll create these template files:
- `.trent/PLAN.md` - Product Requirements Document
- `.trent/TASKS.md` - Master task checklist
- `.trent/BUGS.md` - Bug tracking
- `.trent/PROJECT_CONTEXT.md` - Project mission and goals
- `.trent/SUBSYSTEMS.md` - Component registry
- `.trent/FILE_REGISTRY.md` - File documentation
- `.trent/MCP_TOOLS_INVENTORY.md` - Available MCP tools
- `.trent/IDEA_BOARD.md` - Ideas parking lot (not yet ready for tasks)
- `.trent/PROJECT_GOALS.md` - Strategic goals that steer AI decisions

### 3. Verify MCP Tools
I'll check available MCP tools and document them in MCP_TOOLS_INVENTORY.md

### 4. Scan Existing Codebase (if applicable)
For existing projects, I'll:
- Analyze current file structure
- Identify existing components/subsystems
- Document in SUBSYSTEMS.md and FILE_REGISTRY.md

## Phase-Based Task Organization
- **Phase 0** (Task IDs: 1-99): Setup & Infrastructure
- **Phase 1** (Task IDs: 100-199): Foundation
- **Phase 2** (Task IDs: 200-299): Core Development
- **Phase N** (Task IDs: N×100 to N×100+99): Additional phases

## Task Status Indicators
- `[ ]` - Pending (no file created yet)
- `[📋]` - Ready (task file created)
- `[🔄]` - In Progress
- `[✅]` - Completed
- `[❌]` - Failed/Cancelled

## When to Use
- Starting a new project
- Adding trent to an existing project
- Reinitializing after major changes

Let me set up the trent system for you!
