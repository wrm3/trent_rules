---
phase: 1
name: 'Core Infrastructure'
status: planning
subsystems: [database, mcp_server, memory_tools]
task_range: '100-199'
prerequisites: [0]
started_date: ''
completed_date: ''
pivoted_from: null
pivot_reason: ''
---

# Phase 1: Core Infrastructure

## Overview
Build the PostgreSQL schema and all 4 MCP memory tools. No platform-specific adapter code
yet — just the shared pipeline that all adapters will feed into. End state: can call
memory_ingest_session() with test data and get semantic search results back.

## Objectives
- agent_projects, agent_sessions, agent_turns tables live in PostgreSQL
- All 4 MCP tools implemented and unit-tested
- Plugin registered in main MCP server
- Can ingest sample data and run memory_search() successfully

## Deliverables
- [ ] docker/init_db/05_agent_memory.sql (from Phase 0 Task 005)
- [ ] docker/trent/plugins/agent_memory.py with all 4 tools
- [ ] Plugin registered in docker/trent/server.py (or equivalent entry point)
- [ ] Manual test confirming ingest → search pipeline works

## Acceptance Criteria
- [ ] Docker container rebuilds cleanly with new schema
- [ ] agent_projects, agent_sessions, agent_turns tables exist with correct indexes
- [ ] memory_ingest_session() accepts sample data and stores it
- [ ] memory_search("test query") returns relevant results
- [ ] memory_context() returns formatted briefing string
- [ ] memory_sessions() lists sessions by project
- [ ] Token budget in memory_context() respected (default 2000 tokens)
