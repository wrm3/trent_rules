# Claude Code Reference Cleanup Plan

**Date**: 2026-01-29 19:00:00
**Purpose**: Systematically remove Claude Code IDE references while preserving Claude AI model references and Cursor-compatible concepts (Skills, Agents, Hooks)

---

## Summary

| Category | Files | Matches | Priority |
|----------|-------|---------|----------|
| Markdown (.md) | 79 | 374 | High |
| Python (.py) | 14 | 82 | Medium |
| MDC Rules (.mdc) | 0 | 0 | Done |

**Total**: 93 files, 456 matches to review

---

## Cleanup Rules

### REMOVE These Patterns:
- `.claude/` folder paths → Replace with `.cursor/` where applicable
- "Claude Code" as IDE name → Remove or replace with "Cursor"
- `/project:trent-*` commands → Remove (Cursor uses `@trent-*`)
- Cross-platform sync references → Remove (Cursor-only now)
- CLAUDE.md file references → Remove
- `.claude/settings.json` references → Remove (unless discussing hook compatibility)

### KEEP These Patterns:
- "Claude" as AI model (Claude Opus, Claude Sonnet, etc.)
- "Claude" in Anthropic API context
- Skills, Agents, SubAgents concepts (Cursor now supports these)
- Hooks concepts (Cursor supports with Claude Code hook compatibility)
- "claude" in package names (e.g., `anthropic-ai/claude-code`)

### CONTEXT-DEPENDENT:
- Claude Code hooks → Keep if discussing Cursor's third-party hook compatibility
- Agent SDK references to Claude → Review individually

---

## Phase 1: High-Priority Skills (18 files, ~100 matches)

### 1.1 trent Core Skills (Critical - 3 files)
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/trent-task-management/SKILL.md` | 7 | Update |
| `.cursor/skills/trent-planning/SKILL.md` | 1 | Update |
| `.cursor/skills/trent-qa/SKILL.md` | 1 | Update |

### 1.2 trent Reference Files (6 files)
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/trent-task-management/rules.md` | 3 | Update |
| `.cursor/skills/trent-task-management/reference/cursor_rules_comparison.md` | 16 | Update |
| `.cursor/skills/trent-task-management/reference/windows_emoji_guide.md` | 2 | Update |
| `.cursor/skills/trent-planning/rules.md` | 3 | Update |
| `.cursor/skills/trent-planning/reference/cursor_rules_comparison.md` | 10 | Update |
| `.cursor/skills/trent-qa/rules.md` | 1 | Update |
| `.cursor/skills/trent-qa/reference/cursor_rules_comparison.md` | 7 | Update |

### 1.3 Integration Skills (4 files)
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/github-integration/SKILL.md` | 1 | Update |
| `.cursor/skills/github-integration/rules.md` | 4 | Update |
| `.cursor/skills/hanx-mediawiki/SKILL.md` | 5 | Update |
| `.cursor/skills/hanx-mediawiki/rules.md` | 6 | Update |

### 1.4 Other Skills (5 files)
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/project-setup/SKILL.md` | 3 | Update |
| `.cursor/skills/deep-research/SKILL.md` | 1 | Update |
| `.cursor/skills/hanx-database-tools/SKILL.md` | 2 | Update |
| `.cursor/skills/hanx-knowledge-base/rules.md` | 5 | Update |
| `.cursor/skills/web-tools/reference/search_engines.md` | 6 | Update |

---

## Phase 2: Agent SDK (8 files, ~50 matches)

### 2.1 Core SDK Files
| File | Matches | Action |
|------|---------|--------|
| `.cursor/agents/sdk/README.md` | 4 | Update |
| `.cursor/agents/sdk/IMPLEMENTATION_REPORT.md` | 4 | Update |
| `.cursor/agents/sdk/base_agent.py` | 7 | Review (may be functional) |
| `.cursor/agents/sdk/fallback.py` | 1 | Review |

### 2.2 SDK Primitives
| File | Matches | Action |
|------|---------|--------|
| `.cursor/agents/sdk/primitives/README.md` | 7 | Update |
| `.cursor/agents/sdk/primitives/IMPLEMENTATION_REPORT.md` | 10 | Update |
| `.cursor/agents/sdk/primitives/commands.py` | 5 | Review (functional code) |
| `.cursor/agents/sdk/primitives/plugins.py` | 10 | Review (functional code) |

### 2.3 SDK Context
| File | Matches | Action |
|------|---------|--------|
| `.cursor/agents/sdk/context/README.md` | 1 | Update |

---

## Phase 3: Template & Example Files (12 files, ~80 matches)

### 3.1 trent Examples
| File | Matches | Action |
|------|---------|--------|
| `.trent/examples/PLAN.md` | 23 | Update |
| `.trent/examples/PROJECT_CONTEXT.md` | 11 | Update |
| `.trent/reference/cursor_rules_comparison.md` | 20 | Update |
| `.trent/reference/yaml_schema.md` | 2 | Update |
| `.trent/reference/windows_emoji_guide.md` | 2 | Update |

### 3.2 trent_template (Mirror of above)
| File | Matches | Action |
|------|---------|--------|
| `.trent_template/examples/PLAN.md` | 23 | Update |
| `.trent_template/examples/PROJECT_CONTEXT.md` | 11 | Update |
| `.trent_template/reference/cursor_rules_comparison.md` | 20 | Update |
| `.trent_template/reference/yaml_schema.md` | 2 | Update |
| `.trent_template/reference/windows_emoji_guide.md` | 2 | Update |

