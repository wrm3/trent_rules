"""
RAG List Sources Tool Plugin

List all content sources in a knowledge base.
"""
from typing import Optional

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_list_sources"

TOOL_DESCRIPTION = (
    "List all content sources in a RAG knowledge base. "
    "Shows titles, types, chunk counts, and timestamps. "
    "Use 'subject' to specify which knowledge base to browse. "
    "Filter by source_type (webpage, document) or status (completed, failed)."
)

TOOL_PARAMS = {
    "subject": "Subject/knowledge base to browse (optional, uses default)",
    "source_type": "Filter by source type - 'webpage', 'document' (optional)",
    "status": "Filter by status - 'completed', 'failed', 'pending' (optional)",
    "limit": "Maximum sources to return (default: 50)",
    "offset": "Number of sources to skip for pagination (default: 0)"
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
    source_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    context: dict = None
) -> dict:
    """
    List content sources in knowledge base.
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
        sql = """
            SELECT
                s.id::text,
                s.source_type,
                s.source_id,
                s.title,
                s.author,
                s.url,
                s.status,
                s.created_at,
                COUNT(c.id) as chunk_count,
                COUNT(c.id) FILTER (WHERE c.embedding IS NOT NULL) as embedded_count
            FROM sources s
            LEFT JOIN content_chunks c ON s.id = c.source_id
            WHERE 1=1
        """
        params = []

        if source_type:
            sql += " AND s.source_type = %s"
            params.append(source_type.lower())

        if status:
            sql += " AND s.status = %s"
            params.append(status.lower())

        sql += """
            GROUP BY s.id
            ORDER BY s.created_at DESC
            LIMIT %s OFFSET %s
        """
        params.extend([limit, offset])

        with subject_db.get_cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()

        sources = []
        for row in rows:
            sources.append({
                'id': row['id'],
                'source_type': row['source_type'],
                'source_id': row['source_id'],
                'title': row['title'],
                'author': row['author'],
                'url': row['url'],
                'status': row['status'],
                'created_at': row['created_at'].isoformat() if row['created_at'] else None,
                'chunk_count': row['chunk_count'],
                'embedded_count': row['embedded_count']
            })

        return {
            'success': True,
            'subject': {
                'id': resolved_subject.id,
                'display_name': resolved_subject.display_name
            },
            'source_count': len(sources),
            'sources': sources,
            'pagination': {
                'limit': limit,
                'offset': offset
            }
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
