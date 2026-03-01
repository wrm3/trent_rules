# agent-complete.ps1 - Cursor hook for agent/stop lifecycle
# Triggered when the agent loop ends.
# Captures the conversation into trent agent memory (async, best-effort).

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData    = $inputJson | ConvertFrom-Json
    $status       = $eventData.status
    $loopCount    = $eventData.loop_count
    $conversationId = $eventData.conversation_id
    $timestamp    = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $status         = "unknown"
    $loopCount      = 0
    $conversationId = "unknown"
    $timestamp      = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# ── Directories ──────────────────────────────────────────────────────────────
$logDir = ".cursor/logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$metricsDir = ".cursor/metrics"
if (-not (Test-Path $metricsDir)) { New-Item -ItemType Directory -Path $metricsDir -Force | Out-Null }

$datePrefix  = Get-Date -Format "yyyy-MM-dd"
$logFile     = "$logDir/${datePrefix}_agent_lifecycle.log"
$metricsFile = "$metricsDir/${datePrefix}_completions.csv"

# ── Log the completion event ─────────────────────────────────────────────────
$logEntry = "[$timestamp] [STOP] Conversation: $conversationId | Status: $status | Loops: $loopCount"
Add-Content -Path $logFile -Value $logEntry

$csvEntry = "$timestamp,$conversationId,$status,$loopCount"
Add-Content -Path $metricsFile -Value $csvEntry

# ── Memory Capture (async background job) ────────────────────────────────────
# Only attempt capture for real conversations (skip "unknown" IDs).
if ($conversationId -ne "unknown" -and $conversationId -ne "" -and $conversationId -ne $null) {

    # Resolve the project path (the hook runs from the workspace root)
    $projectPath = (Get-Location).Path

    # Build the python command arguments — no multi-line python -c!
    # cursor_adapter.py uses stdlib only, so any system Python works.
    $adapterScript = Join-Path $PSScriptRoot "cursor_adapter.py"

    if (Test-Path $adapterScript) {
        # Run in a background job so the hook returns immediately to Cursor.
        # Output goes to the adapter log file (not consumed by Cursor).
        $adapterLog = "$logDir/${datePrefix}_memory_adapter.log"

        $jobArgs = @(
            $adapterScript,
            "--conversation-id", $conversationId,
            "--project-path",    $projectPath,
            "--loop-count",      $loopCount,
            "--status",          $(if ($status -eq "success") { "completed" } else { "partial" })
        )

        # Start-Job runs in a subprocess — safe for long-running I/O
        Start-Job -ScriptBlock {
            param($pythonExe, $args, $logFile)
            $output = & $pythonExe @args 2>&1
            $output | Add-Content -Path $logFile
        } -ArgumentList "python", $jobArgs, $adapterLog | Out-Null

        Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Adapter job started for $conversationId"
    } else {
        Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] cursor_adapter.py not found at $adapterScript — skipping"
    }
}

# ── Response (no follow-up message to Cursor) ─────────────────────────────────
$response = @{}
$response | ConvertTo-Json -Compress
exit 0
