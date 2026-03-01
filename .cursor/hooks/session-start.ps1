# session-start.ps1 - Cursor hook for session initialization
# Triggered when a new composer conversation is created.
# Injects past agent-memory context so the AI has continuity across sessions.

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData    = $inputJson | ConvertFrom-Json
    $sessionId    = $eventData.session_id
    $composerMode = $eventData.composer_mode
    $timestamp    = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $sessionId    = "unknown"
    $composerMode = "unknown"
    $timestamp    = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# ── Logging ──────────────────────────────────────────────────────────────────
$logDir = ".cursor/logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile    = "$logDir/${datePrefix}_session_lifecycle.log"

$logEntry = "[$timestamp] [SESSION_START] Session: $sessionId | Mode: $composerMode"
Add-Content -Path $logFile -Value $logEntry

# ── Memory Context Retrieval ─────────────────────────────────────────────────
$additionalContext = "trent task management system is active. Check .trent/TASKS.md for current tasks."

$projectIdFile = ".trent/.project_id"
if (Test-Path $projectIdFile) {
    $projectId = (Get-Content $projectIdFile -Raw).Trim()

    if ($projectId -ne "") {
        try {
            # Call the trent memory REST bridge (synchronous — hook waits for this)
            $mcpUrl = "http://localhost:8082"
            $contextUrl = "$mcpUrl/memory/context?project_id=$projectId&max_tokens=3000&platform=cursor"

            $resp = Invoke-WebRequest -Uri $contextUrl -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
            $body = $resp.Content | ConvertFrom-Json

            if ($body.success -and $body.context -ne "") {
                $memoryContext = $body.context
                $additionalContext = @"
$memoryContext

---
trent task management system is active. Check .trent/TASKS.md for current tasks.
"@
                Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Injected context: sessions=$($body.sessions_included) captures=$($body.captures_included)"
            }
        } catch {
            # Memory bridge unavailable — fall back to default context silently
            Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Context fetch failed (bridge unavailable): $_"
        }
    }
}

# ── Response ─────────────────────────────────────────────────────────────────
$response = @{
    continue           = $true
    additional_context = $additionalContext
}

$response | ConvertTo-Json -Compress
exit 0
