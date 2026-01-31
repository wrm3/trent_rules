---
id: 1
title: 'Create trent_docker folder structure'
type: task
status: pending
priority: high
phase: 0
subsystems: [mcp, docker]
project_context: 'Foundation for unified MCP server - create directory structure based on fstrent_mcp_rag_docker architecture'
dependencies: []
estimated_effort: '30 minutes'
---

# Task 001: Create trent_docker Folder Structure

## Objective
Create the unified MCP server folder structure, renamed from fstrent_mcp_rag_docker to trent_docker.

## Target Structure
```
mcps/trent_docker/
├── server.py                    # Root entry point
├── trent/
│   ├── __init__.py
│   ├── config.py               # Multi-source config loader
│   ├── server.py               # Main FastMCP server
│   ├── plugin_loader.py        # Plugin discovery
│   ├── subjects.py             # Multi-subject management
│   ├── database/
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── embeddings.py
│   │   ├── multi_subject.py
│   │   └── schema.sql
│   └── tools/
│       └── plugins/
│           ├── __init__.py
│           ├── rag_search.py
│           ├── rag_ingest_text.py
│           └── ... (existing RAG tools)
├── admin_dashboard/            # Flask UI
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Acceptance Criteria
- [ ] Folder structure created
- [ ] All __init__.py files present
- [ ] README.md with project description
- [ ] pyproject.toml with base dependencies

## Notes
- Keep plugin architecture from RAG server
- Prepare for additional tool plugins (Oracle, research, mediawiki, template)
