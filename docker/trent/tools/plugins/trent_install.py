"""
trent_install Plugin

Install or upgrade the full trent development environment to a project directory.
Works for both first-time installs and upgrades of existing installations.

HOW IT WORKS (remote-container-safe):
  1. Call trent_install(target_path=...) — no filesystem access needed
  2. Tool returns a ready-to-run shell command (PowerShell or bash)
  3. Run the shell command — it downloads a ZIP from the MCP server's
     /install/download endpoint and unzips it into target_path
  4. No drive mounts, no GitHub API calls, works on remote containers

MERGE HANDLING (agents.md / CLAUDE.md / GEMINI.md):
  Pass the current content of any existing mergeable files via existing_files.
  The server merges the trent-managed section while preserving your custom content.
  Example:
    trent_install(
        target_path="G:\\MyProject",
        existing_files={
            "agents.md": open("G:\\MyProject\\agents.md").read(),
            "CLAUDE.md": open("G:\\MyProject\\CLAUDE.md").read(),
        }
    )

GUARDRAILS.md (skip-if-exists):
  If GUARDRAILS.md already exists and you want to keep it, pass
  skip_files=["GUARDRAILS.md"]. It will be omitted from the ZIP so
  your existing file is not overwritten.

See also:
  trent_plan_reset — Reset .trent/ to blank template (destroys task data!)
"""
import json
import logging

from ...install_rest import issue_token

logger = logging.getLogger(__name__)

# ============================================================
# PLUGIN METADATA (Required)
# ============================================================

TOOL_NAME = "trent_install"

TOOL_DESCRIPTION = (
    "Install or upgrade the full trent development environment to a project directory. "
    "Returns a shell command (PowerShell + bash) to run locally — no drive mounts needed, "
    "works with remote containers. "
    "The command downloads a ZIP of template_v2/ from the MCP server and unzips it into target_path. "
    "For upgrades: pass existing_files with the current content of agents.md/CLAUDE.md/GEMINI.md "
    "so the trent section is updated while your custom content is preserved. "
    "Pass skip_files=['GUARDRAILS.md'] to keep your existing GUARDRAILS.md untouched."
)

TOOL_PARAMS = {
    "target_path": (
        "Target project directory to install / upgrade trent into (required). "
        "Use the exact local path as it appears on your filesystem, e.g. 'G:\\\\MyProject' or '/home/user/myproject'."
    ),
    "existing_files": (
        "Optional dict of {filename: content} for files that should be merged rather than overwritten. "
        "Supported keys: 'agents.md', 'CLAUDE.md', 'GEMINI.md'. "
        "Read these files locally before calling this tool and pass their content here. "
        "The trent-managed section will be updated; all other content is preserved."
    ),
    "skip_files": (
        "Optional list of filenames to omit from the ZIP (never overwrite). "
        "Default: ['GUARDRAILS.md'] — pass an empty list to overwrite GUARDRAILS.md too."
    ),
    "dry_run": "Preview the command that would be run without actually generating a token (default: False)",
}

logger = logging.getLogger(__name__)

_config = None


def setup(context: dict):
    """Called once at plugin load time."""
    global _config
    _config = context.get('config', {})


async def execute(
    target_path: str,
    existing_files: dict = None,
    skip_files: list = None,
    dry_run: bool = False,
    context: dict = None,
) -> dict:
    """
    Generate a shell command to install trent into target_path.

    The command downloads template_v2/ as a ZIP from this MCP server's
    /install/download endpoint and unzips it directly into target_path.
    """
    cfg = (context or {}).get('config', _config or {})
    trent_url = cfg.get('trent_url', 'http://localhost:8082').rstrip('/')

    # Default: skip GUARDRAILS.md to preserve user-accumulated content
    if skip_files is None:
        skip_files = ['GUARDRAILS.md']

    if dry_run:
        return {
            'success': True,
            'tool': 'trent_install',
            'target_path': target_path,
            'dry_run': True,
            'message': (
                f"Dry run: would install template_v2/ from {trent_url}/install/download "
                f"into '{target_path}'. "
                f"Mergeable files: {list((existing_files or {}).keys())}. "
                f"Skip files: {skip_files}."
            ),
        }

    # Issue one-time download token
    token = issue_token()
    endpoint = f"{trent_url}/install/download"

    # Build the POST body the shell command will send
    body = {'token': token}
    if existing_files:
        body['existing_files'] = existing_files
    if skip_files:
        body['skip_files'] = skip_files

    body_json = json.dumps(body).replace("'", "\\'")

    # PowerShell command (Windows)
    ps_body = json.dumps(body).replace('"', '\\"')
    ps_cmd = (
        f"$body = '{ps_body}'; "
        f"$tmp = [System.IO.Path]::GetTempFileName() + '.zip'; "
        f"Invoke-WebRequest -Uri '{endpoint}' -Method POST "
        f"-ContentType 'application/json' -Body $body -OutFile $tmp; "
        f"Expand-Archive -Path $tmp -DestinationPath '{target_path}' -Force; "
        f"Remove-Item $tmp"
    )

    # bash command (Linux / macOS / remote container shell)
    bash_body = json.dumps(body).replace("'", "'\"'\"'")
    bash_cmd = (
        f"curl -sL -X POST '{endpoint}' "
        f"-H 'Content-Type: application/json' "
        f"-d '{bash_body}' "
        f"-o /tmp/trent_install.zip && "
        f"unzip -o /tmp/trent_install.zip -d '{target_path}' && "
        f"rm /tmp/trent_install.zip"
    )

    merge_note = ''
    if existing_files:
        merge_note = (
            f" Merged files: {list(existing_files.keys())}."
        )
    skip_note = f" Skipped (preserved): {skip_files}." if skip_files else ''

    return {
        'success': True,
        'tool': 'trent_install',
        'target_path': target_path,
        'shell_command': {
            'powershell': ps_cmd,
            'bash': bash_cmd,
        },
        'token_expires_seconds': 300,
        'instructions': (
            f"Run the shell_command for your OS to install trent into '{target_path}'. "
            f"The download token expires in 5 minutes.{merge_note}{skip_note}"
        ),
        'mergeable_files_hint': (
            "For upgrades, read agents.md / CLAUDE.md / GEMINI.md locally and pass their "
            "content as existing_files to preserve your customizations."
        ),
    }
