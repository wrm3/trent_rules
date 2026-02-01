"""
Install Trent Full Tool Plugin

Install COMPLETE trent development environment from the source repository.
Copies the full .cursor folder (all rules, skills, commands, agents),
.trent templates, docs/, temp_scripts/, agents.md, and CLAUDE.md.

This is different from install_trent which only copies curated templates.
"""
import os
import sys
import shutil
import asyncio
import logging
import platform
import re
from pathlib import Path
from typing import Optional, Dict, Any, List
from datetime import datetime

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "install_trent_full"

TOOL_DESCRIPTION = (
    "Install COMPLETE trent development environment from source repository. "
    "Copies full .cursor folder (ALL rules, skills, commands, agents), "
    ".trent templates, empty docs/ and temp_scripts/ folders, plus agents.md "
    "and CLAUDE.md. Use this for new projects that need the full development setup. "
    "For agents.md/CLAUDE.md: merges with existing files or skips if merge not possible."
)

TOOL_PARAMS = {
    "target_path": "Target project directory to install to (required)",
    "source_path": "Source trent_rules repository path (default: G:\\trent_rules)",
    "force_overwrite": "Overwrite existing files (default: False)",
    "dry_run": "Preview changes without applying (default: False)",
    "skip_project_files": "Skip agents.md and CLAUDE.md (default: False)"
}


logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN IMPLEMENTATION
# ============================================================

_config = None

# Default source path - the trent_rules repository
DEFAULT_SOURCE_PATH = "G:\\trent_rules"


def setup(context: dict):
    """Called once during plugin loading to set up dependencies."""
    global _config
    _config = context.get('config', {})


def _translate_windows_path(path: str) -> str:
    """
    Translate Windows paths to Docker mount paths when running in container.
    E.g., 'G:\\OpenClaw' -> '/mnt/g/OpenClaw'
    """
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
        # For other files, just return source if dest doesn't exist
        return source_content
    
    # Check if destination already has trent section
    if section_marker in dest_content:
        # Replace existing trent section with new one
        if section_marker in source_content:
            # Extract trent section from source
            start_idx = source_content.find(section_marker)
            end_idx = source_content.find(section_end)
            if end_idx == -1:
                end_idx = len(source_content)
            else:
                end_idx += len(section_end)
            new_section = source_content[start_idx:end_idx]
            
            # Replace in destination
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
            # Source doesn't have section markers either - append whole source
            return dest_content.rstrip() + '\n\n---\n\n' + source_content
    
    return dest_content


