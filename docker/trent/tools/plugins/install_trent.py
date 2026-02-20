"""
Install Trent Tool Plugin

Install trent development environment to a project directory.
Fetches directly from the GitHub repository root (not templates subfolder).

Template source priority:
  1. GITHUB_TOKEN env var (user's own token - full access)
  2. Default read-only token (bundled for public wrm3/trent_rules repo)
  3. Error - if GitHub is unreachable
"""
import os
import sys
import shutil
import asyncio
import logging
import platform
import json
import base64
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "install_trent"

TOOL_DESCRIPTION = (
    "Install trent development environment to a project directory. "
    "Fetches from GitHub repository root: .architecture, .cursor, .claude, .trent, "
    "AGENTS.md, CLAUDE.md, and index files (AGENTS_INDEX.md, COMMANDS_INDEX.md, etc.). "
    "OS-aware: detects Windows Developer Mode for symlink handling. "
    "Merges directories without destroying existing content."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install templates to (required)",
    "force_overwrite": "Overwrite existing files (default: False)",
    "dry_run": "Preview changes without applying (default: False)"
}


logger = logging.getLogger(__name__)

# ============================================================
# DEFAULT TOKEN
# ============================================================
# Read-only PAT for the public wrm3/trent_rules repo.
# This is intentionally committed so install_trent works out-of-the-box
# without requiring users to configure GITHUB_TOKEN.
# Set GITHUB_TOKEN in your environment to override with your own token.
_DEFAULT_GITHUB_TOKEN = (
    "github_pat_11AM6DLNA0MOOBKQOuVXCC_"
    "IXXBaacBSQDTR8mrZnQhLH1O1ChHVjKz0P0ftYI4NKBODDI6D3NV2yESrNf"
)

# ============================================================
# CONFIGURATION
# ============================================================

# Install manifest - everything that gets copied to a new project.
#
# Two formats:
#   str   - simple verbatim copy: same path in source repo and target project
#   tuple - remapped copy: (github_path, dest_subpath, strip_prefix, exclude_prefixes)
#             github_path      path to fetch from source repo
#             dest_subpath     destination dir relative to target root (None = target root)
#             strip_prefix     stripped from entry_path before joining with dest_dir
#             exclude_prefixes list of repo-relative paths to skip entirely (or None)
#
# Use a tuple when the source folder name differs from the target folder name,
# or when parts of the source tree should be excluded.

INSTALL_MANIFEST = [
    # ── Directories (simple copy) ─────────────────────────────────────────────
    '.agent',           # Google Antigravity config (rules, skills, workflows)
    '.architecture',    # Cross-platform architecture docs
    '.claude',          # Claude Code config (agents, skills, rules, commands, hooks)
    '.cursor',          # Cursor IDE config  (rules, skills, agents, commands, hooks)

    # ── Root files (simple copy) ──────────────────────────────────────────────
    'agents.md',        # Universal agent instructions (lowercase - GitHub is case-sensitive)
    'AGENTS_INDEX.md',
    'CLAUDE.md',
    'COMMANDS_INDEX.md',
    'CURSOR_SETUP.md',
    'GUARDRAILS.md',
    'HOOKS_INDEX.md',
    'RULES_INDEX.md',
    'SKILLS_INDEX.md',
    '.env.example',
    'mcp.txt',

    # ── .trent (simple copy) ──────────────────────────────────────────────────
    # .trent/ in this repo IS the template — blank root files, empty tasks/phases,
    # examples/ and reference/ included, no live task data, no templates/ subfolder.
    '.trent',
]

# Files that should be merged (trent section updated, other content preserved)
MERGEABLE_FILES = ['agents.md', 'claude.md']

_config = None
_github_token = None
_github_repo = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _config, _github_token, _github_repo
    _config = context.get('config', {})

    # Read GitHub credentials from environment
    _github_token = os.environ.get('GITHUB_TOKEN')
    _github_repo = os.environ.get('GITHUB_REPO', 'wrm3/trent_rules')


# ============================================================
# GITHUB API FETCH
# ============================================================

def _github_api_request(url: str, token: str) -> Any:
    """
    Make a single GitHub API GET request and return parsed JSON.
    Uses only stdlib urllib - no extra dependencies.
    """
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Bearer {token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('X-GitHub-Api-Version', '2022-11-28')
    req.add_header('User-Agent', 'trent-install-tool/2.0')

    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode('utf-8'))


