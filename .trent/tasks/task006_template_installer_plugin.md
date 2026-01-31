---
id: 6
title: 'Create template installer plugin (OS-aware)'
type: task
status: pending
priority: high
phase: 0
subsystems: [mcp, template, installer]
project_context: 'Install trent template to new projects with OS-aware symlink/copy handling'
dependencies: [2]
estimated_effort: '2 hours'
---

# Task 006: Create Template Installer Plugin (OS-Aware)

## Objective
Create plugin tool that installs trent template files to new projects, with intelligent OS detection for symlink vs copy decisions.

## Sources
- `mcps/fstrent_mcp_tasks/server.py` - Existing template installer logic
- `mcps/fstrent_mcp_silicon_valley/tools/silicon_valley_setup.py` - Similar pattern

## Tools to Create

### template_install.py
```python
@tool
async def template_install(
    target_path: str,
    variant: str = "minimal",  # "minimal" or "full"
    link_strategy: str = "auto",  # "auto", "copy", "symlink"
    force_overwrite: bool = False
) -> InstallResult:
    """
    Install trent template to target project.

    OS Detection:
    - Windows: Default to copy (symlinks require admin/dev mode)
    - macOS/Linux: Default to symlink for shared resources

    Variants:
    - minimal: Core task management only
    - full: All skills, agents, commands
    """
```

### template_check.py
```python
@tool
async def template_check(
    target_path: str
) -> CheckResult:
    """Check if trent is installed and current version"""
```

### template_update.py
```python
@tool
async def template_update(
    target_path: str,
    merge_strategy: str = "preserve"  # "preserve", "overwrite", "interactive"
) -> UpdateResult:
    """Update existing trent installation"""
```

## OS Detection Logic
```python
import platform
import os

def get_link_strategy() -> str:
    system = platform.system()

    if system == "Windows":
        # Check if Developer Mode is enabled
        try:
            import winreg
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock"
            )
            value, _ = winreg.QueryValueEx(key, "AllowDevelopmentWithoutDevLicense")
            if value == 1:
                return "symlink"
        except:
            pass
        return "copy"  # Safe default for Windows

    elif system in ("Darwin", "Linux"):
        return "symlink"  # Native support

    return "copy"  # Unknown OS fallback
```

## Template Contents

### Minimal Variant
```
.trent/
├── PLAN.md
├── TASKS.md
├── PROJECT_CONTEXT.md
├── tasks/
└── phases/

.claude/ (or .cursor/)
├── commands/trent-*.md
└── rules/trent/
```

### Full Variant
```
(All of minimal plus)
.claude/
├── agents/
├── skills/
│   ├── fstrent-task-management/
│   ├── fstrent-planning/
│   ├── fstrent-qa/
│   └── fstrent-code-reviewer/
└── rules/
```

## Acceptance Criteria
- [ ] Plugin loads via plugin_loader
- [ ] OS detection works (Windows/Mac/Linux)
- [ ] Minimal variant installs correctly
- [ ] Full variant installs correctly
- [ ] Symlinks work on Mac/Linux
- [ ] Copy fallback works on Windows
- [ ] Existing files preserved (unless force_overwrite)
- [ ] Reports what was installed

## Notes
- Template source files should be bundled with MCP or fetched from known location
- Consider version tracking for updates
- Handle partial installations gracefully
