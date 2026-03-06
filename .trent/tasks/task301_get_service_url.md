---
id: 301
title: 'MCP tool: get_service_url — dynamic service URL resolver'
type: feature
status: pending
priority: high
phase: 3
subsystem: mcp-tools
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "Service URLs change across environments (home, work, OKE/Kubernetes). A single MCP tool that returns the correct URL for any service — MediaWiki, pgAdmin, trent — based on environment configuration."
---

# Task 301: MCP tool get_service_url

## Objective
Create `docker/trent/tools/plugins/get_service_url.py` — an MCP tool that returns
the correct base URL for any named service, reading from env vars so the URL
automatically reflects the deployment environment (local, work VPN, OKE, etc.).

## Acceptance Criteria
- [ ] Plugin file exists and loads
- [ ] Returns URL for: `mediawiki`, `pgadmin`, `trent`, `postgres`
- [ ] Accepts `service` param
- [ ] Returns `{"service": "mediawiki", "url": "http://...", "note": "..."}`
- [ ] Graceful message when service not configured

## Env vars it reads
```
MEDIAWIKI_URL (or MEDIAWIKI_SERVER)
PGADMIN_URL (new — defaults to http://localhost:8083)
TRENT_URL (new — defaults to http://localhost:8082)
POSTGRES_PUBLIC_URL (new — for pgAdmin connection string display)
```
