"""
trent_install Plugin

Install the full trent development environment to a project directory.
Fetches from the GitHub repository and merges into the target project.

Installs:
  - .cursor/    Cursor IDE configuration (rules, skills, agents, commands, hooks)
  - .claude/    Claude Code configuration (rules, skills, agents, commands, hooks)
  - .agent/     Google Antigravity configuration (rules, skills, workflows)
  - .platform_architecture/  Cross-platform architecture documentation
  - .trent/     Task management template (examples, reference, blank root files)
  - Root files: agents.md, CLAUDE.md, CURSOR_SETUP.md, GUARDRAILS.md, index files, etc.

For agents.md and CLAUDE.md: existing user content is preserved via
section-marker merging. All other files are written as-is.

See also:
  trent_rules_update  — update IDE configs only (preserves .trent/ task data)
  trent_plan_reset    — reset .trent/ to blank template (destroys task data!)
"""
import os
import logging
from pathlib import Path

from ._trent_shared import (
    get_github_token,
    get_github_repo,
    get_os_info,
    resolve_target_path,
    run_install,
    FULL_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install"

TOOL_DESCRIPTION = (
    "Install trent development environment to a project directory. "
    "Fetches from GitHub: .cursor, .claude, .agent, .platform_architecture, .trent, "
    "agents.md, CLAUDE.md, GUARDRAILS.md, and index files. "
    "agents.md and CLAUDE.md are merged (user content preserved). "
    "All other files are written as-is (use force_overwrite=True to overwrite existing). "
    "OS-aware: detects Windows Developer Mode for symlink handling. "
    "See trent_rules_update to update IDE configs without touching .trent/ task data."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install trent into (required)",
    "force_overwrite": "Overwrite existing files without merging (default: False)",
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
    force_overwrite: bool = False,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """
    Install trent to a project directory.

    Fetches all items in FULL_MANIFEST from GitHub.
    agents.md / CLAUDE.md: merged (trent section updated, user content preserved).
    All other files: written directly (skip if exists unless force_overwrite=True).
    """
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
            'hint': "On Windows paths like 'G:\\Project', ensure Docker has access to the drive.",
        }

    logger.info(f"trent_install: target={target}, repo={repo}, force={force_overwrite}, dry={dry_run}")

    result = run_install(
        manifest=FULL_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=force_overwrite,
        dry_run=dry_run,
        original_target_path=original_path,
    )
    result['os_info'] = get_os_info()
    result['tool'] = 'trent_install'
    return result
