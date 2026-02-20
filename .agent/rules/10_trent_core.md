---
description: "trent task management system - core rules for task lifecycle, file organization, and coding standards"
activation: "always_on"
---

# trent Core Rules

## Task Management

### Task Creation (MANDATORY ORDER)

1. Add to `.trent/TASKS.md` with `[ ]` status
2. **Immediately** create task file: `.trent/tasks/taskXXX_name.md`
   - NO underscore after "task": `task052_` NOT `task_052_`
   - Subtask hyphens: `task039-1_` NOT `task039.1_`
3. Include YAML frontmatter + all required sections
4. Update TASKS.md to `[📋]` (file created, ready)
5. Start work → change to `[🔄]`

### Task File Format

```yaml
---
id: {id}
title: 'Task Title'
status: pending|in-progress|completed|failed
priority: critical|high|medium|low
phase: 0
subsystems: [affected_subsystems]
project_context: Brief connection to project goal
dependencies: [task_ids]
---
```

### Status Indicators

- `[ ]` = No file yet — **BLOCKED, DO NOT START**
- `[📋]` = File created, ready — **CAN PROCEED**
- `[🔄]` = In Progress
- `[✅]` = Completed
- `[❌]` = Failed/Cancelled
- `[⏸️]` = Paused

### CRITICAL: No Skipping Steps

```
CORRECT: [ ] → [📋] → [🔄] → [✅]
WRONG:   [ ] → [🔄]  ← VIOLATION!
WRONG:   [ ] → [✅]  ← COMPLIANCE VIOLATION!
```

### Phase-Based Numbering

| Phase | Task IDs | Purpose |
|-------|----------|---------|
| 0 | 1-99 | Setup, infrastructure |
| 1 | 100-199 | Foundation, database |
| 2 | 200-299 | Core development |
| N | N×100 to N×100+99 | Custom phases |

### Atomic Updates (BOTH OR NEITHER)

When changing task status, update BOTH files in the SAME response:
- Task file YAML: `status: completed`
- TASKS.md entry: `[🔄]` → `[✅]`

**NEVER update one without the other.**

### Task Completion Workflow

When you finish implementing a task:

1. **File Check**: Verify `.trent/tasks/task{ID}_*.md` exists (BLOCKING if missing)
2. **Validate**: Code compiles, acceptance criteria met
3. **Update**: Task file + TASKS.md atomically
4. **Offer Git Commit**: Always offer after completion
5. **Check project files**: Update AGENTS.md/CLAUDE.md if new tools/features added

### Pre-Completion Self-Check

```
□ Does .trent/tasks/task{ID}_*.md exist?
  → NO: Create it NOW or mark as [RETRO] if after-the-fact
□ Does YAML frontmatter have all required fields?
□ Does TASKS.md status match task file status?
□ Did I offer git commit?
□ Did I check if AGENTS.md needs updating?
```

## Direct Edit Policy

Edit these files DIRECTLY without asking permission:
- `.trent/PLAN.md`, `.trent/TASKS.md`, `.trent/BUGS.md`
- `.trent/PROJECT_CONTEXT.md`, `.trent/SUBSYSTEMS.md`
- All files in `.trent/tasks/` and `.trent/phases/`

## File Organization

- `.trent/` — ONLY core planning files (PLAN.md, TASKS.md, etc.)
- `docs/` — ALL documentation, migration files, ad-hoc notes
- `temp_scripts/` — Test and utility scripts
- **NEVER** place migration files or summaries in `.trent/`

Auto-create missing folders without asking: `docs/`, `temp_scripts/`, `.trent/`

## Coding Standards

### Python (PEP 8)
- Use black formatter (88-100 char line length)
- Type hints where possible
- Comprehensive docstrings
- **Use UV for virtual environments**

### JavaScript/React
- ESLint + Prettier
- Functional components with hooks
- TypeScript when available

## Scope Control

Default to minimal complexity unless explicitly requested:
- **Auth**: No role permissions unless asked
- **Database**: File-based unless DB explicitly requested
- **API**: No comprehensive REST beyond what's required
- **Architecture**: Monolith unless scale requires separation
