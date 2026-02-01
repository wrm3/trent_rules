# Trent Templates Directory

This directory contains templates for the `install_trent` MCP tool.

## Contents

```
templates/
├── .cursor/                    # Cursor IDE configuration
│   ├── rules/                  # Trent rules (10-17)
│   ├── commands/               # Trent commands (@trent-*)
│   └── skills/                 # Trent skills
├── .trent/                     # Task management data
│   ├── PLAN.md                 # PRD template
│   ├── TASKS.md                # Task list template
│   ├── PROJECT_CONTEXT.md      # Project context template
│   ├── BUGS.md                 # Bug tracking template
│   ├── SUBSYSTEMS.md           # Subsystems registry template
│   ├── tasks/                  # Individual task files
│   ├── phases/                 # Phase documentation
│   └── templates/              # Task/phase templates
├── agents.md                   # Universal AI agent instructions
└── CLAUDE.md                   # Claude Code project context
```

## Usage

```python
# Full installation (all templates)
install_trent(target_path="/path/to/project", template_type="full")

# Cursor IDE only
install_trent(target_path="/path/to/project", template_type="cursor")

# Task management only
install_trent(target_path="/path/to/project", template_type="trent")

# Preview without changes
install_trent(target_path="/path/to/project", dry_run=True)
```

## Template Types

| Type | What's Installed |
|------|------------------|
| `full` | .cursor, .trent, agents.md, CLAUDE.md |
| `cursor` | .cursor only |
| `trent` | .trent only |
| `rules` | .cursor/rules only |
| `skills` | .cursor/skills only |
| `commands` | .cursor/commands only |
| `minimal` | .trent + agents.md |

## Updating Templates

1. Make changes in the main trent_rules repository
2. Copy updated files to this templates directory
3. Rebuild Docker: `docker-compose up -d --build trent`

## Version

Templates version: 1.0.0
Last updated: 2026-02-01
