# trent MCP Consolidation - Task List

## Active Tasks

### Phase 0: MCP Consolidation (Task IDs: 1-99)

- [📋] **Task 001**: Create trent_docker folder structure
- [📋] **Task 002**: Migrate RAG core from fstrent_mcp_rag_docker
- [📋] **Task 003**: Create Oracle database tools plugin
- [📋] **Task 004**: Create deep research tools plugin (no DuckDuckGo)
- [📋] **Task 005**: Create MediaWiki tools plugin
- [📋] **Task 006**: Create template installer plugin (OS-aware)
- [ ] **Task 007**: Update Docker configuration
- [ ] **Task 008**: Consolidate dependencies (pyproject.toml)
- [ ] **Task 009**: Update admin dashboard for new tools
- [ ] **Task 010**: Test all plugins end-to-end
- [ ] **Task 011**: Create .mcp.json example configuration
- [ ] **Task 012**: Document new unified MCP server

### Phase 1: Template System (Task IDs: 100-199)
(After MCP consolidation complete)

- [ ] **Task 100**: Define minimal template contents
- [ ] **Task 101**: Define full template contents
- [ ] **Task 102**: Implement OS detection in installer
- [ ] **Task 103**: Handle symlink vs copy based on OS
- [ ] **Task 104**: Test cross-platform installation

### Phase 2: Claude Code Cleanup (Task IDs: 200-299)
(Remove Claude Code IDE references, keep Claude AI model references)

- [✅] **Task 200**: Clean trent Core Skills (18 files, ~100 matches)
- [✅] **Task 201**: Clean Agent SDK files (8 files, ~50 matches)
- [✅] **Task 202**: Clean Template & Example files (12 files, ~80 matches)
- [❌] **Task 203**: ~~Clean YouTube/Video Analysis files~~ (CANCELLED - YouTube components removed entirely)
- [✅] **Task 204**: Clean Miscellaneous files (30+ files, ~35 matches)
- [📋] **Task 205**: Verify cleanup complete and test skills/agents

## Completed Tasks
(None yet)

## Blocked Tasks
(None yet)

---
**Legend:**
- `[ ]` - Pending (no task file yet)
- `[📋]` - Ready (task file created)
- `[🔄]` - In Progress
- `[✅]` - Completed
- `[❌]` - Failed/Blocked
