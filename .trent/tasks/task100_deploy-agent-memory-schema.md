---
id: 100
title: 'Deploy 05_agent_memory.sql to PostgreSQL and rebuild container'
type: infrastructure
status: completed
priority: critical
phase: 1
subsystems: [database, docker]
project_context: Schema must be live before any MCP tools can be written or tested
dependencies: [5]
---

# Task 100: Deploy Agent Memory Schema

## Objective
Get `05_agent_memory.sql` running inside the Docker PostgreSQL container so that
tables `agent_projects`, `agent_sessions`, `agent_turns`, and `agent_memory_captures`
exist and are queryable.

## Acceptance Criteria
- [ ] 05_agent_memory.sql file exists in `docker/init_db/`
- [ ] Docker container rebuilt with `--build` flag
- [ ] All 4 tables created in PostgreSQL
- [ ] `ivfflat` extension available (needed for vector index)
- [ ] `upsert_agent_project()` function created
- [ ] `memory_search` vector index created

## Steps
1. Confirm `docker/init_db/05_agent_memory.sql` exists (done in Task 005)
2. Rebuild the Docker container: `docker-compose up -d --build trent_rules_docker`
3. Verify tables with: `docker exec -it trent_rules_docker psql -U trent_user -d trent_db -c "\dt agent_*"`
4. Verify vector index: `\d agent_turns`
