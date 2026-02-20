---
name: sv-r3f-integration
description: Integrate 3D characters and environments into React Three Fiber scenes. Covers R3F Canvas setup, Character3D component with animation blending, BehaviorDriver, RoomShell with dynamic wall transparency, Gallery3D layout, Zustand behavior store, and useCharacter3DAnimation hook. This skill should be used when building the R3F frontend scene, rendering 3D characters in the browser, implementing camera-based wall transparency, or wiring the behavior engine to 3D animations.
triggers:
  - "React Three Fiber"
  - "R3F"
  - "Three.js"
  - "3D scene"
  - "Character3D"
  - "BehaviorDriver"
  - "RoomShell"
  - "Gallery3D"
  - "wall transparency"
  - "3D frontend"
  - "useAnimations"
  - "drei"
  - "3D rendering"
agents:
  - frontend-developer
  - animation-engineer
version: 1.0.0
---

# Silicon Valley R3F Integration

Render 3D characters and environments in the browser using React Three Fiber. Bridges the behavior engine to animated 3D models.

## Architecture

```
Maestro Frontend (React)
  └── React Three Fiber (R3F)
       ├── Scene.tsx — Canvas, lighting, camera, Suspense
       ├── Room Components
       │   ├── RoomShell.tsx — walls/floor/ceiling + dynamic transparency
       │   ├── MainOffice3D.tsx — Erlich's Workspace
       │   ├── Gallery3D.tsx — Character showcase
       │   └── Kitchen3D.tsx, etc.
       ├── Character3D.tsx — GLB loader + animation blending
       ├── BehaviorDriver.tsx — Global tick (drives state machine)
       └── useCharacter3DAnimation.ts — Activity→position+animation bridge
```

## Dependencies

```bash
npm install @react-three/fiber @react-three/drei @react-three/rapier three zustand
```

## Scene Entry Point

```tsx
import { Canvas } from '@react-three/fiber';
import { Environment, OrbitControls } from '@react-three/drei';
import { Suspense } from 'react';
import { Room } from './components/Room';
import { Character } from './components/Character';
import { BehaviorDriver } from './components/BehaviorDriver';

const CHARACTERS = ['richard', 'gilfoyle', 'dinesh', 'erlich', 'jared', 'bighead', 'jian_yang'];

export function Scene() {
  return (
    <Canvas camera={{ position: [0, 8, 20], fov: 50 }} shadows>
      <ambientLight intensity={0.4} />
      <directionalLight position={[10, 15, 10]} intensity={1} castShadow
        shadow-mapSize={[2048, 2048]} />

      <Suspense fallback={null}>
        <Room glbPath="/assets/rooms.glb" />
        <Room glbPath="/assets/furniture_placed.glb" />

        {CHARACTERS.map(id => (
          <Character key={id} characterId={id}
            glbPath={`/assets/characters/${id}.glb`} />
        ))}

        <BehaviorDriver characterIds={CHARACTERS} />
        <Environment preset="apartment" />
      </Suspense>

      <OrbitControls target={[0, 1, 0]} />
    </Canvas>
  );
}
```

## Character3D Component

Loads GLB model, plays animations with crossfade blending, handles waypoint walking and anchor snapping.

```tsx
import { useEffect, useRef } from 'react';
import { useGLTF, useAnimations } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';
import * as THREE from 'three';
import { useBehaviorStore } from '../store/behaviorStore';

interface CharacterProps {
  characterId: string;
  glbPath: string;
}

export function Character({ characterId, glbPath }: CharacterProps) {
  const { scene, animations } = useGLTF(glbPath);
  const { actions } = useAnimations(animations, scene);
  const groupRef = useRef<THREE.Group>(null);
  const behavior = useBehaviorStore(state => state.characters[characterId]);
  const currentClip = useRef('');

  // Animation crossfade (0.3s blend)
  useEffect(() => {
    if (!behavior || behavior.animationClip === currentClip.current) return;
    const prev = actions[currentClip.current];
    const next = actions[behavior.animationClip];
    if (prev) prev.fadeOut(0.3);
    if (next) next.reset().fadeIn(0.3).play();
    currentClip.current = behavior.animationClip;
  }, [behavior?.animationClip]);

  // Walk toward next waypoint
  useFrame((_, delta) => {
    if (!groupRef.current || !behavior || behavior.state !== 'walking') return;
    const target = new THREE.Vector3(...behavior.targetPosition);
    const current = groupRef.current.position;
    const direction = target.clone().sub(current);

    if (direction.length() < 0.15) {
      useBehaviorStore.getState().advanceWaypoint(characterId);
    } else {
      direction.normalize().multiplyScalar(delta * 1.8); // 1.8 m/s
      current.add(direction);
      groupRef.current.rotation.y = Math.atan2(direction.x, direction.z);
    }
  });

  return (
    <group ref={groupRef}>
      <primitive object={scene} />
    </group>
  );
}
```

