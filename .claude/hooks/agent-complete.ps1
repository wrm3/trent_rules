# agent-complete.ps1 - Claude Code hook for agent/stop lifecycle
# Triggered when the agent loop ends

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $status = $eventData.status
    $loopCount = $eventData.loop_count
    $conversationId = $eventData.conversation_id
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $status = "unknown"
    $loopCount = 0
    $conversationId = "unknown"
    $timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# Create log directory
$logDir = ".claude/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Date prefix for log files (allows easy cleanup of older logs)
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_agent_lifecycle.log"

# Log agent completion
$logEntry = "[$timestamp] [STOP] Conversation: $conversationId | Status: $status | Loops: $loopCount"
Add-Content -Path $logFile -Value $logEntry

# Create metrics directory
$metricsDir = ".claude/metrics"
if (-not (Test-Path $metricsDir)) {
    New-Item -ItemType Directory -Path $metricsDir -Force | Out-Null
}

# Date prefix for metrics files
$metricsFile = "$metricsDir/${datePrefix}_completions.csv"

# Write completion event to metrics
$csvEntry = "$timestamp,$conversationId,$status,$loopCount"
Add-Content -Path $metricsFile -Value $csvEntry

# Output empty response (no follow-up message)
$response = @{}
$response | ConvertTo-Json -Compress
exit 0
