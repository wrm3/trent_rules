---
description: 'Portainer quick reference - points to full skill'
globs:
  - '**/docker-compose*.yml'
  - '**/docker-compose*.yaml'
  - '**/stacks/**'
  - '**/portainer/**'
alwaysApply: false
---

# Portainer Standards

> Quick reference for Portainer management. Full details in skill.

## Skill Invocation

**Skill**: `portainer-management`

**Triggers**: "Portainer", "container management UI", "deploy stack", "Edge agent"

## Environment Types

- **Docker Standalone**: Single Docker host
- **Docker Swarm**: Swarm cluster orchestration
- **Kubernetes**: K8s cluster integration
- **Edge**: Remote/edge device management

## Stack Naming Convention

Format: `{app}-{environment}` (e.g., `webapp-prod`, `api-staging`)

## Quick API Access

```bash
# Get JWT token
JWT=$(curl -s -X POST "https://portainer:9443/api/auth" \
  -H "Content-Type: application/json" \
  -d '{"Username":"admin","Password":"password"}' | jq -r '.jwt')

# Use token
curl -s -X GET "https://portainer:9443/api/endpoints" \
  -H "Authorization: Bearer $JWT"
```

## Quick Checklist

- [ ] SSL/TLS enabled in production
- [ ] RBAC configured for teams
- [ ] Stack naming convention followed
- [ ] Backup strategy in place
- [ ] Edge agents secured

## Full Documentation

See: `.cursor/skills/portainer-management/`
- Complete stack deployment guides
- API operation examples
- Edge computing setup
- Security configuration
