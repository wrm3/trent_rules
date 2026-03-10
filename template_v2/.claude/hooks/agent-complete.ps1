# agent-complete.ps1 - Claude Code hook for agent/stop lifecycle
# Triggered when the agent loop ends

$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $status = $eventData.status
    $loopCount = $eventData.loop_count
    $sessionId = if ($eventData.session_id) { $eventData.session_id } elseif ($eventData.conversation_id) { $eventData.conversation_id } else { "unknown" }
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $status = "unknown"
    $loopCount = 0
    $sessionId = "unknown"
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# ── Memory Capture (async background job) ────────────────────────────────────
if ($sessionId -ne "unknown" -and $sessionId -ne "" -and $sessionId -ne $null) {
    $projectPath = (Get-Location).Path

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
        $adapterArgs = @(
            $adapterScript,
            "--session-id", $sessionId,
            "--project-path", $projectPath,
            "--status", $(if ($status -eq "success") { "completed" } else { "partial" })
        )
        Start-Job -ScriptBlock {
            param($pythonExe, $args)
            & $pythonExe @args 2>&1 | Out-Null
        } -ArgumentList "python", $adapterArgs | Out-Null
    }
}

$response = @{}
$response | ConvertTo-Json -Compress
exit 0
