"""
RAG List Subjects Tool Plugin

List all available knowledge base subjects.
"""

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "rag_list_subjects"

TOOL_DESCRIPTION = (
    "List all available knowledge base subjects (databases). "
    "Shows subject IDs, display names, descriptions, aliases, and which is default. "
    "Use this to discover available knowledge bases before searching."
)

TOOL_PARAMS = {}


# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_subject_manager = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _subject_manager
    _subject_manager = context.get('subject_manager')


async def execute(
    context: dict = None
) -> dict:
    """
    List all available subjects.
    """
    subject_mgr = context.get('subject_manager', _subject_manager) if context else _subject_manager

    if not subject_mgr:
        return {
            'success': False,
            'error': 'Subject manager not available.'
        }

    try:
        subjects = subject_mgr.list_subjects()
        default_subject = subject_mgr.get_default_subject()

        return {
            'success': True,
            'subject_count': len(subjects),
            'default_subject': default_subject.id if default_subject else None,
            'subjects': [
                {
                    'id': s.id,
                    'display_name': s.display_name,
                    'description': s.description,
                    'database': s.database,
                    'aliases': s.aliases,
                    'is_default': s.is_default
                }
                for s in subjects
            ]
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }
