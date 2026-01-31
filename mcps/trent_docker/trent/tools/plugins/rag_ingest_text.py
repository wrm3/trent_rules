"""
RAG Ingest Text Tool Plugin

Ingest raw text content into a knowledge base.
"""
import uuid
from typing import Optional
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_ingest_text"

TOOL_DESCRIPTION = (
    "Ingest raw text content into a RAG knowledge base. "
    "Use 'subject' to specify which knowledge base to store content in. "
    "Use this for PDFs, documents, notes, or any text content. "
    "Content will be chunked and embedded for semantic search. "
    "You can specify source_type to categorize (e.g., 'pdf', 'notes', 'research')."
)

TOOL_PARAMS = {
    "content": "The text content to ingest",
    "title": "Title for this content",
    "subject": "Subject/knowledge base to store in (optional)",
    "source_type": "Type classification - 'document', 'pdf', 'notes', etc. (default: 'document')",
    "author": "Author of the content (optional)",
    "url": "Source URL if applicable (optional)",
    "chunk_size": "Characters per chunk (default: 1000)",
    "chunk_overlap": "Overlap between chunks (default: 200)"
}


# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_multi_db = None
_embedding_generator = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _multi_db, _embedding_generator
    _multi_db = context.get('multi_db')
    _embedding_generator = context.get('embedding_generator')


async def execute(
    content: str,
    title: str,
    subject: Optional[str] = None,
    source_type: str = 'document',
    author: Optional[str] = None,
    url: Optional[str] = None,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    context: dict = None
) -> dict:
    """
    Ingest text content into knowledge base.
    """
    from trent.database.multi_subject import SubjectAwareDBWrapper

    # Use injected context if provided
    multi_db = context.get('multi_db', _multi_db) if context else _multi_db
    embedding_gen = context.get('embedding_generator', _embedding_generator) if context else _embedding_generator

    if not multi_db or not embedding_gen:
        return {
            'success': False,
            'error': 'RAG components not available. Check PostgreSQL and OpenAI configuration.'
        }

    subject_db = SubjectAwareDBWrapper(multi_db, subject)
    resolved_subject = multi_db.resolve_subject(subject)

    try:
        # Generate unique source_id
        source_id = f"{source_type}-{uuid.uuid4().hex[:8]}"
        db_source_id = str(uuid.uuid4())

        # Create source record
        subject_db.execute_one("""
            INSERT INTO sources (id, source_type, source_id, title, author, url, status, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            db_source_id, source_type, source_id, title, author, url, 'processing',
            '{"ingested_via": "rag_ingest_text"}'
        ))

        # Chunk the content
        chunks = _chunk_text(content, chunk_size, chunk_overlap)

        # Insert chunks with embeddings
        chunk_count = 0
        for i, chunk_text in enumerate(chunks):
            chunk_id = str(uuid.uuid4())

            # Generate embedding
            embedding = embedding_gen.generate(chunk_text)

            subject_db.execute_one("""
                INSERT INTO content_chunks
                (id, source_id, chunk_text, chunk_index, chunk_type, embedding, word_count, char_count)
                VALUES (%s, %s, %s, %s, %s, %s::vector, %s, %s)
            """, (
                chunk_id, db_source_id, chunk_text, i, 'text',
                embedding_gen.to_pg_vector(embedding),
                len(chunk_text.split()), len(chunk_text)
            ))
            chunk_count += 1

        # Update source status
        subject_db.execute_one("""
            UPDATE sources SET status = 'completed' WHERE id = %s
        """, (db_source_id,))

        return {
            'success': True,
            'subject': {
                'id': resolved_subject.id,
                'display_name': resolved_subject.display_name
            },
            'source': {
                'id': db_source_id,
                'source_id': source_id,
                'title': title,
                'source_type': source_type
            },
            'chunks_created': chunk_count
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def _chunk_text(text: str, chunk_size: int, overlap: int) -> list:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind('.')
            last_newline = chunk.rfind('\n')
            break_point = max(last_period, last_newline)
            if break_point > chunk_size // 2:
                chunk = chunk[:break_point + 1]
                end = start + break_point + 1

        chunks.append(chunk.strip())
        start = end - overlap

    return [c for c in chunks if c]  # Remove empty chunks
