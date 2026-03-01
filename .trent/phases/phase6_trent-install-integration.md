---
phase: 6
name: 'trent_install Integration'
status: planning
subsystems: [trent_install, hooks, templates]
task_range: '600-699'
prerequisites: [0, 1, 2, 3, 4, 5]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 6: trent_install Integration

## Overview
Make memory system automatic. When `trent_install` runs on a new project, it should:
1. Generate a stable project_uuid and write it to .trent/PROJECT_CONTEXT.md
2. Create ~/.trent/user_config.json if it doesn't exist (with user_id, machine_id)
3. Deploy all platform hooks (Cursor, Claude Code, Gemini, VS Code)
4. Update AGENTS.md and CLAUDE.md templates with memory tool documentation

## The Two Identity Files

### ~/.trent/user_config.json (global, per machine)
```json
{
  "user_id": "usr_{8-char-hex}",
  "machine_id": "{Windows MachineGuid or generated UUID}",
  "display_name": "{$env:USERNAME}",
  "created_at": "ISO8601",
  "platforms": ["cursor", "claude_code"]
}
```

### .trent/PROJECT_CONTEXT.md addition
Add one line to the existing PROJECT_CONTEXT.md template:
```
project_id: proj_{8-char-hex}
```

## Deliverables
- [ ] trent_install.py: project_uuid generation (idempotent — skip if already exists)
- [ ] trent_install.py: user_config.json creation (idempotent — skip if already exists)
- [ ] trent_install.py: hook deployment for each known platform
- [ ] AGENTS.md template: memory tools documented
- [ ] CLAUDE.md template: memory tools + session-start usage documented
- [ ] 00_always.mdc (or session-start rule): memory_context call pattern

## Acceptance Criteria
- [ ] Fresh trent_install on empty project generates project_uuid
- [ ] Second trent_install on same project preserves existing project_uuid (idempotent)
- [ ] ~/.trent/user_config.json created with stable machine_id
- [ ] All hooks deployed to correct locations per platform
- [ ] AGENTS.md in new project shows memory tool documentation
