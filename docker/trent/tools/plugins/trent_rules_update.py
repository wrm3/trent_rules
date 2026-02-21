"""
trent_rules_update Plugin

Update trent IDE configurations and rules — WITHOUT touching .trent/ task data.

Use this when a new version of trent is released and you want to pull in the
latest rules, skills, agents, and workflows without blowing away your project's
task list, plan, bugs, or phases.

What gets updated:
  - .cursor/    Cursor IDE rules, skills, agents, commands, hooks
  - .claude/    Claude Code rules, skills, agents, commands, hooks
  - .agent/     Google Antigravity rules, skills, workflows
  - .platform_architecture/  Cross-platform architecture docs
  - Root files: agents.md, CLAUDE.md, CURSOR_SETUP.md, GUARDRAILS.md, index files, etc.

What is NEVER touched:
  - .trent/     Your task data, plan, bugs, phases — completely preserved

For agents.md and CLAUDE.md: the trent-managed section (between HTML comment
markers) is updated while all other user content is preserved.
All other files are force-overwritten to ensure you get the latest versions.

See also:
  trent_install       — full first-time install (includes .trent/ template)
  trent_plan_reset    — reset .trent/ to blank template (destroys task data!)
"""
import logging
from pathlib import Path

from ._trent_shared import (
    get_github_token,
    get_github_repo,
    get_os_info,
    resolve_target_path,
    run_install,
    RULES_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_rules_update"

TOOL_DESCRIPTION = (
    "Update trent IDE configurations (rules, skills, agents, workflows) to the latest version. "
    "Downloads and overwrites .cursor, .claude, .agent, .platform_architecture, and root index files. "
    "NEVER modifies .trent/ — your task data, plan, phases, and bugs are always preserved. "
    "agents.md and CLAUDE.md are merged (trent section updated, user customizations preserved). "
    "All other config files are force-overwritten with the latest version from GitHub."
)

TOOL_PARAMS = {
    "target_path": "Target project directory containing the trent installation to update (required)",
    "dry_run": "Preview what would be updated without making changes (default: False)",
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
    """
    Update trent IDE configs to the latest version from GitHub.

    Rules, skills, agents, and workflow files are force-overwritten.
    agents.md / CLAUDE.md are merged (preserving user sections).
    .trent/ is never touched.
    """
    token = get_github_token()
    repo = get_github_repo()
    original_path = target_path

    try:
        target = resolve_target_path(target_path)
        if not target.exists():
            return {
                'success': False,
                'error': f"Target path does not exist: {original_path}",
                'hint': (
                    "Run trent_install first to set up the full trent environment, "
                    "then use trent_rules_update to keep it current."
                ),
            }
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid target path '{target_path}': {e}",
        }

    logger.info(f"trent_rules_update: target={target}, repo={repo}, dry={dry_run}")

    # force_overwrite=True: rules/skills/agents always get the latest version
    result = run_install(
        manifest=RULES_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=True,
        dry_run=dry_run,
        original_target_path=original_path,
    )
    result['os_info'] = get_os_info()
    result['tool'] = 'trent_rules_update'
    result['trent_preserved'] = True
    result['note'] = '.trent/ task data was not modified'
    return result
