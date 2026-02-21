"""
Shared utilities for trent_install, trent_rules_update, and trent_plan_reset plugins.

This module is NOT a plugin (underscore prefix prevents auto-loading).
Import it directly in each trent plugin file.
"""
import os
import sys
import logging
import platform
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# ============================================================
# TOKEN AND REPO DEFAULTS
# ============================================================

# Read-only PAT for the public wrm3/trent_rules repo.
# Intentionally committed so trent tools work out-of-the-box
# without requiring the user to configure GITHUB_TOKEN.
# Set GITHUB_TOKEN in your environment to override.
DEFAULT_GITHUB_TOKEN = (
    "github_pat_11AM6DLNA0MOOBKQOuVXCC_"
    "IXXBaacBSQDTR8mrZnQhLH1O1ChHVjKz0P0ftYI4NKBODDI6D3NV2yESrNf"
)

DEFAULT_GITHUB_REPO = "wrm3/trent_rules"


def get_github_token() -> str:
    """Return GitHub token: env var first, bundled default as fallback."""
    return os.environ.get("GITHUB_TOKEN") or DEFAULT_GITHUB_TOKEN


def get_github_repo() -> str:
    """Return GitHub repo slug from env var or default."""
    return os.environ.get("GITHUB_REPO") or DEFAULT_GITHUB_REPO


# ============================================================
# INSTALL MANIFESTS
# ============================================================

# ── Full install — all systems + .trent template ──────────────────────────────
FULL_MANIFEST: List[str] = [
    # IDE Configurations
    '.agent',                   # Google Antigravity / Gemini
    '.platform_architecture',   # Cross-platform architecture docs
    '.claude',                  # Claude Code
    '.cursor',                  # Cursor IDE

    # Root files
    'agents.md',                # Universal agent instructions  (merged)
    'AGENTS_INDEX.md',
    'CLAUDE.md',                # Claude-specific context        (merged)
    'COMMANDS_INDEX.md',
    'CURSOR_SETUP.md',
    'GEMINI.md',
    'GUARDRAILS.md',
    'HOOKS_INDEX.md',
    'RULES_INDEX.md',
    'SKILLS_INDEX.md',
    '.env.example',
    'mcp.txt',

    # .trent/ in this repo IS the template — blank root files, empty tasks/phases,
    # examples/ and reference/ included.  No live task data.
    '.trent',
]

# ── IDE-only manifests (platform-specific installs, never touch .trent/) ──────

# Cursor IDE — rules, skills, agents, commands, hooks + shared root files
CURSOR_MANIFEST: List[str] = [
    '.cursor',
    '.platform_architecture',
    'agents.md',                # merged
    'AGENTS_INDEX.md',
    'COMMANDS_INDEX.md',
    'CURSOR_SETUP.md',
    'GUARDRAILS.md',
    'HOOKS_INDEX.md',
    'RULES_INDEX.md',
    'SKILLS_INDEX.md',
    '.env.example',
    'mcp.txt',
]

# Claude Code — rules, skills, agents, commands, hooks + CLAUDE.md
CLAUDE_MANIFEST: List[str] = [
    '.claude',
    'CLAUDE.md',                # merged
    'GUARDRAILS.md',
]

# Google Antigravity / Gemini — rules, skills, workflows + GEMINI.md
GEMINI_MANIFEST: List[str] = [
    '.agent',
    'GEMINI.md',
    'GUARDRAILS.md',
]

# .trent-only manifest — for plan reset
TRENT_MANIFEST: List[str] = ['.trent']

# Files where user content is preserved via section-marker merging
MERGEABLE_FILES = {'agents.md', 'claude.md'}


# ============================================================
# GITHUB API
# ============================================================

def github_api_request(url: str, token: str) -> Any:
    """Make a single GitHub API GET request and return parsed JSON."""
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    req.add_header('User-Agent', 'trent-tools/3.0')

    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode('utf-8'))


