---
description: "Prevent curl alias issues in PowerShell on Windows"
activation: "always_on"
---

# Curl Command Fix for Windows PowerShell

## The Problem

In PowerShell on Windows, `curl` is an **alias** for `Invoke-WebRequest`, NOT the actual curl executable. This causes commands like:

```powershell
curl https://example.com/install -fsS | bash
```

To fail with errors like:
```
Invoke-WebRequest : A parameter cannot be found that matches parameter name 'fsS'.
```

## Solutions

### Option 1: Use curl.exe (if installed)
```powershell
curl.exe https://example.com/install -fsS
```

### Option 2: Use Invoke-WebRequest properly
```powershell
Invoke-WebRequest -Uri "https://example.com/api" -UseBasicParsing
```

### Option 3: Use WSL for bash-piped commands
```powershell
wsl curl https://example.com/install -fsS | bash
```

### Option 4: Use Git Bash
Open Git Bash terminal and run curl commands natively.

## Common Scenarios

### Cursor CLI Installation
**WRONG (fails in PowerShell):**
```powershell
curl https://cursor.com/install -fsS | bash
```

**CORRECT (use WSL or Git Bash):**
```bash
# In WSL or Git Bash:
curl https://cursor.com/install -fsS | bash
```

### API Testing
**WRONG:**
```powershell
curl -s http://localhost:5000/api/status
```

**CORRECT:**
```powershell
# Option A: Use curl.exe
curl.exe -s http://localhost:5000/api/status

# Option B: Use Invoke-WebRequest
Invoke-WebRequest -Uri "http://localhost:5000/api/status" -UseBasicParsing

# Option C: Use iwr shorthand
iwr "http://localhost:5000/api/status" -UseBasicParsing
```

### Downloading Files
**WRONG:**
```powershell
curl -O https://example.com/file.zip
```

**CORRECT:**
```powershell
# Option A: curl.exe
curl.exe -O https://example.com/file.zip

# Option B: Invoke-WebRequest
Invoke-WebRequest -Uri "https://example.com/file.zip" -OutFile "file.zip"
```

## Quick Reference

| Curl Flag | PowerShell Equivalent |
|-----------|----------------------|
| `-s` (silent) | `-UseBasicParsing` (partial) |
| `-o file` | `-OutFile "file"` |
| `-X POST` | `-Method POST` |
| `-H "Header: value"` | `-Headers @{"Header"="value"}` |
| `-d "data"` | `-Body "data"` |
| `-fsS` | No direct equivalent - use curl.exe or WSL |

## Rule Summary

1. **NEVER** use bare `curl` in PowerShell - it's aliased to `Invoke-WebRequest`
2. **ALWAYS** use `curl.exe` if you need actual curl behavior
3. **For bash-piped installs** (like `| bash`), use WSL or Git Bash
4. **For simple HTTP requests**, prefer `Invoke-WebRequest` with `-UseBasicParsing`
