# .cursor/rules/ - Numbered Rules Directory

Rules are loaded in numeric order. Use the numbering convention below.

## Numbering Convention

| Range | Category | Description |
|-------|----------|-------------|
| **00-09** | Universal | Always loaded first (always, documentation, git) |
| **10-19** | trent | Task management system core rules |
| **20-29** | Reserved | Future use |
| **30-39** | Platform | OS-specific (PowerShell, curl, Python venv) |
| **40-49** | Database/RAG | Oracle APEX, RAG knowledge base |
| **50-59** | DevOps | CI/CD, Kubernetes, Portainer |
| **60-69** | Business | Product development, resource access |
| **70-79** | Workflows | Parallel execution, orchestration |

## Current Files

```
00_always.mdc                  Universal guidelines
01_documentation.mdc           Doc file placement rules
02_git_workflow.mdc            Git commit conventions
03_code_review.mdc             Code review guidelines

10_trent_core.mdc            Task management core
11_trent_planning.mdc        PRD and planning
12_trent_qa.mdc              Bug tracking, QA
13_trent_workflow.mdc        Workflow management
14_trent_index.mdc           System overview

23_cursor_cli.mdc              Cursor CLI reference

30_powershell.mdc              Windows PowerShell helpers
31_curl.mdc                    Curl command fixes
32_python_venv.mdc             Python virtual environments

40_oracle_apex.mdc             Oracle APEX (pointer to skill)
41_rag_knowledge_base.mdc      RAG MCP tools

50_cicd.mdc                    CI/CD (pointer to skill)
51_kubernetes.mdc              Kubernetes (pointer to skill)
52_portainer.mdc               Portainer (pointer to skill)

60_product_development.mdc     Product development rules
61_resource_access.mdc         Startup resource access

70_parallel_workflows.mdc      Parallel SubAgent execution
```

## Rule File Format (.mdc)

Cursor uses `.mdc` (Markdown Cursor) files with YAML frontmatter:

```markdown
---
description: 'Brief description of the rule purpose'
globs:
  - '**/*.py'  # Optional: Apply only to specific file patterns
alwaysApply: false  # or true for always-on rules
---

# Rule Content Here
```

### Frontmatter Options

- **description**: Brief text shown in rule picker
- **globs**: File patterns to auto-activate (optional)
- **alwaysApply**: `true` = always loaded, `false` = on-demand

## Adding New Rules

1. Choose the appropriate number range
2. Use format: `{NN}_{descriptive_name}.mdc`
3. Keep names lowercase with underscores
4. Update this README

## Gaps Are OK

Leave gaps for future additions:
- 04-09: Reserved for future universal rules
- 15-19: Reserved for future trent rules
- 20-29: Reserved for future rules
- etc.

---

## Context Budget

**Total context available:** ~200K tokens per conversation
**Rule files should use:** <2% (~4K tokens max)

**Guidelines:**
- Keep files under 100 lines when possible
- Mission-critical files can be longer (up to 500 lines)
- Skills have complete details; rules are reminders/pointers

## Related

- **Skills:** `.cursor/skills/` - Lazy-loaded, complete implementations
- **Agents:** `.cursor/agents/` - SubAgent definitions
- **Commands:** `.cursor/commands/` - Slash commands

---

*Last updated: 2026-01-29*
