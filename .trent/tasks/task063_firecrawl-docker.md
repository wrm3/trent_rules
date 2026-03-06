---
id: 63
title: 'Create docker-compose additions for firecrawl service'
type: feature
status: pending
priority: high
phase: 0
subsystems: [platform-docs]
ai_safe: false
blast_radius: medium
requires_verification: true
requires_solo_agent: false
dependencies: [60, 62]
project_context: 'The firecrawl service runs alongside the existing trent MCP server in Docker — needs its own container with volume mounts, environment variables, and health check without disrupting the existing docker-compose setup'
---

# Task 063: Create docker-compose additions for firecrawl service

## Objective
Create the docker-compose service definition for the Firecrawl scheduler in `template_v2/docker/` — a new service that runs alongside the existing trent MCP server without modifying its configuration.

## IMPORTANT CONSTRAINT
DO NOT modify the existing `docker/docker-compose.yml` for the live trent server.
Create a new `template_v2/docker/docker-compose.firecrawl.yml` that extends the main compose file, OR create a standalone compose file for the firecrawl service.

## docker-compose.firecrawl.yml

```yaml
# docker-compose.firecrawl.yml
# Firecrawl Platform Docs Service
# Usage: docker-compose -f docker-compose.yml -f docker-compose.firecrawl.yml up -d
version: "3.8"

services:
  firecrawl_scheduler:
    build:
      context: .
      dockerfile: firecrawl/Dockerfile
    container_name: trent_firecrawl
    restart: unless-stopped
    environment:
      - FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB:-trent_rag}
      - POSTGRES_USER=${POSTGRES_USER:-trent}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - GIT_REPO_PATH=/workspace
      - GIT_USER_EMAIL=${GIT_USER_EMAIL:-trent-bot@local}
      - GIT_USER_NAME=${GIT_USER_NAME:-trent-firecrawl}
      - RULES_VERSION=${TRENT_RULES_VERSION:-5.0.0}
    volumes:
      - ${WORKSPACE_PATH:-.}:/workspace    # Mount project root for git operations
      - firecrawl_data:/app/crawled         # Persistent crawl storage
    ports:
      - "8081:8080"    # HTTP trigger endpoint
    networks:
      - trent_network
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/status"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  firecrawl_data:
    driver: local

networks:
  trent_network:
    external: true    # Shared with main trent compose
```

## firecrawl/Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY firecrawl/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install git for commit operations
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

COPY firecrawl/ .

# Configure git for container
RUN git config --global --add safe.directory /workspace

CMD ["python", "scheduler.py"]
```

## firecrawl/requirements.txt

```
firecrawl-py>=1.0.0
apscheduler>=3.10.0
fastapi>=0.110.0
uvicorn>=0.27.0
psycopg2-binary>=2.9.0
gitpython>=3.1.40
pyyaml>=6.0.0
```

## .env.example additions

```bash
# Firecrawl Service
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
WORKSPACE_PATH=/path/to/your/project
GIT_USER_EMAIL=your-bot@example.com
GIT_USER_NAME=trent-firecrawl
```

## Acceptance Criteria
- [ ] `template_v2/docker/docker-compose.firecrawl.yml` exists
- [ ] `template_v2/docker/firecrawl/Dockerfile` exists
- [ ] `template_v2/docker/firecrawl/requirements.txt` exists
- [ ] Service uses `trent_network` external (shared with main trent)
- [ ] `WORKSPACE_PATH` volume mount for git operations
- [ ] `FIRECRAWL_API_KEY` from environment (not hardcoded)
- [ ] `.env.example` shows the new required variables
- [ ] Health check endpoint defined

## Verification Steps
- [ ] docker-compose.firecrawl.yml has all required fields
- [ ] Dockerfile exists and installs git
- [ ] requirements.txt lists all dependencies
- [ ] FIRECRAWL_API_KEY is an env var (not in any file)
- [ ] Uses extend pattern (doesn't duplicate trent postgres service)

## When Stuck
- This should NOT modify the live docker-compose.yml
- Use `docker-compose -f docker-compose.yml -f docker-compose.firecrawl.yml up -d` pattern
- The `trent_network: external: true` is key — shares the network with the main trent container
