# session-start.ps1 - Cursor hook for session initialization
# Triggered when a new composer conversation is created.
# Injects past agent-memory context so the AI has continuity across sessions.

# Read JSON input from stdin
$inputJson = $input | Out-String

try {
    $eventData    = $inputJson | ConvertFrom-Json
    $sessionId    = $eventData.session_id
    $composerMode = $eventData.composer_mode
    $timestamp    = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
} catch {
    $sessionId    = "unknown"
    $composerMode = "unknown"
    $timestamp    = Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ"
}

# ── Logging ──────────────────────────────────────────────────────────────────
$logDir = ".cursor/logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }

$datePrefix = Get-Date -Format "yyyy-MM-dd"
$logFile    = "$logDir/${datePrefix}_session_lifecycle.log"

$logEntry = "[$timestamp] [SESSION_START] Session: $sessionId | Mode: $composerMode"
Add-Content -Path $logFile -Value $logEntry

# ── User config check ────────────────────────────────────────────────────────
$userConfigDir  = Join-Path $env:USERPROFILE ".trent"
$userConfigFile = Join-Path $userConfigDir "user_config.json"

$setupNeeded = $false
if (-not (Test-Path $userConfigFile)) {
    # First run — create minimal skeleton so adapters don't crash, but flag for setup
    try {
        if (-not (Test-Path $userConfigDir)) {
            New-Item -ItemType Directory -Path $userConfigDir -Force | Out-Null
        }
        $machineId = ""
        try {
            $machineId = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Cryptography" `
                          -Name "MachineGuid" -ErrorAction Stop).MachineGuid
        } catch {}
        if (-not $machineId) { $machineId = [System.Guid]::NewGuid().ToString() }

        $cfg = [ordered]@{
            user_id         = "SETUP_NEEDED"
            machine_id      = $machineId
            mcp_url         = "http://localhost:8082"
            created_at      = (Get-Date -Format "yyyy-MM-ddTHH:mm:ssZ")
            platform        = "windows"
            created_by      = "session-start.ps1"
            setup_completed = $false
        }
        $cfg | ConvertTo-Json | Set-Content -Path $userConfigFile -Encoding UTF8
        Add-Content -Path $logFile -Value "[$timestamp] [CONFIG] Created skeleton user_config.json — setup needed"
    } catch {
        Add-Content -Path $logFile -Value "[$timestamp] [CONFIG] Failed to create user_config.json: $_"
    }
    $setupNeeded = $true
} else {
    # Check if user has completed setup (not just the auto-generated skeleton)
    try {
        $cfgCheck = Get-Content $userConfigFile -Raw | ConvertFrom-Json
        if ($cfgCheck.user_id -eq "SETUP_NEEDED" -or $cfgCheck.setup_completed -eq $false) {
            $setupNeeded = $true
        }
    } catch {}
}

# ── Memory Context Retrieval ─────────────────────────────────────────────────

# --- Setup banner ---
$setupBanner = ""
if ($setupNeeded) {
    $setupBanner = @"
⚠️  TRENT FIRST-TIME SETUP NEEDED
Your trent user ID has not been configured yet. Please run this command in a terminal:

  powershell -ExecutionPolicy Bypass -File .cursor/hooks/trent-setup-user.ps1

You can use your email, a nickname, or anything you like. This only needs to be done once.
AI memory features will work but sessions won't be linked to a named user until setup is complete.

---
"@
    Add-Content -Path $logFile -Value "[$timestamp] [CONFIG] Injecting setup reminder into context"
}

# --- Reflection reminder (letta-style step-count trigger) ---
# If the previous session was long (≥5 loops), inject a one-time reminder
# asking the AI to capture any valuable insights before starting new work.
$reflectionBanner = ""
$reflectionFile   = "$logDir/pending_reflection.json"
if (Test-Path $reflectionFile) {
    try {
        $reflData  = Get-Content $reflectionFile -Raw | ConvertFrom-Json

        # cursor_adapter writes turn_count; agent-complete writes loop_count
        $sessionSize = 0
        if ($reflData.turn_count) { $sessionSize = [int]$reflData.turn_count }
        elseif ($reflData.loop_count) { $sessionSize = [int]$reflData.loop_count }

        if ($sessionSize -ge 5) {
            # Build topic hint block if cursor_adapter enriched the file
            $topicHint = ""
            if ($reflData.recent_topics -and $reflData.recent_topics.Count -gt 0) {
                $topicHint = "`nSession covered (rough summary from first/last messages):`n"
                foreach ($t in $reflData.recent_topics) {
                    $topicHint += "  - $t`n"
                }
            }

            $reflectionBanner = @"
## 🧠 Memory Check Reminder
Your previous session had $sessionSize turns.$topicHint
Before starting new work, briefly review and call **``memory_capture_insight``** for anything worth preserving:

- **procedure** — how to do something (deploy, test, git workflow)
- **preference** — user preferences (code style, naming, formatting)
- **correction** — mistakes to avoid next time
- **decision** — architectural choices + rationale
- **context** — project background worth remembering

Keep captures concise (1-3 sentences each). Skip trivial exchanges.

---
"@
            Add-Content -Path $logFile -Value "[$timestamp] [REFLECT] Injecting memory check reminder (turns=$sessionSize)"
        }
        # Consume the file so we don't repeat the reminder
        Remove-Item $reflectionFile -ErrorAction SilentlyContinue
    } catch {
        Add-Content -Path $logFile -Value "[$timestamp] [REFLECT] Failed to read reflection hint: $_"
        Remove-Item $reflectionFile -ErrorAction SilentlyContinue
    }
}

$additionalContext = "${setupBanner}${reflectionBanner}trent task management system is active. Check .trent/TASKS.md for current tasks."

$projectIdFile = ".trent/.project_id"
if (Test-Path $projectIdFile) {
    $projectId = (Get-Content $projectIdFile -Raw).Trim()

    if ($projectId -ne "") {
        try {
            # Read mcp_url from user_config.json — falls back to localhost
            $mcpUrl = "http://localhost:8082"
            $userConfigPath = Join-Path $env:USERPROFILE ".trent\user_config.json"
            if (Test-Path $userConfigPath) {
                try {
                    $userConfig = Get-Content $userConfigPath -Raw | ConvertFrom-Json
                    if ($userConfig.mcp_url) { $mcpUrl = $userConfig.mcp_url.TrimEnd("/") }
                } catch {}
            }

            # Call the trent memory REST bridge (synchronous — hook waits for this)
            $contextUrl = "$mcpUrl/memory/context?project_id=$projectId&max_tokens=3000&platform=cursor"

            $resp = Invoke-WebRequest -Uri $contextUrl -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
            $body = $resp.Content | ConvertFrom-Json

            if ($body.success -and $body.context -ne "") {
                $memoryContext = $body.context
                $additionalContext = @"
$memoryContext

---
trent task management system is active. Check .trent/TASKS.md for current tasks.
"@
                Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Injected context: sessions=$($body.sessions_included) captures=$($body.captures_included)"
            }
        } catch {
            # Memory bridge unavailable — fall back to default context silently
            Add-Content -Path $logFile -Value "[$timestamp] [MEMORY] Context fetch failed (bridge unavailable): $_"
        }
    }
}

# ── Response ─────────────────────────────────────────────────────────────────
$response = @{
    continue           = $true
    additional_context = $additionalContext
}

$response | ConvertTo-Json -Compress
exit 0
