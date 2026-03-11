# agent-complete.ps1 - Cursor hook for agent/stop lifecycle
# Triggered when the agent loop ends.
# Captures the conversation into trent agent memory (async, best-effort).

$inputJson = $input | Out-String

try {
    $eventData      = $inputJson | ConvertFrom-Json
    $status         = $eventData.status
    $loopCount      = $eventData.loop_count
    $conversationId = $eventData.conversation_id
} catch {
    $status         = "unknown"
    $loopCount      = 0
    $conversationId = "unknown"
}

# ── Memory Capture (async background job) ────────────────────────────────────
$projectPath   = (Get-Location).Path
$adapterScript = Join-Path $PSScriptRoot "cursor_adapter.py"

if (Test-Path $adapterScript) {
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

    Start-Job -ScriptBlock {
        param($pythonExe, $args)
        & $pythonExe @args 2>&1 | Out-Null
    } -ArgumentList "python", $jobArgs | Out-Null
}

# ── Reflection hint file ─────────────────────────────────────────────────────
# If the session had enough loops (≥5), write a pending_reflection.json so that
# session-start.ps1 injects a memory-check reminder on the NEXT session.
if ([int]$loopCount -ge 5) {
    try {
        $logsDir = ".trent/logs"
        if (-not (Test-Path $logsDir)) { New-Item -ItemType Directory -Path $logsDir -Force | Out-Null }
        $reflectionData = @{
            conversation_id = $conversationId
            loop_count      = [int]$loopCount
            status          = $status
        }
        $reflectionData | ConvertTo-Json -Compress | Set-Content -Path "$logsDir/pending_reflection.json" -Encoding UTF8
    } catch {}
}

$response = @{}
$response | ConvertTo-Json -Compress
exit 0
