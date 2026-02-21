"""
trent_install_claude Plugin

Install or upgrade Claude Code configuration only.
Does NOT touch .cursor/, .agent/, or .trent/.

Installs and UPGRADES (overwrites):
  - .claude/                Rules, skills, agents, commands, hooks
  - .platform_architecture/ Cross-platform architecture docs
  - agents.md               (merged — compatible with both Cursor and Claude Code)
  - CLAUDE.md               (merged — trent section updated, user content preserved)
  - AGENTS_INDEX.md, COMMANDS_INDEX.md, HOOKS_INDEX.md, RULES_INDEX.md,
    SKILLS_INDEX.md, GUARDRAILS.md, .env.example, mcp.txt

NOTE: CURSOR_SETUP.md is intentionally excluded (Cursor-specific).

Use this when:
  - You want to pull the latest Claude rules/skills without touching other platforms
  - You are a Claude Code-only user
  - You want to refresh only the Claude config after a trent update

See also:
  trent_install        — All platforms (Cursor + Claude + Gemini + .trent)
  trent_install_cursor — Cursor IDE only
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
    CLAUDE_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install_claude"

TOOL_DESCRIPTION = (
    "Install or upgrade Claude Code configuration only. "
    "Installs: .claude/, agents.md (merged), CLAUDE.md (merged), AGENTS_INDEX.md, "
    "COMMANDS_INDEX.md, HOOKS_INDEX.md, RULES_INDEX.md, SKILLS_INDEX.md, "
    "GUARDRAILS.md, .env.example, mcp.txt. "
    "Always overwrites existing files — safe to run on existing installations. "
    "Does NOT touch .cursor/, .agent/, or .trent/ task data. "
    "CURSOR_SETUP.md excluded (Cursor-specific). "
    "Use trent_install for a full all-platforms install."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install / upgrade Claude config into (required)",
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
    """Install or upgrade Claude Code configuration."""
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

    logger.info(f"trent_install_claude: target={target}, repo={repo}, dry={dry_run}")

    result = run_install(
        manifest=CLAUDE_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=True,
        dry_run=dry_run,
        original_target_path=original_path,
    )
    result['tool'] = 'trent_install_claude'
    result['os_info'] = get_os_info()
    return result
