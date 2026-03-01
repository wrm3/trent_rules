# agent-complete.ps1 - Claude Code hook for agent/stop lifecycle
# Triggered when the agent loop ends

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $status = $eventData.status
    $loopCount = $eventData.loop_count
    # Claude Code Stop hook provides session_id; fallback to conversation_id for older versions
    $sessionId = if ($eventData.session_id) { $eventData.session_id } elseif ($eventData.conversation_id) { $eventData.conversation_id } else { "unknown" }
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $status = "unknown"
    $loopCount = 0
    $sessionId = "unknown"
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# Create log directory
$logDir = ".claude/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_agent_lifecycle.log"

# Log agent completion
$logEntry = "[$timestamp] [STOP] Session: $sessionId | Status: $status | Loops: $loopCount"
Add-Content -Path $logFile -Value $logEntry

# Create metrics directory
$metricsDir = ".claude/metrics"
if (-not (Test-Path $metricsDir)) {
    New-Item -ItemType Directory -Path $metricsDir -Force | Out-Null
}

$metricsFile = "$metricsDir/${datePrefix}_completions.csv"
$csvEntry = "$timestamp,$sessionId,$status,$loopCount"
Add-Content -Path $metricsFile -Value $csvEntry

# ── Memory Capture (async background job) ────────────────────────────────────
# Only attempt capture for real sessions (skip "unknown" IDs).
if ($sessionId -ne "unknown" -and $sessionId -ne "" -and $sessionId -ne $null) {
    $projectPath = (Get-Location).Path

    # Find claude_adapter.py — check .claude/hooks/ first, then .cursor/hooks/
    $adapterScript = $null
    foreach ($candidate in @(
        (Join-Path $PSScriptRoot "claude_adapter.py"),
        (Join-Path $projectPath ".claude\hooks\claude_adapter.py"),
        (Join-Path $projectPath ".cursor\hooks\claude_adapter.py")
    )) {
        if (Test-Path $candidate) {
            $adapterScript = $candidate
            break
        }
    }

    if ($adapterScript) {
        $adapterLog = "$logDir/${datePrefix}_memory_claude_adapter.log"
        $adapterArgs = @(
            $adapterScript,
            "--session-id", $sessionId,
            "--project-path", $projectPath,
            "--status", $(if ($status -eq "success") { "completed" } else { "partial" })
        )
        Start-Job -ScriptBlock {
            param($pythonExe, $args, $logFile)
            $output = & $pythonExe @args 2>&1
            $output | Add-Content -Path $logFile
        } -ArgumentList "python", $adapterArgs, $adapterLog | Out-Null
        Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Adapter job started for session $sessionId"
    } else {
        Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] claude_adapter.py not found — skipping"
    }
}

# Output empty response (no follow-up message)
$response = @{}
$response | ConvertTo-Json -Compress
exit 0
