# validate-shell.ps1 - Claude Code hook for shell command validation
# Validates shell commands before execution

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData = $inputJson | ConvertFrom-Json
    $command = $eventData.command
    $cwd = $eventData.cwd
} catch {
    $command = ""
    $cwd = ""
}

# Default: allow the command
$response = @{
    permission = "allow"
}

# Block dangerous commands (examples - customize as needed)
$dangerousPatterns = @(
    "rm -rf /",
    "rm -rf /*",
    "format c:",
    "del /s /q c:\*",
    ":(){:|:&};:"  # Fork bomb
)

foreach ($pattern in $dangerousPatterns) {
    if ($command -like "*$pattern*") {
        $response = @{
            permission = "deny"
            user_message = "Dangerous command blocked: $pattern"
            agent_message = "This command has been blocked by a security hook because it matches a dangerous pattern."
        }
        $response | ConvertTo-Json -Compress
        exit 2  # Exit code 2 blocks the action
    }
}

# Log the command for audit
$logDir = ".claude/logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Date prefix for log files (allows easy cleanup of older logs)
$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile = "$logDir/${datePrefix}_shell_commands.log"

$timestamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
$logEntry = "[$timestamp] [SHELL] Command: $command | CWD: $cwd"
Add-Content -Path $logFile -Value $logEntry

# Allow the command
$response | ConvertTo-Json -Compress
exit 0
