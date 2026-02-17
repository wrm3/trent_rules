"""
RAG Create Subject Tool Plugin

Create a new knowledge base subject.
"""
from typing import Optional, List

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_create_subject"

TOOL_DESCRIPTION = (
    "Create a new knowledge base subject (database). "
    "This creates a new PostgreSQL database with the RAG schema. "
    "Use aliases to provide short names for the subject. "
    "Set is_default to make this the default subject for operations."
)

TOOL_PARAMS = {
    "subject_id": "Unique identifier for the subject (snake_case, e.g., 'crypto_trading')",
    "display_name": "Human-readable name (e.g., 'Crypto Trading')",
    "description": "Description of what this knowledge base contains",
    "aliases": "Comma-separated short aliases (e.g., 'crypto,trading,ct')",
    "is_default": "Set as the default subject (true/false)"
}


# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_subject_manager = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _subject_manager
    _subject_manager = context.get('subject_manager')


async def execute(
    subject_id: str,
    display_name: str,
    description: str = "",
    aliases: str = "",
    is_default: bool = False,
    context: dict = None
) -> dict:
    """
    Create a new knowledge base subject.
    """
    subject_mgr = context.get('subject_manager', _subject_manager) if context else _subject_manager

    if not subject_mgr:
        return {
            'success': False,
            'error': 'Subject manager not available.'
        }

    try:
        # Parse aliases
        alias_list = [a.strip() for a in aliases.split(',') if a.strip()] if aliases else []

        # Create the subject
        subject = subject_mgr.create_subject(
            subject_id=subject_id,
            display_name=display_name,
            description=description,
            aliases=alias_list,
            is_default=is_default,
            create_database=True
        )

        return {
            'success': True,
            'message': f"Created subject '{subject_id}'",
            'subject': {
                'id': subject.id,
                'display_name': subject.display_name,
                'description': subject.description,
                'database': subject.database,
                'aliases': subject.aliases,
                'is_default': subject.is_default
            }
        }

    except ValueError as e:
        return {
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'success': False,
            'error': f"Failed to create subject: {e}"
        }
