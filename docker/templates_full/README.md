# Trent Full Templates Directory

This directory contains the COMPLETE trent development environment for the `install_trent_full` MCP tool.

## Contents

```
templates_full/
├── .cursor/                    # Cursor IDE configuration (FULL)
│   ├── rules/                  # ALL 18 rules (00-70)
│   ├── commands/               # ALL 17 trent commands
│   ├── skills/                 # ALL 36 skills
│   └── agents/                 # ALL 38 agents
├── .trent/                     # Task management templates
│   ├── PLAN.md
│   ├── TASKS.md
│   ├── PROJECT_CONTEXT.md
│   ├── BUGS.md
│   ├── SUBSYSTEMS.md
│   ├── tasks/
│   ├── phases/
│   └── templates/
├── agents.md                   # Universal AI agent instructions
├── CLAUDE.md                   # Claude Code project context
├── AGENTS_INDEX.md             # Quick reference for agents
├── SKILLS_INDEX.md             # Quick reference for skills
├── COMMANDS_INDEX.md           # Quick reference for commands
├── HOOKS_INDEX.md              # Quick reference for hooks
└── RULES_INDEX.md              # Quick reference for rules
```

## Difference from templates/

| Feature | templates/ | templates_full/ |
|---------|------------|-----------------|
| Rules | 9 (trent only) | 18 (all) |
| Skills | 3 (trent only) | 36 (all) |
| Commands | 17 | 17 |
| Agents | 0 | 38 |
| Use case | Minimal trent setup | Full dev environment |

## Usage

```python
# Full installation (all templates)
install_trent_full(target_path="/path/to/project")

# Preview without changes
install_trent_full(target_path="/path/to/project", dry_run=True)
```

## Updating Templates

When you update rules, skills, agents, or commands in the main repository:

1. Copy updated files to this templates_full directory
2. Rebuild Docker: `docker-compose up -d --build trent`
3. Commit and push changes

## Version

Templates version: 1.0.0
Last updated: 2026-02-01
