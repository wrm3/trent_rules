---
name: sv-character-roster
description: Canonical reference for the Silicon Valley cast of 14+ characters. Contains actor names, MB-Lab body presets, personality-driven idle behaviors, voice IDs, desk positions, and character-specific rendering config. This skill should be used when looking up character data, creating a specific cast member, or configuring character-specific parameters.
triggers:
  - "character roster"
  - "Silicon Valley cast"
  - "Richard Hendricks"
  - "Gilfoyle"
  - "Dinesh"
  - "Erlich"
  - "Jared Dunn"
  - "Monica"
  - "Big Head"
  - "Jian Yang"
  - "Gavin Belson"
  - "Russ Hanneman"
  - "Laurie Bream"
  - "character list"
  - "cast data"
agents:
  - 3d-character-artist
  - sv-pipeline-orchestrator
version: 1.0.0
---

# Silicon Valley Character Roster

Canonical data source for all Silicon Valley cast characters. When creating a character, look up their data here first.

## Erlich's Workspace Regulars (7)

| Character | Actor | MB-Lab Base | Mass | Tone | Key Visual Features |
|-----------|-------|-------------|------|------|---------------------|
| Richard Hendricks | Thomas Middleditch | m_ca01 | 0.40 | 0.45 | Curly brown hair, plaid shirt, anxious expression |
| Gilfoyle | Martin Starr | m_ca01 | 0.45 | 0.50 | Long black hair, goatee, all black clothes |
| Dinesh Chugtai | Kumail Nanjiani | m_la01 | 0.45 | 0.50 | Short dark hair, colorful polo shirts |
| Erlich Bachman | TJ Miller | m_ca01 | 0.78 | 0.30 | Curly hair, beard, Aviato shirt + robe, heavyset |
| Jared Dunn | Zach Woods | m_ca01 | 0.35 | 0.40 | Short blond hair, button-down oxford, tall & thin |
| Big Head | Josh Brener | m_ca01 | 0.55 | 0.40 | Brown hair with bangs, Stanford hoodie |
| Jian Yang | Jimmy O. Yang | m_as01 | 0.42 | 0.45 | Short black hair, plain white t-shirt, slim |

## Extended Cast (7)

| Character | Actor | MB-Lab Base | Mass | Tone | Key Visual Features |
|-----------|-------|-------------|------|------|---------------------|
| Monica Hall | Amanda Crew | f_ca01 | 0.45 | 0.50 | Long brown hair, blazer, professional |
| Carla Walton | Alice Wetterlund | f_ca01 | 0.45 | 0.50 | Blue hair streak, black tank top, edgy |
| Gavin Belson | Matt Ross | m_ca01 | 0.55 | 0.55 | Grey-brown hair, expensive suit |
| Russ Hanneman | Chris Diamantopoulos | m_ca01 | 0.50 | 0.55 | Spiky hair, V-neck, gold chain |
| Laurie Bream | Suzanne Cryer | f_ca01 | 0.40 | 0.45 | Blonde bun, glasses, grey suit |
| Peter Gregory | Christopher Evan Welch | m_ca01 | 0.45 | 0.40 | Balding, grey suit, glasses |
| Sophia (AI) | N/A | f_ca01 | 0.42 | 0.55 | Silver/white, LED eyes, futuristic |

## AI Characters (Procedural — No GLB)

| Character | Type | Rendered As |
|-----------|------|-------------|
| AI Gilfoyle | Tron-style | Glowing wireframe in R3F |
| AI Dinesh | Tron-style | Glowing wireframe in R3F |
| Son of Anton | AI entity | Custom procedural mesh |

## R3F Configuration

### Scale Overrides (default 0.90)

```typescript
const CHARACTER_SCALE_OVERRIDES: Record<string, number> = {
  jared: 0.98,     // Tall (6'3")
  erlich: 0.95,    // Stocky/tall
  sophia: 0.78,    // AI robot, shorter
}
```

### Desk Positions (Erlich's Workspace)

```typescript
const DESK_3D_POSITIONS: Record<string, [number, number, number]> = {
  richard: [-0.8, 0, -0.9],    // Front of central table
  gilfoyle: [0.8, 0, -0.9],    // Front, dual monitors
  dinesh: [-0.2, 0, 0.9],      // Back of table
  jared: [1.2, 0, 0.9],        // Back, laptop
  erlich: [2.5, 0, 2],         // By the couch
  bighead: [-2.5, 0, -2.5],    // Near piano
  jian_yang: [-3.5, 0, 1.5],   // By the door
  monica: [0, 0, -2],
  carla: [-1, 0, 1],
}
```

### Y Offsets (Floor Alignment)

```typescript
const CHARACTER_Y_OFFSETS: Record<string, number> = {
  sophia: 0.05,    // Slight lift for robot feet
}
```

### Model Paths

```typescript
const CHARACTER_MODELS: Record<string, string> = {
  richard: '/models/characters/richard_hendricks.glb',
  gilfoyle: '/models/characters/gilfoyle.glb',
  dinesh: '/models/characters/dinesh.glb',
  erlich: '/models/characters/erlich.glb',
  jared: '/models/characters/jared.glb',
  bighead: '/models/characters/bighead.glb',
  jian_yang: '/models/characters/jian_yang.glb',
  monica: '/models/characters/monica.glb',
  carla: '/models/characters/carla.glb',
  gavin: '/models/characters/gavin.glb',
  russ: '/models/characters/russ.glb',
  laurie: '/models/characters/laurie.glb',
  peter: '/models/characters/peter.glb',
  sophia: '/models/characters/sophia.glb',
}
```

## Personality-Driven Idle Behaviors

These drive the autonomous behavior tree in `sv-environment-3d`:

| Character | Preferred Zones | Idle Duration (s) | Arcade % | Kitchen % | Unique Idle |
|-----------|----------------|-------------------|----------|-----------|-------------|
| Richard | desk, kanban, swot | 60-180 | 5% | 30% | Fidgeting, anxious pacing |
| Gilfoyle | desk, arcade | 30-90 | 20% | 10% | Typing aggressively |
| Dinesh | desk, couch, arcade | 20-60 | 40% | 20% | Looking at phone |
| Erlich | couch, swot, kanban | 10-40 | 15% | 40% | Drinking beer, lounging |
| Jared | desk, center, kanban | 40-120 | 5% | 15% | Organizing things |
| Big Head | piano, couch, center | 15-45 | 25% | 35% | Looking confused |
| Jian Yang | door, kitchen | 20-60 | 10% | 50% | Standing near door |

## Voice Configuration

For ElevenLabs voice IDs, see `sv-voice-lipsync` skill.

## File Locations

| Path | Purpose |
|------|---------|
| `docker/frontend/public/models/characters/` | Final GLB character models |
| `docker/frontend/public/models/characters/bases/` | MB-Lab base body GLBs |
| `docker/themes/trentworks/characters.json` | Character theme data |
| `docker/frontend/src/components/trentworks3d/Character3D.tsx` | Character renderer |
| `docker/frontend/src/components/trentworks3d/types.ts` | 3D positions, configs |

## Reference Files

- `reference/character_roster.md` — Extended character data, facial morph parameters, clothing details, voice samples
