"""
install_rest.py — REST endpoint for trent template downloads.

Provides a single HTTP endpoint that packages /app/template_v2/ as a ZIP
and streams it to the caller. Used by the trent_install MCP tool so that
any AI agent (local or remote container) can install trent by running a
single shell command — no drive mounts, no GitHub API calls needed.

Endpoints:
  POST /install/download  — stream template_v2/ as ZIP (token required)

Token lifecycle:
  1. trent_install tool calls issue_token() to get a one-time token
  2. Tool returns the token embedded in a ready-to-run shell command
  3. AI runs the shell command; it POSTs to this endpoint with the token
  4. Token is consumed (one-time use, 5-min TTL) and ZIP is streamed back
  5. Shell unzips directly into the target project directory

Merge handling:
  For agents.md, CLAUDE.md, GEMINI.md: if the caller supplies the current
  file content in the POST body (existing_files dict), merge_markdown_file()
  is called so the trent-managed section is updated while preserving all
  user content outside the markers.

  For GUARDRAILS.md (skip_if_exists): if the caller flags it, the file is
  omitted from the ZIP so the existing copy on disk is never overwritten.
"""
import io
import json
import logging
import secrets
import time
import zipfile
from pathlib import Path
from typing import Optional

from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

logger = logging.getLogger(__name__)

TEMPLATE_DIR = Path("/app/template_v2")

# One-time tokens: token -> expiry_timestamp
_pending_tokens: dict[str, float] = {}

TOKEN_TTL_SECONDS = 300  # 5 minutes


def issue_token() -> str:
    """Issue a one-time download token (called by trent_install tool)."""
    token = secrets.token_urlsafe(16)
    _pending_tokens[token] = time.time() + TOKEN_TTL_SECONDS
    return token


def _consume_token(token: str) -> bool:
    """Validate and consume a token. Returns True if valid."""
    expiry = _pending_tokens.pop(token, None)
    return expiry is not None and time.time() < expiry


async def download(request: Request):
    """
    POST /install/download

    Body (JSON):
      token           str   required  one-time token from trent_install
      existing_files  dict  optional  {"agents.md": "<content>", ...} for merge
      skip_files      list  optional  ["GUARDRAILS.md"] — omit from ZIP

    Returns: application/zip stream
    """
    try:
        body = await request.json()
    except Exception:
        body = {}

    token = body.get("token", "")
    if not token or not _consume_token(token):
        return JSONResponse(
            {"error": "invalid or expired token"},
            status_code=401,
        )

    if not TEMPLATE_DIR.exists():
        return JSONResponse(
            {"error": f"template directory not found: {TEMPLATE_DIR}"},
            status_code=500,
        )

    existing_files: dict[str, str] = body.get("existing_files") or {}
    skip_files: set[str] = {f.lower() for f in (body.get("skip_files") or [])}

    # Import merge logic from _trent_shared (same package)
    try:
        from .tools.plugins._trent_shared import merge_markdown_file, MERGEABLE_FILES
    except ImportError:
        merge_markdown_file = None
        MERGEABLE_FILES = set()

    buf = io.BytesIO()
    files_included = []
    files_skipped = []
    files_merged = []

    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(TEMPLATE_DIR.rglob("*")):
            if not path.is_file():
                continue

            # Arc name strips /app/template_v2/ prefix so files land at project root
            arcname = str(path.relative_to(TEMPLATE_DIR))
            filename_lower = path.name.lower()

            # Skip files flagged by caller (e.g. GUARDRAILS.md on upgrade)
            if filename_lower in skip_files:
                files_skipped.append(arcname)
                continue

            content = path.read_bytes()

            # Merge logic for agents.md / CLAUDE.md / GEMINI.md
            if (
                merge_markdown_file is not None
                and filename_lower in MERGEABLE_FILES
                and path.name in existing_files
            ):
                source_text = content.decode("utf-8", errors="replace")
                dest_text = existing_files[path.name]
                merged_text = merge_markdown_file(source_text, dest_text, path.name)
                content = merged_text.encode("utf-8")
                files_merged.append(arcname)
            else:
                files_included.append(arcname)

            zf.writestr(arcname, content)

    buf.seek(0)
    zip_bytes = buf.read()

    logger.info(
        f"install_rest: serving ZIP — "
        f"{len(files_included) + len(files_merged)} files "
        f"({len(files_merged)} merged, {len(files_skipped)} skipped), "
        f"{len(zip_bytes):,} bytes"
    )

    return Response(
        content=zip_bytes,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=trent_template.zip"},
    )


INSTALL_ROUTES = [
    Route("/install/download", endpoint=download, methods=["POST"]),
]


def init_install_rest(config: Optional[dict] = None) -> None:
    """Called from server.py after components are initialized."""
    logger.info(
        f"install_rest: initialized (template_dir={TEMPLATE_DIR}, "
        f"exists={TEMPLATE_DIR.exists()})"
    )
