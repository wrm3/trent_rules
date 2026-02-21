"""
trent_plan_reset Plugin

Reset .trent/ to a blank template by deleting it and re-downloading from GitHub.

USE WITH CAUTION: This permanently deletes all local .trent/ content including:
  - TASKS.md        (your entire task list)
  - PLAN.md         (your PRD / project plan)
  - BUGS.md         (your bug tracking)
  - PROJECT_CONTEXT.md
  - SUBSYSTEMS.md
  - All files in .trent/tasks/   (every task file)
  - All files in .trent/phases/  (every phase file)

After reset, .trent/ contains the blank trent template from the GitHub repo:
  - Blank root files (ready to fill in for a new project)
  - .trent/examples/   (example files for reference)
  - .trent/reference/  (reference documentation)
  - Empty tasks/ and phases/ directories

Safety gate: requires confirm=True to proceed. Call with confirm=False first
to see a summary of what will be deleted before committing.

See also:
  trent_install       — full first-time install
  trent_rules_update  — update IDE configs only (NEVER touches .trent/)
"""
import shutil
import logging
from pathlib import Path

from ._trent_shared import (
    get_github_token,
    get_github_repo,
    get_os_info,
    resolve_target_path,
    fetch_from_github,
)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_plan_reset"

TOOL_DESCRIPTION = (
    "Reset .trent/ task management folder to the blank template by deleting it "
    "and re-downloading from GitHub. "
    "WARNING: Permanently destroys all local task data (TASKS.md, PLAN.md, BUGS.md, "
    "task files, phase files). "
    "Requires confirm=True to actually execute — call with confirm=False first to "
    "preview what will be deleted. "
    "Use this when starting a new project in an existing trent directory, or when "
    "you want to completely reset the task management state."
)

TOOL_PARAMS = {
    "target_path": "Target project directory containing the .trent/ folder to reset (required)",
    "confirm": (
        "Must be True to actually delete and reset. "
        "Pass confirm=False (default) to preview what would be deleted. "
        "REQUIRED explicit opt-in — there is no undo."
    ),
    "dry_run": "Preview GitHub download without writing files (default: False). Only meaningful when confirm=True.",
}

logger = logging.getLogger(__name__)

_config = None


def setup(context: dict):
    """Called once at plugin load time."""
    global _config
    _config = context.get('config', {})


def _inventory_trent(trent_dir: Path) -> dict:
    """
    Build an inventory of .trent/ contents to show in the preview.
    Returns counts and a sample file listing.
    """
    if not trent_dir.exists():
        return {'exists': False, 'total_files': 0, 'files': []}

    all_files = sorted(trent_dir.rglob('*'))
    files = [f for f in all_files if f.is_file() and f.name != '.gitkeep']
    dirs = [f for f in all_files if f.is_dir()]

    # Highlight the critical data files
    critical_files = []
    for name in ['TASKS.md', 'PLAN.md', 'BUGS.md', 'PROJECT_CONTEXT.md',
                 'SUBSYSTEMS.md', 'FILE_REGISTRY.md', 'MCP_TOOLS_INVENTORY.md']:
        fp = trent_dir / name
        if fp.exists():
            critical_files.append(name)

    task_files = list((trent_dir / 'tasks').glob('*.md')) if (trent_dir / 'tasks').exists() else []
    phase_files = list((trent_dir / 'phases').glob('*.md')) if (trent_dir / 'phases').exists() else []
    # Exclude .gitkeep
    task_files = [f for f in task_files if f.name != '.gitkeep']
    phase_files = [f for f in phase_files if f.name != '.gitkeep']

    return {
        'exists': True,
        'total_files': len(files),
        'total_dirs': len(dirs),
        'critical_files': critical_files,
        'task_count': len(task_files),
        'phase_count': len(phase_files),
        'task_files': [f.name for f in task_files[:20]],  # cap sample at 20
        'phase_files': [f.name for f in phase_files],
    }


