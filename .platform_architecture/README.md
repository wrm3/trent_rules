# AI Platform Architecture Documentation

**Purpose**: Source of truth for AI coding platform setup, features, and cross-platform compatibility.

## Overview

This folder documents the architecture, features, and setup requirements for major AI coding platforms, enabling developers to:
- **Understand platform differences** - File formats, directory structures, unique features
- **Switch platforms mid-project** - Migration guides and compatibility notes
- **Set up new projects** - Platform-specific configuration templates
- **Stay current** - Track new features as platforms evolve

### The Simple Truth About Platform Architectures

**Two primary architectures for this project:**

1. **Cursor IDE** - `.cursor/` with `.mdc` rules, `@` command prefix
2. **Claude Code** - `.claude/` with `.md` rules, `/` command prefix

Both share agents, skills, commands, and hooks. Content is identical; only file extensions and invocation syntax differ.

**Key Insight**: Cursor now supports agents, skills, and commands just like Claude Code. The only real differences are `.mdc` vs `.md` extensions and `@` vs `/` command prefix.

### Platforms Documented
- **Claude Code** (Anthropic's VSCode extension/CLI) - Unique architecture with Skills/SubAgents
- **Google Antigravity** (Google's AI-first IDE) - Unique `.agent/` folder, Artifacts, Knowledge Items, Workflows
- **Gemini CLI** (Google's multi-system) - Unique hierarchical context cascade (CLI + VSCode + GitHub)
- **Cursor** (AI-first IDE) - Rules-based, uses `.mdc`
- **Windsurf** (Codeium's IDE) - Rules-based, uses `.md`
- **Cline** (VSCode extension) - Rules-based, uses `.md`
- **Roo-Code** (VSCode extension) - Rules-based, uses `.md`

## Documentation Files

| File/Folder | Description | Status |
|-------------|-------------|--------|
| [CLAUDE_CODE.md](CLAUDE_CODE.md) | **Claude Code architecture and config guide** | ✅ Updated 2026-02 |
| [ANTIGRAVITY.md](ANTIGRAVITY.md) | **Google Antigravity architecture and config guide** | ✅ Added 2026-02 |
| [CURSOR.md](CURSOR.md) | Complete Cursor architecture | ✅ Complete |
| [PLATFORM_ARCHITECTURE.md](PLATFORM_ARCHITECTURE.md) | Cross-platform comparison and migration | ✅ Updated 2026-02 |
| [ide-template/](ide-template/) | Generic IDE template for new platforms | ✅ Complete |
| [Claude_Code/](Claude_Code/) | Detailed Claude Code research docs | ✅ Complete |
| ├─ [ARCHITECTURE.md](Claude_Code/ARCHITECTURE.md) | Deep dive: Skills, SubAgents, plugins | ✅ Complete |
| ├─ [RESEARCH_TOPICS.md](Claude_Code/RESEARCH_TOPICS.md) | Research topics | 🔍 Active |
| ├─ [PLATFORM_OVERVIEW.md](Claude_Code/PLATFORM_OVERVIEW.md) | Quick reference guide | ✅ Complete |

**Note**: Additional platform-specific folders (Gemini/, Cursor/, Windsurf/, Cline/, Roo_Code/) created for future detailed research.

## Quick Start

### For Template Maintainers

1. **Read PLATFORM_COMPARISON.md first** - Understand key differences
2. **Check platform-specific docs** before making changes
3. **Test on multiple platforms** when adding features
4. **Update docs** when discovering new information

### For Platform-Specific Users

If you're only using one platform, read your platform's doc:
- Using Claude Code? → [Claude_Code/](Claude_Code/) folder (comprehensive docs)
  - Quick start: [PLATFORM_OVERVIEW.md](Claude_Code/PLATFORM_OVERVIEW.md)
  - Deep dive: [ARCHITECTURE.md](Claude_Code/ARCHITECTURE.md)
  - Research: [RESEARCH_TOPICS.md](Claude_Code/RESEARCH_TOPICS.md)
- **Using Google Antigravity?** → [ANTIGRAVITY.md](ANTIGRAVITY.md) ← NEW
  - Config directory: `.agent/rules/` and `.agent/workflows/`
  - Working template: `.agent/` at project root
- Using Gemini CLI? → [GEMINI.md](GEMINI.md)
- Using Cursor? → [CURSOR.md](CURSOR.md)
- Using Windsurf? → [WINDSURF.md](WINDSURF.md)
- Using Cline/Roo-Code? → [CLINE_AND_ROO_CODE.md](CLINE_AND_ROO_CODE.md)

## Critical Differences

### Architecture Patterns

**Pattern 1: Claude Code (Unique)**
```
✅ Skills system - Reusable knowledge modules
✅ SubAgents - Specialized AI assistants  
✅ Complex structure - agents/, skills/, commands/
✅ File format: .md with YAML frontmatter
✅ Commands: /command prefix
```

**Pattern 2: Google Antigravity (Unique)**
```
✅ Artifacts - task.md, implementation_plan.md, walkthrough.md
✅ Knowledge Items - Auto-generated persistent memory
✅ Workflows - Slash commands (/workflow-name)
✅ Simple structure - .agent/rules/ + .agent/workflows/
✅ File format: .md (standard markdown)
✅ Global config: ~/.gemini/GEMINI.md
✅ // turbo - Auto-execute workflow steps
✅ Multi-model - Gemini + Claude + GPT
```

**Pattern 3: Non-Claude/Antigravity Platforms (Nearly Identical)**
```
✅ Rules-based - Custom instructions
✅ Simple structure - rules/ folder
✅ File format: .md (or .mdc for Cursor only)
✅ YAML frontmatter - Same format across all
✅ Commands: Platform-specific (@command for Cursor)
```

### The ONLY Real Difference Between Non-Claude Platforms

**File Extension:**
```
Cursor:       .mdc ← ONLY difference from others
Windsurf:     .md
Cline:        .md
Roo-Code:     .md
```

**Everything else is the same:**
- Same YAML frontmatter format
- Same rule structure
- Same markdown syntax
- Same directory pattern (`.{platform}/rules/`)
- Migration = rename folder + change extension!

## Maintenance Schedule

### Quarterly Review (Every 3 Months)
- [ ] Check all platform official docs for updates
- [ ] Test template on each platform
- [ ] Update architecture docs
- [ ] Update comparison table
- [ ] Document breaking changes

### When Adding Features
- [ ] Document platform compatibility
- [ ] Test on Claude Code and Cursor (primary)
- [ ] Update platform-specific folders
- [ ] Update comparison doc
- [ ] Tag release with compatibility notes

### When Discovering Issues
- [ ] Document in platform-specific file
- [ ] Add to "Known Issues" in comparison
- [ ] Provide workaround if available
- [ ] Update affected migration guides

## How to Contribute

### Researching Unknown Platforms

For Windsurf, Cline, Roo-Code (incomplete docs):

1. **Install the Platform**
   - Download and install
   - Set up a test project
   - Try basic features

2. **Test Structure**
   ```bash
   # Create test files
   mkdir -p .platform/rules
   echo "test" > .platform/rules/test.md

   # Test if recognized
   # Check AI behavior
   # Document findings
   ```

3. **Document Findings**
   - Update platform-specific .md file
   - Add to comparison table
   - Share examples
   - Note limitations

4. **Submit Update**
   - Edit relevant docs
   - Add examples
   - Update README
   - Note verification status

### Improving Existing Docs

- Clarify confusing sections
- Add examples
- Fix errors
- Update outdated information
- Add troubleshooting tips

## Key Concepts

### Universal Features
Work on all platforms:
- **Markdown files** - All platforms support `.md` files
- **YAML frontmatter** - Widely supported for metadata
- **MCP (Model Context Protocol)** - Standard tool integration
- **Custom instructions** - All platforms support AI behavior customization
- **File-based configuration** - All use file-based setup

### Platform-Specific Features
Only work on specific platforms:
- **Skills/SubAgents**: Claude Code only
- **.mdc files**: Cursor only (must use `.mdc` not `.md`)
- **Command prefixes**: `/` (Claude Code), `@` (Cursor), varies for others
- **MCP UI**: Built-in (Claude Code), VSCode settings (others)
- **Directory names**: `.claude/`, `.cursor/`, `.windsurf/`, etc.

### Cross-Platform Strategy
1. **Start with universal features** - Markdown, YAML, MCP
2. **Add platform-specific configs** - Create platform folders as needed
3. **Document requirements** - Note which features need which platform
4. **Test on target platforms** - Verify before committing
5. **Keep docs updated** - Track platform changes quarterly

## Common Tasks

### Adding New Rule/Instruction

```bash
# 1. Create for Claude Code
echo "---
name: my-rule
description: What it does
---
# My Rule
Content..." > .claude/skills/my-rule/SKILL.md

# 2. Create for Cursor
echo "---
description: What it does
alwaysApply: true
---
# My Rule
Content..." > .cursor/rules/my-rule.mdc

# 3. Document
# Add to PLATFORM_COMPARISON.md
```

### Testing Cross-Platform

```bash
# 1. Test in Claude Code
code . # Open in VSCode with Claude Code

# 2. Test in Cursor
cursor . # Open in Cursor

# 3. Document results
# Update platform-specific docs
```

### Migrating Between Platforms

See migration guides in [PLATFORM_COMPARISON.md](PLATFORM_COMPARISON.md):
- Claude Code → Cursor
- Cursor → Claude Code
- To Windsurf/Cline/Roo-Code

## Verification Status

| Platform | Directory Structure | File Format | Commands | MCP | Skills/Agents |
|----------|-------------------|-------------|-----------|-----|---------------|
| Claude Code | ✅ Verified | ✅ `.md` | ✅ `/command` | ✅ Built-in | ✅ Yes |
| Google Antigravity | ✅ Verified | ✅ `.md` | ✅ `/workflow-name` | ✅ Yes | ❌ No (Workflows instead) |
| Cursor | ✅ Verified | ✅ `.mdc` | ✅ `@command` | ✅ VSCode | ✅ Yes |
| Windsurf | ❓ Unknown | ❓ Unknown | ❓ Unknown | ❓ Unknown | ❓ Unknown |
| Cline | ❓ Unknown | ❓ Unknown | ❓ Unknown | ✅ Likely VSCode | ❌ Likely No |
| Roo-Code | ❓ Unknown | ❓ Unknown | ❓ Unknown | ✅ Likely VSCode | ❌ Likely No |

Legend:
- ✅ Confirmed working
- ❌ Confirmed not supported
- ❓ Needs verification
- ⚠️ Partial support

## Official Resources

- **Claude Code**: https://docs.anthropic.com/en/docs/claude-code
- **Google Antigravity**: https://antigravity.google/docs
- **Cursor**: https://docs.cursor.com
- **Windsurf**: https://codeium.com/windsurf
- **Cline**: [Add link when found]
- **Roo-Code**: [Add link when found]
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Antigravity Community**: https://antigravity.codes

## Questions?

1. Check platform-specific documentation
2. Check PLATFORM_COMPARISON.md
3. Search official platform docs
4. Ask in platform community (Discord/forum)
5. Update this documentation with answer

## Version History

- **2026-02-19**: Added Google Antigravity support
  - New `ANTIGRAVITY.md` architecture documentation
  - Working `.agent/rules/` and `.agent/workflows/` template
  - Updated `PLATFORM_ARCHITECTURE.md` with Antigravity comparison
  - Added migration guides: Cursor ↔ Antigravity, Claude Code → Antigravity
  - trent workflows as Antigravity slash commands (`/trent-*`)

- **2025-10-26**: Initial documentation
  - Complete docs for Claude Code and Cursor
  - Placeholder docs for Windsurf, Cline, Roo-Code
  - Comprehensive comparison table
  - Migration guides
  - Maintenance schedule

---

**Maintained by**: Template maintainers
**Last Review**: 2025-10-26
**Next Review**: 2026-01-26
**Status**: Active documentation, community contributions welcome