## BehaviorDriver (Global Tick)

Drives autonomous behavior for all characters every frame:

```tsx
import { useFrame } from '@react-three/fiber';
import { useBehaviorStore } from '../store/behaviorStore';

export function BehaviorDriver({ characterIds }: { characterIds: string[] }) {
  useFrame((_, delta) => {
    const store = useBehaviorStore.getState();
    for (const id of characterIds) {
      store.tickCharacter(id, delta);
    }
  });
  return null; // renders nothing, just drives logic
}
```

## RoomShell with Dynamic Wall Transparency

Walls between camera and characters automatically fade out:

```tsx
<RoomShell
  width={8} depth={6} height={3}
  wallColor="#C4956A" floorColor="#A0784C"
  isNight={isNight}
  dynamicWalls  // Enable camera-based transparency
/>
```

### Wall Transparency Algorithm

- Uses `useFrame` to check camera angle each frame
- Dot product between camera direction and each wall's inward normal
- When camera looks "through" a wall (dot > threshold), wall fades to transparent
- `THREE.MathUtils.lerp` for smooth opacity transition
- Ceiling also fades when camera is above room

## useCharacter3DAnimation Hook

Bridges 2D behavior engine activities to 3D positions and animation states:

### Activity → Position Mapping

```typescript
const ACTIVITY_POSITIONS = {
  'main-office': {
    desk: [0, 0, 0],
    whiteboard: [0, 0, -3.8],
    kanban: [-4, 0, 0],
    center: [0, 0, 0.5],
    couch: [3, 0, 2.5],
    foosball: [3.5, 0, -1],
    piano: [-3, 0, -3],
    standing: [1, 0, 2],
    door: [-4, 0, 2],
  },
}
```

### Activity → Animation State Mapping

```typescript
const ACTIVITY_ARRIVAL_STATE = {
  desk: 'typing',
  whiteboard: 'thinking',
  kanban: 'thinking',
  foosball: 'idle',
  couch: 'idle',
  piano: 'idle',
  center: 'talking',
}
```

### Animation Clip Mapping

```typescript
const CLIP_MAP: Record<string, string> = {
  idle: 'Idle',
  walking: 'Walking',
  typing: 'Typing',
  thinking: 'Thinking',
  talking: 'Talking',
  eating: 'Eating',
  presenting: 'Gesture',
  celebrating: 'Victory',
  frustrated: 'Head Down',
  sleeping: 'Sleeping',
  laughing: 'Laughing',
  panicking: 'Panic',
}
```

## Gallery3D Layout

Dynamic character showcase with evenly-spaced rows:

```typescript
function buildGalleryLayout(characters: string[]) {
  const count = characters.length;
  const rowSize = Math.min(7, Math.ceil(Math.sqrt(count)));
  // Centers each row, distributes characters evenly
  // Prevents "jammed front line" issue
}
```

## Movement System

Characters interpolate smoothly between positions:

```typescript
useFrame((_, delta) => {
  if (state === 'walking') {
    positionRef.current.lerp(targetPosition, delta * walkSpeed);
    // Face direction of travel
    const direction = new THREE.Vector3()
      .subVectors(targetPosition, positionRef.current).normalize();
    const targetRotation = Math.atan2(direction.x, direction.z);
    rotationRef.current = THREE.MathUtils.lerp(rotationRef.current, targetRotation, delta * 5);
    // Arrival check
    if (positionRef.current.distanceTo(targetPosition) < 0.1) {
      state = arrivalState;
    }
  }
});
```

## Performance

- **Max animated characters on screen**: 7-10
- **Animation crossfade**: 0.3 seconds
- **Walk speed**: 1.8 m/s
- **LOD**: Distant characters freeze or use simpler animations
- **Shadow map**: 2048×2048

## File Locations

| Path | Purpose |
|------|---------|
| `docker/frontend/src/components/trentworks3d/` | All R3F 3D components |
| `docker/frontend/src/components/trentworks3d/rooms/` | Room components |
| `docker/frontend/src/components/trentworks3d/Character3D.tsx` | Character renderer |
| `docker/frontend/src/components/trentworks3d/useCharacter3DAnimation.ts` | Animation bridge hook |
| `docker/frontend/src/components/trentworks3d/types.ts` | 3D type definitions |
| `docker/frontend/public/models/characters/` | Character GLB files |
| `docker/themes/trentworks/locations.json` | Room/location theme data |
