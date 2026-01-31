"""
RAG Search Tool Plugin

Semantic search across knowledge bases using OpenAI embeddings.
"""
from typing import Optional

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_search"

TOOL_DESCRIPTION = (
    "Search a knowledge base using semantic similarity. "
    "Returns relevant content chunks matching your natural language query. "
    "Searches ALL content types: webpages, documents, PDFs, etc. "
    "Use 'subject' to specify which knowledge base to search (e.g., 'work', 'ai_coding'). "
    "Supports filtering by source_type (webpage/document), chunk_type (text/code/heading/list), "
    "and minimum similarity threshold (0.0-1.0). "
    "Results include similarity scores, source metadata, and URLs."
)

TOOL_PARAMS = {
    "query": "Natural language search query (e.g., 'How do Cursor rules work?')",
    "subject": "Subject/knowledge base to search (e.g., 'work_knowledge', 'ai_coding'). Uses default if not specified.",
    "limit": "Maximum results to return (1-50, default: 5)",
    "source_type": "Filter by source type - 'webpage', 'document' (optional)",
    "source_id": "Filter to specific source ID (optional)",
    "chunk_type": "Filter by type - 'text', 'code', 'heading', 'list' (optional)",
    "min_similarity": "Minimum similarity threshold 0.0-1.0 (default: 0.0)"
}


# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

# Context will be injected by the loader
_db = None
_multi_db = None
_embedding_generator = None
_subject_manager = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _db, _multi_db, _embedding_generator, _subject_manager
    _db = context.get('db')
    _multi_db = context.get('multi_db')
    _embedding_generator = context.get('embedding_generator')
    _subject_manager = context.get('subject_manager')


async def execute(
    query: str,
    subject: Optional[str] = None,
    limit: int = 5,
    source_type: Optional[str] = None,
    source_id: Optional[str] = None,
    chunk_type: Optional[str] = None,
    min_similarity: float = 0.0,
    context: dict = None
) -> dict:
    """
    Search knowledge base using semantic similarity.
    """
    from trent.tools.search import rag_search
    from trent.database.multi_subject import SubjectAwareDBWrapper

    # Use injected context if provided
    db = context.get('db', _db) if context else _db
    multi_db = context.get('multi_db', _multi_db) if context else _multi_db
    embedding_gen = context.get('embedding_generator', _embedding_generator) if context else _embedding_generator
    subject_mgr = context.get('subject_manager', _subject_manager) if context else _subject_manager

    if not multi_db or not embedding_gen:
        return {
            'success': False,
            'error': 'RAG components not available. Check PostgreSQL and OpenAI configuration.'
        }

    # Get subject-specific database wrapper
    subject_db = SubjectAwareDBWrapper(multi_db, subject) if subject else db
    resolved_subject = multi_db.resolve_subject(subject)

    result = await rag_search(
        subject_db, embedding_gen,
        query=query,
        limit=limit,
        source_type=source_type,
        source_id=source_id,
        chunk_type=chunk_type,
        min_similarity=min_similarity
    )

    # Add subject info to result
    if result.get('success'):
        result['subject'] = {
            'id': resolved_subject.id,
            'display_name': resolved_subject.display_name
        }

    return result
