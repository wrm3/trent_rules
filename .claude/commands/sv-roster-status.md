Show Silicon Valley character roster status: $ARGUMENTS

## What This Command Does

Checks which characters have been built, which need work, and what's missing.

## Checks Performed

### 1. GLB Files
- Scan `docker/frontend/public/models/characters/` for existing GLBs
- Compare against full roster (14 characters)
- Report: built, missing, file sizes

### 2. Animation Status
- For each GLB: check if animation clips are embedded
- Report which clips are present vs required (8 minimum)

### 3. Voice Status
- Check for audio files per character
- Check for lip sync JSON files
- Report which characters have voice + lip sync ready

### 4. R3F Registration
- Check CHARACTER_MODELS entries in Character3D.tsx
- Check DESK_3D_POSITIONS entries
- Check CHARACTER_SCALE_OVERRIDES entries
- Report unregistered characters

## Output Format

```
## Silicon Valley Roster Status

| Character | GLB | Animations | Voice | Lip Sync | R3F |
|-----------|-----|------------|-------|----------|-----|
| Richard   | ✅  | 8/8        | ✅    | ✅       | ✅  |
| Gilfoyle  | ❌  | —          | ❌    | ❌       | ❌  |
| ...       |     |            |       |          |     |
```

## Skills Used
- sv-character-roster
