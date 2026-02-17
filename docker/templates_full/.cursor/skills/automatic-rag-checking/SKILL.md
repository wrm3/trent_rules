---
name: automatic-rag-checking
description: Automatically check RAG knowledge base for relevant content before answering questions. Uses MCP RAG tools for intelligent content retrieval.
triggers:
  - "check knowledge base"
  - "search stored content"
  - "what do we have on"
  - Automatic on technical questions
dependencies:
  - user-fstrent_mcp_rag_docker (RAG search tools)
version: 2.1.0
---

# Automatic RAG Checking Skill

Intelligently check the RAG knowledge base for relevant stored content before answering questions.

## RAG System Architecture

**MCP Server**: `user-fstrent_mcp_rag_docker` (PostgreSQL + pgvector, Docker)

**Subjects (Knowledge Domains)**:
| Subject ID | Display Name | Aliases | Default |
|------------|--------------|---------|---------|
| `ai_coding` | AI & Coding | ai, coding, programming, dev | ✅ |
| `crypto_trading` | Crypto Trading | crypto, trading, bitcoin, ta | |
| `future_shadows` | Future Shadows | fs, writing, story | |

Custom subjects can be created with `rag_create_subject_tool`.

## Overview

This skill provides automatic knowledge base integration:

1. **Detect Relevant Questions**: Identify when a question might be answered by stored content
2. **Select Subject**: Choose the appropriate knowledge domain to search
3. **Search RAG Database**: Query the vector database for similar content
4. **Blend Responses**: Combine RAG content with general knowledge
5. **Cite Sources**: Properly attribute content to original sources

## Automatic Triggers

### Always Check RAG For:
- Programming and development questions → `ai_coding`
- "How do I..." tutorial-style questions → `ai_coding`
- Framework and tool-specific queries → `ai_coding`
- Questions about previously ingested videos
- Best practices and design patterns
- Trading/crypto questions → `crypto_trading`

### Skip RAG Check For:
- Current project/codebase specific questions
- File editing requests
- Meta/conversational messages
- User explicitly requests "no search"

## Core Workflow

```
User Question
     ↓
┌─────────────────────┐
│ Relevance Detection │
│  Is this a topic    │
│  likely in RAG?     │
└─────────────────────┘
     ↓ Yes
┌─────────────────────┐
│  Subject Selection  │
│  ai_coding? crypto? │
└─────────────────────┘
     ↓
┌─────────────────────┐
│  RAG Search Query   │
│  rag_search_tool()  │
└─────────────────────┘
     ↓
┌─────────────────────┐
│ Evaluate Results    │
│  similarity > 0.6?  │
└─────────────────────┘
     ↓ Yes
┌─────────────────────┐
│  Blend Response     │
│  RAG + General      │
└─────────────────────┘
     ↓
Final Response with Citations
```

## Usage Examples

### Example 1: Automatic Technical Question

**User**: "How do branches work in Git?"

**Skill Actions**:
1. Detect: Git question → Check RAG
2. Subject: `ai_coding` (or alias `ai`)
3. Search: `rag_search_tool(query="How do branches work in Git", subject="ai", limit=5)`
4. Results: Found 3 chunks from "Git Fundamentals" video (similarity 0.82)
5. Respond with citations

**Output**:
```
📺 **From Knowledge Base**: "Git Fundamentals Tutorial"
Subject: AI & Coding
Similarity: 0.82

Based on stored content from this video:
> "Git branches are like parallel universes for your code. When you create 
> a branch, you're making a copy of your project at that moment..."

[Continues with explanation...]
```

### Example 2: No Relevant Content

**User**: "What's the best pizza topping?"

**Skill Actions**:
1. Detect: Food question → Not technical → Skip RAG
2. Answer normally without RAG search

### Example 3: Explicit Search Request

**User**: "Check what we have stored about React hooks"

**Skill Actions**:
1. Detect: Explicit "check stored" request → Must search RAG
2. Subject: `ai_coding`
3. Search: `rag_search_tool(query="React hooks", subject="ai", limit=10)`
4. Report findings even if low similarity

### Example 4: Trading Question

**User**: "What are the best technical analysis patterns for crypto?"

**Skill Actions**:
1. Detect: Crypto trading question → Check RAG
2. Subject: `crypto_trading` (or alias `crypto`)
3. Search: `rag_search_tool(query="technical analysis patterns crypto", subject="crypto", limit=5)`
4. Respond with trading-specific content

## MCP Tool Integration

**Server Name**: `user-fstrent_mcp_rag_docker`

When calling tools, use `CallMcpTool` with:
- `server`: `user-fstrent_mcp_rag_docker`
- `toolName`: the tool name (e.g., `rag_search`)

### Subject Management Tools

```json
// List all available subjects
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_list_subjects",
  "arguments": {}
}

// Get details about a specific subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_get_subject",
  "arguments": {"identifier": "ai_coding"}
}

// Create a new subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_create_subject",
  "arguments": {
    "subject_id": "my_project",
    "display_name": "My Project",
    "description": "Project-specific knowledge"
  }
}

// Set default subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_set_default_subject",
  "arguments": {"subject_id": "ai_coding"}
}
```

### Search Tools

