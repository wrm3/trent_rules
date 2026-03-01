# Project Context: trent MCP Consolidation

## Mission
Consolidate multiple standalone MCP servers into a unified `trent_rules_docker` server with modular plugin architecture, providing RAG, database, research, and template installation capabilities.

## Current Phase
**Phase 0: Setup & Infrastructure**

Building the unified MCP server from fstrent_mcp_rag_docker base, integrating tools from 5 other MCPs.

## Success Criteria

### Primary Objectives
- [🔄] Rename and restructure fstrent_mcp_rag_docker to trent_rules_docker
- [ ] Integrate Oracle database tools (thick client support)
- [ ] Integrate deep research tools (NO DuckDuckGo)
- [ ] Integrate MediaWiki tools
- [ ] Create template installer tool for new projects (OS-aware)
- [ ] All tools working via Docker container

### Quality Standards
- Plugin architecture maintained (tools/plugins/)
- Multi-transport support (stdio, HTTP)
- Admin dashboard functional
- Cross-platform template installation (Windows/Mac/Linux)

### User Experience Goals
- Single Docker container for all MCP needs
- Easy project initialization via template installer
- Seamless IDE integration (Cursor)

## Current Status

### Completed
(None yet)

### In Progress
- MCP exploration and analysis complete
- Architecture decisions made
- Task tracking initialized

### Upcoming
- Create trent_rules_docker folder structure
- Migrate RAG core components
- Add Oracle tools plugin
- Add research tools plugin (no DuckDuckGo)
- Add MediaWiki tools plugin
- Add template installer plugin

## Scope Boundaries

### In Scope
- RAG/vector search functionality
- Oracle database operations (read/write with thick client)
- Deep research (Perplexity, Google, NOT DuckDuckGo)
- MediaWiki page management
- Template installation for new projects
- OS detection for symlink/copy decisions

### Out of Scope
- DuckDuckGo search (explicitly rejected)
- Silicon Valley rules (novelty only, skip)
- Separate MCP servers (consolidating into one)

### Approved Complexity
- Docker-based deployment
- PostgreSQL with pgvector
- Plugin architecture for tools
- Multi-transport MCP (stdio + HTTP)

## Architecture Principles

### Design Philosophy
- **Modular plugins**: Each tool category as separate plugin file
- **Single container**: One Docker image, multiple services
- **Backward compatible**: Support existing .mcp.json configs
- **Cross-platform**: Template installer detects OS for symlink handling

## Key Metrics

### Technical Metrics
- All existing RAG tools functional
- Oracle read/write operations working
- Research tools (minus DuckDuckGo) operational
- Template installer creates valid project structure

### User Metrics
- Time to initialize new project < 30 seconds
- Cursor IDE integration working

## Integration Points
- PostgreSQL database (RAG storage)
- Oracle databases (via thick client, OCI VPN)
- MediaWiki server (OCI VPN)
- OpenAI API (embeddings)
- Perplexity/Google APIs (research)

## Reference Links
- Source MCPs: `mcps/` folder
- Template backup: `.trent_template/`

## Next Steps

### Immediate
1. Create trent_rules_docker folder structure
2. Copy and rename RAG core from fstrent_mcp_rag_docker
3. Create task files for each integration step
4. Begin tool migrations

---

**Last Updated**: 2026-01-28
**Project Status**: In Progress
**Current Phase**: Phase 0 - MCP Consolidation
