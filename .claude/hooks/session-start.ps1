# session-start.ps1 - Claude Code hook for session initialization
# Triggered when a new composer conversation is created

$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $sessionId = $eventData.session_id
} catch {
    $sessionId = "unknown"
}

# ── Fallback Drain ────────────────────────────────────────────────────────────
$fallbackFile = ".trent/memory_fallback.jsonl"
if (Test-Path $fallbackFile) {
    try {
        $mcpUrlFb = "http://localhost:8082"
        $userConfigPathFb = Join-Path $env:USERPROFILE ".trent\user_config.json"
        if (Test-Path $userConfigPathFb) {
            try {
                $ucFb = Get-Content $userConfigPathFb -Raw | ConvertFrom-Json
                if ($ucFb.mcp_url) { $mcpUrlFb = $ucFb.mcp_url.TrimEnd("/") }
            } catch {}
        }

        Invoke-WebRequest -Uri "$mcpUrlFb/memory/health" -UseBasicParsing -TimeoutSec 3 -ErrorAction Stop | Out-Null

        $lines = Get-Content $fallbackFile
        $failedLines = @()
        foreach ($line in $lines) {
            $line = $line.Trim()
            if (-not $line) { continue }
            try {
                $headers = @{ "Content-Type" = "application/json" }
                Invoke-WebRequest -Uri "$mcpUrlFb/memory/ingest" -Method POST -Body $line -Headers $headers -UseBasicParsing -TimeoutSec 30 -ErrorAction Stop | Out-Null
            } catch {
                $failedLines += $line
            }
        }

        if ($failedLines.Count -eq 0) {
            Remove-Item $fallbackFile -ErrorAction SilentlyContinue
        } else {
            Set-Content -Path $fallbackFile -Value ($failedLines -join "`n") -Encoding UTF8
        }
    } catch {}
}

$response = @{
    continue = $true
    additional_context = "trent task management system is active. Check .trent/TASKS.md for current tasks."
}

$response | ConvertTo-Json -Compress
exit 0