def fetch_from_github(
    repo: str,
    path: str,
    target_dir: Path,
    token: str,
    strip_prefix: Optional[str] = None,
    exclude_prefixes: Optional[List[str]] = None,
    overwrite: bool = True,
) -> Dict[str, Any]:
    """
    Recursively fetch files from a GitHub repository path and write to target_dir.

    Uses the GitHub Contents API:
      GET https://api.github.com/repos/{repo}/contents/{path}

    Args:
        repo:             GitHub repo slug, e.g. "wrm3/trent_rules"
        path:             Path within the repo, e.g. ".cursor" or "AGENTS.md"
        target_dir:       Local directory to write files into
        token:            GitHub personal access token
        strip_prefix:     Optional prefix to strip from entry_path before
                          joining with target_dir (for path remapping).
        exclude_prefixes: Optional list of repo-relative path prefixes to skip.
        overwrite:        If False, skip files that already exist locally.

    Returns:
        {'success': bool, 'files_fetched': [str], 'files_skipped': [str], 'errors': [str], 'error': str|None}
    """
    result: Dict[str, Any] = {
        'success': False,
        'files_fetched': [],
        'files_skipped': [],
        'errors': [],
        'error': None,
    }

    api_path = path.strip('/')
    url = f'https://api.github.com/repos/{repo}/contents/{api_path}'

    try:
        data = github_api_request(url, token)
    except urllib.error.HTTPError as exc:
        result['error'] = f"GitHub API HTTP {exc.code} for {url}: {exc.reason}"
        return result
    except urllib.error.URLError as exc:
        result['error'] = f"GitHub network error for {url}: {exc.reason}"
        return result
    except Exception as exc:
        result['error'] = f"GitHub unexpected error for {url}: {exc}"
        return result

    entries = [data] if isinstance(data, dict) else data

    for entry in entries:
        entry_type = entry.get('type')
        entry_path = entry.get('path', '')
        entry_name = entry.get('name', '')

        # Skip excluded paths
        if exclude_prefixes:
            if any(entry_path == p or entry_path.startswith(p + '/') for p in exclude_prefixes):
                logger.debug(f"Skipping excluded: {entry_path}")
                continue

        # Compute local destination path
        rel_path = entry_path
        if strip_prefix and rel_path.startswith(strip_prefix):
            rel_path = rel_path[len(strip_prefix):].lstrip('/')
        local_target = target_dir / rel_path if rel_path else target_dir / entry_name

        if entry_type == 'dir':
            sub = fetch_from_github(
                repo, entry_path, target_dir, token, strip_prefix, exclude_prefixes, overwrite
            )
            result['files_fetched'].extend(sub['files_fetched'])
            result['files_skipped'].extend(sub['files_skipped'])
            result['errors'].extend(sub['errors'])
            if sub.get('error'):
                result['errors'].append(sub['error'])

        elif entry_type == 'file':
            # Skip existing files if overwrite is disabled
            if not overwrite and local_target.exists():
                result['files_skipped'].append(str(local_target))
                logger.debug(f"Skipped (exists): {local_target}")
                continue

            try:
                encoding = entry.get('encoding', 'base64')
                raw_content = entry.get('content', '')

                if encoding == 'base64' and raw_content:
                    file_bytes = base64.b64decode(raw_content)
                else:
                    download_url = entry.get('download_url')
                    if not download_url:
                        result['errors'].append(f"No download_url for {entry_path}")
                        continue
                    req = urllib.request.Request(download_url)
                    req.add_header('Authorization', f'Bearer {token}')
                    req.add_header('User-Agent', 'trent-tools/3.0')
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        file_bytes = resp.read()

                local_target.parent.mkdir(parents=True, exist_ok=True)
                local_target.write_bytes(file_bytes)
                result['files_fetched'].append(str(local_target))
                logger.debug(f"Fetched: {entry_path} -> {local_target}")

            except Exception as exc:
                msg = f"Failed to write {entry_path}: {exc}"
                logger.warning(msg)
                result['errors'].append(msg)

    result['success'] = True
    return result


# ============================================================
# MARKDOWN MERGE (for agents.md / CLAUDE.md)
# ============================================================

def merge_markdown_file(source_content: str, dest_content: str, filename: str) -> str:
    """
    Merge trent-managed section from source into dest, preserving all other content.

    For agents.md / CLAUDE.md: replaces the <!-- TRENT SYSTEM SECTION --> block
    from source while leaving everything else in dest untouched.
    """
    fname = filename.lower()
    if fname == 'agents.md':
        start_marker = '<!-- TRENT SYSTEM SECTION -->'
        end_marker = '<!-- END TRENT SYSTEM SECTION -->'
    elif fname == 'claude.md':
        start_marker = '<!-- TRENT SYSTEM CONTEXT -->'
        end_marker = '<!-- END TRENT SYSTEM CONTEXT -->'
    else:
        return source_content

    if start_marker not in source_content:
        # Source has no trent section — fall back to full overwrite
        return source_content

    # Extract trent section from source
    src_start = source_content.find(start_marker)
    src_end = source_content.find(end_marker)
    src_end = (src_end + len(end_marker)) if src_end != -1 else len(source_content)
    new_section = source_content[src_start:src_end]

    if start_marker in dest_content:
        # Replace existing trent section in dest
        dst_start = dest_content.find(start_marker)
        dst_end = dest_content.find(end_marker)
        dst_end = (dst_end + len(end_marker)) if dst_end != -1 else len(dest_content)
        return dest_content[:dst_start] + new_section + dest_content[dst_end:]
    else:
        # Append trent section to end of dest
        return dest_content.rstrip() + '\n\n' + new_section + '\n'