async def execute(
    target_path: str,
    confirm: bool = False,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """
    Reset .trent/ to blank template.

    If confirm=False: returns a preview of what would be deleted (no changes made).
    If confirm=True:  deletes .trent/, then downloads fresh template from GitHub.
    """
    token = get_github_token()
    repo = get_github_repo()
    original_path = target_path

    try:
        target = resolve_target_path(target_path)
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid target path '{target_path}': {e}",
        }

    trent_dir = target / '.trent'
    inventory = _inventory_trent(trent_dir)

    # ── Preview mode (no confirm) ─────────────────────────────────────────────
    if not confirm:
        if not inventory['exists']:
            return {
                'success': True,
                'tool': 'trent_plan_reset',
                'confirm_required': True,
                'message': (
                    f".trent/ does not exist at {original_path}. "
                    "Pass confirm=True to download the blank template."
                ),
                'inventory': inventory,
                'action': 'none — .trent/ not present',
            }

        return {
            'success': True,
            'tool': 'trent_plan_reset',
            'confirm_required': True,
            'message': (
                f"PREVIEW ONLY — no changes made.\n\n"
                f"Calling trent_plan_reset with confirm=True will:\n"
                f"  1. PERMANENTLY DELETE .trent/ at: {original_path}\n"
                f"  2. Download the blank trent template from GitHub ({repo})\n\n"
                f"The following data will be PERMANENTLY DESTROYED:"
            ),
            'inventory': inventory,
            'warning': (
                "This cannot be undone. Make sure you have committed or backed up "
                "your task data before proceeding."
            ),
            'next_step': "Call trent_plan_reset with confirm=True to proceed.",
        }

    # ── Confirmed execution ───────────────────────────────────────────────────
    from datetime import datetime
    start_time = datetime.now()

    result = {
        'success': False,
        'tool': 'trent_plan_reset',
        'target_path': original_path,
        'target_path_resolved': str(target),
        'source': f'github:{repo}',
        'dry_run': dry_run,
        'pre_reset_inventory': inventory,
        'deleted': False,
        'downloaded_files': [],
        'warnings': [],
        'operation_time_seconds': 0,
    }

    # Step 1: Delete existing .trent/
    if trent_dir.exists() and not dry_run:
        try:
            shutil.rmtree(str(trent_dir))
            result['deleted'] = True
            logger.info(f"trent_plan_reset: deleted {trent_dir}")
        except Exception as e:
            result['error'] = f"Failed to delete .trent/: {e}"
            return result
    elif dry_run and trent_dir.exists():
        result['deleted'] = 'would_delete (dry_run)'
        logger.info(f"trent_plan_reset: dry_run — would delete {trent_dir}")

    # Step 2: Download fresh .trent/ from GitHub
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)

    gh_result = fetch_from_github(
        repo=repo,
        path='.trent',
        target_dir=target,
        token=token,
        overwrite=True,
    )

    if gh_result.get('error'):
        result['error'] = f"Failed to download .trent/ from GitHub: {gh_result['error']}"
        result['warnings'].append(
            "WARNING: .trent/ was deleted but the re-download failed. "
            "Run trent_plan_reset again or trent_install to restore."
        )
        return result

    result['downloaded_files'] = gh_result['files_fetched']
    if gh_result['errors']:
        result['warnings'].extend(gh_result['errors'])

    result['operation_time_seconds'] = round(
        (datetime.now() - start_time).total_seconds(), 2
    )
    result['success'] = True
    result['message'] = (
        f"Successfully reset .trent/ "
        f"({'deleted ' + str(inventory.get('total_files', 0)) + ' files, ' if inventory['exists'] else ''}"
        f"downloaded {len(result['downloaded_files'])} template files) "
        f"in {result['operation_time_seconds']}s"
    )
    result['os_info'] = get_os_info()
    return result
