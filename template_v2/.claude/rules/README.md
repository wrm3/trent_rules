# .claude/rules/ - Numbered Rules Directory

Claude Code rules use `.md` (standard Markdown) files with optional YAML frontmatter.
Rules are loaded in numeric order. Use the numbering convention below.

## Numbering Convention

| Range | Category | Description |
|-------|----------|-------------|
| **00-09** | Universal | Always loaded first (always, docs, git, code quality, memory, CLIs, shell, venv) |
| **20-30** | Trent | Task management system rules |

## Current Files (23 files)

```
00_always.md                       Universal guidelines + datetime awareness
01_documentation.md                Doc file placement rules
02_git_workflow.md                 Git commit conventions
03_code_review.md                  Code review guidelines
04_code_reusability.md             DRY enforcement, shared modules
05_agent_memory.md                 Session memory capture (Gemini + VS Code)
06_cursor_cli.md                   Cursor CLI reference
07_claude_cli.md                   Claude Code CLI reference
08_powershell.md                   Windows PowerShell helpers
09_python_venv.md                  Python UV virtual environments

20_trent_tasks.md                  Task creation, status, sync, completion, phase gates
21_trent_infrastructure.md         File placement, direct edit policy, scope control
22_trent_planning.md               PRD, phase management, phase sync, pivot workflow
23_trent_qa.md                     Bug tracking, zero-tolerance error reporting
24_trent_workflow.md               Task expansion, complexity scoring, story points
25_trent_index.md                  System overview, directory structure, commands
26_trent_agents_multi.md           Parallel agent execution, worktrees
27_trent_self_improvement.md       System issue detection and reporting
28_trent_project_files.md          agents.md/CLAUDE.md management
29_trent_codebase_analysis.md      Codebase integration analysis command
30_trent_ideas_goals.md            IDEA_BOARD + PROJECT_GOALS

silicon_valley_personality.md      SV character personas (all characters)
README.md                          This file
```

## Rule File Format (.md)

```markdown
---
description: 'Brief description of the rule purpose'
globs:
  - '**/*.py'
alwaysApply: false
---

# Rule Content Here
```

> **Note**: Cursor uses `.mdc` extension. Content is identical; only the extension differs.

## Adding New Rules

1. Choose the appropriate number range
2. Use format: `{NN}_{descriptive_name}.md`
3. Keep names lowercase with underscores
4. Update this README

## Related

- **Skills:** `.claude/skills/` — lazy-loaded skill modules
- **Commands:** `.claude/commands/` — trent-* slash commands
- **Cursor mirror:** `.cursor/rules/*.mdc`
- **Antigravity mirror:** `.agent/rules/*.md`

---

*Last updated: 2026-03-03*
