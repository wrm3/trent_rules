"""
memory_setup_user — MCP tool
Creates ~/.trent/user_config.json for cross-platform user identity.

machine_id is a generated UUID stored in ~/.trent/machine_id.
No OS-native APIs used — works identically on Windows, macOS, Linux,
and inside shared Docker containers.

Usage:
    memory_setup_user(display_name="FSTrent", user_id="usr_fstrent")
    memory_whoami()
"""

import json
import platform
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

TOOL_NAME = "memory_setup_user"
TOOL_DESCRIPTION = (
    "Create or update ~/.trent/user_config.json for memory identity tracking. "
    "Generates a stable machine_id (random UUID, stored in ~/.trent/machine_id) "
    "that works across Windows, macOS, Linux, and shared Docker containers. "
    "Also provides memory_whoami() to read the current user config. "
    "Call this once per machine when setting up trent. "
    "Teammates each call it on their own machine with their own user_id."
)
TOOL_PARAMS = {
    "type": "object",
    "properties": {
        "action": {
            "type": "string",
            "description": "Action to perform: 'setup' (create/update config) or 'whoami' (read current config).",
            "enum": ["setup", "whoami"],
            "default": "whoami",
        },
        "user_id": {
            "type": "string",
            "description": (
                "Your personal user ID. Use a consistent short slug like 'usr_alice' or 'usr_fstrent'. "
                "Required for action='setup'."
            ),
        },
        "display_name": {
            "type": "string",
            "description": "Human-readable name shown in memory search results (e.g. 'FSTrent', 'Alice'). Required for action='setup'.",
        },
    },
    "required": ["action"],
}


def _trent_user_dir() -> Path:
    """Returns ~/.trent/ resolved on any platform."""
    return Path.home() / ".trent"


def _machine_id_path() -> Path:
    return _trent_user_dir() / "machine_id"


def _user_config_path() -> Path:
    return _trent_user_dir() / "user_config.json"


def _get_or_create_machine_id() -> str:
    """
    Read machine_id from ~/.trent/machine_id.
    If the file doesn't exist, generate a UUID4 and save it.
    This is intentionally simple — no OS-native APIs, works everywhere.
    """
    mid_path = _machine_id_path()
    if mid_path.exists():
        mid = mid_path.read_text(encoding="utf-8").strip()
        if mid:
            return mid
    # Generate and persist
    mid = str(uuid.uuid4())
    mid_path.parent.mkdir(parents=True, exist_ok=True)
    mid_path.write_text(mid, encoding="utf-8")
    return mid


def _detect_platform() -> str:
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "macos"
    elif system == "linux":
        return "linux"
    return system or "unknown"


async def execute(
    action: str = "whoami",
    user_id: Optional[str] = None,
    display_name: Optional[str] = None,
) -> dict[str, Any]:

    config_path = _user_config_path()

    # ── whoami ────────────────────────────────────────────────────────────────
    if action == "whoami":
        if not config_path.exists():
            return {
                "configured": False,
                "message": (
                    "No user config found at ~/.trent/user_config.json. "
                    "Run memory_setup_user(action='setup', user_id='usr_yourname', display_name='Your Name') "
                    "to create it."
                ),
                "config_path": str(config_path),
            }
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
            return {
                "configured": True,
                "config_path": str(config_path),
                **config,
            }
        except Exception as e:
            return {"configured": False, "error": f"Could not read config: {e}"}

    # ── setup ─────────────────────────────────────────────────────────────────
    if action == "setup":
        if not user_id:
            return {
                "success": False,
                "error": "user_id is required for action='setup'. Example: usr_fstrent",
            }
        if not display_name:
            return {
                "success": False,
                "error": "display_name is required for action='setup'. Example: FSTrent",
            }

        # Validate user_id format (no spaces, reasonable length)
        if " " in user_id or len(user_id) > 64:
            return {
                "success": False,
                "error": "user_id must have no spaces and be ≤64 characters. Example: usr_fstrent",
            }

        machine_id = _get_or_create_machine_id()
        now = datetime.now(timezone.utc).isoformat()

        # Preserve created_at if updating existing config
        existing_created_at = now
        if config_path.exists():
            try:
                existing = json.loads(config_path.read_text(encoding="utf-8"))
                existing_created_at = existing.get("created_at", now)
            except Exception:
                pass

        config = {
            "user_id": user_id,
            "display_name": display_name,
            "machine_id": machine_id,
            "platform": _detect_platform(),
            "created_at": existing_created_at,
            "updated_at": now,
        }

        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        return {
            "success": True,
            "message": f"User config created at {config_path}",
            "config_path": str(config_path),
            "user_id": user_id,
            "display_name": display_name,
            "machine_id": machine_id,
            "platform": config["platform"],
            "tip": (
                "Pass user_id and machine_id to memory_ingest_session / "
                "memory_capture_session to tag your sessions with your identity."
            ),
        }

    return {"success": False, "error": f"Unknown action '{action}'. Use 'setup' or 'whoami'."}
