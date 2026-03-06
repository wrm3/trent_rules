# CLAUDE.md - trent

## Project Overview
trent is an AI-powered task management and development system for Cursor IDE and Claude Code. It provides structured task tracking, project planning, quality assurance, and workflow management through a file-based system with enforced synchronization.

## This Repository's Purpose
This is the **source repository** for the trent system. It contains:
- The complete rule set for task management
- Templates for installing trent in other projects
- MCP server for RAG, research, Oracle, and video analysis tools

When making changes here, consider:
1. Does this affect the docker/templates/ files?
2. Does this need to update agents.md trent section?
3. Should this trigger a version bump?

## Tech Stack
- **Rules**: `.claude/rules/*.md` (Claude Code) / `.cursor/rules/*.mdc` (Cursor)
- **Skills**: Markdown with YAML frontmatter in `.claude/skills/` and `.cursor/skills/`
- **MCP Server**: Python with FastMCP, PostgreSQL/pgvector for RAG, Oracle support
- **Task Files**: Markdown with YAML frontmatter
- **Package Management**: UV for Python

## Key Directories
```
.cursor/                # Cursor IDE configuration
.claude/                # Claude Code configuration (rules, skills, agents)
.agent/                 # Gemini/Antigravity configuration
.trent/                 # Task management data (TASKS.md, tasks/, phases/)
docker/                 # MCP server (Docker)
docs/                   # Project documentation
temp_scripts/           # Test and utility scripts
```

## MCP Tools Available
| Tool | Description |
|------|-------------|
| `rag_search` | Semantic search in knowledge base |
| `rag_ingest_text` | Add content to knowledge base |
| `rag_list_subjects` | List available knowledge bases |
| `research_deep` | Comprehensive research with Perplexity |
| `research_search` | Web search for research |
| `oracle_query` | Read-only SQL on Oracle |
| `oracle_execute` | Write SQL on Oracle |
| `mediawiki_page` | MediaWiki CRUD operations |
| `mediawiki_search` | Search MediaWiki |
| `trent_install` | Install full trent environment |
| `trent_rules_update` | Update IDE configs/rules |
| `trent_plan_reset` | Reset .trent/ to blank template |
| `trent_server_status` | Health check |
| `md_to_html` | Convert markdown to HTML |
| `memory_ingest_session` | Ingest raw turns from file adapters |
| `memory_capture_session` | AI self-reports session summary |
| `memory_search` | Semantic search over session memory |
| `memory_sessions` | List recent sessions for a project |
| `memory_context` | Token-budgeted context block |

## Development Commands
```bash
cd docker && docker-compose up -d              # Start MCP server
docker ps | grep trent_rules_docker            # Check status
docker logs trent_rules_docker -f              # View logs
cd docker && docker-compose up -d --build trent_rules_docker  # Rebuild
```

## Rules & Configuration
All detailed rules are in `.claude/rules/`. Key areas:
- **00-04**: Core (response format, docs, git, code review, reusability)
- **05-09**: Memory, Cursor CLI, Claude CLI, PowerShell, Python/UV
- **20-32**: Trent task management system (vNext: tasks, infra, planning, QA, workflow, autonomous, verification, platform parity)
- **SV**: Silicon Valley personalities

## Security
- Never commit API keys, tokens, or passwords
- Use environment variables for secrets
- Always use parameterized queries
- Oracle credentials passed per-query via tool parameters

---
**Version**: 5.0.0
**Last Updated**: 2026-03-03
**Supported IDEs**: Cursor, Claude Code, Gemini
