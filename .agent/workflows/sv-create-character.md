---
description: "Create a new Silicon Valley 3D character from photo/description"
---

Create a 3D character: $ARGUMENTS

## What This Command Does

Runs the full character creation pipeline: photo/description → rigged, toon-shaded, web-optimized GLB.

## Workflow

### 1. Identify Character
- Look up character data in `sv-character-roster` skill
- Determine: MB-Lab base (mass, tone) or RPM photo-to-avatar
- Note key visual features (hair, clothing, accessories)

### 2. Generate Base Avatar
- **With photo**: RPM API (cartoon style) with `?morphTargets=ARKit,Oculus Visemes`
- **Without photo**: MB-Lab in headless Blender with correct preset

### 3. Apply Toon Shading
- Import GLB into headless Blender
- Apply Toon BSDF shader + solidify outline
- Decimate to ~5K vertices
- Add mesh hair and clothing

### 4. Export & Register
- Export as GLB to `docker/frontend/public/models/characters/`
- Update `CHARACTER_MODELS` in `Character3D.tsx`
- Add scale override and desk position if needed

## Skills Used
- sv-character-generation
- sv-character-shading
- sv-character-roster

## What I Need From You
- Character name (from Silicon Valley cast)
- Reference photo path (optional — will use MB-Lab if none)
- Style preference: cartoon (default) or realistic
