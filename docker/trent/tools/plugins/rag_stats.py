"""
RAG Stats Tool Plugin

Get statistics about a knowledge base.
"""
from typing import Optional

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_stats"

TOOL_DESCRIPTION = (
    "Get statistics about a RAG knowledge base. "
    "Shows total sources, chunks, embeddings, and breakdowns by type. "
    "Use 'subject' to specify which knowledge base to analyze."
)

TOOL_PARAMS = {
    "subject": "Subject/knowledge base to analyze (optional, uses default)"
}


# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_multi_db = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _multi_db
    _multi_db = context.get('multi_db')


async def execute(
    subject: Optional[str] = None,
    context: dict = None
) -> dict:
    """
    Get knowledge base statistics.
    """
    from trent.database.multi_subject import SubjectAwareDBWrapper

    multi_db = context.get('multi_db', _multi_db) if context else _multi_db

    if not multi_db:
        return {
            'success': False,
            'error': 'RAG components not available. Check PostgreSQL configuration.'
        }

    subject_db = SubjectAwareDBWrapper(multi_db, subject)
    resolved_subject = multi_db.resolve_subject(subject)

    try:
        # Get source counts by type
        type_counts = subject_db.execute_query("""
            SELECT source_type, COUNT(*) as count
            FROM sources
            GROUP BY source_type
            ORDER BY count DESC
        """)

        # Get total stats
        totals = subject_db.execute_one("""
            SELECT
                COUNT(DISTINCT s.id) as total_sources,
                COUNT(c.id) as total_chunks,
                COUNT(c.id) FILTER (WHERE c.embedding IS NOT NULL) as embedded_chunks,
                SUM(c.word_count) as total_words
            FROM sources s
            LEFT JOIN content_chunks c ON s.id = c.source_id
        """)

        # Get status breakdown
        status_counts = subject_db.execute_query("""
            SELECT status, COUNT(*) as count
            FROM sources
            GROUP BY status
        """)

        # Get chunk type breakdown
        chunk_type_counts = subject_db.execute_query("""
            SELECT chunk_type, COUNT(*) as count
            FROM content_chunks
            GROUP BY chunk_type
            ORDER BY count DESC
        """)

        return {
            'success': True,
            'subject': {
                'id': resolved_subject.id,
                'display_name': resolved_subject.display_name,
                'database': resolved_subject.database
            },
            'totals': {
                'sources': totals['total_sources'] or 0,
                'chunks': totals['total_chunks'] or 0,
                'embedded_chunks': totals['embedded_chunks'] or 0,
                'total_words': totals['total_words'] or 0
            },
            'by_source_type': {row['source_type']: row['count'] for row in type_counts},
            'by_status': {row['status']: row['count'] for row in status_counts},
            'by_chunk_type': {row['chunk_type']: row['count'] for row in chunk_type_counts}
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
