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
# Always attempt capture. cursor_adapter.py will auto-detect the conversation
# from state.vscdb if Cursor didn't pass conversation_id in the hook payload
# (which is normal — most Cursor versions don't include it).
$projectPath = (Get-Location).Path
$adapterScript = Join-Path $PSScriptRoot "cursor_adapter.py"

if (Test-Path $adapterScript) {
    $adapterLog = "$logDir/${datePrefix}_memory_adapter.log"

    # Pass conversation_id if we have it; adapter auto-detects if "unknown"
    $jobArgs = @(
        $adapterScript,
        "--project-path", $projectPath,
        "--loop-count",   $loopCount,
        "--status",       $(if ($status -eq "success") { "completed" } else { "partial" })
    )
    if ($conversationId -and $conversationId -ne "unknown") {
        $jobArgs += "--conversation-id"
        $jobArgs += $conversationId
    }

    # Start-Job runs in a subprocess — returns immediately to Cursor
    Start-Job -ScriptBlock {
        param($pythonExe, $args, $logFile)
        $output = & $pythonExe @args 2>&1
        $output | Add-Content -Path $logFile
    } -ArgumentList "python", $jobArgs, $adapterLog | Out-Null

    Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Adapter job started (conv=$conversationId loops=$loopCount)"
} else {
    Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] cursor_adapter.py not found at $adapterScript — skipping"
}

# ── Reflection hint file ─────────────────────────────────────────────────────
# If the session had enough loops (≥5), write a pending_reflection.json so that
# session-start.ps1 injects a memory-check reminder on the NEXT session.
# This is the letta-code "step-count reflection trigger" adapted for Cursor hooks.
$reflectionThreshold = 5
if ([int]$loopCount -ge $reflectionThreshold) {
    try {
        $reflectionFile = "$logDir/pending_reflection.json"
        $reflectionData = @{
            conversation_id = $conversationId
            loop_count      = [int]$loopCount
            timestamp       = $timestamp
            status          = $status
        }
        $reflectionData | ConvertTo-Json -Compress | Set-Content -Path $reflectionFile -Encoding UTF8
        Add-Content -Path $logFile -Value "[$timestamp] [REFLECT] Wrote reflection hint ($loopCount loops)"
    } catch {
        Add-Content -Path $logFile -Value "[$timestamp] [REFLECT] Failed to write hint: $_"
    }
}

# ── Response (no follow-up message to Cursor) ─────────────────────────────────
$response = @{}
$response | ConvertTo-Json -Compress
exit 0