async def execute(
    target_path: str,
    source_path: str = DEFAULT_SOURCE_PATH,
    force_overwrite: bool = False,
    dry_run: bool = False,
    skip_project_files: bool = False,
    context: dict = None
) -> dict:
    """
    Install complete trent development environment from source repository.
    """
    config = context.get('config', _config) if context else _config

    # Store original paths for reporting
    original_target_path = target_path
    original_source_path = source_path
    
    # Translate Windows paths if running in Docker container
    if os.path.exists('/mnt'):
        target_path = _translate_windows_path(target_path)
        source_path = _translate_windows_path(source_path)
        if target_path != original_target_path:
            logger.info(f"Translated target: {original_target_path} -> {target_path}")
        if source_path != original_source_path:
            logger.info(f"Translated source: {original_source_path} -> {source_path}")

    logger.info(f"Full install from: {source_path} to: {target_path}")
    logger.info(f"dry_run: {dry_run}, force_overwrite: {force_overwrite}")

    # Validate paths
    try:
        target = Path(target_path).resolve()
        source = Path(source_path).resolve()
        
        if not dry_run:
            target.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        return {
            'success': False,
            'error': f"Invalid path: {e}",
            'hint': "Ensure Docker has access to the drives (G:, P:, M: are mounted)."
        }

    if not source.exists():
        return {
            'success': False,
            'error': f"Source repository not found: {source}",
            'hint': f"Expected trent_rules at {original_source_path}"
        }

    # Check OS capabilities
    os_info = _get_os_info()

    result = {
        'success': False,
        'target_path': original_target_path,
        'source_path': original_source_path,
        'target_path_resolved': str(target),
        'source_path_resolved': str(source),
        'os_info': os_info,
        'dry_run': dry_run,
        'copied_files': [],
        'skipped_files': [],
        'merged_files': [],
        'created_dirs': [],
        'warnings': [],
        'operation_time_seconds': 0
    }

    start_time = datetime.now()

    try:
        # 1. Copy .cursor folder (full, not templates)
        cursor_source = source / '.cursor'
        cursor_dest = target / '.cursor'
        if cursor_source.exists():
            logger.info("Copying .cursor folder...")
            if dry_run:
                file_count = _count_files(cursor_source)
                result['copied_files'].append({
                    'directory': '.cursor',
                    'action': 'would_copy',
                    'file_count': file_count
                })
            else:
                copied = await _merge_directories(
                    cursor_source, cursor_dest, force_overwrite, os_info,
                    exclude_patterns=['logs/', 'metrics/', 'mcp.json']
                )
                result['copied_files'].extend(copied['copied'])
                result['skipped_files'].extend(copied['skipped'])
        else:
            result['warnings'].append(".cursor folder not found in source")

        # 2. Copy .trent folder (from template, not populated)
        trent_template = source / '.trent_template'
        trent_dest = target / '.trent'
        if trent_template.exists():
            logger.info("Copying .trent templates...")
            if dry_run:
                file_count = _count_files(trent_template)
                result['copied_files'].append({
                    'directory': '.trent',
                    'action': 'would_copy',
                    'file_count': file_count
                })
            else:
                copied = await _merge_directories(
                    trent_template, trent_dest, force_overwrite, os_info,
                    exclude_patterns=['examples/']
                )
                result['copied_files'].extend(copied['copied'])
                result['skipped_files'].extend(copied['skipped'])
        else:
            result['warnings'].append(".trent_template folder not found in source")

        # 3. Create empty docs/ folder
        docs_dest = target / 'docs'
        if dry_run:
            result['created_dirs'].append('docs/')
        else:
            docs_dest.mkdir(parents=True, exist_ok=True)
            gitkeep = docs_dest / '.gitkeep'
            if not gitkeep.exists():
                gitkeep.write_text('')
                result['copied_files'].append(str(gitkeep))
            result['created_dirs'].append('docs/')

        # 4. Create empty temp_scripts/ folder
        temp_scripts_dest = target / 'temp_scripts'
        if dry_run:
            result['created_dirs'].append('temp_scripts/')
        else:
            temp_scripts_dest.mkdir(parents=True, exist_ok=True)
            gitkeep = temp_scripts_dest / '.gitkeep'
            if not gitkeep.exists():
                gitkeep.write_text('')
                result['copied_files'].append(str(gitkeep))
            result['created_dirs'].append('temp_scripts/')

        # 5. Copy index files
        index_files = ['AGENTS_INDEX.md', 'SKILLS_INDEX.md', 'COMMANDS_INDEX.md', 'HOOKS_INDEX.md', 'RULES_INDEX.md']
        for filename in index_files:
            source_file = source / filename
            dest_file = target / filename
            
            if source_file.exists():
                if dry_run:
                    result['copied_files'].append({
                        'file': filename,
                        'action': 'would_copy'
                    })
                else:
                    if dest_file.exists() and not force_overwrite:
                        result['skipped_files'].append(str(dest_file))
                    else:
                        try:
                            shutil.copy2(str(source_file), str(dest_file))
                            result['copied_files'].append(str(dest_file))
                            logger.info(f"Copied: {filename}")
                        except Exception as e:
                            logger.warning(f"Failed to copy {filename}: {e}")
                            result['skipped_files'].append(str(dest_file))

        # 6. Handle agents.md and CLAUDE.md (merge or skip)
        if not skip_project_files:
            for filename in ['agents.md', 'CLAUDE.md']:
                source_file = source / 'template' / filename
                if not source_file.exists():
                    source_file = source / filename
                
                dest_file = target / filename
                
                if source_file.exists():
                    if dry_run:
                        if dest_file.exists():
                            result['merged_files'].append({
                                'file': filename,
                                'action': 'would_merge'
                            })
                        else:
                            result['copied_files'].append({
                                'file': filename,
                                'action': 'would_copy'
                            })
                    else:
                        source_content = source_file.read_text(encoding='utf-8')
                        
                        if dest_file.exists():
                            # Merge with existing
                            dest_content = dest_file.read_text(encoding='utf-8')
                            merged_content = _merge_markdown_files(
                                source_content, dest_content, filename
                            )
                            dest_file.write_text(merged_content, encoding='utf-8')
                            result['merged_files'].append(str(dest_file))
                            logger.info(f"Merged: {filename}")
                        else:
                            # Copy new
                            dest_file.write_text(source_content, encoding='utf-8')
                            result['copied_files'].append(str(dest_file))
                            logger.info(f"Copied: {filename}")
                else:
                    result['warnings'].append(f"{filename} not found in source")

        result['operation_time_seconds'] = round((datetime.now() - start_time).total_seconds(), 2)
        result['success'] = True
        
        total_items = len(result['copied_files']) + len(result['merged_files']) + len(result['created_dirs'])
        result['message'] = (
            f"Successfully installed {total_items} items in {result['operation_time_seconds']}s"
            if not dry_run else
            f"Dry run: would install {total_items} items"
        )

        return result

    except Exception as e:
        logger.error(f"Full install failed: {e}")
        result['operation_time_seconds'] = round((datetime.now() - start_time).total_seconds(), 2)
        result['error'] = str(e)
        return result