def _fetch_from_github(
    repo: str,
    path: str,
    target_dir: Path,
    token: str,
    strip_prefix: str = None,
    exclude_prefixes: list = None,
) -> Dict[str, Any]:
    """
    Recursively fetch files from a GitHub repository path and write them
    to target_dir.

    Uses the GitHub Contents API:
      GET https://api.github.com/repos/{repo}/contents/{path}

    Args:
        repo:             GitHub repo slug, e.g. "wrm3/trent_rules"
        path:             Path within the repo, e.g. ".cursor" or "AGENTS.md"
        target_dir:       Local directory to write files into
        token:            GitHub personal access token
        strip_prefix:     Optional repo-relative prefix to strip from entry_path
                          before joining with target_dir. Used for path remapping,
                          e.g. strip ".trent_template" so files land at target_dir
                          root rather than target_dir/.trent_template/.
        exclude_prefixes: Optional list of repo-relative path prefixes to skip.
                          Entries whose path starts with any of these are ignored.
                          e.g. ['.trent_template/templates'] skips that subfolder.

    Returns:
        {
            'success': bool,
            'files_fetched': [str, ...],
            'errors': [str, ...],
            'error': str | None,
        }
    """
    result: Dict[str, Any] = {
        'success': False,
        'files_fetched': [],
        'errors': [],
        'error': None,
    }

    # Normalize the API path
    api_path = path.strip('/')
    url = f'https://api.github.com/repos/{repo}/contents/{api_path}'

    try:
        data = _github_api_request(url, token)
    except urllib.error.HTTPError as exc:
        result['error'] = f"GitHub API HTTP {exc.code} for {url}: {exc.reason}"
        return result
    except urllib.error.URLError as exc:
        result['error'] = f"GitHub API network error for {url}: {exc.reason}"
        return result
    except Exception as exc:
        result['error'] = f"GitHub API unexpected error for {url}: {exc}"
        return result

    # Single file response (dict) vs directory listing (list)
    if isinstance(data, dict):
        entries = [data]
    else:
        entries = data

    for entry in entries:
        entry_type = entry.get('type')
        entry_path = entry.get('path', '')
        entry_name = entry.get('name', '')

        # Skip excluded paths (e.g. .trent_template/templates)
        if exclude_prefixes:
            if any(entry_path == p or entry_path.startswith(p + '/') for p in exclude_prefixes):
                logger.debug(f"Skipping excluded path: {entry_path}")
                continue

        # Use the full repo-relative path so folder structure is preserved.
        # entry_path is already relative to repo root, e.g. ".cursor/rules/file.mdc"
        # If strip_prefix is set, remove it before joining with target_dir so
        # that path remapping works (e.g. ".trent_template/X" → target_dir/"X").
        rel_path = entry_path
        if strip_prefix and rel_path.startswith(strip_prefix):
            rel_path = rel_path[len(strip_prefix):].lstrip('/')
        local_target = target_dir / rel_path if rel_path else target_dir / entry_name

        if entry_type == 'dir':
            # Recurse into subdirectory (pass both params through)
            sub_result = _fetch_from_github(
                repo, entry_path, target_dir, token, strip_prefix, exclude_prefixes
            )
            result['files_fetched'].extend(sub_result['files_fetched'])
            result['errors'].extend(sub_result['errors'])
            if sub_result.get('error'):
                result['errors'].append(sub_result['error'])

        elif entry_type == 'file':
            # Download file content
            try:
                encoding = entry.get('encoding', 'base64')
                raw_content = entry.get('content', '')

                if encoding == 'base64' and raw_content:
                    file_bytes = base64.b64decode(raw_content)
                else:
                    # Fallback: fetch via download_url
                    download_url = entry.get('download_url')
                    if not download_url:
                        result['errors'].append(f"No download_url for {entry_path}")
                        continue
                    req = urllib.request.Request(download_url)
                    req.add_header('Authorization', f'Bearer {token}')
                    req.add_header('User-Agent', 'trent-install-tool/2.0')
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        file_bytes = resp.read()

                # Write file, creating parent dirs as needed
                local_target.parent.mkdir(parents=True, exist_ok=True)
                local_target.write_bytes(file_bytes)
                result['files_fetched'].append(str(local_target))
                logger.debug(f"GitHub fetch: {entry_path} -> {local_target}")

            except Exception as exc:
                msg = f"Failed to write {entry_path}: {exc}"
                logger.warning(msg)
                result['errors'].append(msg)

    result['success'] = True
    return result


