---
name: rag-mcp-server
description: Multi-subject RAG knowledge base via MCP tools. Semantic search over PostgreSQL/pgvector. Use to store and retrieve project knowledge, research notes, code patterns, and documentation.
triggers:
  - "search the knowledge base"
  - "find in RAG"
  - "save this to the knowledge base"
  - "store this information"
  - "what do we know about"
  - "remember this"
  - "add to knowledge"
version: 1.0.0
---

# RAG MCP Server Skill

Access your multi-subject knowledge base through MCP tools for semantic search and content ingestion.

## Overview

This skill provides AI-powered knowledge management through:

1. **Semantic Search**: Find relevant content using natural language queries
2. **Multi-Subject Organization**: Separate knowledge domains (ai_coding, work_knowledge, etc.)
3. **Content Ingestion**: Store URLs, text, and documentation for future retrieval
4. **Persistent Storage**: PostgreSQL with pgvector for production-ready storage

## When to Use This Skill

### Automatic Triggers
- User asks "what do we know about X?"
- User wants to "save this to the knowledge base"
- User requests "search for patterns about Y"
- User mentions "remember this for later"

### Proactive Use Cases
- **Before implementing a feature**: Search for existing patterns or prior decisions
- **After learning something useful**: Store it for future reference
- **During research sessions**: Store and retrieve findings

## Available MCP Tools

### Search Tools
| Tool | Description |
|------|-------------|
| `rag_search` | Semantic search using natural language queries |
| `rag_list_sources` | Browse the content catalog |
| `rag_get_source` | Get full source details |
| `rag_stats` | Knowledge base statistics |

### Ingestion Tools
| Tool | Description |
|------|-------------|
| `rag_ingest_url` | Store webpage content (use with web_scrape_url first) |
| `rag_ingest_text` | Store any text content with metadata |

### Subject Management
| Tool | Description |
|------|-------------|
| `rag_list_subjects` | List all available knowledge domains |
| `rag_get_subject` | Get details about a specific subject |
| `rag_create_subject` | Create a new subject with its own database |
| `rag_set_default_subject` | Change the default subject |

### Server Tools
| Tool | Description |
|------|-------------|
| `rag_server_status` | Health check and server info |

## MCP Server Details

**Server Name**: `user-fstrent_mcp_rag_docker`
**Endpoint**: `http://127.0.0.1:8082/mcp`

When calling tools, use `CallMcpTool` with:
- `server`: `user-fstrent_mcp_rag_docker`
- `toolName`: the tool name (e.g., `rag_search`)

## Workflow Examples

### Example 1: Search Before Implementing

**User**: "How should I handle authentication in this project?"

**AI Actions** (using CallMcpTool):
```json
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_search",
  "arguments": {
    "query": "authentication implementation patterns",
    "subject": "ai_coding"
  }
}
```

### Example 2: Store Useful Information

**User**: "Remember this pattern for handling database connections"

**AI Actions**:
```json
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_ingest_text",
  "arguments": {
    "content": "[the pattern explanation]",
    "title": "Database Connection Pattern",
    "source_type": "pattern",
    "subject": "ai_coding",
    "metadata": {"category": "database", "language": "python"}
  }
}
```

### Example 3: Research and Store Web Content

**User**: "Search for best practices on Docker and save them"

**AI Actions**:
1. Use web search to find articles
2. Use `web_scrape_url` to extract content
3. Store using `rag_ingest_url`

## Subject Organization

| Subject | Alias | Description |
|---------|-------|-------------|
| `work_knowledge` | `work` | Work-related documentation, processes, standards |
| `ai_coding` | `ai`, `coding` | AI/ML patterns, coding tutorials, development docs |

## Search Best Practices

### Query Formulation

**Good Queries:**
- "How do we handle database connection pooling in Python?"
- "What's our authentication strategy for REST APIs?"
- "Error handling patterns for async operations"

**Less Effective:**
- Single words: "database"
- Too broad: "how to code"

### Relevance Thresholds

| Score | Meaning |
|-------|---------|
| 0.8+ | Highly relevant, near-exact match |
| 0.6-0.8 | Relevant, strong semantic match |
| 0.4-0.6 | Possibly relevant, moderate match |
| <0.4 | Weak match, may not be useful |

## Ingestion Best Practices

### What to Store

**Good candidates:**
- Architectural decisions and rationale
- Code patterns that work well
- Troubleshooting solutions
- Project-specific standards
- Research findings and summaries

**Skip:**
- Volatile data that changes frequently
- Large raw datasets
- Sensitive credentials or secrets

### Metadata for Better Search

```
rag_ingest_text(
  content="[your content]",
  title="Descriptive Title",
  source_type="pattern|tutorial|decision|documentation|research",
  subject="ai_coding",
  metadata={
    "category": "database|api|frontend|devops",
    "language": "python|javascript|sql"
  }
)
```

## Configuration

- **MCP Endpoint**: http://127.0.0.1:8082/mcp
- **Default Subject**: work_knowledge
- **Admin Dashboard**: http://localhost:8083

---

**Version**: 1.0.0
**Created**: 2026-01-27
