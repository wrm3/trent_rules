# Trent Templates Directory

This directory contains templates for the `install_trent` MCP tool.

## Structure

```
templates/
├── .cursor/                    # Cursor IDE configuration
│   ├── rules/                  # Trent rules (10-17)
│   │   ├── 10_trent_core.mdc
│   │   ├── 11_trent_planning.mdc
│   │   ├── 12_trent_qa.mdc
│   │   ├── 13_trent_workflow.mdc
│   │   ├── 14_trent_index.mdc
│   │   ├── 15_trent_agents_multi.mdc
│   │   ├── 16_trent_self_improvement.mdc
│   │   └── 17_trent_project_files.mdc
│   ├── commands/               # Trent commands (@trent-*)
│   └── skills/                 # Trent skills
│       ├── trent-task-management/
│       ├── trent-planning/
│       ├── trent-qa/
│       └── trent-code-reviewer/
├── .trent/                     # Task management data
│   ├── PLAN.md                 # PRD template
│   ├── TASKS.md                # Task list template
│   ├── PROJECT_CONTEXT.md      # Project context template
│   ├── BUGS.md                 # Bug tracking template
│   ├── SUBSYSTEMS.md           # Subsystems registry template
│   ├── FILE_REGISTRY.md        # File registry template
│   ├── MCP_TOOLS_INVENTORY.md  # MCP tools template
│   ├── tasks/                  # Individual task files
│   ├── phases/                 # Phase documentation
│   └── templates/              # Task/phase templates
├── agents.md                   # Universal AI agent instructions
└── CLAUDE.md                   # Claude Code project context
```

## Usage

The `install_trent` tool copies these templates to target projects:

```python
# Full installation (all templates)
install_trent(target_path="/path/to/project", template_type="full")

# Cursor only
install_trent(target_path="/path/to/project", template_type="cursor")

# Trent task management only
install_trent(target_path="/path/to/project", template_type="trent")
```

## Template Types

| Type | Directories Copied |
|------|-------------------|
| `full` | .cursor, .trent, agents.md, CLAUDE.md |
| `cursor` | .cursor |
| `trent` | .trent |
| `rules` | .cursor/rules |

## Updating Templates

When updating trent rules or templates:

1. Make changes in the main repository
2. Copy updated files to this templates directory
3. Rebuild the Docker image: `docker-compose up -d --build trent`

## Version

Templates version: 1.0.0
Last updated: 2026-02-01
