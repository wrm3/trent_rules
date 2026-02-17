---
description: 'CI/CD pipeline quick reference - points to full skill'
globs:
  - '**/.github/workflows/**'
  - '**/.gitlab-ci.yml'
  - '**/Jenkinsfile'
  - '**/azure-pipelines.yml'
alwaysApply: false
---

# CI/CD Standards

> Quick reference for CI/CD pipelines. Full details in skill.

## Skill Invocation

**Skill**: `cicd-pipelines`

**Triggers**: "CI/CD", "GitHub Actions", "GitLab CI", "Jenkins", "Azure DevOps", "pipeline", "workflow"

## Pipeline Stages (Recommended Order)

1. **Lint/Format** - Code style checks (fastest)
2. **Build** - Compile and package
3. **Unit Tests** - Fast, isolated tests
4. **Integration Tests** - Service interaction tests
5. **Security Scan** - SAST, dependency scanning
6. **Build Artifacts** - Docker images, packages
7. **Deploy Staging** - Non-production deployment
8. **E2E Tests** - Full system tests
9. **Deploy Production** - Production release

## Core Principles

- **Fast Feedback**: Fail fast, run quick checks first
- **Reproducibility**: Same inputs produce same outputs
- **Isolation**: Each job runs in clean environment
- **Security**: Never expose secrets in logs
- **Efficiency**: Maximize caching and parallelization

## Quick Checklist

- [ ] Secrets in platform secret manager (not code)
- [ ] Caching configured for dependencies
- [ ] Matrix builds for multi-platform testing
- [ ] Security scanning in pipeline
- [ ] Rollback plan documented

## Full Documentation

See: `.cursor/skills/cicd-pipelines/`
- Complete GitHub Actions, GitLab CI, Jenkins, Azure DevOps examples
- Deployment strategies (blue-green, canary, rolling)
- Security scanning integration
- Optimization techniques
