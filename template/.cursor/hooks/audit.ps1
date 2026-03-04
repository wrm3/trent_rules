# audit.ps1 - Cursor hook for auditing all events
# Generic audit hook that logs all JSON input

# Read JSON input from stdin
$inputJson = $input | Out-String
$timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"

# Create log directory
$logDir = ".cursor/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Get hook event name from input
try {
    $eventData = $inputJson | ConvertFrom-Json
    $hookEvent = $eventData.hook_event_name
    if (-not $hookEvent) { $hookEvent = "unknown" }
} catch {
    $hookEvent = "unknown"
}

# Date prefix for log files (allows easy cleanup of older logs)
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_agent-audit.log"

# Write the timestamped JSON entry to the audit log
$logEntry = "[$timestamp] [$hookEvent] $inputJson"
Add-Content -Path $logFile -Value $logEntry

# Output empty response
Write-Output "{}"
exit 0
