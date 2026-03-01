"""
memory_sessions — list recent agent sessions for a project.
"""
import logging
from typing import Optional

from ._agent_memory_shared import init

logger = logging.getLogger(__name__)

TOOL_NAME = "memory_sessions"
TOOL_DESCRIPTION = (
    "List recent agent sessions for a project. "
    "Use to review what was worked on recently across all IDE platforms."
)
TOOL_PARAMS = {
    "project_id": "Project UUID from .trent/.project_id (required)",
    "limit":      "Max sessions to return (1-50, default: 20)",
    "platform":   "Filter by platform: 'cursor' | 'claude_code' | 'antigravity' | 'vscode' (optional)",
}


def setup(context: dict):
    init(context)


def execute(
    project_id: str,
    limit: int = 20,
    platform: Optional[str] = None,
) -> dict:
    from ._agent_memory_shared import _db
    if not _db:
        return {"success": False, "error": "Database not available"}

    limit = max(1, min(limit, 50))
    sql = """
        SELECT
            s.id, s.conversation_id, s.platform, s.capture_tier,
            s.status, s.loop_count, s.session_summary,
            s.ended_at, s.created_at,
            COUNT(t.id) AS turn_count,
            COUNT(c.id) AS capture_count
        FROM agent_sessions s
        JOIN agent_projects p ON p.id = s.project_id
        LEFT JOIN agent_turns t ON t.session_id = s.id
        LEFT JOIN agent_memory_captures c ON c.session_id = s.id
        WHERE p.project_id = %s
    """
    params: list = [project_id]
    if platform:
        sql += " AND s.platform = %s"; params.append(platform)
    sql += " GROUP BY s.id ORDER BY s.ended_at DESC NULLS LAST LIMIT %s"
    params.append(limit)

    sessions = []
    with _db.get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            for row in cur.fetchall():
                sessions.append({
                    "session_id":    row[0],
                    "conversation_id": row[1],
                    "platform":      row[2],
                    "capture_tier":  row[3],
                    "status":        row[4],
                    "loop_count":    row[5],
                    "summary":       row[6],
                    "ended_at":      str(row[7]),
                    "created_at":    str(row[8]),
                    "turn_count":    row[9],
                    "capture_count": row[10],
                })

    return {
        "success": True,
        "project_id": project_id,
        "sessions": sessions,
        "total": len(sessions),
    }