# ============================================================
# PATH UTILITIES
# ============================================================

def _translate_windows_path(path: str) -> str:
    """
    Translate Windows paths to Docker mount paths when running in container.
    E.g., 'G:\\OpenClaw' -> '/mnt/g/OpenClaw'
    """
    import re
    match = re.match(r'^([a-zA-Z]):[/\\](.*)$', path)
    if match:
        drive_letter = match.group(1).lower()
        rest_of_path = match.group(2).replace('\\', '/')
        return f'/mnt/{drive_letter}/{rest_of_path}'
    return path


# ============================================================
# MARKDOWN MERGE
# ============================================================

def _merge_markdown_files(source_content: str, dest_content: str, filename: str) -> str:
    """
    Merge two markdown files intelligently.
    For agents.md/CLAUDE.md: preserve existing content, add trent sections if missing.
    """
    # Define section markers
    if filename.lower() == 'agents.md':
        section_marker = '<!-- TRENT SYSTEM SECTION -->'
        section_end = '<!-- END TRENT SYSTEM SECTION -->'
    elif filename.lower() == 'claude.md':
        section_marker = '<!-- TRENT SYSTEM CONTEXT -->'
        section_end = '<!-- END TRENT SYSTEM CONTEXT -->'
    else:
        return source_content

    # Check if destination already has trent section
    if section_marker in dest_content:
        # Replace existing trent section with new one
        if section_marker in source_content:
            start_idx = source_content.find(section_marker)
            end_idx = source_content.find(section_end)
            if end_idx == -1:
                end_idx = len(source_content)
            else:
                end_idx += len(section_end)
            new_section = source_content[start_idx:end_idx]

            dest_start = dest_content.find(section_marker)
            dest_end = dest_content.find(section_end)
            if dest_end == -1:
                dest_end = len(dest_content)
            else:
                dest_end += len(section_end)

            return dest_content[:dest_start] + new_section + dest_content[dest_end:]
    else:
        # Destination doesn't have trent section - append it
        if section_marker in source_content:
            start_idx = source_content.find(section_marker)
            end_idx = source_content.find(section_end)
            if end_idx == -1:
                end_idx = len(source_content)
            else:
                end_idx += len(section_end)
            new_section = source_content[start_idx:end_idx]

            return dest_content.rstrip() + '\n\n' + new_section + '\n'
        else:
            return dest_content.rstrip() + '\n\n---\n\n' + source_content

    return dest_content


# ============================================================
# OS DETECTION
# ============================================================

def _get_os_info() -> dict:
    """Get OS information and capabilities."""
    is_windows = platform.system() == 'Windows'
    can_create_symlinks = False

    if is_windows:
        can_create_symlinks = _check_windows_symlink_capability()
    else:
        can_create_symlinks = True

    return {
        'platform': platform.system(),
        'is_windows': is_windows,
        'can_create_symlinks': can_create_symlinks,
        'python_version': sys.version,
        'machine': platform.machine()
    }


def _check_windows_symlink_capability() -> bool:
    """Check if Windows can create symlinks (Developer Mode or admin)."""
    import tempfile

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "test_file.txt"
            test_link = Path(temp_dir) / "test_link.txt"

            test_file.write_text("test")

            try:
                test_link.symlink_to(test_file)
                return True
            except OSError:
                return False

    except Exception:
        return False


# ============================================================
# FILE COUNT HELPER
# ============================================================

def _count_files(directory: Path) -> int:
    """Count files in a directory recursively."""
    count = 0
    for item in directory.rglob('*'):
        if item.is_file():
            count += 1
    return count


# ============================================================
# MAIN EXECUTE
# ============================================================

