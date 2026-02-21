"""
trent_install_cursor Plugin

Install or upgrade Cursor IDE configuration only.
Does NOT touch .claude/, .agent/, or .trent/.

Installs and UPGRADES (overwrites):
  - .cursor/               Rules, skills, agents, commands, hooks
  - .platform_architecture/ Cross-platform architecture docs
  - agents.md              (merged — trent section updated, user content preserved)
  - CURSOR_SETUP.md, GUARDRAILS.md, index files, mcp.txt, .env.example

Use this when:
  - You want to pull the latest Cursor rules/skills without touching other platforms
  - You are a Cursor-only user
  - You want to refresh only the Cursor config after a trent update

See also:
  trent_install        — All platforms (Cursor + Claude + Gemini + .trent)
  trent_install_claude — Claude Code only
  trent_install_gemini — Google Antigravity / Gemini only
"""
import logging
from pathlib import Path

from ._trent_shared import (
    get_github_token,
    get_github_repo,
    get_os_info,
    resolve_target_path,
    run_install,
    CURSOR_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install_cursor"

TOOL_DESCRIPTION = (
    "Install or upgrade Cursor IDE configuration only (.cursor/, .platform_architecture/, "
    "agents.md, CURSOR_SETUP.md, GUARDRAILS.md, index files). "
    "Always overwrites existing files — safe to run on existing installations. "
    "Does NOT touch .claude/, .agent/, or .trent/ task data. "
    "agents.md is merged (user content preserved). "
    "Use trent_install for a full all-platforms install."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install / upgrade Cursor config into (required)",
    "dry_run": "Preview what would be installed without making changes (default: False)",
}

logger = logging.getLogger(__name__)

_config = None


def setup(context: dict):
    """Called once at plugin load time."""
    global _config
    _config = context.get('config', {})


async def execute(
    target_path: str,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """Install or upgrade Cursor IDE configuration."""
    token = get_github_token()
    repo = get_github_repo()
    original_path = target_path

    try:
        target = resolve_target_path(target_path)
        if not dry_run:
            target.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid target path '{target_path}': {e}",
        }

    logger.info(f"trent_install_cursor: target={target}, repo={repo}, dry={dry_run}")

    result = run_install(
        manifest=CURSOR_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=True,
        dry_run=dry_run,
        original_target_path=original_path,
    )
    result['tool'] = 'trent_install_cursor'
    result['os_info'] = get_os_info()
    return result
