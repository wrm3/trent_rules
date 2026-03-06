---
id: 302
title: 'pgAdmin service info tool + admin-login env enforcement'
type: feature
status: pending
priority: medium
phase: 3
subsystem: mcp-tools
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: [301]
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "pgAdmin is already deployed under --profile admin. Add PGADMIN_EMAIL and PGADMIN_PASSWORD to .env with strong defaults. The get_service_url tool (T-301) handles URL resolution; this task hardens the .env defaults and documents the admin login requirement."
---

# Task 302: pgAdmin admin login hardening

## Objective
1. Change pgAdmin default credentials in docker-compose from `admin@trent.local / admin` to require real env vars
2. Add PGADMIN_EMAIL and PGADMIN_PASSWORD to .env / .env.example with clear comments
3. Add validation in trent_server_status: warn if PGADMIN_PASSWORD is "admin" (default)

## Acceptance Criteria
- [ ] `.env.example` has PGADMIN_EMAIL + PGADMIN_PASSWORD with comments
- [ ] docker-compose.yml pgadmin block has no hardcoded password fallback (fails-fast if not set)
- [ ] trent_server_status returns a warning key if pgadmin is running with default password
