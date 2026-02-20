---
description: "Design and build a 3D room environment for Silicon Valley"
---

Build a 3D room environment: $ARGUMENTS

## What This Command Does

Designs a room layout, sources assets, and assembles the 3D environment with furniture and interaction zones.

## Workflow

### 1. Define Room Layout
- Create room entry in `scene_definition.json`
- Define dimensions, position, connections to other rooms
- Define interactive zones with anchor points

### 2. Source Assets
- Search Poly Pizza / KennyNL for required furniture
- Generate custom props with HunyuaN3D-2 if needed
- Normalize all assets (scale, orient, decimate)

### 3. Build Scene
- Generate room geometry in headless Blender
- Place furniture at zone positions
- Export as GLB

### 4. Configure Navigation
- Add waypoints for room center and doorways
- Connect to waypoint graph
- Add activity positions for character behavior

### 5. Create R3F Component
- Create TSX component using RoomShell
- Add furniture as mesh geometry or GLB imports
- Register in `rooms/types.ts` and `locations.json`

## Skills Used
- sv-environment-3d
- sv-asset-pipeline
- sv-r3f-integration

## What I Need From You
- Room name and purpose (e.g., "Server Room", "Conference Room")
- Key furniture/props to include
- Which characters should be placed here by default
