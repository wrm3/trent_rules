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

Safety features:
  backup_trent=True (default):
    If .trent/ already exists AND contains user task data (task files, phase files,
    or a populated TASKS.md), a zip backup is created as
    .trent_backup_YYYYMMDD_HHMMSS.zip BEFORE any files are written.
    This protects against accidental overwrite when force_overwrite=True is used.
    The backup is excluded from git commits automatically.

See also:
  trent_rules_update  — update IDE configs only (preserves .trent/ task data)
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
    backup_trent_dir,
    trent_dir_has_user_data,
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
    "All other files are written as-is (skipped if they already exist, unless "
    "force_overwrite=True). "
    "SAFETY: If .trent/ already contains task data and backup_trent=True (default), "
    "a zip backup is created before any files are written. "
    "OS-aware: detects Windows Developer Mode for symlink handling. "
    "See trent_rules_update to update IDE configs without touching .trent/ task data."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install trent into (required)",
    "force_overwrite": (
        "Overwrite existing files without merging (default: False). "
        "When True, combined with backup_trent=True, a backup of .trent/ is created "
        "before overwriting if user task data is detected."
    ),
    "backup_trent": (
        "Create a zip backup of .trent/ before installing if user task data is detected "
        "(default: True). "
        "The backup is saved as .trent_backup_YYYYMMDD_HHMMSS.zip in target_path. "
        "Only triggers when .trent/ exists AND contains task files, phase files, "
        "or a populated TASKS.md. "
        "Pass backup_trent=False to skip the backup check (not recommended on "
        "projects with active task data)."
    ),
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
    backup_trent: bool = True,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """
    Install trent to a project directory.

    Fetches all items in FULL_MANIFEST from GitHub.
    agents.md / CLAUDE.md: merged (trent section updated, user content preserved).
    All other files: written directly (skip if exists unless force_overwrite=True).

    If backup_trent=True and .trent/ exists with user data, creates a zip backup
    before writing any files.
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

    logger.info(
        f"trent_install: target={target}, repo={repo}, "
        f"force={force_overwrite}, backup={backup_trent}, dry={dry_run}"
    )

    # ── Backup .trent/ if it contains user data ───────────────────────────────
    backup_result = None
    trent_dir = target / '.trent'

    if backup_trent and not dry_run:
        if trent_dir_has_user_data(trent_dir):
            logger.info("trent_install: user task data detected in .trent/ — creating backup")
            backup_result = backup_trent_dir(trent_dir, target)

            if not backup_result['success']:
                return {
                    'success': False,
                    'tool': 'trent_install',
                    'target_path': original_path,
                    'error': (
                        f"Backup of .trent/ failed: {backup_result['error']}. "
                        "Install aborted to protect your task data. "
                        "Fix the backup issue or pass backup_trent=False to skip "
                        "(not recommended when task data exists)."
                    ),
                    'backup_result': backup_result,
                }

            kb = round(backup_result['backup_size_bytes'] / 1024, 1)
            logger.info(
                f"trent_install: backup created → {backup_result['backup_name']} "
                f"({backup_result['file_count']} files, {kb} KB)"
            )
        else:
            logger.info("trent_install: no user task data in .trent/ — backup skipped")

    # ── Run install ───────────────────────────────────────────────────────────
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
    result['backup_trent_requested'] = backup_trent
    result['backup_result'] = backup_result

    # Append backup info to the success message
    if result.get('success') and backup_result and backup_result.get('success') and not backup_result.get('skipped'):
        kb = round(backup_result['backup_size_bytes'] / 1024, 1)
        result['message'] = (
            f"[Backup created: {backup_result['backup_name']} "
            f"({backup_result['file_count']} files, {kb} KB)] "
            + result.get('message', '')
        )

    return result
