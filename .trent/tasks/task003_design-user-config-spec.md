---
id: 3
title: 'Design user_config.json spec and generation logic'
type: design
status: completed
priority: high
phase: 0
subsystems: [trent_install, identity]
project_context: 'Establishes stable user identity across all platforms and projects.'
dependencies: []
---

# Task 003: Design user_config.json Spec

## Objective
Define the exact structure, generation logic, and storage path for the global user
identity file. This file provides stable user_id and machine_id that persist across
IDE switches, project renames, and machine reboots.

## Acceptance Criteria
- [ ] File path agreed upon (~/.trent/user_config.json)
- [ ] All required fields defined with types and generation logic
- [ ] Machine ID generation strategy confirmed (Windows MachineGuid vs generated)
- [ ] Idempotency behavior documented (what happens on second trent_install?)
- [ ] Multi-user scenario documented (two devs, same project)

## Proposed Spec

### File Path
```
~/.trent/user_config.json
```
On Windows: `C:\Users\{username}\.trent\user_config.json`
Cross-platform: `os.path.expanduser("~/.trent/user_config.json")`

### Fields
```json
{
  "version": "1",
  "user_id": "usr_a1b2c3d4",
  "machine_id": "mach_e5f6g7h8",
  "display_name": "FSTrent",
  "created_at": "2026-03-01T00:00:00Z",
  "platforms_seen": ["cursor", "claude_code"]
}
```

### Generation Logic
```python
def get_or_create_user_config(config_path):
    if os.path.exists(config_path):
        return json.load(open(config_path))  # idempotent — never overwrite
    
    # Generate stable machine_id
    machine_id = get_windows_machine_guid()  # from registry
    if not machine_id:
        machine_id = str(uuid.uuid4())[:8]  # fallback
    
    config = {
        "version": "1",
        "user_id": f"usr_{uuid.uuid4().hex[:8]}",
        "machine_id": f"mach_{machine_id[:8]}",
        "display_name": os.environ.get("USERNAME") or os.environ.get("USER") or "unknown",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "platforms_seen": []
    }
    
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    json.dump(config, open(config_path, 'w'), indent=2)
    return config
```

### Windows MachineGuid
```python
import winreg
def get_windows_machine_guid():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             r"SOFTWARE\Microsoft\Cryptography")
        return winreg.QueryValueEx(key, "MachineGuid")[0]
    except:
        return None
```

### PowerShell equivalent (for hooks):
```powershell
(Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Cryptography" -Name MachineGuid -ErrorAction SilentlyContinue).MachineGuid
```

## Decisions to Confirm
1. Use `~/.trent/` (global) or `~/.config/trent/` (XDG-compliant)?
2. Use Windows MachineGuid as machine_id, or always generate UUID?
3. platforms_seen: auto-update per hook, or manual?

## Output
Write final spec as comments in trent_install.py when Task 601 is implemented.
