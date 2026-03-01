---
id: 5
title: 'Write 05_agent_memory.sql PostgreSQL schema'
type: design
status: completed
priority: high
phase: 0
subsystems: [database]
project_context: 'The data model for all agent memory storage. Must be right before Phase 1 begins.'
dependencies: [3, 4]
---

# Task 005: Write 05_agent_memory.sql

## Objective
Write the complete PostgreSQL schema for agent memory tables. This will be added to
docker/init_db/ alongside the existing schema files. Must include all indexes for
semantic search performance, full-text search fallback, and project/session scoping.

## Acceptance Criteria
- [ ] agent_projects table defined (project_id UUID as natural key)
- [ ] agent_sessions table defined (conversation_id, platform, project FK)
- [ ] agent_turns table defined (embedding vector, content hash for dedup)
- [ ] All indexes defined (ivfflat for vector search, GIN for FTS, B-tree for lookups)
- [ ] Schema idempotent (CREATE TABLE IF NOT EXISTS throughout)
- [ ] File placed at docker/init_db/05_agent_memory.sql

## Schema Draft

```sql
-- ============================================================
-- Agent Memory System
-- Stores AI agent conversation history with semantic search
-- ============================================================

-- Projects: one record per project, keyed by project_uuid from .trent/.project_id
CREATE TABLE IF NOT EXISTS agent_projects (
    id           SERIAL PRIMARY KEY,
    project_id   VARCHAR(64) UNIQUE NOT NULL,  -- e.g. "proj_a1b2c3d4" from .trent/.project_id
    user_id      VARCHAR(64),                   -- e.g. "usr_e5f6g7h8" from ~/.trent/user_config.json
    machine_id   VARCHAR(64),
    project_path TEXT,                          -- last known path (informational only)
    display_name VARCHAR(255),
    created_at   TIMESTAMPTZ DEFAULT NOW(),
    updated_at   TIMESTAMPTZ DEFAULT NOW()
);

-- Sessions: one record per IDE conversation/session
CREATE TABLE IF NOT EXISTS agent_sessions (
    id              SERIAL PRIMARY KEY,
    conversation_id VARCHAR(255) UNIQUE NOT NULL, -- from hook payload
    project_id      INTEGER REFERENCES agent_projects(id) ON DELETE CASCADE,
    platform        VARCHAR(50) NOT NULL,          -- 'cursor' | 'claude_code' | 'gemini' | 'vscode'
    status          VARCHAR(50),
    loop_count      INTEGER,
    session_summary TEXT,                          -- LLM-generated rolling summary
    started_at      TIMESTAMPTZ,
    ended_at        TIMESTAMPTZ DEFAULT NOW(),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Turns: one record per user→assistant exchange
CREATE TABLE IF NOT EXISTS agent_turns (
    id              SERIAL PRIMARY KEY,
    session_id      INTEGER REFERENCES agent_sessions(id) ON DELETE CASCADE,
    turn_index      INTEGER NOT NULL,
    content_hash    VARCHAR(64),               -- MD5(user_message + agent_response) for dedup
    user_message    TEXT,
    agent_response  TEXT,
    llm_title       VARCHAR(255),              -- LLM-generated 10-15 word title
    llm_description TEXT,                      -- LLM-generated 2-4 sentence summary
    embedding       vector(1536),              -- text-embedding-3-small
    platform        VARCHAR(50),               -- denormalized for fast per-platform queries
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_agent_turns_session
    ON agent_turns(session_id);

CREATE INDEX IF NOT EXISTS idx_agent_turns_embedding
    ON agent_turns USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

CREATE INDEX IF NOT EXISTS idx_agent_turns_content_hash
    ON agent_turns(content_hash);

CREATE INDEX IF NOT EXISTS idx_agent_turns_fts
    ON agent_turns USING GIN (
        to_tsvector('english',
            COALESCE(llm_title, '') || ' ' || COALESCE(llm_description, ''))
    );

CREATE INDEX IF NOT EXISTS idx_agent_sessions_project
    ON agent_sessions(project_id);

CREATE INDEX IF NOT EXISTS idx_agent_sessions_conversation
    ON agent_sessions(conversation_id);

CREATE INDEX IF NOT EXISTS idx_agent_projects_project_id
    ON agent_projects(project_id);
```

## Notes on Decisions
- `platform` denormalized onto agent_turns for fast "search only Cursor turns" queries
- `vector(1536)` matches text-embedding-3-small (same as existing RAG tables)
- content_hash on agent_turns enables deduplication without reading full content
- agent_projects.project_path is informational only — never used as a key
- project_id (the trent UUID) is the true identity, not the path

## Output
Final file: docker/init_db/05_agent_memory.sql
This gets picked up by Docker on `docker-compose up` or container rebuild.
