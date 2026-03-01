"""
trent_install Plugin

Install or upgrade the full trent development environment to a project directory.
Works for both first-time installs and upgrades of existing installations.

Installs and UPGRADES (overwrites):
  - .cursor/              Cursor IDE configuration
  - .claude/              Claude Code configuration
  - .agent/               Google Antigravity / Gemini configuration
  - .platform_architecture/  Cross-platform architecture docs
  - Root files: agents.md (merged), CLAUDE.md (merged), GUARDRAILS.md,
                GEMINI.md, CURSOR_SETUP.md, index files, etc.

.trent/ handling (special — user task data protected):
  - New files only: blank template files are added if they don't already exist.
  - Existing files: NEVER overwritten — your TASKS.md, PLAN.md, task files, etc.
    are always preserved.
  - Backup: if .trent/ contains user task data, a zip backup is created first
    at .trent_backup_YYYYMMDD_HHMMSS.zip (auto-excluded from git).

agents.md / CLAUDE.md: trent section is updated; all other user content preserved.

See also:
  trent_install_cursor  — Cursor IDE only
  trent_install_claude  — Claude Code only
  trent_install_gemini  — Google Antigravity / Gemini only
  trent_plan_reset        — Reset .trent/ to blank template (destroys task data!)
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
    RULES_MANIFEST,
    TRENT_MANIFEST,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install"

TOOL_DESCRIPTION = (
    "Install or upgrade the full trent development environment to a project directory. "
    "Always overwrites IDE config files (.cursor, .claude, .agent, root files) — "
    "safe to run on existing installations to get the latest rules and skills. "
    ".trent/ task data is NEVER overwritten: only missing template files are added. "
    "If .trent/ contains user task data, a backup zip is created automatically before "
    "writing anything. "
    "agents.md and CLAUDE.md are merged (user content preserved). "
    "Use trent_install_cursor / trent_install_claude / trent_install_gemini "
    "to update a single platform."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install / upgrade trent into (required)",
    "backup_trent": (
        "Create a zip backup of .trent/ before installing if user task data is detected "
        "(default: True). Backup saved as .trent_backup_YYYYMMDD_HHMMSS.zip. "
        "Pass backup_trent=False only if data is already committed/disposable."
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
    backup_trent: bool = True,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """
    Install or upgrade trent to a project directory.

    Phase 1 — IDE configs (RULES_MANIFEST): always overwrite — upgrades rules/skills.
    Phase 2 — .trent template (TRENT_MANIFEST): skip existing files — preserves user data.
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

    logger.info(f"trent_install: target={target}, repo={repo}, dry={dry_run}")

    # ── Backup .trent/ if it contains user task data ──────────────────────────
    backup_result = None
    trent_dir = target / '.trent'

    if backup_trent and not dry_run:
        if trent_dir_has_user_data(trent_dir):
            logger.info("trent_install: user task data detected — creating .trent backup")
            backup_result = backup_trent_dir(trent_dir, target)
            if not backup_result['success']:
                return {
                    'success': False,
                    'tool': 'trent_install',
                    'target_path': original_path,
                    'error': (
                        f"Backup of .trent/ failed: {backup_result['error']}. "
                        "Install aborted. Fix the backup issue or pass backup_trent=False."
                    ),
                    'backup_result': backup_result,
                }

    # ── Phase 1: IDE configs — always overwrite (upgrade) ─────────────────────
    ide_result = run_install(
        manifest=RULES_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=True,
        dry_run=dry_run,
        original_target_path=original_path,
    )

    if not ide_result.get('success'):
        ide_result['tool'] = 'trent_install'
        ide_result['phase'] = 'ide_configs'
        ide_result['backup_result'] = backup_result
        return ide_result

    # ── Phase 2: .trent template — skip existing files ────────────────────────
    trent_result = run_install(
        manifest=TRENT_MANIFEST,
        target=target,
        github_repo=repo,
        github_token=token,
        force_overwrite=False,   # Never overwrite user task data
        dry_run=dry_run,
        original_target_path=original_path,
    )

    # ── Phase 3: Generate .trent/.project_id if not present ──────────────────
    project_id_path = trent_dir / '.project_id'
    project_id_created = False
    if not dry_run and not project_id_path.exists():
        try:
            import uuid as _uuid
            import hashlib as _hashlib
            # Derive a short, stable ID from the project path
            path_hash = _hashlib.sha256(str(target).encode()).hexdigest()[:8]
            project_name = target.name.lower().replace('_', '-').replace(' ', '-')
            # Keep it short and human-readable: proj-<name>-<hash8>
            proj_id = f"proj-{project_name[:20]}-{path_hash}"
            project_id_path.parent.mkdir(parents=True, exist_ok=True)
            project_id_path.write_text(proj_id, encoding='utf-8')
            project_id_created = True
            logger.info(f"trent_install: created .trent/.project_id = {proj_id}")
        except Exception as e:
            logger.warning(f"trent_install: could not create .project_id: {e}")

    # ── Merge results ─────────────────────────────────────────────────────────
    from datetime import datetime
    total_copied = len(ide_result.get('copied_files', [])) + len(trent_result.get('copied_files', []))
    total_skipped = len(ide_result.get('skipped_files', [])) + len(trent_result.get('skipped_files', []))
    total_merged = len(ide_result.get('merged_files', [])) + len(trent_result.get('merged_files', []))
    all_warnings = ide_result.get('warnings', []) + trent_result.get('warnings', [])
    total_time = round(
        ide_result.get('operation_time_seconds', 0) +
        trent_result.get('operation_time_seconds', 0), 2
    )

    backup_summary = ''
    if backup_result and backup_result.get('success') and not backup_result.get('skipped'):
        kb = round(backup_result['backup_size_bytes'] / 1024, 1)
        backup_summary = (
            f" [.trent backup: {backup_result['backup_name']} "
            f"({backup_result['file_count']} files, {kb} KB)]"
        )

    result = {
        'success': True,
        'tool': 'trent_install',
        'target_path': original_path,
        'target_path_resolved': str(target),
        'source': f'github:{repo}',
        'dry_run': dry_run,
        'backup_result': backup_result,
        'ide_phase': {
            'copied': len(ide_result.get('copied_files', [])),
            'skipped': len(ide_result.get('skipped_files', [])),
            'merged': len(ide_result.get('merged_files', [])),
        },
        'trent_phase': {
            'copied': len(trent_result.get('copied_files', [])),
            'skipped': len(trent_result.get('skipped_files', [])),
            'note': 'Existing .trent/ files preserved (not overwritten)',
        },
        'project_id': project_id_path.read_text(encoding='utf-8').strip() if not dry_run and project_id_path.exists() else None,
        'project_id_created': project_id_created,
        'warnings': all_warnings,
        'operation_time_seconds': total_time,
        'message': (
            f"trent_install complete: {total_copied} files installed/upgraded, "
            f"{total_skipped} skipped, {total_merged} merged "
            f"in {total_time}s.{backup_summary}"
        ),
        'os_info': get_os_info(),
    }
    return result
