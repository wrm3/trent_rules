# Agents Index

> Quick reference for all available AI agents in this system.
> 
> **Location**: `.cursor/agents/`
> **Usage**: Agents are invoked via the Task tool with `subagent_type` parameter.

---

## Development Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `frontend-developer` | React, TypeScript, UI components, responsive design | ❌ |
| `backend-developer` | API design, server logic, database integration | ❌ |
| `full-stack-developer` | End-to-end implementation across entire stack | ❌ |
| `database-expert` | Schema design, query optimization, migrations | ✅ hanx-database-tools |
| `api-designer` | REST/GraphQL API design, versioning, documentation | ❌ |

## AI/ML Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `ai-model-trainer` | Training, fine-tuning, RLHF, research integration | ✅ ai-ml-development |
| `ai-model-developer` | Tool integration, multi-modal, memory, production | ✅ ai-ml-development |
| `mlops-engineer` | Model hosting, HuggingFace, deployment, inference | ✅ ai-ml-development |

## DevOps & Infrastructure Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `devops-engineer` | CI/CD, infrastructure as code, deployment | ✅ cicd-pipelines |
| `docker-specialist` | Containerization, Docker Compose, optimization | ❌ |
| `kubernetes-specialist` | K8s cluster management, Helm, orchestration | ✅ kubernetes-operations |
| `portainer-specialist` | Container management UI, stack deployments | ✅ portainer-management |
| `cicd-specialist` | GitHub Actions, GitLab CI, Jenkins, Azure DevOps | ✅ cicd-pipelines |
| `cloud-engineer` | AWS/GCP/Azure, Terraform, cost optimization | ✅ cloud-engineering |
| `solution-architect` | System architecture, tech selection, scalability | ❌ |
| `security-auditor` | Vulnerability assessment, compliance, audits | ❌ |

## Quality & Testing Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `test-runner` | Run tests, diagnose failures, fix them | ❌ |
| `qa-engineer` | Test planning, quality metrics, coverage | ❌ |
| `code-reviewer` | Code quality, security, best practices | ✅ trent-code-reviewer |
| `debugger` | Error diagnosis, stack traces, root cause | ❌ |

## Business & Startup Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `startup-formation-specialist` | Business entity formation, structuring (USA) | ✅ startup-business-formation |
| `startup-operations-specialist` | Running startups, hiring, compliance, growth | ✅ startup-product-development |
| `fundraising-specialist` | VC fundraising, pitch decks, investor relations | ✅ startup-vc-fundraising |
| `nonprofit-specialist` | 501(c)(3), 501(c)(4), churches, PACs | ✅ nonprofit-formation |
| `patent-specialist` | Patent filing, claims, prior art, USPTO | ✅ patent-filing-ai |

## HR & Finance Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `hr-specialist` | Hiring, onboarding, employee relations, policies | ✅ business-operations |
| `compensation-benefits-specialist` | Salary, equity, benefits packages | ✅ business-operations |
| `accounting-finance-specialist` | Bookkeeping, financial statements, taxes | ✅ business-operations |

## Marketing & Content Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `sales-marketing-specialist` | Sales strategy, marketing campaigns, growth | ✅ social-media-marketing |
| `social-media-influencer` | Content strategy, platform growth, engagement | ✅ social-media-marketing |
| `video-producer` | YouTube, short-form video, editing, thumbnails | ✅ social-media-marketing |
| `linkedin-specialist` | Professional networking, B2B content | ✅ social-media-marketing |

## Blockchain & Web3 Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `web3-blockchain-developer` | Solidity, Solana, Cosmos, Bitcoin, DeFi, NFTs | ✅ web3-blockchain |

## Documentation & Utility Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `technical-writer` | API docs, README, code comments, user guides | ❌ |
| `cursor-cli` | Cursor CLI vs IDE orchestration | ❌ |
| `orchestrator` | Multi-agent coordination for parallel work | ❌ |

## Trent System Agents

| Agent | Description | Has Skill? |
|-------|-------------|------------|
| `trent-project-initializer` | Set up Trent task management in new projects | ✅ trent-task-management |
| `trent-task-expander` | Task complexity assessment, sub-task breakdown | ✅ trent-task-management |

---

## Agent Count Summary

- **Total Agents**: 38
- **With Skills**: 24 (63%)
- **Without Skills**: 14 (37% - intentionally generic)

## How to Use Agents

```python
# Via Task tool
Task(
    subagent_type="backend-developer",
    prompt="Design a REST API for user authentication",
    description="Design auth API"
)

# Parallel agents
Task(subagent_type="frontend-developer", prompt="...", description="...")
Task(subagent_type="backend-developer", prompt="...", description="...")
```

---

*Last updated: 2026-02-01*
