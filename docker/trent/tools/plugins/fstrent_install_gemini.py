"""
fstrent_install_gemini Plugin

Install or upgrade Google Antigravity / Gemini configuration only.
Does NOT touch .cursor/, .claude/, or .trent/.

Installs and UPGRADES (overwrites):
  - .agent/     Rules, skills, workflows
  - GEMINI.md   Gemini-specific project context
  - GUARDRAILS.md

Use this when:
  - You want to pull the latest Gemini rules/skills without touching other platforms
  - You are a Gemini Antigravity-only user
  - You want to refresh only the Gemini config after a trent update

See also:
  fstrent_install        — All platforms (Cursor + Claude + Gemini + .trent)
  fstrent_install_cursor — Cursor IDE only
  fstrent_install_claude — Claude Code only
"""
import logging
from pathlib import Path

from ._trent_shared import (
    get_github_token,
    get_github_repo,
    get_os_info,
    resolve_target_path,
    run_install,
    GEMINI_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "fstrent_install_gemini"

TOOL_DESCRIPTION = (
    "Install or upgrade Google Antigravity / Gemini configuration only "
    "(.agent/, GEMINI.md, GUARDRAILS.md). "
    "Always overwrites existing files — safe to run on existing installations. "
    "Does NOT touch .cursor/, .claude/, or .trent/ task data. "
    "Use fstrent_install for a full all-platforms install."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install / upgrade Gemini config into (required)",
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
    """Install or upgrade Google Antigravity / Gemini configuration."""
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

    logger.info(f"fstrent_install_gemini: target={target}, repo={repo}, dry={dry_run}")

    result = run_install(
        manifest=GEMINI_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=True,
        dry_run=dry_run,
        original_target_path=original_path,
    )
    result['tool'] = 'fstrent_install_gemini'
    result['os_info'] = get_os_info()
    return result
