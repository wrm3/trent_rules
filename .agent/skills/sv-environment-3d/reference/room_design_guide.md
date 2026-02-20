# Room/Set Design Guide

## Architecture: Procedural vs. Imported

Rooms in Maestro are **procedurally generated** using React Three Fiber components, NOT imported as GLB models. This gives us:

- Zero model download time
- Infinite customizability
- Dynamic features (wall transparency, lighting changes, interactive elements)
- Easy iteration

## Room Component Pattern

Every room follows this pattern:

```typescript
import { RoomShell } from '../RoomShell'

export function MyRoom3D({ isNight, children }: RoomProps) {
  return (
    <RoomShell
      width={8} depth={6} height={3}
      wallColor="#C4956A" floorColor="#A0784C"
      isNight={isNight} dynamicWalls
    >
      <CentralTable />
      <Whiteboard position={[0, 1.5, -2.9]} />
      {children}
    </RoomShell>
  )
}
```

## Dynamic Wall Transparency

Camera-based wall transparency system:
1. Each frame, calculate camera forward direction
2. Dot product between camera direction and each wall's inward normal
3. When dot > threshold (~0.3), wall is between camera and interior
4. Smoothly lerp opacity from 1.0 to 0.0
5. Ceiling also fades when viewed from above

## Erlich's Workspace — Source Material

Based on Silicon Valley TV show "Hacker Hostel" set:

### Key Features
- Large open-plan living room converted into incubator workspace
- Central table: Long farmhouse-style table where the team codes
- Back wall: Large whiteboard with algorithms/diagrams
- Left wall: Kanban board, bookshelves
- Right side: Beat-up couch, foosball table
- Back-left: Upright piano
- Lighting: Warm residential (pendant lamps, table lamps)
- Vibe: Messy, lived-in, startup garage feel

### Color Palette
- Walls: Warm brown/tan (#C4956A)
- Floor: Dark hardwood (#6B4226)
- Furniture: Mismatched wood tones
- Couch: Dark blue/grey
- Tech: Silver/grey laptops, monitors

### Furniture Dimensions (meters)

| Item | Width | Depth | Height | Position |
|------|-------|-------|--------|----------|
| Central table | 2.4 | 1.2 | 0.75 | Center |
| Whiteboard | 2.0 | 0.05 | 1.2 | Back wall, y=1.5 |
| Kanban board | 1.2 | 0.05 | 0.9 | Left wall |
| Couch | 2.0 | 0.8 | 0.8 | Right-rear |
| Foosball table | 1.4 | 0.75 | 0.9 | Right-front |
| Piano (upright) | 1.5 | 0.6 | 1.2 | Back-left corner |

## Lighting Guidelines

### Residential Warm (Erlich's Workspace)
```typescript
<ambientLight intensity={0.3} color="#FFF5E1" />
<pointLight position={[0, 2.8, 0]} intensity={0.6} color="#FFE4B5" />
```

### Cool Tech (Server Room)
```typescript
<ambientLight intensity={0.1} color="#E0E8F0" />
<spotLight position={[0, 3, 0]} intensity={0.8} color="#FFFFFF" />
```

## Room Registration Checklist

1. Create TSX component in `rooms/` using `RoomShell`
2. Add entry to `ROOMS` in `rooms/types.ts`
3. Add camera presets to `locations.json`
4. Add activity positions to `ACTIVITY_POSITIONS`
5. Add character positions to `CHARACTER_3D_POSITIONS`
6. Test camera-based wall transparency
