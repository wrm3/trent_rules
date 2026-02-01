"""
Install Trent Tool Plugin

Install trent development templates (IDE configs, rules, skills) to a project.
OS-aware with special handling for Windows symlinks (Developer Mode detection).
"""
import os
import sys
import shutil
import asyncio
import logging
import platform
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "install_trent"

TOOL_DESCRIPTION = (
    "Install trent development templates to a project directory. "
    "Copies IDE configurations (.claude, .cursor, .vscode), rules, skills, and agents. "
    "OS-aware: detects Windows Developer Mode for symlink handling. "
    "Merges directories without destroying existing content."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install templates to (required)",
    "template_type": "Template type: 'full', 'cursor', 'trent', 'rules', 'skills', 'commands', 'minimal' (default: 'full')",
    "force_overwrite": "Overwrite existing files (default: False)",
    "dry_run": "Preview changes without applying (default: False)"
}


logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_config = None
_template_path = None


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _config, _template_path
    _config = context.get('config', {})

    # Get template path from config or use default
    _template_path = _config.get('template_path')
    if not _template_path:
        # Default: templates/ relative to package root
        package_root = Path(__file__).parent.parent.parent.parent
        _template_path = package_root / 'templates'


async def execute(
    target_path: str,
    template_type: str = "full",
    force_overwrite: bool = False,
    dry_run: bool = False,
    context: dict = None
) -> dict:
    """
    Install templates to a project directory.
    """
    config = context.get('config', _config) if context else _config

    logger.info(f"Template install to: {target_path}")
    logger.info(f"Template type: {template_type}, dry_run: {dry_run}")

    # Validate target path
    try:
        target = Path(target_path).resolve()
        if not dry_run:
            target.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid target path: {e}"
        }

    # Get template source
    template_source = Path(_template_path) if _template_path else None
    if not template_source or not template_source.exists():
        return {
            'success': False,
            'error': f"Template source not found: {template_source}"
        }

    # Check OS and capabilities
    os_info = _get_os_info()

    # Determine which directories to copy based on template_type
    dirs_to_copy = _get_template_dirs(template_type)

    result = {
        'success': False,
        'target_path': str(target),
        'template_source': str(template_source),
        'template_type': template_type,
        'os_info': os_info,
        'dry_run': dry_run,
        'copied_files': [],
        'skipped_files': [],
        'warnings': [],
        'operation_time_seconds': 0
    }

    start_time = datetime.now()

    try:
        # Check Windows symlink capability
        if os_info['is_windows'] and not os_info['can_create_symlinks']:
            result['warnings'].append(
                "Windows symlink creation requires Developer Mode or admin privileges. "
                "Symlinks will be converted to regular copies."
            )

        # Process each directory or file
        for item_name in dirs_to_copy:
            source_item = template_source / item_name
            if not source_item.exists():
                result['warnings'].append(f"Template item not found: {item_name}")
                continue

            dest_item = target / item_name
            logger.info(f"Processing: {item_name}")

            if source_item.is_file():
                # Handle individual file copy
                if dry_run:
                    result['copied_files'].append({
                        'file': item_name,
                        'action': 'would_copy',
                        'source': str(source_item),
                        'destination': str(dest_item)
                    })
                else:
                    if dest_item.exists() and not force_overwrite:
                        result['skipped_files'].append(str(dest_item))
                    else:
                        try:
                            await asyncio.to_thread(
                                shutil.copy2, str(source_item), str(dest_item)
                            )
                            result['copied_files'].append(str(dest_item))
                        except Exception as e:
                            logger.warning(f"Failed to copy {source_item}: {e}")
                            result['skipped_files'].append(str(dest_item))
            else:
                # Handle directory copy
                if dry_run:
                    # Preview mode - just list files
                    file_count = _count_files(source_item)
                    result['copied_files'].append({
                        'directory': item_name,
                        'action': 'would_copy',
                        'file_count': file_count,
                        'source': str(source_item),
                        'destination': str(dest_item)
                    })
                else:
                    # Actual copy
                    copied = await _merge_directories(
                        source_item, dest_item, force_overwrite, os_info
                    )
                    result['copied_files'].extend(copied['copied'])
                    result['skipped_files'].extend(copied['skipped'])

        result['operation_time_seconds'] = round((datetime.now() - start_time).total_seconds(), 2)
        result['success'] = True
        result['message'] = (
            f"Successfully installed {len(result['copied_files'])} items "
            f"in {result['operation_time_seconds']}s"
            if not dry_run else
            f"Dry run completed: would install {len(result['copied_files'])} directories"
        )

        return result

    except Exception as e:
        logger.error(f"Template install failed: {e}")
        result['operation_time_seconds'] = round((datetime.now() - start_time).total_seconds(), 2)
        result['error'] = str(e)
        return result


def _get_os_info() -> dict:
    """Get OS information and capabilities."""
    is_windows = platform.system() == 'Windows'
    can_create_symlinks = False

    if is_windows:
        # Check if we can create symlinks (Developer Mode or admin)
        can_create_symlinks = _check_windows_symlink_capability()
    else:
        # Unix-like systems can create symlinks
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
        # Try to create a test symlink
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


def _get_template_dirs(template_type: str) -> List[str]:
    """Get list of directories/files to copy based on template type."""
    all_dirs = {
        'full': ['.cursor', '.trent', 'agents.md', 'CLAUDE.md'],
        'cursor': ['.cursor'],
        'trent': ['.trent'],
        'rules': ['.cursor/rules'],
        'skills': ['.cursor/skills'],
        'commands': ['.cursor/commands'],
        'minimal': ['.trent', 'agents.md']  # Just task management + agents.md
    }

    return all_dirs.get(template_type.lower(), all_dirs['full'])


def _count_files(directory: Path) -> int:
    """Count files in a directory recursively."""
    count = 0
    for item in directory.rglob('*'):
        if item.is_file():
            count += 1
    return count


async def _merge_directories(
    source: Path,
    dest: Path,
    force_overwrite: bool,
    os_info: dict
) -> dict:
    """Merge source directory into destination without destroying existing content."""
    result = {'copied': [], 'skipped': []}

    if not source.exists():
        return result

    dest.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        source_item = source / item.name
        dest_item = dest / item.name

        if source_item.is_dir():
            # Recursively merge subdirectories
            sub_result = await _merge_directories(
                source_item, dest_item, force_overwrite, os_info
            )
            result['copied'].extend(sub_result['copied'])
            result['skipped'].extend(sub_result['skipped'])
        else:
            # Handle file copy
            if dest_item.exists() and not force_overwrite:
                result['skipped'].append(str(dest_item))
            else:
                try:
                    # Check if source is a symlink
                    if source_item.is_symlink():
                        if os_info['can_create_symlinks']:
                            # Copy as symlink
                            if dest_item.exists():
                                dest_item.unlink()
                            dest_item.symlink_to(source_item.readlink())
                        else:
                            # Windows without symlink capability - copy as regular file
                            await asyncio.to_thread(
                                shutil.copy2, str(source_item.resolve()), str(dest_item)
                            )
                    else:
                        # Regular file copy
                        await asyncio.to_thread(
                            shutil.copy2, str(source_item), str(dest_item)
                        )

                    result['copied'].append(str(dest_item))
                    logger.debug(f"Copied: {source_item} -> {dest_item}")

                except Exception as e:
                    logger.warning(f"Failed to copy {source_item}: {e}")
                    result['skipped'].append(str(dest_item))

    return result
