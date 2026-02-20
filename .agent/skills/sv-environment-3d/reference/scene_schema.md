# Scene Definition JSON Schema

The `scene_definition.json` file is the single source of truth that drives both the Blender scene assembly and the R3F web scene.

## Top-Level Structure

```json
{
  "environment": {
    "name": "string",
    "scale": "meters",
    "rooms": [ Room ],
    "doorways": [ Doorway ]
  }
}
```

## Room Object

```json
{
  "id": "string (unique)",
  "name": "string (display name)",
  "dimensions": { "w": number, "d": number, "h": number },
  "position": [x, y, z],
  "connected_to": ["room_id", ...],
  "zones": [ Zone ]
}
```

- `dimensions`: Width, depth, height in meters
- `position`: World-space origin of the room
- `connected_to`: IDs of adjacent rooms (must have matching doorway)

## Zone Object

```json
{
  "id": "string (unique)",
  "type": "workstation | interactive_wall | seating | arcade | game_table | appliance",
  "position": [x, y, z],
  "facing": number (degrees, Y-axis rotation),
  "interactions": ["sit", "use_laptop", "stand_up", ...],
  "anchor": {
    "sit": [x, y, z],
    "stand": [x, y, z]
  }
}
```

- `type`: Determines which props to place (see `ZONE_PROP_MAP` in sv-asset-pipeline)
- `facing`: Direction the character faces when at this zone (0 = +Z, 90 = +X)
- `anchor`: Named positions where characters snap to for interactions. At minimum, provide `sit` or `stand`.

## Doorway Object

```json
{
  "from": "room_id",
  "to": "room_id",
  "position": [x, y, z],
  "width": number (meters)
}
```

## Zone Types Reference

| Type | Description | Default Props | Default Interactions |
|------|-------------|---------------|---------------------|
| `workstation` | Desk + chair + computer | desk, chair, laptop | sit, use_laptop, stand_up |
| `interactive_wall` | Wall-mounted board | whiteboard or kanban | walk_to, point_at, idle_study |
| `seating` | Couch or chairs | couch, coffee table | sit, idle_talk, stand_up |
| `arcade` | Game machine | arcade cabinet | walk_to, play_game, idle_play |
| `game_table` | Table game | ping pong, foosball | walk_to, play_game (2 anchors) |
| `appliance` | Kitchen/utility | coffee maker, etc | walk_to, use, idle_wait |

## Anchor Naming Convention

- `sit` — Character seated at this zone
- `stand` — Character standing near this zone
- `player_a`, `player_b` — For 2-player games (ping pong, foosball)
- Custom names allowed but must be referenced in behavior config

## Validation Rules

1. Every room `id` must be unique
2. Every zone `id` must be unique across all rooms
3. `connected_to` rooms must exist and have a matching doorway
4. Every zone must have at least one anchor point
5. Doorway `from` and `to` must reference existing room IDs
6. Positions are in world space (not relative to room)

## Example: Complete Hacker Hostel

See the full `scene_definition.json` in the `sv-environment-3d` SKILL.md for the complete Pied Piper Hacker Hostel definition with Main Office, Garage/Arcade, and Kitchen.
