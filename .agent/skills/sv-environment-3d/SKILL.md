---
name: sv-environment-3d
description: Design and build interactive 3D environments for Silicon Valley characters. Covers room layout JSON, Blender room geometry generation, anchor-point interaction system, waypoint navigation, and the character behavior state machine. This skill should be used when designing room layouts, building 3D office environments, configuring interaction zones, setting up character navigation, or defining autonomous character behavior.
triggers:
  - "room design"
  - "3D environment"
  - "room layout"
  - "anchor point"
  - "waypoint"
  - "navmesh"
  - "behavior tree"
  - "interaction zone"
  - "Pied Piper"
  - "hacker hostel"
  - "Erlich's workspace"
  - "office 3D"
  - "furniture placement"
agents:
  - 3d-environment-artist
  - full-stack-developer
version: 1.0.0
---

# Silicon Valley 3D Environment Design

Build interactive 3D office/startup environments that characters inhabit, navigate, and interact with. Covers room layout, anchor-point interaction system, waypoint navigation, and autonomous behavior state machine.

## Decision Tree

```
Have a room layout already?
  YES → Skip to Anchor System
  NO  → Start at Room Layout JSON

How many interactive zones?
  1-5 zones  → Simple anchor-point system
  6+ zones   → Full waypoint graph

Characters need autonomous behavior?
  YES → Behavior State Machine (Phase 4)
  NO  → Scripted interactions only (Phase 3)
```

## Phase 1: Room Layout as JSON Scene Graph

Define the environment as structured JSON — the single source of truth for both Blender and R3F:

```json
{
  "environment": {
    "name": "Pied Piper Hacker Hostel",
    "scale": "meters",
    "rooms": [
      {
        "id": "main_office",
        "name": "Main Office",
        "dimensions": { "w": 12, "d": 10, "h": 3 },
        "position": [0, 0, 0],
        "connected_to": ["kitchen", "garage_arcade"],
        "zones": [
          {
            "id": "desk_richard",
            "type": "workstation",
            "position": [2, 0, 2],
            "facing": 90,
            "interactions": ["sit", "use_laptop", "stand_up"],
            "anchor": { "sit": [2, 0.5, 2], "stand": [2, 0, 3.2] }
          }
        ]
      }
    ],
    "doorways": [
      { "from": "main_office", "to": "garage_arcade", "position": [12, 0, 1], "width": 2 }
    ]
  }
}
```

Save as `scene_definition.json`. Every subsequent script reads from it. For the full schema spec, see `reference/scene_schema.md`.

## Phase 2: Room Geometry (Blender Python)

Generate walls, floors, ceilings, and doorway cutouts from the scene definition:

```bash
blender --background --python build_rooms.py -- scene_definition.json output/rooms.glb
```

The script reads `scene_definition.json`, creates room shell geometry (floor + 4 walls + ceiling per room), and exports as GLB. For the full script, see `sv-asset-pipeline` skill (normalize + export).

## Phase 3: Anchor-Point Interaction System

An **anchor point** is a named position+rotation where a character stands/sits when performing an interaction. Every interactive zone must have at least one anchor.

### TypeScript Types

```typescript
export interface AnchorPoint {
  id: string;
  position: [number, number, number];
  rotation: number;          // Y-axis rotation in degrees
  interactionType: InteractionType;
  occupiedBy: string | null; // character id, or null if free
}

export type InteractionType =
  | 'sit_desk'        // sit in chair, use laptop
  | 'sit_couch'       // sit on couch, idle chat
  | 'stand_board'     // stand facing whiteboard/kanban
  | 'stand_appliance' // stand at coffee machine etc
  | 'arcade'          // stand at arcade machine
  | 'walk_through'    // doorway/transit point
```

### Anchor Registry (Generated from scene_definition.json)

```typescript
import sceneData from '../scene_definition.json';

export function buildAnchorRegistry(): Record<string, AnchorPoint> {
  const registry: Record<string, AnchorPoint> = {};
  for (const room of sceneData.environment.rooms) {
    for (const zone of room.zones) {
      for (const [anchorName, pos] of Object.entries(zone.anchor)) {
        const anchorId = `${zone.id}:${anchorName}`;
        registry[anchorId] = {
          id: anchorId,
          position: pos as [number, number, number],
          rotation: zone.facing ?? 0,
          interactionType: zone.type as InteractionType,
          occupiedBy: null,
        };
      }
    }
  }
  return registry;
}
```

### Waypoint Navigation Graph

For navigation between rooms, use a waypoint graph — simpler than a full navmesh:

```typescript
export interface Waypoint {
  id: string;
  position: [number, number, number];
  connectedTo: string[];
  roomId: string;
}

export const WAYPOINTS: Waypoint[] = [
  { id: "wp_main_office_center", position: [0, 0, 5],
    connectedTo: ["wp_door_office_arcade", "wp_door_office_kitchen"],
    roomId: "main_office" },
  { id: "wp_arcade_center", position: [18, 0, 4],
    connectedTo: ["wp_door_office_arcade"],
    roomId: "garage_arcade" },
  { id: "wp_kitchen_center", position: [2, 0, 13],
    connectedTo: ["wp_door_office_kitchen"],
    roomId: "kitchen" },
  // Doorway waypoints
  { id: "wp_door_office_arcade", position: [12, 0, 1],
    connectedTo: ["wp_main_office_center", "wp_arcade_center"],
    roomId: "main_office" },
  { id: "wp_door_office_kitchen", position: [1, 0, 11],
    connectedTo: ["wp_main_office_center", "wp_kitchen_center"],
    roomId: "main_office" },
];

export function findPath(fromWP: string, toWP: string): string[] {
  // BFS pathfinding over waypoint graph
  const queue: string[][] = [[fromWP]];
  const visited = new Set<string>([fromWP]);
  while (queue.length > 0) {
    const path = queue.shift()!;
    const current = path[path.length - 1];
    if (current === toWP) return path;
    const wp = WAYPOINTS.find(w => w.id === current);
    if (!wp) continue;
    for (const neighbor of wp.connectedTo) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push([...path, neighbor]);
      }
    }
  }
  return [fromWP];
}
```

## Phase 4: Character Behavior State Machine

Each character runs an independent state machine. States transition based on timers, random rolls, and zone availability. Personality config is in the `sv-character-roster` skill.

### States

```typescript
export type CharacterState =
  | 'idle_sit'      | 'idle_stand'   | 'typing'
  | 'walking'       | 'interacting'  | 'talking'
  | 'transitioning'
```

### Behavior Tick (Once Per Second Per Character)

```typescript
export function tickCharacterBehavior(character, config, anchorRegistry, deltaTime) {
  const newTimer = character.stateTimer - deltaTime;
  if (character.state === 'transitioning') return { stateTimer: newTimer };
  if (newTimer > 0) return { stateTimer: newTimer };
  return chooseNextActivity(character, config, anchorRegistry);
}

function chooseNextActivity(character, config, anchorRegistry) {
  const roll = Math.random();
  let targetZone: string;

  if (roll < config.arcadeFrequency) {
    targetZone = 'arcade_machine';
  } else if (roll < config.arcadeFrequency + config.kitchenFrequency) {
    targetZone = 'coffee_station';
  } else {
    // Choose from preferred zones that aren't occupied
    const freePreferred = config.preferredZones.filter(zoneId => {
      const anchorKey = `${zoneId}:sit`;
      return !anchorRegistry[anchorKey]?.occupiedBy;
    });
    targetZone = freePreferred.length > 0
      ? freePreferred[Math.floor(Math.random() * freePreferred.length)]
      : config.preferredZones[0];
  }

  if (character.currentZoneId === targetZone) {
    return { state: 'idle_sit', stateTimer: randomDuration(config.idleDuration) };
  }

  const path = findPath(currentWP, targetWP);
  return { state: 'walking', targetZoneId: targetZone, waypointPath: path };
}
```

## Room Catalog

| Room | Status | Key Zones |
|------|--------|-----------|
| Main Office (Erlich's Workspace) | Built | 4 desks, kanban, whiteboard, couch, foosball, piano |
| Garage / Arcade | Built | Arcade machine, ping pong |
| Kitchen | Built | Coffee station, counter, stools |
| Gallery | Built | Character pedestals |
| Server Room | Planned | Server racks, terminals |
| Conference Room | Planned | Conference table, projector |
| Bedrooms | Planned | Beds, personal items |
| Exterior Patio | Planned | Outdoor furniture |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Character walks through walls | Add Rapier colliders or invisible plane colliders |
| Character snaps to anchor abruptly | Tween position over 0.5s with gsap |
| Two characters at same zone | Check `occupiedBy` before selecting target |
| Assets wrong size in scene | `normalize_assets.py` sets 1m max — apply explicit scale |

## Reference Files

- `reference/room_design_guide.md` — Procedural room pattern, wall transparency, Erlich's workspace layout
- `reference/scene_schema.md` — Full JSON scene_definition format specification