async def execute(
    target_path: str,
    force_overwrite: bool = False,
    dry_run: bool = False,
    context: dict = None
) -> dict:
    """
    Install trent development environment to a project directory.

    Fetches directly from GitHub repository root.
    Uses bundled read-only token if GITHUB_TOKEN is not set in environment.
    """
    config = context.get('config', _config) if context else _config

    # Re-read env vars at execute time (allows hot-reload without restart)
    # Fall back to bundled read-only token if none is configured
    github_token = (
        os.environ.get('GITHUB_TOKEN')
        or _github_token
        or _DEFAULT_GITHUB_TOKEN
    )
    github_repo = os.environ.get('GITHUB_REPO', _github_repo or 'wrm3/trent_rules')

    # Store original path for reporting
    original_target_path = target_path

    # Translate Windows paths if running in Docker container
    if os.path.exists('/mnt'):
        target_path = _translate_windows_path(target_path)
        if target_path != original_target_path:
            logger.info(f"Translated Windows path: {original_target_path} -> {target_path}")

    logger.info(f"Installing trent to: {target_path}")
    logger.info(f"Source: GitHub repo {github_repo}")
    logger.info(f"dry_run: {dry_run}, force_overwrite: {force_overwrite}")

    # Validate target path
    try:
        target = Path(target_path).resolve()
        if not dry_run:
            target.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid target path: {e}",
            'hint': (
                "If using Windows paths like 'G:\\Project', "
                "ensure Docker has access to the drive."
            )
        }

    # Check OS and capabilities
    os_info = _get_os_info()

    result = {
        'success': False,
        'target_path': original_target_path,
        'target_path_resolved': str(target),
        'source': 'github',
        'github_repo': github_repo,
        'os_info': os_info,
        'dry_run': dry_run,
        'items_to_install': [e if isinstance(e, str) else e[0] for e in INSTALL_MANIFEST],
        'copied_files': [],
        'skipped_files': [],
        'merged_files': [],
        'warnings': [],
        'operation_time_seconds': 0
    }

    start_time = datetime.now()

    if dry_run:
        result['success'] = True
        result['message'] = f"Dry run: would install {len(INSTALL_MANIFEST)} items from {github_repo}"
        for entry in INSTALL_MANIFEST:
            gh_path = entry if isinstance(entry, str) else entry[0]
            dest    = gh_path if isinstance(entry, str) else entry[1]
            result['copied_files'].append({
                'item': gh_path,
                'dest': dest,
                'action': 'would_copy',
                'source': f"https://github.com/{github_repo}/tree/main/{gh_path}"
            })
        return result

    logger.info(f"Fetching {len(INSTALL_MANIFEST)} items from GitHub ({github_repo})")

    import tempfile

    for entry in INSTALL_MANIFEST:
        # Normalize: str → simple copy; tuple → remapped copy
        if isinstance(entry, str):
            gh_path         = entry
            dest_subpath    = None      # write relative to target root
            strip_prefix    = None
            exclude_prefixes = None
        else:
            gh_path, dest_subpath, strip_prefix, exclude_prefixes = entry

        dest_dir = (target / dest_subpath) if dest_subpath else target
        logger.info(f"Fetching: {gh_path}" + (f" -> {dest_subpath}" if dest_subpath else ""))

        # Mergeable files: fetch to temp dir first, then merge
        is_mergeable = isinstance(entry, str) and gh_path.lower() in MERGEABLE_FILES
        dest_item = target / gh_path
        if is_mergeable and dest_item.exists() and not force_overwrite:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                gh_result = _fetch_from_github(
                    repo=github_repo, path=gh_path,
                    target_dir=tmp_path, token=github_token,
                )
                if gh_result.get('error'):
                    result['warnings'].append(f"Failed to fetch {gh_path}: {gh_result['error']}")
                    continue
                source_file = tmp_path / gh_path
                if source_file.exists():
                    try:
                        merged = _merge_markdown_files(
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

        # Standard fetch (with optional path remapping and exclusions)
        gh_result = _fetch_from_github(
            repo=github_repo,
            path=gh_path,
            target_dir=dest_dir,
            token=github_token,
            strip_prefix=strip_prefix,
            exclude_prefixes=exclude_prefixes,
        )
        if gh_result.get('error'):
            result['warnings'].append(f"Failed to fetch {gh_path}: {gh_result['error']}")
        else:
            result['copied_files'].extend(gh_result['files_fetched'])
            if gh_result['errors']:
                result['warnings'].extend(gh_result['errors'])

    result['operation_time_seconds'] = round(
        (datetime.now() - start_time).total_seconds(), 2
    )

    total_items = len(result['copied_files']) + len(result['merged_files'])
    if total_items > 0:
        result['success'] = True
        result['message'] = (
            f"Successfully installed {total_items} files from GitHub ({github_repo}) "
            f"in {result['operation_time_seconds']}s"
        )
    else:
        result['success'] = False
        result['error'] = "No files were installed"

    return result
