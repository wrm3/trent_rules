# .claude/rules/ - Numbered Rules Directory

Claude Code rules use `.md` (standard Markdown) files with YAML frontmatter.
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
| **80-89** | 3D Pipeline | Blender, 3D assets, Silicon Valley project |

## Current Files

```
00_always.md                   Universal guidelines
01_documentation.md            Doc file placement rules
02_git_workflow.md             Git commit conventions
03_code_review.md              Code review guidelines
04_current_datetime_awareness.md  Date/time awareness

10_trent_core.md               Task management core
11_trent_planning.md           PRD and planning
12_trent_qa.md                 Bug tracking, QA
13_trent_workflow.md           Workflow management
14_trent_index.md              System overview
15_trent_agents_multi.md       Parallel agent execution
16_trent_self_improvement.md   Self-improvement protocol
17_trent_project_files.md      Project file management
18_trent_codebase_analysis.md  Codebase analysis

23_cursor_cli.md               Cursor CLI reference

30_powershell.md               Windows PowerShell helpers
31_curl.md                     Curl command fixes
32_python_venv.md              Python virtual environments

41_rag_knowledge_base.md       RAG MCP tools

50_cicd.md                     CI/CD (pointer to skill)
51_kubernetes.md               Kubernetes (pointer to skill)
52_portainer.md                Portainer (pointer to skill)

60_product_development.md      Product development rules
61_resource_access.md          Startup resource access

80_3d_pipeline.md              3D character pipeline
81_blender_safety.md           Blender safety rules

silicon_valley_personality.md  SV character personas
```

## Rule File Format (.md)

Claude Code uses `.md` (standard Markdown) files with YAML frontmatter:

```markdown
---
description: 'Brief description of the rule purpose'
globs:
  - '**/*.py'  # Optional: Apply only to specific file patterns
alwaysApply: false  # or true for always-on rules
---

# Rule Content Here
```

> **Note**: Cursor uses `.mdc` (Markdown Cursor) extension. The `.cursor/rules/` directory
> has `.mdc` files. Content is identical; only the extension differs between platforms.

### Frontmatter Options

- **description**: Brief text shown in rule picker
- **globs**: File patterns to auto-activate (optional)
- **alwaysApply**: `true` = always loaded, `false` = on-demand

## Adding New Rules

1. Choose the appropriate number range
2. Use format: `{NN}_{descriptive_name}.md`
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

- **Skills:** `.claude/skills/` - Lazy-loaded, complete implementations
- **Agents:** `.claude/agents/` - SubAgent definitions
- **Commands:** `.claude/commands/` - Slash commands

---

*Last updated: 2026-02-19*
