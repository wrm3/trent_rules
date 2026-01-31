# Cursor Rules and Skills Integration

## Overview

This document describes how the trent task management system is implemented in Cursor using rules and skills architecture.

## Cursor Architecture

### Rules (`.cursor/rules/`)
- **Format**: `.mdc` files (Markdown Cursor)
- **Location**: `.cursor/rules/trent/rules/`
- **Activation**: Always active or globs-based
- **Purpose**: Provide persistent instructions for task management

### Skills (`.cursor/skills/`)
- **Format**: `SKILL.md` files with reference/ folders
- **Location**: `.cursor/skills/trent-*/`
- **Activation**: Natural language triggers
- **Purpose**: Conversational task management assistance

### Commands (`.cursor/commands/`)
- **Format**: `.md` files
- **Prefix**: `@trent-*`
- **Examples**: `@trent-setup`, `@trent-task-new`
- **Purpose**: Quick access to common operations

### Agents (`.cursor/agents/`)
- **Format**: `.md` files describing agent roles
- **Location**: `.cursor/agents/`
- **Purpose**: Specialized SubAgents for complex workflows

## File Format Standards

### Task File Structure
```yaml
---
id: 001
title: 'Task Title'
status: pending
priority: high
phase: 0
subsystems: [subsystem1, subsystem2]
project_context: 'Brief description'
dependencies: []
---

# Task 001: Task Title

## Objective
[Task description]

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
```

### TASKS.md Format
```markdown
# Project Name - Task List

## Phase 0: Setup & Infrastructure
- [ ] Task 001: Task Title
- [🔄] Task 002: In Progress Task
- [✅] Task 003: Completed Task
```

## Task Management Workflow

### Creating a Task
1. User: "Create a task to implement user authentication"
2. Skill activates based on natural language
3. Creates `task001_implement_user_auth.md`
4. Updates `TASKS.md`

### Using Commands
1. User: `@trent-task-new`
2. Command guides task creation
3. Creates task file and updates TASKS.md

### Updating Task Status
1. User: "Mark task 001 as in-progress"
2. Updates task file status field
3. Updates TASKS.md emoji to `[🔄]`

## Directory Structure

```
.cursor/
├── commands/
│   ├── trent-setup.md
│   ├── trent-plan.md
│   ├── trent-task-new.md
│   └── ... (15 total trent-* commands)
├── rules/
│   └── trent/
│       └── rules/
│           ├── _index.mdc
│           ├── rules.mdc
│           ├── plans.mdc
│           ├── qa.mdc
│           └── workflow.mdc
├── skills/
│   ├── trent-task-management/
│   │   ├── SKILL.md
│   │   └── reference/
│   ├── trent-planning/
│   │   ├── SKILL.md
│   │   └── reference/
│   └── trent-qa/
│       ├── SKILL.md
│       └── reference/
└── agents/
    └── trent-task-expander.md

.trent/
├── PLAN.md
├── TASKS.md
├── PROJECT_CONTEXT.md
├── tasks/
│   └── taskXXX_description.md
└── phases/
    └── phaseN_name.md
```

## Feature Matrix

| Feature | Supported | Notes |
|---------|-----------|-------|
| Task Creation | ✅ | Via skill or command |
| Task Status Update | ✅ | Emoji indicators |
| Sub-task Creation | ✅ | task42.1, 42.2 format |
| Task Dependencies | ✅ | Array in frontmatter |
| YAML Frontmatter | ✅ | Standard format |
| Windows-safe Emojis | ✅ | 🔄 ✅ ❌ |
| Auto-folder Creation | ✅ | Silent operation |
| Phase Organization | ✅ | Phase-based task IDs |
| Bug References | ✅ | Links to BUGS.md |
| Retroactive Tasks | ✅ | Document past work |

## Best Practices

### 1. Use Commands for Quick Access
- `@trent-setup` for initialization
- `@trent-task-new` for task creation
- `@trent-status` for project overview

### 2. Skill Activation
- Mention "task", "todo", "work item" for natural activation
- Skills provide conversational guidance

### 3. Direct File Operations
- `.trent/` files are working files
- Edit directly without asking permission
- User reviews in IDE diff view

### 4. Version Control
- Keep `.trent/` in version control
- Task files are plain markdown with YAML

## Troubleshooting

### Issue: Skill not recognizing task files
**Solution:** Ensure `.cursor/skills/trent-task-management/` exists with SKILL.md

### Issue: Rules not applying
**Solution:** Ensure `.cursor/rules/trent/` exists with rules.mdc

### Issue: Task files not updating
**Solution:** Check file permissions for `.trent/`

### Issue: Commands not found
**Solution:** Verify `.cursor/commands/` contains trent-*.md files

## Summary

The trent system uses Cursor's rules, skills, commands, and agents architecture to provide comprehensive task management with YAML frontmatter and Windows-safe emoji indicators.
