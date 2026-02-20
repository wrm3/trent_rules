# Windows-Safe Emoji Guide

## Overview

The trent system uses Windows-safe emojis for task status indicators. This document explains the emoji choices, why they're Windows-safe, and how to use them correctly.

## Why Windows-Safe Emojis?

### The Problem
Many emojis don't render correctly on Windows systems, appearing as:
- Empty boxes (Γûí)
- Question marks (?)
- Garbled characters
- Missing symbols

This causes issues when:
- Viewing files in Windows terminals
- Using Windows-based IDEs
- Sharing files across platforms
- Committing to Git on Windows

### The Solution
Use a carefully selected set of emojis that:
- Render correctly on Windows 10/11
- Display properly in all major terminals
- Work in VS Code, Cursor
- Are Git-friendly
- Have clear, unambiguous meanings

## Status Indicator Emojis

### Γ£à Completed (Γ£à)
- **Unicode**: U+2705
- **Name**: White Heavy Check Mark
- **Usage**: Task successfully completed
- **Windows Support**: Γ£à Excellent
- **Alternatives**: Γÿæ∩╕Å (U+2611), Γ£ö∩╕Å (U+2714)

**Example:**
```markdown
- [Γ£à] Task 001: Implement user authentication
```

**Why This Emoji:**
- Universally recognized as "done"
- Renders on all Windows versions
- Clear visual distinction from pending
- Green color conveys success

### ≡ƒöä In Progress (≡ƒöä)
- **Unicode**: U+1F504
- **Name**: Counterclockwise Arrows Button
- **Usage**: Task currently being worked on
- **Windows Support**: Γ£à Excellent
- **Alternatives**: Γƒ│ (U+27F3), Γå╗ (U+21BB)

**Example:**
```markdown
- [≡ƒöä] Task 002: Create fstrent-planning Skill
```

**Why This Emoji:**
- Circular arrows suggest ongoing work
- Renders reliably on Windows
- Blue color indicates active state
- Distinct from completed/pending

### Γ¥î Failed (Γ¥î)
- **Unicode**: U+274C
- **Name**: Cross Mark
- **Usage**: Task attempted but failed
- **Windows Support**: Γ£à Excellent
- **Alternatives**: Γ£û∩╕Å (U+2716), Γ¿» (U+2A2F)

**Example:**
```markdown
- [Γ¥î] Task 003: Deploy to production
```

**Why This Emoji:**
- Clear indication of failure
- Renders on all Windows versions
- Red color signals error/problem
- Universally understood meaning

### [ ] Pending (Empty Checkbox)
- **Unicode**: N/A (ASCII characters)
- **Name**: Empty Checkbox
- **Usage**: Task not yet started
- **Windows Support**: Γ£à Perfect (ASCII)
- **Alternatives**: ΓÿÉ (U+2610)

**Example:**
```markdown
- [ ] Task 004: Add reference materials
```

**Why This Format:**
- Pure ASCII, works everywhere
- Markdown-compatible checkbox
- Clear visual indicator
- GitHub/GitLab render as checkbox

## Additional Emojis Used

### ≡ƒö╡ Blue Circle
- **Unicode**: U+1F535
- **Usage**: Information, neutral status
- **Windows Support**: Γ£à Excellent

### ≡ƒƒó Green Circle
- **Unicode**: U+1F7E2
- **Usage**: Success, healthy status
- **Windows Support**: Γ£à Good (Windows 10+)

### ≡ƒö┤ Red Circle
- **Unicode**: U+1F534
- **Usage**: Error, critical status
- **Windows Support**: Γ£à Excellent

### ΓÜá∩╕Å Warning Sign
- **Unicode**: U+26A0
- **Name**: Warning Sign
- **Usage**: Caution, attention needed
- **Windows Support**: Γ£à Excellent

## Emojis to AVOID

### Γ¥î Don't Use These on Windows

| Emoji | Issue | Windows Display |
|-------|-------|-----------------|
| ≡ƒÜÇ | Rocket | May show as box |
| ≡ƒÆí | Light Bulb | Inconsistent rendering |
| ≡ƒÄ» | Dart | May not display |
| ≡ƒô¥ | Memo | Can appear garbled |
| ≡ƒöº | Wrench | Unreliable on older Windows |
| ≡ƒÉ¢ | Bug | May show as box |
| ≡ƒÄë | Party Popper | Inconsistent |
| ≡ƒæì | Thumbs Up | May not render |

**Why They Fail:**
- Require newer emoji fonts
- Not in Windows default emoji set
- Terminal emulators don't support them
- Git diff tools may corrupt them

## Usage Guidelines

### In TASKS.md

**Correct:**
```markdown
# Project Tasks

## Active Tasks
- [ ] Task 001: Implement feature
- [≡ƒöä] Task 002: Fix bug
- [Γ£à] Task 003: Write documentation
- [Γ¥î] Task 004: Deploy to staging
```

**Incorrect:**
```markdown
# Project Tasks

## Active Tasks
- ≡ƒÜÇ Task 001: Implement feature  # Don't use rocket
- ΓÅ│ Task 002: Fix bug  # Hourglass may not render
- ≡ƒæì Task 003: Write documentation  # Thumbs up unreliable
- ≡ƒÆÑ Task 004: Deploy to staging  # Explosion may fail
```

