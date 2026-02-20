---
description: "Audit Silicon Valley 3D scene assets against requirements"
---

Audit 3D assets against scene requirements: $ARGUMENTS

## What This Command Does

Scans the `assets/` directory and compares against what `scene_definition.json` requires.

## Checks Performed

### 1. Required vs Available
- Parse scene_definition.json for all zones and their types
- Map zone types to required props via ZONE_PROP_MAP
- Scan `assets/normalized/` for available GLBs
- Report: available, missing, extra

### 2. Asset Quality
- Check file sizes (flag anything >5MB for props, >10MB for furniture)
- Report poly counts if readable from GLB metadata
- Flag un-normalized assets (not in `normalized/` directory)

### 3. Room Completeness
- For each room in scene definition: list required furniture
- Check against available assets
- Report readiness percentage per room

## Output Format

```
## Asset Audit Report

### Main Office (75% ready)
- ✅ desk.glb (320 KB)
- ✅ office_chair.glb (180 KB)
- ❌ MISSING: whiteboard.glb
- ❌ MISSING: kanban_board.glb

### Kitchen (50% ready)
- ✅ coffee_maker.glb (95 KB)
- ❌ MISSING: counter.glb
- ❌ MISSING: bar_stool.glb
```

## Skills Used
- sv-asset-pipeline
- sv-environment-3d