# ============================================================
# PATH UTILITIES
# ============================================================

def translate_windows_path(path: str) -> str:
    """Translate Windows drive path to Docker /mnt/ path when running in container."""
    import re
    match = re.match(r'^([a-zA-Z]):[/\\](.*)$', path)
    if match:
        drive = match.group(1).lower()
        rest = match.group(2).replace('\\', '/')
        return f'/mnt/{drive}/{rest}'
    return path


def resolve_target_path(target_path: str) -> Path:
    """Translate and resolve the target path, handling Windows/Docker differences."""
    if os.path.exists('/mnt'):
        target_path = translate_windows_path(target_path)
    return Path(target_path).resolve()


# ============================================================
# BACKUP UTILITIES
# ============================================================

def backup_trent_dir(trent_dir: Path, target_dir: Path) -> dict:
    """
    Create a timestamped zip backup of .trent/ before destructive operations.

    The backup is saved as .trent_backup_YYYYMMDD_HHMMSS.zip in target_dir.
    Also ensures .gitignore excludes the backup pattern (if .gitignore exists).

    Returns:
        {
            'success': bool,
            'backup_path': str | None,
            'backup_name': str | None,
            'file_count': int,
            'backup_size_bytes': int,
            'skipped': bool,          # True if nothing to back up
            'error': str | None,
        }
    """
    import zipfile
    from datetime import datetime

    if not trent_dir.exists():
        return {
            'success': True,
            'backup_path': None,
            'backup_name': None,
            'file_count': 0,
            'backup_size_bytes': 0,
            'skipped': True,
            'skip_reason': '.trent/ does not exist — nothing to back up',
            'error': None,
        }

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'.trent_backup_{timestamp}.zip'
    backup_path = target_dir / backup_name

    try:
        files_added = []
        with zipfile.ZipFile(str(backup_path), 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in sorted(trent_dir.rglob('*')):
                if file_path.is_file():
                    # Store path relative to target_dir (e.g., .trent/TASKS.md)
                    arcname = file_path.relative_to(target_dir)
                    zf.write(str(file_path), str(arcname))
                    files_added.append(str(arcname))

        backup_size = backup_path.stat().st_size

        # Keep .gitignore clean — exclude backup zips from commits
        _ensure_gitignore_pattern(target_dir, '.trent_backup_*.zip')

        logger.info(
            f"Backed up .trent/ → {backup_name} "
            f"({len(files_added)} files, {backup_size} bytes)"
        )
        return {
            'success': True,
            'backup_path': str(backup_path),
            'backup_name': backup_name,
            'file_count': len(files_added),
            'backup_size_bytes': backup_size,
            'skipped': False,
            'error': None,
        }

    except Exception as e:
        # Clean up an incomplete zip if it was partially written
        try:
            if backup_path.exists():
                backup_path.unlink()
        except Exception:
            pass
        logger.error(f"backup_trent_dir failed: {e}")
        return {
            'success': False,
            'backup_path': None,
            'backup_name': None,
            'file_count': 0,
            'backup_size_bytes': 0,
            'skipped': False,
            'error': str(e),
        }


def _ensure_gitignore_pattern(target_dir: Path, pattern: str) -> None:
    """
    Append pattern to .gitignore in target_dir if not already present.
    Does nothing if .gitignore does not exist (we don't create it).
    """
    gitignore = target_dir / '.gitignore'
    if not gitignore.exists():
        return
    try:
        content = gitignore.read_text(encoding='utf-8')
        if pattern not in content:
            with open(str(gitignore), 'a', encoding='utf-8') as f:
                f.write(f'\n# trent backup archives\n{pattern}\n')
            logger.info(f"Added '{pattern}' to .gitignore")
    except Exception as e:
        logger.warning(f"Could not update .gitignore with backup pattern: {e}")


def trent_dir_has_user_data(trent_dir: Path) -> bool:
    """
    Return True if .trent/ appears to contain real user task data
    (i.e. it has been used, not just installed as a blank template).

    Checks for:
      - Any task*.md files in .trent/tasks/
      - Any phase*.md files in .trent/phases/
      - Any task list items (- [ ], - [x], etc.) in TASKS.md
    """
    if not trent_dir.exists():
        return False

    tasks_dir = trent_dir / 'tasks'
    phases_dir = trent_dir / 'phases'

    if tasks_dir.exists():
        task_files = [f for f in tasks_dir.glob('task*.md') if f.name != '.gitkeep']
        if task_files:
            return True

    if phases_dir.exists():
        phase_files = [f for f in phases_dir.glob('phase*.md') if f.name != '.gitkeep']
        if phase_files:
            return True

    tasks_md = trent_dir / 'TASKS.md'
    if tasks_md.exists():
        try:
            for line in tasks_md.read_text(encoding='utf-8').splitlines():
                stripped = line.strip()
                # Any markdown task list item indicates user has started populating
                if stripped.startswith('- [') and len(stripped) > 6:
                    return True
        except Exception:
            pass

    return False


# ============================================================
# OS INFO
# ============================================================

def get_os_info() -> dict:
    """Return OS platform information."""
    is_windows = platform.system() == 'Windows'
    can_symlink = False

    if is_windows:
        import tempfile
        try:
            with tempfile.TemporaryDirectory() as tmp:
                src = Path(tmp) / 'test.txt'
                lnk = Path(tmp) / 'link.txt'
                src.write_text('test')
                try:
                    lnk.symlink_to(src)
                    can_symlink = True
                except OSError:
                    can_symlink = False
        except Exception:
            can_symlink = False
    else:
        can_symlink = True

    return {
        'platform': platform.system(),
        'is_windows': is_windows,
        'can_create_symlinks': can_symlink,
        'python_version': sys.version,
        'machine': platform.machine(),
    }


# ============================================================
# CORE INSTALL LOGIC (shared by trent_install and trent_rules_update)
# ============================================================

def run_install(
    manifest: List[str],
    target: Path,
    github_repo: str,
    github_token: str,
    force_overwrite: bool,
    dry_run: bool,
    original_target_path: str,
) -> dict:
    """
    Core install logic: fetch each item in manifest from GitHub to target.

    Handles mergeable files (agents.md, CLAUDE.md) separately to preserve
    user content outside the trent-managed section markers.

    Returns a result dict suitable for returning from an MCP tool execute().
    """
    import tempfile
    from datetime import datetime

    result = {
        'success': False,
        'target_path': original_target_path,
        'target_path_resolved': str(target),
        'source': f'github:{github_repo}',
        'dry_run': dry_run,
        'manifest_items': len(manifest),
        'copied_files': [],
        'skipped_files': [],
        'merged_files': [],
        'warnings': [],
        'operation_time_seconds': 0,
    }

    if dry_run:
        result['success'] = True
        result['message'] = (
            f"Dry run: would install {len(manifest)} items from {github_repo}"
        )
        for gh_path in manifest:
            result['copied_files'].append({
                'item': gh_path,
                'action': 'would_copy',
                'source': f'https://github.com/{github_repo}/tree/main/{gh_path}',
            })
        return result

    start_time = datetime.now()

    for gh_path in manifest:
        logger.info(f"Fetching: {gh_path}")

        # Mergeable file handling: fetch to temp, then merge to preserve user content
        is_mergeable = gh_path.lower() in MERGEABLE_FILES
        dest_item = target / gh_path

        if is_mergeable and dest_item.exists() and not force_overwrite:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                gh_result = fetch_from_github(
                    repo=github_repo, path=gh_path,
                    target_dir=tmp_path, token=github_token, overwrite=True,
                )
                if gh_result.get('error'):
                    result['warnings'].append(f"Failed to fetch {gh_path}: {gh_result['error']}")
                    continue
                source_file = tmp_path / gh_path
                if source_file.exists():
                    try:
                        merged = merge_markdown_file(
                            source_file.read_text(encoding='utf-8'),
                            dest_item.read_text(encoding='utf-8'),
                            gh_path,
                        )
                        dest_item.write_text(merged, encoding='utf-8')
                        result['merged_files'].append(str(dest_item))
                        logger.info(f"Merged: {gh_path}")
                    except Exception as e:
                        result['warnings'].append(f"Failed to merge {gh_path}: {e}")
            continue

        # Standard fetch
        gh_result = fetch_from_github(
            repo=github_repo,
            path=gh_path,
            target_dir=target,
            token=github_token,
            overwrite=force_overwrite,
        )
        if gh_result.get('error'):
            result['warnings'].append(f"Failed to fetch {gh_path}: {gh_result['error']}")
        else:
            result['copied_files'].extend(gh_result['files_fetched'])
            result['skipped_files'].extend(gh_result['files_skipped'])
            if gh_result['errors']:
                result['warnings'].extend(gh_result['errors'])

    result['operation_time_seconds'] = round(
        (datetime.now() - start_time).total_seconds(), 2
    )

    total = len(result['copied_files']) + len(result['merged_files'])
    if total > 0:
        result['success'] = True
        result['message'] = (
            f"Successfully installed {total} files "
            f"({len(result['skipped_files'])} skipped, {len(result['merged_files'])} merged) "
            f"from {github_repo} in {result['operation_time_seconds']}s"
        )
    else:
        result['success'] = False
        result['error'] = (
            f"No files were installed. "
            f"Skipped: {len(result['skipped_files'])}. "
            f"Warnings: {result['warnings']}"
        )

    return result