```json
// Search the knowledge base (specify subject)
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_search",
  "arguments": {
    "query": "your search query",
    "subject": "ai",           // Subject ID or alias
    "limit": 5,                 // Number of results
    "min_similarity": 0.6       // Minimum similarity threshold
  }
}

// List available sources in a subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_list_sources",
  "arguments": {
    "subject": "ai",
    "limit": 20,
    "source_type": "webpage"    // Filter by type
  }
}

// Get statistics for a subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_stats",
  "arguments": {"subject": "ai"}
}
```

### Ingestion Tools

```json
// Ingest webpage content into a subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_ingest_url",
  "arguments": {
    "url": "https://example.com/article",
    "content": "<scraped content>",
    "subject": "ai"
  }
}

// Ingest text/documents into a subject
{
  "server": "user-fstrent_mcp_rag_docker",
  "toolName": "rag_ingest_text",
  "arguments": {
    "content": "Your text content here",
    "title": "Document Title",
    "subject": "ai",
    "source_type": "document"
  }
}
```

### Search Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| query | (required) | Natural language search query |
| subject | ai_coding | Subject ID or alias to search |
| limit | 5 | Maximum results to return |
| min_similarity | 0.6 | Minimum similarity score (0.0-1.0) |
| source_type | null | Filter by source type (webpage/document) |
| chunk_type | null | Filter by chunk type (text/code/heading) |

## Response Formatting

### When RAG Content Found

```markdown
📚 **From Knowledge Base**: [Source Title]
- Subject: AI & Coding
- Source Type: Webpage / Document
- Similarity: X.XX

> [Relevant quote or summary from stored content]

Based on this stored content, [explanation...]

Additionally, [supplementary information from general knowledge]
```

### When No Content Found

Simply answer normally without mentioning the search:
- Don't apologize for empty results
- Proceed with general knowledge
- Optionally suggest ingesting relevant content

### When Multiple Sources Match

```markdown
📚 **Found in Knowledge Base** (3 sources):

1. **[Source 1 Title]** (0.85 similarity)
   > [Key excerpt]

2. **[Source 2 Title]** (0.78 similarity)
   > [Key excerpt]

Synthesizing from these sources:
[Combined explanation...]
```

## Configuration

### Subject Selection by Topic

```yaml
ai_coding:  # Use for these topics
  - programming, coding, development
  - git, github, version control
  - api, database, cloud, devops
  - frameworks (react, flask, etc.)
  - tutorials, how-to guides
  - claude, anthropic, openai, AI tools

crypto_trading:  # Use for these topics
  - trading, crypto, cryptocurrency
  - bitcoin, ethereum, altcoins
  - technical analysis, charts
  - trading bots, algorithms

future_shadows:  # Use for these topics
  - writing, story, novel
  - fiction, creative writing
```

### Similarity Thresholds

```yaml
thresholds:
  high_confidence: 0.8    # Very relevant, quote directly
  good_match: 0.65        # Good match, synthesize
  possible_match: 0.5     # Might be relevant, mention cautiously
  no_match: < 0.5         # Skip, don't cite
```

## Best Practices

### Do's
- ✅ Cite sources when using RAG content
- ✅ Specify the correct subject for searches
- ✅ Blend RAG content with general knowledge
- ✅ Be transparent about source quality (similarity scores)
- ✅ Update stored content if obviously outdated
- ✅ Suggest ingesting new content when gaps found

### Don'ts
- ❌ Don't over-rely on RAG content alone
- ❌ Don't cite low-similarity matches as authoritative
- ❌ Don't apologize excessively for empty results
- ❌ Don't mention RAG search when skipping it
- ❌ Don't search the wrong subject for a topic

## Adding New Content

When user asks about a topic with no RAG content:
```
"I don't have specific stored content on [topic] in the AI & Coding knowledge base. 
Would you like me to find and ingest relevant content on this?"
```

Use the `rag_ingest_text` or `rag_ingest_url` tools to add new content to the appropriate subject.

## Troubleshooting

### No Results When Expected

1. Check if content was actually ingested:
   ```json
   {
     "server": "user-fstrent_mcp_rag_docker",
     "toolName": "rag_list_sources",
     "arguments": {"subject": "ai"}
   }
   ```

2. Verify correct subject:
   ```json
   {
     "server": "user-fstrent_mcp_rag_docker",
     "toolName": "rag_list_subjects",
     "arguments": {}
   }
   ```

3. Lower similarity threshold:
   ```json
   {
     "server": "user-fstrent_mcp_rag_docker",
     "toolName": "rag_search",
     "arguments": {
       "query": "...",
       "subject": "ai",
       "min_similarity": 0.4
     }
   }
   ```

4. Try different query formulation

### Results Don't Match Question

- The embedding model captures semantic meaning
- Try rephrasing query to match how content might be described
- Use specific technical terms from the original content
- Ensure you're searching the correct subject

### Wrong Subject

- List subjects: Use `rag_list_subjects` tool
- Check aliases: ai = ai_coding, crypto = crypto_trading, fs = future_shadows
- Use correct subject parameter in search

## Future Enhancements

- [ ] Query caching for common questions
- [ ] Automatic subject detection
- [ ] Cross-subject search
- [ ] Image/diagram search
- [ ] Voice query support

---

**Version**: 2.1.0
**Updated**: 2026-01-30
**Dependencies**: user-fstrent_mcp_rag_docker
