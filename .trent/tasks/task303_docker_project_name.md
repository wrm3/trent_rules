---
id: 303
title: 'Fix docker-compose project name — change from "docker" to "trent_rules"'
type: fix
status: pending
priority: medium
phase: 3
subsystem: infrastructure
blast_radius: low
ai_safe: true
requires_solo_agent: false
dependencies: []
created_date: "2026-03-06"
completed_date: null
rules_version: "5.1.0"
project_context: "Docker Compose defaults the project name to the directory name. Since the compose file lives in docker/, the project name is 'docker' — visible in Portainer, docker ps labels, and network names. Fix by setting the name explicitly."
---

# Task 303: Fix docker compose project name

## Objective
Set explicit `name: trent_rules` at the top of docker-compose.yml so Portainer,
docker ps, and network names show `trent_rules_*` rather than `docker_*`.

## Acceptance Criteria
- [ ] `name: trent_rules` added to top of docker-compose.yml
- [ ] Containers still use explicit `container_name:` values (unchanged)
- [ ] Network becomes `trent_rules_trent_rules_network` or simply `trent_rules_network`
- [ ] Requires `docker compose down && docker compose up -d` to take effect
