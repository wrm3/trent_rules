# session-start.ps1 - Claude Code hook for session initialization
# Triggered when a new composer conversation is created

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $sessionId = $eventData.session_id
    $composerMode = $eventData.composer_mode
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $sessionId = "unknown"
    $composerMode = "unknown"
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# Create log directory
$logDir = ".claude/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Date prefix for log files (allows easy cleanup of older logs)
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_session_lifecycle.log"

# Log session start
$logEntry = "[$timestamp] [SESSION_START] Session: $sessionId | Mode: $composerMode"
Add-Content -Path $logFile -Value $logEntry

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

        $healthUrl = "$mcpUrlFb/memory/health"
        Invoke-WebRequest -Uri $healthUrl -UseBasicParsing -TimeoutSec 3 -ErrorAction Stop | Out-Null

        $lines = Get-Content $fallbackFile
        $failedLines = @()
        foreach ($line in $lines) {
            $line = $line.Trim()
            if (-not $line) { continue }
            try {
                $headers = @{ "Content-Type" = "application/json" }
                Invoke-WebRequest -Uri "$mcpUrlFb/memory/ingest" -Method POST -Body $line -Headers $headers -UseBasicParsing -TimeoutSec 30 -ErrorAction Stop | Out-Null
                Add-Content -Path $logFile -Value "[$timestamp] [FALLBACK] Drained 1 record"
            } catch {
                $failedLines += $line
            }
        }

        if ($failedLines.Count -eq 0) {
            Remove-Item $fallbackFile -ErrorAction SilentlyContinue
        } else {
            Set-Content -Path $fallbackFile -Value ($failedLines -join "`n") -Encoding UTF8
        }
    } catch {
        Add-Content -Path $logFile -Value "[$timestamp] [FALLBACK] Server unavailable — preserving fallback"
    }
}

# Output response (allow session to continue, optionally inject context)
$response = @{
    continue = $true
    additional_context = "trent task management system is active. Check .trent/TASKS.md for current tasks."
}

$response | ConvertTo-Json -Compress
exit 0
