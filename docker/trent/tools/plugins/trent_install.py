"""
trent_install Plugin

Install or upgrade the full trent development environment to a project directory.
Works for both first-time installs and upgrades of existing installations,
including remote containers — no drive mounts needed.

HOW IT WORKS:
  1. Call trent_install(target_path=...) to get a ready-to-run shell command
  2. Run the shell command — it downloads a ZIP from this MCP server's
     /install/download endpoint and unzips it into target_path
  3. No GitHub API calls, no drive mounts, works on remote containers

MERGE HANDLING (agents.md / CLAUDE.md / GEMINI.md):
  For upgrades, read those files locally and pass their content via existing_files.
  The server merges the trent-managed section while preserving your custom content.

GUARDRAILS.md:
  Omitted from the ZIP by default (skip_files). Pass skip_files=[] to overwrite it.
"""
import json
import logging

logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install"

TOOL_DESCRIPTION = (
    "Install or upgrade the full trent development environment to a project directory. "
    "Required parameter: target_path (the local directory path to install into). "
    "Returns a shell command (PowerShell + bash) to run locally — works with remote containers, no drive mounts needed. "
    "The command downloads template_v2/ as a ZIP from this MCP server and unzips it into target_path. "
    "For upgrades: pass existing_files with current content of agents.md/CLAUDE.md/GEMINI.md "
    "so the trent section is updated while your custom content is preserved. "
    "GUARDRAILS.md is preserved by default (pass skip_files=[] to overwrite it)."
)

TOOL_PARAMS = {
    "target_path": (
        "Target project directory to install trent into (required). "
        "Use the exact local path as it appears on your filesystem, "
        "e.g. 'G:\\\\MyProject' or '/home/user/myproject'."
    ),
    "existing_files": (
        "Optional dict of {filename: content} for files to merge rather than overwrite. "
        "Supported keys: 'agents.md', 'CLAUDE.md', 'GEMINI.md'. "
        "Read these files locally before calling this tool and pass their content here."
    ),
    "skip_files": (
        "Optional list of filenames to omit from the ZIP. "
        "Default: ['GUARDRAILS.md']. Pass [] to overwrite GUARDRAILS.md too."
    ),
    "dry_run": "Preview the command without running it (default: False)",
}

_config = None


def setup(context: dict):
    global _config
    _config = context.get('config', {})


async def execute(
    target_path: str,
    existing_files: dict = None,
    skip_files: list = None,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """Return a shell command that downloads and installs trent into target_path."""
    cfg = (context or {}).get('config', _config or {})
    trent_url = cfg.get('trent_url', 'http://localhost:8082').rstrip('/')
    endpoint = f"{trent_url}/install/download"

    if skip_files is None:
        skip_files = ['GUARDRAILS.md']

    # Build POST body (only needed when merging or skipping files)
    needs_post = bool(existing_files or skip_files)
    body = {}
    if existing_files:
        body['existing_files'] = existing_files
    if skip_files:
        body['skip_files'] = skip_files

    if dry_run:
        return {
            'success': True,
            'tool': 'trent_install',
            'target_path': target_path,
            'dry_run': True,
            'endpoint': endpoint,
            'needs_post': needs_post,
            'skip_files': skip_files,
            'existing_files_keys': list((existing_files or {}).keys()),
        }

    if needs_post:
        ps_body = json.dumps(body).replace('"', '\\"')
        ps_cmd = (
            f"$body = \"{ps_body}\"; "
            f"$tmp = [System.IO.Path]::GetTempFileName() + '.zip'; "
            f"Invoke-WebRequest -Uri '{endpoint}' -Method POST "
            f"-ContentType 'application/json' -Body $body -OutFile $tmp; "
            f"Expand-Archive -Path $tmp -DestinationPath '{target_path}' -Force; "
            f"Remove-Item $tmp"
        )
        bash_body = json.dumps(body).replace("'", "'\"'\"'")
        bash_cmd = (
            f"curl -sL -X POST '{endpoint}' "
            f"-H 'Content-Type: application/json' "
            f"-d '{bash_body}' "
            f"-o /tmp/trent_install.zip && "
            f"unzip -o /tmp/trent_install.zip -d '{target_path}' && "
            f"rm /tmp/trent_install.zip"
        )
    else:
        ps_cmd = (
            f"$tmp = [System.IO.Path]::GetTempFileName() + '.zip'; "
            f"Invoke-WebRequest -Uri '{endpoint}' -OutFile $tmp; "
            f"Expand-Archive -Path $tmp -DestinationPath '{target_path}' -Force; "
            f"Remove-Item $tmp"
        )
        bash_cmd = (
            f"curl -sL '{endpoint}' -o /tmp/trent_install.zip && "
            f"unzip -o /tmp/trent_install.zip -d '{target_path}' && "
            f"rm /tmp/trent_install.zip"
        )

    merge_note = f" Merged: {list(existing_files.keys())}." if existing_files else ''
    skip_note = f" Preserved (skipped): {skip_files}." if skip_files else ''

    # Post-install: generate .project_id and run user setup
    project_name = target_path.replace('\\', '/').rstrip('/').split('/')[-1].lower().replace(' ', '-')[:20]
    post_install_ps = (
        f"$hash = (python -c \"import hashlib; print(hashlib.sha256(r'{target_path}'.encode()).hexdigest()[:8])\") 2>$null; "
        f"if (-not $hash) {{ $hash = (Get-Random -Maximum 99999999).ToString('x8') }}; "
        f"$projId = 'proj-{project_name}-' + $hash; "
        f"Set-Content -Path '{target_path}\\.trent\\.project_id' -Value $projId; "
        f"Write-Host \"Project ID: $projId\"; "
        f"powershell -ExecutionPolicy Bypass -File '{target_path}\\.cursor\\hooks\\trent-setup-user.ps1'"
    )
    post_install_bash = (
        f"hash=$(python3 -c \"import hashlib; print(hashlib.sha256('{target_path}'.encode()).hexdigest()[:8])\"); "
        f"echo \"proj-{project_name}-$hash\" > '{target_path}/.trent/.project_id'; "
        f"echo \"Project ID: proj-{project_name}-$hash\"; "
        f"bash '{target_path}/.cursor/hooks/trent-setup-user.sh' 2>/dev/null || echo 'Run trent-setup-user.ps1 on Windows'"
    )

    return {
        'success': True,
        'tool': 'trent_install',
        'target_path': target_path,
        'shell_command': {
            'powershell': ps_cmd,
            'bash': bash_cmd,
        },
        'post_install': {
            'powershell': post_install_ps,
            'bash': post_install_bash,
        },
        'instructions': (
            f"STEP 1: Run shell_command to install trent into '{target_path}'."
            f"{merge_note}{skip_note} "
            f"STEP 2: Run post_install to generate .project_id and set up user config (~/.trent/user_config.json)."
        ),
        'upgrade_hint': (
            "For upgrades: read agents.md/CLAUDE.md/GEMINI.md locally first and pass "
            "their content as existing_files to preserve your customizations."
        ),
    }
