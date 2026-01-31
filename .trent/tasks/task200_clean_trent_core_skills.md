---
id: 200
title: 'Clean trent Core Skills - Remove Claude Code References'
type: refactor
status: completed
priority: high
phase: 2
subsystems: [skills, trent-task-management, trent-planning, trent-qa]
project_context: Remove Claude Code IDE references from trent skills while keeping Claude AI model references
dependencies: []
completed_date: '2026-01-29'
---

# Task 200: Clean trent Core Skills

## Objective
Remove all `.claude/` folder paths and "Claude Code" IDE references from the trent core skills, while preserving references to Claude AI models and Cursor-compatible concepts (Skills, Agents, Hooks).

## Files to Update (18 files, ~100 matches)

### 1.1 trent Core Skills (3 files)
- [ ] `.cursor/skills/trent-task-management/SKILL.md` (7 matches)
- [ ] `.cursor/skills/trent-planning/SKILL.md` (1 match)
- [ ] `.cursor/skills/trent-qa/SKILL.md` (1 match)

### 1.2 trent Reference Files (7 files)
- [ ] `.cursor/skills/trent-task-management/rules.md` (3 matches)
- [ ] `.cursor/skills/trent-task-management/reference/cursor_rules_comparison.md` (16 matches)
- [ ] `.cursor/skills/trent-task-management/reference/windows_emoji_guide.md` (2 matches)
- [ ] `.cursor/skills/trent-planning/rules.md` (3 matches)
- [ ] `.cursor/skills/trent-planning/reference/cursor_rules_comparison.md` (10 matches)
- [ ] `.cursor/skills/trent-qa/rules.md` (1 match)
- [ ] `.cursor/skills/trent-qa/reference/cursor_rules_comparison.md` (7 matches)

### 1.3 Integration Skills (4 files)
- [ ] `.cursor/skills/github-integration/SKILL.md` (1 match)
- [ ] `.cursor/skills/github-integration/rules.md` (4 matches)
- [ ] `.cursor/skills/hanx-mediawiki/SKILL.md` (5 matches)
- [ ] `.cursor/skills/hanx-mediawiki/rules.md` (6 matches)

### 1.4 Other Skills (5 files)
- [ ] `.cursor/skills/project-setup/SKILL.md` (3 matches)
- [ ] `.cursor/skills/deep-research/SKILL.md` (1 match)
- [ ] `.cursor/skills/hanx-database-tools/SKILL.md` (2 matches)
- [ ] `.cursor/skills/hanx-knowledge-base/rules.md` (5 matches)
- [ ] `.cursor/skills/web-tools/reference/search_engines.md` (6 matches)

## Cleanup Rules

### REMOVE:
- `.claude/` folder paths → Replace with `.cursor/`
- "Claude Code" as IDE → Remove or replace with "Cursor"
- `/project:trent-*` commands → Remove
- Cross-platform sync references → Remove
- CLAUDE.md references → Remove

### KEEP:
- "Claude" as AI model (Claude Opus, Sonnet)
- Skills, Agents, SubAgents concepts
- Hooks concepts

## Acceptance Criteria
- [ ] All 18 files updated
- [ ] No `.claude/` paths remain in these files
- [ ] No "Claude Code" IDE references remain
- [ ] Claude AI model references preserved
- [ ] Skills still load correctly in Cursor

## Progress Log
- 2026-01-29: Task created, starting execution
- 2026-01-29: Completed - all 18 files updated

### Files Updated:
1. ✅ `.cursor/skills/trent-task-management/SKILL.md` - Updated compatibility notes, removed cross-platform sections
2. ✅ `.cursor/skills/trent-planning/SKILL.md` - Updated compatibility notes
3. ✅ `.cursor/skills/trent-qa/SKILL.md` - Updated compatibility notes
4. ✅ `.cursor/skills/trent-task-management/rules.md` - Updated header, usage notes, footer
5. ✅ `.cursor/skills/trent-task-management/reference/cursor_rules_comparison.md` - Complete rewrite for Cursor-only
6. ✅ `.cursor/skills/trent-task-management/reference/windows_emoji_guide.md` - Removed Claude Code from IDE list
7. ✅ `.cursor/skills/trent-planning/rules.md` - Updated header, usage notes, footer
8. ✅ `.cursor/skills/trent-planning/reference/cursor_rules_comparison.md` - Complete rewrite for Cursor-only
9. ✅ `.cursor/skills/trent-qa/rules.md` - Updated header, footer
10. ✅ `.cursor/skills/trent-qa/reference/cursor_rules_comparison.md` - Complete rewrite for Cursor-only
11. ✅ `.cursor/skills/github-integration/SKILL.md` - No Claude Code references found
12. ✅ `.cursor/skills/github-integration/rules.md` - No Claude Code references found
13. ✅ `.cursor/skills/hanx-mediawiki/SKILL.md` - Updated to Cursor references
14. ✅ `.cursor/skills/hanx-mediawiki/rules.md` - Updated to Cursor references
15. ✅ `.cursor/skills/project-setup/SKILL.md` - Updated structure, removed Claude Code configs
16. ✅ `.cursor/skills/deep-research/SKILL.md` - Updated researcher attribution
17. ✅ `.cursor/skills/hanx-database-tools/SKILL.md` - Updated MCP integration and compatibility
18. ✅ `.cursor/skills/hanx-knowledge-base/rules.md` - Updated Claude Code to Cursor
19. ✅ `.cursor/skills/web-tools/reference/search_engines.md` - Updated Claude Code to Cursor

---
**Created**: 2026-01-29
**Completed**: 2026-01-29
**Phase**: 2 - Claude Code Cleanup
