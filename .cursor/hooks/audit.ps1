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
$hookEvent = "unknown"
$conversationId = "unknown"
try {
    $eventData = $inputJson | ConvertFrom-Json
    if ($eventData.hook_event_name) { $hookEvent = $eventData.hook_event_name }
    if ($eventData.conversation_id) { $conversationId = $eventData.conversation_id }
} catch {}

# Date prefix for log files
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_agent-audit.log"

# Write the timestamped JSON entry to the audit log
$logEntry = "[$timestamp] [$hookEvent] conv=$conversationId $inputJson"
Add-Content -Path $logFile -Value $logEntry

# Output empty response
Write-Output "{}"
exit 0