### In Task Files

**Status Field (YAML):**
```yaml
status: pending  # Use text, not emoji
status: in-progress
status: completed
status: failed
```

**Markdown Content:**
```markdown
## Status
Current status: ≡ƒöä In Progress

## Acceptance Criteria
- [Γ£à] Completed criterion
- [≡ƒöä] In progress criterion
- [ ] Pending criterion
```

### In Commit Messages

**Good:**
```
Γ£à Task 001: Complete user authentication

- Implemented login/logout
- Added session management
- Tests passing
```

**Avoid:**
```
≡ƒÜÇ Task 001: Launch user authentication  # Rocket may not show

- Implemented login/logout ≡ƒÆ¬  # Muscle emoji unreliable
- Added session management ≡ƒöÑ  # Fire emoji may fail
- Tests passing ≡ƒÄë  # Party popper inconsistent
```

## Platform Compatibility

### Windows 10/11
- Γ£à All recommended emojis work
- ≡ƒöä Renders correctly in terminals
- Γ¥î Displays properly in Git
- [ ] ASCII always works

### Windows Terminal
- Full emoji support
- Color rendering
- Font fallback works well
- Recommended for best experience

### PowerShell
- Basic emoji support
- May need font configuration
- Recommended: Install Cascadia Code font

### Git Bash (Windows)
- Limited emoji support
- ASCII recommended for commits
- May show boxes for complex emojis

### VS Code / Cursor
- Excellent emoji support
- All recommended emojis render
- Color display works
- Best experience on Windows

## Configuration Tips

### Windows Terminal Setup

1. **Install Cascadia Code Font:**
   ```powershell
   # Via winget
   winget install Microsoft.CascadiaCode
   ```

2. **Configure Terminal:**
   ```json
   {
     "profiles": {
       "defaults": {
         "fontFace": "Cascadia Code",
         "fontSize": 10
       }
     }
   }
   ```

### VS Code Setup

1. **Settings.json:**
   ```json
   {
     "editor.fontFamily": "Cascadia Code, Consolas, 'Courier New', monospace",
     "terminal.integrated.fontFamily": "Cascadia Code"
   }
   ```

### Git Configuration

1. **Ensure UTF-8 Encoding:**
   ```bash
   git config --global core.quotepath false
   git config --global i18n.commitencoding utf-8
   git config --global i18n.logoutputencoding utf-8
   ```

## Testing Emoji Support

### Quick Test
Create a test file and check if emojis render:

```markdown
# Emoji Test

Status Indicators:
- [ ] Pending (ASCII)
- [≡ƒöä] In Progress
- [Γ£à] Completed
- [Γ¥î] Failed

Additional:
- ≡ƒö╡ Blue Circle
- ≡ƒƒó Green Circle
- ≡ƒö┤ Red Circle
- ΓÜá∩╕Å Warning
```

**Expected Result:**
- All emojis should display correctly
- Colors should be visible
- No boxes or question marks

### Troubleshooting

**Problem:** Emojis show as boxes
**Solution:**
1. Install Cascadia Code font
2. Update Windows to latest version
3. Configure terminal/editor font
4. Restart application

**Problem:** Emojis in Git look wrong
**Solution:**
1. Set UTF-8 encoding in Git config
2. Use Git Bash or Windows Terminal
3. Avoid complex emojis in commit messages

**Problem:** Different rendering across tools
**Solution:**
1. Stick to recommended emoji set
2. Use ASCII for maximum compatibility
3. Test in target environments

## Best Practices

### 1. Consistency
- Always use the same emoji for the same status
- Don't mix different checkmark styles
- Maintain emoji usage across team

### 2. Simplicity
- Prefer ASCII when possible
- Use emojis only for status indicators
- Avoid decorative emojis

### 3. Accessibility
- Emojis should enhance, not replace text
- Always include text status in YAML
- Don't rely solely on color

### 4. Cross-Platform
- Test on Windows before committing
- Verify in Git diff
- Check in target IDE

### 5. Documentation
- Document emoji meanings
- Provide legend in README
- Train team on usage

## Quick Reference Card

```
Task Status Emojis (Windows-Safe):

[ ]  Pending      - Not started
[≡ƒöä] In Progress  - Currently working
[Γ£à] Completed    - Successfully done
[Γ¥î] Failed       - Attempted but failed

Additional:
≡ƒö╡ Info/Neutral
≡ƒƒó Success/Healthy
≡ƒö┤ Error/Critical
ΓÜá∩╕Å Warning/Caution

AVOID: ≡ƒÜÇ ≡ƒÆí ≡ƒÄ» ≡ƒô¥ ≡ƒöº ≡ƒÉ¢ ≡ƒÄë ≡ƒæì
(These may not render on Windows)
```

## Summary

The trent system uses a carefully curated set of Windows-safe emojis that:
- Γ£à Render correctly on all Windows versions
- Γ£à Display properly in terminals and IDEs
- Γ£à Work reliably in Git
- Γ£à Provide clear visual indicators
- Γ£à Are universally understood

Stick to the recommended emoji set for the best cross-platform experience.

