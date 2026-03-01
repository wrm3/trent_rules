---
description: "File organization, tool integration, context management, scope control, and coding standards"
activation: "always_on"
---

## File Organization

### Working Directory: `/.trent/` (99% of operations)
- Active task management (TASKS.md updates)
- Project planning (PRD creation, goals)
- Documentation updates
- Memory archival operations

### Template Directory: `/templates/trent/` (1% of operations)
- Updating installation templates
- Adding rules that ALL projects need
- MCP server deployment preparation

### File Categories
- **Config**: Configuration files, environment settings, build scripts
- **Source**: Application code, business logic, utilities
- **Data**: Schemas, migrations, seed data, static resources
- **Tests**: Unit tests, integration tests, test utilities
- **Docs**: Documentation, README files, architectural diagrams
- **Tools**: Build tools, scripts, development utilities

### Project Documentation Rules
- **Project Documentation**: All `.md` files documenting project aspects go in `docs/` folder in project root
- **Auto-Create**: If `docs/` folder doesn't exist, create it automatically
- **Examples**: API documentation, architecture docs, user guides, technical specifications

### Test Scripts Rules
- **Test Scripts**: All script files for testing project code go in `temp_scripts/` folder in project root
- **Auto-Create**: If `temp_scripts/` folder doesn't exist, create it automatically
- **Examples**: Test automation scripts, data validation scripts, performance testing scripts

### ⚠️ CRITICAL: File Placement Rules (MUST FOLLOW)
- **.trent/**: ONLY core planning documents (PLAN.md, TASKS.md, BUGS.md, PROJECT_CONTEXT.md, SUBSYSTEMS.md, FILE_REGISTRY.md, MCP_TOOLS_INVENTORY.md)
- **docs/**: ALL temporary, migration, or ad-hoc documentation files (including setup summaries, conversion reports, migration files, etc.)
- **temp_scripts/**: Test scripts and utility files
- **NEVER** place task migration files, conversion summaries, or temporary documentation in `.trent/`

### � NO PERMISSION REQUIRED - Direct Edit Policy

**CRITICAL FOR Cursor AI IDE:**

The following files in `.trent/` are **working files** that SHOULD BE EDITED DIRECTLY WITHOUT ASKING FOR USER PERMISSION:

**Core Planning Files (CAPITALIZED names):**
- `PLAN.md` - Product Requirements Document
- `TASKS.md` - Master task checklist
- `PROJECT_CONTEXT.md` - Project mission and goals
- `BUGS.md` - Bug tracking
- `SUBSYSTEMS.md` - Component registry
- `FILE_REGISTRY.md` - File organization documentation
- `MCP_TOOLS_INVENTORY.md` - Tool inventory

**Task Files:**
- All files in `.trent/tasks/` (e.g., `task001_description.md`)
- All files in `.trent/phases/` 

**Rules:**
- ✅ **EDIT DIRECTLY** - These are your working files, not user source code
- ✅ **NO CONFIRMATION NEEDED** - Just make the edit
- ✅ **NO "Should I update...?" PROMPTS** - Just do it
- ✅ **AUTO-CREATE** - Create missing files with templates automatically
- ✅ **SILENT OPERATIONS** - Create folders/files silently, report what was done

**Why?** These files track YOUR work as an AI assistant. They are management artifacts, not user deliverables. The user will review changes in their IDE's diff view.

### Auto-Creation Rules
- **Auto-Create Folders**: Always create missing folders (`docs/`, `temp_scripts/`, `.trent/`, etc.) without asking
- **Auto-Create Templates**: Create missing `.md` files with blank templates if they don't exist
- **Direct Editing**: Edit files directly - user will accept/reject final changes in their IDE

### Complete System Setup
When initializing or updating the system, automatically create:

#### Required Folders:
- `.trent/` - Main system directory
- `.trent/tasks/` - Task files directory
- `.trent/phases/` - Phase documentation directory
- `docs/` - Project documentation directory
- `temp_scripts/` - Test scripts directory

#### Required Template Files:
- `.trent/PLAN.md` - Product Requirements Document template
- `.trent/TASKS.md` - Master task checklist template
- `.trent/PROJECT_CONTEXT.md` - Project context template
- `.trent/SUBSYSTEMS.md` - Component registry template
- `.trent/FILE_REGISTRY.md` - File structure documentation template
- `.trent/MCP_TOOLS_INVENTORY.md` - Tool inventory template

#### File Placement Reminder:
- **Migration files, conversion summaries, setup reports**: Place in `docs/` folder, NOT in `.trent/`
- **Core planning documents only**: Keep `.trent/` clean and focused

## Tool Integration (MCP)

### Tool-First Principle
**Before implementing any solution manually, check available MCP tools first.**

### Tool Categories
- **Web/Browser**: Navigation, clicking, form filling, content extraction
- **Database**: Read queries, write operations, schema management
- **Research**: Web search, content scraping, API calls
- **Screen/Visual**: Screenshots, image analysis, visual automation
- **Code/System**: Code execution, system commands, file operations

### Tool Workflow Patterns
- **Web Testing**: Database Read → Web Interaction → Visual Tools → Database Verification
- **Database Operations**: Read Current State → Make Changes → Verify Changes
- **Research**: Search → Extract → Process → Document

## Context Management

### Project Context Display
When starting tasks, display:
```
� PROJECT CONTEXT OVERVIEW
� Mission: [Brief mission from PROJECT_CONTEXT.md]
� Current Phase: [Phase and focus area]
✅ Success Criteria: [Key objectives for current phase]
� Current Status: [Active tasks, progress, blockers]
�️ Scope Boundaries: [Key limitations and approved complexity]
```

### Context Optimization
- **75% threshold**: Archive low-priority content automatically
- **90% threshold**: Emergency cleanup, defer non-essential content
- **Priority levels**: Critical (always retained) → High → Medium → Low (aggressive cleanup)

## Scope Control

### Over-Engineering Prevention
- **Authentication**: Don't add role permissions unless requested
- **Database**: Use simple file-based unless DB explicitly requested
- **API**: Don't add comprehensive REST beyond required
- **Architecture**: Default monolith unless scale requires separation

### Scope Validation Questions
1. **User Context**: Personal use, small team, or broader deployment?
2. **Security Requirements**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration Needs**: Standalone, basic, standard, or enterprise?

## Coding Standards

### Code Reusability (see 04_code_reusability.md for full details)
- **3-Strike Rule**: Logic appearing 3+ times MUST be extracted to a shared module
- **Shared module roots**: `src/lib/` (TS/JS) or `lib/` (Python) — utilities, services, types, config
- **No inline utilities**: Functions used 2+ times belong in `lib/utils/`, not inline
- **Barrel exports**: Every shared folder needs `index.ts` / `__init__.py`
- **No magic values**: Constants and config belong in `lib/config/constants`

### Python
- Follow PEP 8 guidelines (relaxed enforcement)
- Use black formatter, 88-100 character line length
- Use type hints when possible
- Write comprehensive docstrings

### JavaScript/React
- Follow ESLint configuration, use Prettier for formatting
- Use functional components with hooks
- Use React.memo, useCallback, useMemo for performance
- Use Jest and React Testing Library for testing
