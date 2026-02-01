---
description: 'Kubernetes quick reference - points to full skill'
globs:
  - '**/k8s/**'
  - '**/helm/**'
  - '**/charts/**'
alwaysApply: false
---

# Kubernetes Standards

> Quick reference for Kubernetes operations. Full details in skill.

## Skill Invocation

**Skill**: `kubernetes-operations`

**Triggers**: "Kubernetes", "k8s", "kubectl", "Helm", "pods", "deployment", "ingress"

## Deployment Essentials

```yaml
# Always include in Deployments:
resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

## Security Defaults

```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
```

## Quick kubectl Commands

```bash
kubectl get pods -n <ns> -o wide      # List pods
kubectl describe pod <name> -n <ns>   # Debug pod
kubectl logs -f <pod> -n <ns>         # Follow logs
kubectl rollout status deploy/<name>  # Check rollout
```

## Quick Checklist

- [ ] Resource requests AND limits set
- [ ] Liveness and readiness probes configured
- [ ] Security context (non-root, read-only)
- [ ] Pod disruption budgets for HA
- [ ] Network policies for isolation

## Full Documentation

See: `.cursor/skills/kubernetes-operations/`
- Complete manifest examples
- Helm chart development
- Troubleshooting guides
- Security best practices
