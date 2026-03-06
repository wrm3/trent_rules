---
id: 300
title: 'Migrate MediaWiki to PostgreSQL + integrate into trent docker-compose'
type: feature
status: pending
priority: high
phase: 3
subsystem: mediawiki
blast_radius: medium
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "Eliminate the separate mediawiki_mysql container by running MediaWiki on the existing trent Postgres instance. Consolidate the separate M:\\fstrent_mcp_mediawiki compose setup into g:\\trent_rules\\docker\\docker-compose.yml under a mediawiki profile."
---

# Task 300: Migrate MediaWiki to PostgreSQL + docker-compose integration

## Objective
1. Add `mediawiki` service to `docker/docker-compose.yml` under `profiles: [mediawiki]`
2. Write an env-driven `LocalSettings.php` template — no more wizard clicks
3. Add `mediawiki_setup.sh` init script that creates the mediawiki Postgres DB
4. Add all MEDIAWIKI_* vars to `.env` and `.env.example`
5. Document teardown of `M:\fstrent_mcp_mediawiki\`

## Acceptance Criteria
- [ ] `docker compose --profile mediawiki up -d` starts MediaWiki against Postgres
- [ ] No MySQL container required
- [ ] LocalSettings.php generated from env vars (no manual wizard)
- [ ] Admin login works with credentials from `.env`
- [ ] `mediawiki_page` and `mediawiki_search` MCP tools connect successfully
- [ ] Bot password pre-configured from `.env`

## New env vars
```
MEDIAWIKI_SITE_NAME=trent Knowledge Base
MEDIAWIKI_SERVER=http://localhost:8880
MEDIAWIKI_ADMIN_USER=FSTrent
MEDIAWIKI_ADMIN_PASSWORD=...
MEDIAWIKI_ADMIN_EMAIL=...
MEDIAWIKI_DB_NAME=mediawiki
MEDIAWIKI_DB_PREFIX=mw_
MEDIAWIKI_SECRET_KEY=... (generate with openssl)
MEDIAWIKI_UPGRADE_KEY=... (generate with openssl)
MEDIAWIKI_USERNAME=FSTrent@trent_MCP
MEDIAWIKI_PASSWORD=...
```
