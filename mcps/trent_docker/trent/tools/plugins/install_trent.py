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
    "Copies .cursor (rules, commands, skills), .trent (task management), "
    "agents.md, and CLAUDE.md. OS-aware: detects Windows Developer Mode "
    "for symlink handling. Merges directories without destroying existing content."
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


def _translate_windows_path(path: str) -> str:
    """
    Translate Windows paths to Docker mount paths when running in container.
    E.g., 'G:\\OpenClaw' -> '/mnt/g/OpenClaw'
    """
    import re
    # Check if it's a Windows-style path (e.g., G:\, C:\, g:/, etc.)
    match = re.match(r'^([a-zA-Z]):[/\\](.*)$', path)
    if match:
        drive_letter = match.group(1).lower()
        rest_of_path = match.group(2).replace('\\', '/')
        return f'/mnt/{drive_letter}/{rest_of_path}'
    return path


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

    # Store original path for reporting
    original_target_path = target_path
    
    # Translate Windows paths if running in Docker container
    if os.path.exists('/mnt'):
        target_path = _translate_windows_path(target_path)
        if target_path != original_target_path:
            logger.info(f"Translated Windows path: {original_target_path} -> {target_path}")

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
            'error': f"Invalid target path: {e}",
            'hint': "If using Windows paths like 'G:\\Project', ensure Docker has access to the drive."
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
        'target_path': original_target_path,  # Show original Windows path to user
        'target_path_resolved': str(target),  # Actual path used
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
                # Handle individual file copy (with merge support for agents.md/CLAUDE.md)
                is_mergeable = item_name.lower() in ['agents.md', 'claude.md']
                
                if dry_run:
                    if dest_item.exists() and is_mergeable:
                        result['copied_files'].append({
                            'file': item_name,
                            'action': 'would_merge',
                            'source': str(source_item),
                            'destination': str(dest_item)
                        })
                    else:
                        result['copied_files'].append({
                            'file': item_name,
                            'action': 'would_copy',
                            'source': str(source_item),
                            'destination': str(dest_item)
                        })
                else:
                    if dest_item.exists():
                        if is_mergeable:
                            # Merge agents.md/CLAUDE.md with existing
                            try:
                                source_content = source_item.read_text(encoding='utf-8')
                                dest_content = dest_item.read_text(encoding='utf-8')
                                merged = _merge_markdown_files(source_content, dest_content, item_name)
                                dest_item.write_text(merged, encoding='utf-8')
                                result['copied_files'].append(f"{dest_item} (merged)")
                                logger.info(f"Merged: {item_name}")
                            except Exception as e:
                                logger.warning(f"Failed to merge {item_name}: {e}")
                                result['skipped_files'].append(str(dest_item))
                        elif not force_overwrite:
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
    # Index files to include with full/minimal installs
    index_files = ['AGENTS_INDEX.md', 'SKILLS_INDEX.md', 'COMMANDS_INDEX.md', 'HOOKS_INDEX.md', 'RULES_INDEX.md']
    
    all_dirs = {
        'full': ['.cursor', '.trent', 'agents.md', 'CLAUDE.md'] + index_files,
        'cursor': ['.cursor'],
        'trent': ['.trent'],
        'rules': ['.cursor/rules'],
        'skills': ['.cursor/skills'],
        'commands': ['.cursor/commands'],
        'minimal': ['.trent', 'agents.md'] + index_files  # Task management + agents.md + indexes
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
