---
id: 403
title: 'Add Antigravity installation_id as machine_id source'
type: task
status: completed
priority: low
phase: 4
subsystems: [cursor_adapter, claude_adapter]
project_context: >
  Use ~/.gemini/antigravity/installation_id as machine_id when Windows MachineGuid
  is unavailable or when running on non-Windows platforms.
dependencies: [400]
completed_date: '2026-03-01'
---

# Task 403: Antigravity installation_id Integration

## Changes Made
- `cursor_adapter.py`: `_detect_machine_id()` now checks antigravity_id_path before /etc/machine-id
- `claude_adapter.py`: `_get_machine_id()` refactored with full cross-platform support:
  1. Windows: HKLM\SOFTWARE\Microsoft\Cryptography\MachineGuid
  2. Antigravity: ~/.gemini/antigravity/installation_id (cross-platform)
  3. Linux: /etc/machine-id
  4. macOS: ioreg IOPlatformUUID
  5. Fallback: UUID from MAC address

## Known value on this machine
installation_id = 4bedca94-6e04-448a-9c8d-fe221fdc7302
