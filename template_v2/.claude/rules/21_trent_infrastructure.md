---
description: "File organization, direct edit policy, scope control"
globs:
alwaysApply: true
---

# File Organization & Scope Control

## File Placement Rules (MUST FOLLOW)

| Location | What Goes Here |
|----------|---------------|
| `.trent/` | ONLY core planning documents (PRD.md, TASKS.md, BUGS.md, PROJECT_CONTEXT.md, SUBSYSTEMS.md) |
| `.trent/tasks/` | Individual task files |
| `.trent/phases/` | Phase documentation |
| `docs/` | ALL temporary, migration, ad-hoc documentation |
| `temp_scripts/` | Test scripts and utility files |

**NEVER place migration files, conversion summaries, or temporary documentation in `.trent/`.**

Auto-create `docs/`, `temp_scripts/`, `.trent/`, `.trent/tasks/`, `.trent/phases/` if missing — no permission needed.

---

## Direct Edit Policy (NO PERMISSION REQUIRED)

**Edit these files DIRECTLY without asking. NEVER prompt "Should I update...?"**

- `.trent/PRD.md`, `TASKS.md`, `PROJECT_CONTEXT.md`, `BUGS.md`, `SUBSYSTEMS.md`
- All files in `.trent/tasks/` and `.trent/phases/`
- `.trent/IDEA_BOARD.md`, `PROJECT_GOALS.md`

These are AI working files, not user source code. Edit silently, report what was done.

---

## Scope Control

### Over-Engineering Prevention
- **Authentication**: Don't add role permissions unless requested
- **Database**: Use simple file-based unless DB explicitly requested
- **API**: Don't add comprehensive REST beyond required
- **Architecture**: Default monolith unless scale requires separation

### Scope Validation Questions (ask before creating PRD)
1. **User Context**: Personal use, small team, or broader deployment?
2. **Security**: Minimal, standard, enhanced, or enterprise?
3. **Scalability**: Basic, moderate, high, or enterprise?
4. **Feature Complexity**: Minimal, standard, feature-rich, or enterprise?
5. **Integration Needs**: Standalone, basic, standard, or enterprise?

---

## Coding Standards (Pointers)

- **Reusability**: See `04_code_reusability.md` — 3-strike rule, shared module conventions
- **Python**: PEP 8, black formatter, type hints, UV for venv
- **JS/React**: ESLint + Prettier, functional components, hooks
- **MCP tools**: Always check available MCP tools before implementing manually

---

## Platform Compatibility

- **Cursor**: `.mdc` rules, `@command` prefix, skills and agents
- **Claude Code**: `.md` rules, `/command` prefix, CLAUDE.md for context
- **Task files**: `.md` with YAML frontmatter (universal across all platforms)
- **Cross-platform changes**: Check `.trent/PLATFORM_COMPARISON.md` before modifying formats
