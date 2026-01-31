"""
RAG Set Default Subject Tool Plugin

Set the default knowledge base subject.
"""

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_set_default_subject"

TOOL_DESCRIPTION = (
    "Set the default knowledge base subject. "
    "Operations that don't specify a subject will use this default. "
    "Use rag_list_subjects to see available subjects."
)

TOOL_PARAMS = {
    "subject": "Subject ID or alias to set as default"
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
    subject: str,
    context: dict = None
) -> dict:
    """
    Set the default subject.
    """
    subject_mgr = context.get('subject_manager', _subject_manager) if context else _subject_manager

    if not subject_mgr:
        return {
            'success': False,
            'error': 'Subject manager not available.'
        }

    try:
        # Resolve subject first to validate it exists
        resolved = subject_mgr.get_subject(subject)
        if not resolved:
            available = [s.id for s in subject_mgr.list_subjects()]
            return {
                'success': False,
                'error': f"Subject '{subject}' not found. Available: {available}"
            }

        # Update to set as default
        updated = subject_mgr.update_subject(resolved.id, is_default=True)

        return {
            'success': True,
            'message': f"Set '{resolved.id}' as default subject",
            'subject': {
                'id': updated.id,
                'display_name': updated.display_name,
                'is_default': updated.is_default
            }
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
