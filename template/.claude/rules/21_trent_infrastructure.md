---
description: File organization, tool integration, context management, scope control, and coding standards
globs: 
alwaysApply: true
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

---

## 🚨 trent_install: Existing Project Detection (MANDATORY)

**Before calling `trent_install`, you MUST detect whether this is a fresh or existing project.**

### Detection Criteria

Run this check FIRST:

```
□ Does .trent/TASKS.md exist AND have more than 20 lines?
□ Does .trent/tasks/ have more than 5 task files?
□ Does .trent/PROJECT_CONTEXT.md exist with non-template content?

If ANY of the above is TRUE → this is an EXISTING PROJECT install.
If ALL are FALSE → this is a FRESH install. Proceed normally.
```

### Fresh Install Protocol
Proceed with `trent_install` normally.

### Existing Project Install Protocol

**STOP. Do NOT call trent_install blindly. Instead:**

1. **Read first** — Read `.trent/TASKS.md`, `PROJECT_CONTEXT.md`, and any `ARCHITECTURE_CONSTRAINTS.md`
2. **Read instruction files** — Read existing `CLAUDE.md` and `agents.md` to pass as `existing_files` to preserve customizations
3. **Call trent_install** with `existing_files` parameter containing the content to preserve
4. **After install**: Compare old vs new `.trent/` and report what changed to the user
5. **NEVER overwrite** these user-data files:
   - `.trent/TASKS.md`
   - `.trent/tasks/` (all task files)
   - `.trent/phases/` (all phase files)
   - `.trent/BUGS.md`
   - `.trent/logs/`
   - `.trent/IDEA_BOARD.md`
   - `.trent/ARCHITECTURE_CONSTRAINTS.md`

### Backup Folder Migration Detection

**After any `trent_install`, scan the project root for previous trent data:**

```
□ Look for: .trent_YYYYMMDD/ folders (e.g., .trent_20260307/)
□ Look for: .trent_backup/, .trent_old/, .trent_prev/
```

**If backup folder found AND the new `.trent/` has blank/template files:**

```markdown
⚠️ PREVIOUS TRENT DATA DETECTED

Found: {backup_folder_name}/ in project root.
New .trent/ appears to have template/blank files.

This looks like an upgrade install that needs data migration.

Recommended action: Migrate the following from {backup_folder_name}/ to .trent/:
- TASKS.md (task history — preserve this)
- tasks/ (all task files — preserve these)
- phases/ (phase files — preserve these)
- BUGS.md (bug history — preserve this)
- logs/ (execution history — preserve this)
- ARCHITECTURE_CONSTRAINTS.md (project constraints — preserve this)
- IDEA_BOARD.md (captured ideas — preserve this)

The following will be REPLACED by new install versions:
- PROJECT_CONTEXT.md → populated from old data
- SUBSYSTEMS.md → regenerated (staleness check will run)
- PROJECT_GOALS.md → regenerated if template placeholders found
- .project_id → keep the NEW install's .project_id

Proceed with migration? (yes/no)
```

**If user confirms**: Copy the preserve list from backup to `.trent/`, keeping new `.project_id`.
**If user declines**: Leave as-is, note that old data is in `{backup_folder_name}/`.

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


---

---
description: Integration points, template maintenance, and platform architecture reference
globs: 
alwaysApply: true
---

## Integration Points

### Task System Integration
- Automatically record metrics during task lifecycle events
- Track effort estimation accuracy for continuous improvement
- Monitor task pipeline health and bottlenecks

### File System Integration
- Use FILE_REGISTRY.md to understand current system structure
- Map file organization to component architecture
- Identify component boundaries from directory structure

### Tool System Integration
- Reference MCP_TOOLS_INVENTORY.md for available tools
- Use tool combinations for comprehensive workflows
- Validate tool selection against task requirements

## Template Maintenance and Platform Architecture

### Platform Architecture Reference

When maintaining this template or adding new features, **ALWAYS** consult the `.trent/` folder for platform-specific requirements and compatibility considerations.

**Key Documentation:**
- `.trent/PLATFORM_COMPARISON.md` - Cross-platform comparison table
- `.trent/CURSOR.md` - Cursor specific architecture
- `.trent/PLATFORM_ARCHITECTURE.md` - Overview and maintenance schedule

### When to Reference Platform Architecture

**ALWAYS check `.trent/` platform documentation before:**
1. Adding new rules or commands
2. Modifying task file formats or naming conventions
3. Creating new instructions or documentation
4. Updating file organization structure
5. Making changes that affect cross-IDE compatibility

### Critical Platform Differences

**File Formats (IMPORTANT):**
- Cursor: Uses `.mdc` for rules files (Markdown Cursor) - UNIQUE to Cursor
- Other platforms: Use `.md` files
- Task files: Use `.md` with YAML frontmatter (cross-platform compatible)

**Platform-Specific Features:**
- Cursor: Now Has Skills and SubAgents (no equivalent in Cursor)
- Cursor: Uses `.mdc` rule format (other platforms can't read these)
- Commands: Cursor uses `@command`, not `/command`

**Universal Features (work everywhere):**
- `.trent/` task management system
- YAML frontmatter in task files
- Markdown documentation
- Standard file organization
- Task status indicators ([ ], [�], [�], [✅])

### Periodic Verification

**Quarterly Review (Every 3 Months):**
- [ ] Check Cursor official documentation for updates
- [ ] Check other platform documentation for new features
- [ ] Test template on multiple platforms
- [ ] Update `.trent/` platform documentation
- [ ] Update PLATFORM_COMPARISON.md if differences found
- [ ] Document any breaking changes

### Adding Features Cross-Platform

When adding features to this template, ensure compatibility:

1. **Test on multiple platforms**: Test thoroughly
2. **Document compatibility**: Update `.trent/CURSOR.md` and other platform docs
3. **Provide fallbacks**: For features that don't work on all platforms
4. **Update comparison table**: Add new features to PLATFORM_COMPARISON.md
5. **Migration guides**: Update if file structure or format changes

### Template Maintenance Workflow

When maintaining this template:

1. **Check platform docs** in `.trent/`
2. **Identify compatibility requirements** from PLATFORM_COMPARISON.md
3. **Make Cursor-specific changes** in `.cursor/rules/*.mdc` files
4. **Update platform documentation** in `.trent/CURSOR.md`
5. **Update comparison table** if new differences emerge

### File Format Rules for Cursor

**Cursor Rules (.mdc files):**
- MUST use `.mdc` extension (not `.md`)
- Located in `.cursor/rules/` directory
- Can be in subdirectories (e.g., `.cursor/rules/trent/`)
- Include YAML frontmatter with `description`, `globs`, `alwaysApply`

**Cursor Commands:**
- Located in `.cursor/rules/*/commands/` directories
- Use `@command` prefix (not `/command`)
- Can reference rules and other commands

### Resources

- **Platform Comparison**: `.trent/PLATFORM_COMPARISON.md`
- **Cursor Architecture**: `.trent/CURSOR.md`
- **Official Cursor Docs**: https://docs.cursor.com
- **Platform Architecture Overview**: `.trent/PLATFORM_ARCHITECTURE.md`

---

*This consolidated rule provides all essential trent functionality in a single, efficient rule optimized for daily coding work.*
