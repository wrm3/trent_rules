---
description: "Pointer rule for 3D character/environment pipeline. Triggers sv-* skills on 3D, character, animation, or environment keywords."
activation: "always_on"
---

# 3D Character & Environment Pipeline

When work involves 3D characters, animations, environments, or the Silicon Valley avatar project, load the relevant `sv-*` skills:

## Skill Map

| Topic | Skill to Load |
|-------|---------------|
| Creating characters from photos/descriptions | `sv-character-generation` |
| Toon shading, materials, mesh optimization | `sv-character-shading` |
| Silicon Valley cast data, body presets, roster | `sv-character-roster` |
| Mixamo animations, BVH, retargeting | `sv-animation-pipeline` |
| Voice synthesis, lip sync, visemes | `sv-voice-lipsync` |
| Room layout, anchors, navigation, behavior | `sv-environment-3d` |
| Asset sourcing, normalization, placement | `sv-asset-pipeline` |
| React Three Fiber scene, components | `sv-r3f-integration` |

## Agents

| Agent | When to Use |
|-------|------------|
| `3d-character-artist` | Creating character models |
| `3d-environment-artist` | Building rooms, placing furniture |
| `animation-engineer` | Rigging animations, voice, R3F wiring |
| `sv-pipeline-orchestrator` | Full end-to-end pipeline |
| `voice-artist` | Voice generation + lip sync only |

## Commands

- `/sv-create-character` — Photo → toon-shaded GLB
- `/sv-build-room` — Design + build a 3D room
- `/sv-animate-character` — Apply animations + optional voice
- `/sv-full-pipeline` — Complete photo-to-scene pipeline
- `/sv-roster-status` — Check which characters are built
- `/sv-asset-audit` — Check assets vs requirements

## Universal Rules

- **Never use BlenderMCP** — always headless Python
- **Never use Hyper3D for human characters** — props only
- **Always decimate for web** — ~5K verts per character
- **scene_definition.json** is the single source of truth for environments
