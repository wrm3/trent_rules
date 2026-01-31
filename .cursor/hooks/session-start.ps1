# session-start.ps1 - Cursor hook for session initialization
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
$logDir = ".cursor/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Date prefix for log files (allows easy cleanup of older logs)
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_session_lifecycle.log"

# Log session start
$logEntry = "[$timestamp] [SESSION_START] Session: $sessionId | Mode: $composerMode"
Add-Content -Path $logFile -Value $logEntry

# Output response (allow session to continue, optionally inject context)
$response = @{
    continue = $true
    additional_context = "trent task management system is active. Check .trent/TASKS.md for current tasks."
}

$response | ConvertTo-Json -Compress
exit 0
