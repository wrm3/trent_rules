# Firecrawl Platform Documentation Service
# docker/firecrawl/

## Overview
Self-hosted web crawler that keeps AI platform documentation (Cursor, Claude, Gemini)
up to date in the trent RAG knowledge base. Uses **Firecrawl API v2** (`https://api.firecrawl.dev/v2`) when `FIRECRAWL_API_KEY` is set; v2 supports `sitemap: "include"` and is the recommended API.

## Architecture
```
docker/firecrawl/
├── crawler.py          # Crawl targets, doc extraction, chunking
├── scheduler.py        # Weekly cron job, diff detection, git commit, RAG ingest
├── config.py           # Crawl targets, RAG config, DB config
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container definition
├── platforms/          # Persisted doc snapshots (committed to git)
│   ├── cursor/         # docs.cursor.com snapshots
│   ├── claude/         # docs.anthropic.com snapshots
│   └── gemini/         # ai.google.dev snapshots
└── README.md           # This file
```

## Crawl Targets

| Platform | URL | Frequency | Priority |
|----------|-----|-----------|---------|
| Cursor | https://docs.cursor.com | Weekly | High |
| Claude | https://docs.anthropic.com/en/docs | Weekly | High |
| Claude API | https://docs.anthropic.com/en/api | Weekly | High |
| Gemini | https://ai.google.dev/gemini-api/docs | Weekly | Medium |

## Environment Variables

```bash
FIRECRAWL_API_KEY=    # Optional: Firecrawl.dev API key (use self-hosted without this)
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=rag_knowledge   # Must match postgres service (same DB as trent RAG)
POSTGRES_USER=trent
POSTGRES_PASSWORD=          # Must match postgres; use same .env when running
RAG_SUBJECT=platform_docs   # Subject for RAG ingestion
PLATFORMS_DIR=/data/platforms  # Set in compose; snapshots visible at <repo>/.platforms/snapshots/
REPO_ROOT=/repo             # Set in compose; CHANGELOG and CRAWL_STATUS go to <repo>/.platforms/
CRAWL_SCHEDULE=0 2 * * 0  # Cron: Sundays at 2am UTC
GIT_AUTO_COMMIT=true   # Commit snapshots to git after crawl
```

## How It Works

1. **Scheduler** triggers weekly crawl per the cron schedule
2. **Crawler** fetches all pages from each target using Firecrawl
3. **Diff detection** compares new content to stored snapshots in `platforms/`
4. **Changed pages** are updated in `platforms/` and re-ingested to RAG
5. **Git commit** records the update with a `platform-docs(update):` commit
6. **CHANGELOG.md** is updated with human-readable summary of changes

## Running Manually

Use the **same env file as postgres** so `POSTGRES_USER` and `POSTGRES_PASSWORD` match the running Postgres (e.g. `docker/.env`). If you get "password authentication failed", override when running: `-e POSTGRES_USER=trent -e POSTGRES_PASSWORD=trent_secret` (or whatever your postgres was initialized with). After changing code, rebuild so the container has the latest snapshot path: `docker compose --profile platform-docs build firecrawl`.

```bash
cd docker
# Full crawl and ingest (all targets)
docker compose --env-file .env --profile platform-docs run --rm firecrawl python scheduler.py --now

# Crawl one platform only (e.g. claude-platform for platform.claude.com docs)
docker compose --env-file .env --profile platform-docs run --rm firecrawl python scheduler.py --now --platform claude-platform

# Crawl only, no RAG ingest (writes MDs to .platforms/snapshots only)
docker compose --env-file .env --profile platform-docs run --rm firecrawl python crawler.py --platform cursor

# Check what changed since last crawl
docker compose --env-file .env --profile platform-docs run --rm firecrawl python scheduler.py --diff-only
```

## Verifying Intermediary Steps

1. **Markdown snapshots** — After a crawl, check `<repo>/.platforms/snapshots/`. Each platform has a subdir (e.g. `claude/`) with one `.md` file per page and a `.json` sidecar.
2. **Changelog and status** — `<repo>/.platforms/CHANGELOG.md` and `.platforms/CRAWL_STATUS.json` are updated after each run.
3. **RAG (database)** — The `platform_docs_search` MCP tool queries the `memory_captures` table in Postgres. If the table is missing (e.g. existing DB created before `08_platform_docs_memory_captures.sql`), create it once:
   ```bash
   docker exec -i trent_rules_postgres psql -U trent -d rag_knowledge < docker/init_db/08_platform_docs_memory_captures.sql
   ```
