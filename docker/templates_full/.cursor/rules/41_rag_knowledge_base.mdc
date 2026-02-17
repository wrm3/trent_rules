# RAG Knowledge Base MCP Tools

This project includes an MCP server for semantic search and knowledge storage.

**MCP Server**: `user-fstrent_mcp_rag_docker`

## Available Tools

**Search:**
- `rag_search` - Semantic search with natural language (e.g., "authentication patterns")
- `rag_list_sources` - Browse content catalog
- `rag_stats` - Knowledge base statistics

**Ingest:**
- `rag_ingest_text` - Store text content with metadata
- `rag_ingest_url` - Store web content (use after scraping)

**Subjects:**
- `rag_list_subjects` - List knowledge domains
- `rag_create_subject` - Create new subject/database
- `rag_server_status` - Health check

## When to Use

- **Search first**: Before implementing features, search for existing patterns
- **Store useful info**: Save architectural decisions, patterns, troubleshooting solutions
- **Research sessions**: Store findings from web research for later retrieval

## Subjects

| Subject | Use For |
|---------|---------|
| `work_knowledge` | Work docs, processes, standards (default) |
| `ai_coding` | Technical patterns, tutorials, AI/ML docs |

## Example Usage (CallMcpTool)

```json
// Search
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_search",
  "arguments": {"query": "database connection pooling", "subject": "ai_coding"}
}

// Store
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_ingest_text",
  "arguments": {
    "content": "[content here]",
    "title": "Connection Pool Pattern",
    "source_type": "pattern",
    "subject": "ai_coding"
  }
}
```

## Server Info

- **MCP Server Name**: `user-fstrent_mcp_rag_docker`
- **Endpoint**: http://127.0.0.1:8082/mcp
- **Admin UI**: http://localhost:8083
