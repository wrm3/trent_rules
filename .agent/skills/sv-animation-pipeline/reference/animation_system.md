# Animation System Reference

## Overview

Characters in Maestro are animated through a **three-layer** system:

```
Layer 1: Behavior Engine (2D logic)
  ↓ Emits activity states (coding, thinking, talking, etc.)
Layer 2: useCharacter3DAnimation (bridge hook)
  ↓ Maps activities → 3D waypoints + animation states
Layer 3: GLB Model Animations (Three.js useAnimations)
  ↓ Plays Mixamo clips (walk, sit, type, idle, etc.)
```

## Layer 1: Behavior Engine

The behavior engine (2D system) decides what each character is doing based on:
- Time of day
- Active conversations
- Task assignments
- Random idle behaviors
- User interactions

Output: An `activity` string like `"coding"`, `"meeting"`, `"idle"`, `"coffee"`.

## Layer 2: useCharacter3DAnimation Hook

### State Machine

```
                     ┌─────────────────────┐
                     │     idle (default)   │
                     └──────┬──────┬───────┘
                            │      │
            Activity change │      │ No activity
                            ▼      │
                     ┌──────────────┐
                     │   walking    │ ← Moving to waypoint
                     └──────┬───────┘
                            │
              Arrived at    │
              waypoint      ▼
                     ┌──────────────┐
                     │  destination │ ← typing/thinking/talking/etc.
                     │    state     │
                     └──────────────┘
```

### Movement System

Characters interpolate between positions smoothly:

```typescript
useFrame((_, delta) => {
  if (state === 'walking') {
    positionRef.current.lerp(targetPosition, delta * walkSpeed)
    const direction = new THREE.Vector3()
      .subVectors(targetPosition, positionRef.current).normalize()
    const targetRotation = Math.atan2(direction.x, direction.z)
    rotationRef.current = THREE.MathUtils.lerp(rotationRef.current, targetRotation, delta * 5)
    if (positionRef.current.distanceTo(targetPosition) < 0.1) {
      state = arrivalState
    }
  }
})
```

## Layer 3: GLB Animations (Mixamo)

### Required Animation Clips per Character

| Clip Name | Duration | Loop | Source | Use Case |
|-----------|----------|------|--------|----------|
| `Idle` | 3-5s | Yes | Mixamo "Breathing Idle" | Default standing |
| `Walking` | 1-2s | Yes | Mixamo "Walking" | Movement |
| `Typing` | 2-4s | Yes | Mixamo "Typing" | At computer |
| `Sitting_Idle` | 3-5s | Yes | Mixamo "Sitting Idle" | Seated rest |
| `Talking` | 2-4s | Yes | Mixamo "Talking" | Conversation |
| `Thinking` | 3-5s | Yes | Mixamo "Weight Shift" | At whiteboard |
| `Standing_Up` | 1-2s | No | Mixamo "Standing Up" | Transition |
| `Sitting_Down` | 1-2s | No | Mixamo "Sitting Down" | Transition |

### Animation State Blending

- **Crossfade duration**: 0.3 seconds
- **Transition animations**: Use Standing Up / Sitting Down for desk transitions
- **Idle variation**: Randomly select from 2-3 idle variations to prevent sync

## Character-Specific Idle Behaviors

| Character | Unique Idle | Description |
|-----------|-------------|-------------|
| Erlich | Drinking beer | Lounging on couch |
| Gilfoyle | Typing aggressively | Never stops coding |
| Dinesh | Looking at phone | Checking Tesla rank |
| Richard | Fidgeting | Anxious pacing |
| Jared | Organizing | Straightening things |
| Big Head | Looking confused | Wandering aimlessly |
| Jian Yang | Smoking | Standing near door |

## Performance Considerations

- **Max animated characters on screen**: 7-10 (browser dependent)
- **LOD**: Distant characters freeze or use simpler animations
- **Animation update rate**: 30fps for distant, 60fps for close
- **Skeleton sharing**: Characters with same base can share skeleton definition
- **GPU instancing**: Not available for animated meshes (each needs unique pose)
