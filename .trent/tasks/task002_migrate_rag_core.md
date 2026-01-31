---
id: 2
title: 'Migrate RAG core from fstrent_mcp_rag_docker'
type: task
status: pending
priority: high
phase: 0
subsystems: [mcp, rag, database]
project_context: 'Copy and adapt core RAG functionality from existing server'
dependencies: [1]
estimated_effort: '1 hour'
---

# Task 002: Migrate RAG Core from fstrent_mcp_rag_docker

## Objective
Copy the core RAG server functionality from fstrent_mcp_rag_docker, updating imports and references to new package name.

## Source Files to Migrate
From `mcps/fstrent_mcp_rag_docker/fstrent_mcp_rag/`:
- `config.py` - Update package references
- `server.py` - Main server (update imports)
- `plugin_loader.py` - Keep as-is
- `subjects.py` - Keep as-is
- `database/*` - All files
- `tools/plugins/*` - All RAG tools
- `admin_dashboard/*` - Keep as-is

## Changes Required
1. Replace all `fstrent_mcp_rag` with `trent`
2. Update Docker service names
3. Update admin dashboard branding
4. Keep all RAG tools functional

## Acceptance Criteria
- [ ] All RAG tools migrated and renamed
- [ ] Plugin loader finds tools in new location
- [ ] Database client connects properly
- [ ] Admin dashboard accessible
- [ ] No references to old package name

## Notes
- This is primarily a rename/refactor operation
- All RAG functionality should work identically after migration
