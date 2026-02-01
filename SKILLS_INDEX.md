# Skills Index

> Quick reference for all available AI skills in this system.
> 
> **Location**: `.cursor/skills/`
> **Usage**: Skills are automatically activated by triggers or can be explicitly read.

---

## AI/ML Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `ai-ml-development` | Training, fine-tuning, RLHF, tool integration, deployment | ai-model-trainer, ai-model-developer, mlops-engineer |

## Blockchain & Web3 Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `web3-blockchain` | Solidity, Solana, Cosmos, Bitcoin, DeFi, NFTs, security | web3-blockchain-developer |

## Business Operations Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `business-operations` | HR, compensation, benefits, accounting, finance | hr-specialist, compensation-benefits, accounting-finance |
| `startup-business-formation` | Entity formation, structuring, legal protection (USA) | startup-formation-specialist |
| `startup-product-development` | Product development lifecycle, MVP, scaling | startup-operations-specialist |
| `startup-vc-fundraising` | VC fundraising, pitch decks, term sheets | fundraising-specialist |
| `startup-resource-access` | Grants, accelerators, cloud credits, resources | - |
| `nonprofit-formation` | 501(c)(3), 501(c)(4), churches, PACs, compliance | nonprofit-specialist |
| `patent-filing-ai` | Patent documentation, claims, USPTO procedures | patent-specialist |

## Cloud & Infrastructure Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `cloud-engineering` | AWS/GCP/Azure, Terraform, cost optimization | cloud-engineer |
| `kubernetes-operations` | K8s management, Helm, cloud-native orchestration | kubernetes-specialist |
| `portainer-management` | Container management UI, stack deployments | portainer-specialist |
| `cicd-pipelines` | GitHub Actions, GitLab CI, Jenkins, Azure DevOps | devops-engineer, cicd-specialist |

## Database Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `hanx-database-tools` | MySQL/Oracle operations, queries, connection management | database-expert |
| `hanx-knowledge-base` | Document ingestion, semantic search, RAG | - |
| `rag-mcp-server` | Multi-subject RAG via MCP, PostgreSQL/pgvector | - |

## Development Tools Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `github-integration` | GitHub workflows, issues, PRs, releases, API | - |
| `atlassian-integration` | Jira, Confluence, Bitbucket, Trello | - |
| `mcp-builder` | Creating MCP servers (Python/Node) | - |
| `web-tools` | Web search, scraping, browser automation | - |
| `computer-use-agent` | Desktop automation via screenshots and vision | - |

## Document Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `document-skills/docx` | Word document creation, editing, tracked changes | - |
| `document-skills/pdf` | PDF manipulation, extraction, forms | - |
| `document-skills/pptx` | PowerPoint creation, editing, layouts | - |
| `document-skills/xlsx` | Excel spreadsheets, formulas, data analysis | - |

## Marketing & Content Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `social-media-marketing` | Content strategy, video production, platform growth | social-media-influencer, video-producer, linkedin-specialist |

## Research Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `deep-research` | Deep research methodology | - |
| `research-methodology` | Systematic research approaches | - |
| `automatic-rag-checking` | Auto-check RAG before answering | - |

## Trent System Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `trent-task-management` | Task lifecycle, status, TASKS.md management | trent-project-initializer, trent-task-expander |
| `trent-planning` | PRD creation, phases, scope validation | - |
| `trent-qa` | Bug tracking, quality assurance, fixes | - |
| `trent-code-reviewer` | Code review following trent standards | code-reviewer |

## Utility Skills

| Skill | Description | Agents |
|-------|-------------|--------|
| `project-setup` | Initialize new projects with proper structure | - |
| `skill-creator` | Guide for creating new skills | - |
| `template-skill` | Template for new skill creation | - |
| `internal-comms` | Internal communications templates | - |
| `artifacts-builder` | Claude.ai HTML artifacts with React/Tailwind | - |
| `hanx-mediawiki` | MediaWiki page management | - |

---

## Skill Count Summary

- **Total Skills**: 36
- **With Agents**: 18 (50%)
- **Utility/Standalone**: 18 (50%)

## How to Use Skills

Skills are activated automatically by triggers in the SKILL.md frontmatter, or can be explicitly referenced:

```markdown
# Automatic (via triggers)
User: "How do I fine-tune a model?"
→ ai-ml-development skill activates

# Explicit reference
"Using the web3-blockchain skill, explain Solidity security"
```

## Skill File Structure

```
.cursor/skills/
├── skill-name/
│   ├── SKILL.md          # Main skill definition
│   ├── reference/        # Reference documents
│   └── templates/        # Code/doc templates
```

---

*Last updated: 2026-02-01*