def _get_os_info() -> dict:
    """Get OS information and capabilities."""
    is_windows = platform.system() == 'Windows'
    can_create_symlinks = not is_windows or _check_windows_symlink_capability()

    return {
        'platform': platform.system(),
        'is_windows': is_windows,
        'can_create_symlinks': can_create_symlinks,
        'python_version': sys.version,
        'machine': platform.machine()
    }


def _check_windows_symlink_capability() -> bool:
    """Check if Windows can create symlinks."""
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
    os_info: dict,
    exclude_patterns: List[str] = None
) -> dict:
    """Merge source directory into destination without destroying existing content."""
    result = {'copied': [], 'skipped': []}
    exclude_patterns = exclude_patterns or []

    if not source.exists():
        return result

    dest.mkdir(parents=True, exist_ok=True)

    for item in source.iterdir():
        # Check exclusions
        rel_path = str(item.relative_to(source))
        if any(pattern.rstrip('/') in rel_path for pattern in exclude_patterns):
            continue

        source_item = source / item.name
        dest_item = dest / item.name

        if source_item.is_dir():
            sub_result = await _merge_directories(
                source_item, dest_item, force_overwrite, os_info, exclude_patterns
            )
            result['copied'].extend(sub_result['copied'])
            result['skipped'].extend(sub_result['skipped'])
        else:
            if dest_item.exists() and not force_overwrite:
                result['skipped'].append(str(dest_item))
            else:
                try:
                    if source_item.is_symlink():
                        if os_info['can_create_symlinks']:
                            if dest_item.exists():
                                dest_item.unlink()
                            dest_item.symlink_to(source_item.readlink())
                        else:
                            await asyncio.to_thread(
                                shutil.copy2, str(source_item.resolve()), str(dest_item)
                            )
                    else:
                        await asyncio.to_thread(
                            shutil.copy2, str(source_item), str(dest_item)
                        )
                    result['copied'].append(str(dest_item))
                except Exception as e:
                    logger.warning(f"Failed to copy {source_item}: {e}")
                    result['skipped'].append(str(dest_item))

    return result
