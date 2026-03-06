# Firecrawl Platform Documentation Service
# docker/firecrawl/

## Overview
Self-hosted web crawler that keeps AI platform documentation (Cursor, Claude, Gemini)
up to date in the trent RAG knowledge base.

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
POSTGRES_HOST=        # From docker-compose (default: trent_postgres)
POSTGRES_PORT=5432
POSTGRES_DB=trent_memory
POSTGRES_USER=trent
POSTGRES_PASSWORD=    # From docker-compose secrets
RAG_SUBJECT=platform_docs  # Subject for RAG ingestion
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

```bash
# Full crawl and ingest
docker-compose run firecrawl python scheduler.py --now

# Crawl only (no RAG ingest)
docker-compose run firecrawl python crawler.py --platform cursor

# Check what changed since last crawl
docker-compose run firecrawl python scheduler.py --diff-only
```
