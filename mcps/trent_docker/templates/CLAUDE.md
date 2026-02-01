# CLAUDE.md - Project Template

## Project Overview
{Brief description of what this project does}

## Tech Stack
- {Language/Framework}
- {Database}
- {Other technologies}

## Key Directories
```
src/           # Source code
tests/         # Test files
docs/          # Documentation
.trent/        # Task management (trent system)
```

## Development Commands
```bash
# Install dependencies
{install_command}

# Run development server
{dev_command}

# Run tests
{test_command}

# Build for production
{build_command}
```

## Coding Conventions
- {Style guide reference}
- {Linting rules}
- {Formatting requirements}

## Testing
- {Test framework}
- {How to run tests}
- {Coverage requirements}

## Important Notes
- {Project-specific gotchas}
- {Common pitfalls}
- {Security considerations}

---

<!-- TRENT SYSTEM CONTEXT - DO NOT EDIT MANUALLY -->
## Task Management (Trent)

This project uses trent for task management. Key points:

- **Task data**: `.trent/` folder contains all task files
- **Master list**: `.trent/TASKS.md` is the source of truth
- **Status flow**: [ ] → [📋] → [🔄] → [✅]
- **Phase IDs**: Phase N uses task IDs N×100 to N×100+99
- **Direct edits**: Edit `.trent/` files without asking permission
- **Sync required**: Always update both TASKS.md and task files together

When working on tasks:
1. Check `.trent/TASKS.md` for current status
2. Read task file in `.trent/tasks/` for details
3. Update both files atomically when changing status
<!-- END TRENT SYSTEM CONTEXT -->

---

<!-- Additional context below is safe for manual editing -->