### 3.3 Template Core
| File | Matches | Action |
|------|---------|--------|
| `template/.trent/PLAN.md` | 1 | Update |
| `.trent/templates/PLAN.md` | 1 | Update |
| `.trent_template/templates/PLAN.md` | 1 | Update |

---

## Phase 4: YouTube/Video Analysis (15 files, ~100 matches)

### 4.1 Video Analysis Skills
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/youtube-video-analysis/skill.md` | 1 | Update |
| `.cursor/skills/youtube-video-analysis/REFACTOR_NOTES.md` | 15 | Update |
| `.cursor/skills/youtube-video-analysis/ENHANCEMENTS.md` | 5 | Update |
| `.cursor/skills/youtube-video-analysis/reference/multimodal_integration.md` | 5 | Update |
| `.cursor/skills/youtube-video-analysis/output/README.md` | 3 | Update |
| `.cursor/skills/youtube-rag-storage/IMPLEMENTATION_SUMMARY.md` | 1 | Update |

### 4.2 Video Analysis Scripts (Python)
| File | Matches | Action |
|------|---------|--------|
| `.cursor/skills/youtube-video-analysis/scripts/analyze_video.py` | 29 | Review carefully |
| `.cursor/skills/youtube-video-analysis/scripts/vision_analyzer.py` | 14 | Review carefully |
| `.cursor/skills/youtube-video-analysis/scripts/multimodal_integration.py` | 4 | Review carefully |
| `.cursor/skills/youtube-video-analysis/mcp/tools/analyze_video.py` | 2 | Review carefully |

### 4.3 YouTube Analyzer Tool
| File | Matches | Action |
|------|---------|--------|
| `tools/youtube_analyzer/README.md` | 1 | Update |
| `tools/youtube_analyzer/docs/ANALYSIS_COMPREHENSIVE.md` | 11 | Update |
| `tools/youtube_analyzer/docs/ANALYSIS_ACTIONABLE.md` | 15 | Update |
| `tools/youtube_analyzer/docs/MULTIMODAL_ENHANCEMENT_PLAN.md` | 10 | Update |
| `tools/youtube_analyzer/docs/IMPLEMENTATION_ROADMAP.md` | 8 | Update |

---

## Phase 5: Miscellaneous (10 files, ~30 matches)

### 5.1 Project Documentation
| File | Matches | Action |
|------|---------|--------|
| `CONTRIBUTING.md` | 2 | Update |
| `docs/20260127_173500_Cursor_trent_CODE_REVIEW.md` | 3 | Update |
| `docs/20260127_180000_Cursor_FIXES_APPLIED.md` | 1 | Update |
| `docs/youtube_analysis/README.md` | 1 | Update |

### 5.2 MCP Docker
| File | Matches | Action |
|------|---------|--------|
| `mcps/trent_docker/README.md` | 2 | Update |
| `mcps/trent_docker/trent/tools/plugins/template_install.py` | 1 | Review |

### 5.3 Agents
| File | Matches | Action |
|------|---------|--------|
| `.cursor/agents/youtube-researcher.md` | 4 | Update |
| `.cursor/agents/cursor-cli.md` | 1 | Update |

### 5.4 Hooks
| File | Matches | Action |
|------|---------|--------|
| `.cursor/hooks/README.md` | 1 | Update (keep hook compatibility info) |

### 5.5 Task Files
| File | Matches | Action |
|------|---------|--------|
| `.trent/tasks/task006_template_installer_plugin.md` | 2 | Update |

---

## Execution Strategy

### Batch 1: trent Core (Execute First)
Files: 9 files in `.cursor/skills/trent-*/`
Approach: These are the most visible and important - update carefully

### Batch 2: Reference/Comparison Files
Files: 6 files named `cursor_rules_comparison.md`
Approach: These specifically discuss Cursor vs Claude Code - major rewrite needed

### Batch 3: Example Files
Files: 6 files in `examples/` folders
Approach: Update to be Cursor-only examples

### Batch 4: Integration Skills
Files: 10+ files in other skills
Approach: Simple find/replace for most

### Batch 5: Agent SDK
Files: 10+ files in `.cursor/agents/sdk/`
Approach: Careful review - some may be functional code

### Batch 6: Python Scripts
Files: 14 Python files
Approach: Most careful review - these are functional code

### Batch 7: YouTube/Video Tools
Files: 15+ files
Approach: Batch update documentation, careful with scripts

### Batch 8: Miscellaneous
Files: Remaining files
Approach: Individual updates

---

## Verification Steps

After each batch:
1. Run `grep -r "\.claude/" .cursor/` to verify removal
2. Run `grep -r "Claude Code" .cursor/` to verify removal
3. Check that "Claude" (AI model) references are preserved
4. Test that skills/agents still load in Cursor

---

## Files to SKIP (Already Clean or Special)

- `docs/20260128_121237_Claude_SWOT_DETAILED_ANALYSIS.md` - User requested skip
- `.cursor/logs/*` - Auto-generated logs
- `agent-transcripts/*` - Conversation history
- Any `.log` files

---

## Estimated Effort

| Phase | Files | Est. Time | Complexity |
|-------|-------|-----------|------------|
| Phase 1 | 18 | 30 min | Medium |
| Phase 2 | 8 | 20 min | High (code review) |
| Phase 3 | 12 | 20 min | Low |
| Phase 4 | 15 | 40 min | High (Python scripts) |
| Phase 5 | 10 | 15 min | Low |
| **Total** | **63** | **~2 hours** | |

---

## Ready to Execute?

Confirm to proceed with Phase 1 (trent Core Skills).

---

**Plan Created**: 2026-01-29 19:00:00 UTC
**Status**: AWAITING APPROVAL
