# Viseme Mapping Reference

## Rhubarb Phoneme Codes → RPM Oculus Visemes

| Rhubarb Code | Mouth Shape | RPM Viseme | ARKit Equivalent | Description |
|---|---|---|---|---|
| `A` | Wide open | `viseme_aa` | `jawOpen` | "ah" sound |
| `B` | Lips together | `viseme_PP` | `mouthClose` | b, m, p sounds |
| `C` | Narrow open | `viseme_I` | `mouthSmileLeft/Right` | "ee" sound |
| `D` | Slight open | `viseme_E` | `mouthFunnel` (partial) | "eh" sound |
| `E` | Round open | `viseme_O` | `mouthFunnel` | "oh" sound |
| `F` | Teeth on lip | `viseme_FF` | `mouthFunnel` + `jawOpen` | f, v sounds |
| `G` | Pucker | `viseme_U` | `mouthPucker` | "oo" sound |
| `H` | Teeth showing | `viseme_CH` | `jawOpen` + `mouthSmileLeft` | sh, ch sounds |
| `X` | Closed | `viseme_sil` | (neutral) | Silence |

## Python Mapping Dict

```python
RHUBARB_TO_RPM = {
    'A': 'viseme_aa',
    'B': 'viseme_PP',
    'C': 'viseme_I',
    'D': 'viseme_E',
    'E': 'viseme_O',
    'F': 'viseme_FF',
    'G': 'viseme_U',
    'H': 'viseme_CH',
    'X': 'viseme_sil',
}
```

## ARKit Morph Targets (Full Set on RPM Avatars)

RPM avatars include 52 ARKit blend shapes when downloaded with `?morphTargets=ARKit`:

### Eye/Brow (for emotion, not lip sync)
- `eyeBlinkLeft`, `eyeBlinkRight`
- `eyeWideLeft`, `eyeWideRight`
- `browDownLeft`, `browDownRight`
- `browInnerUp`, `browOuterUpLeft`, `browOuterUpRight`

### Mouth (primary for lip sync)
- `jawOpen`, `jawForward`, `jawLeft`, `jawRight`
- `mouthClose`, `mouthFunnel`, `mouthPucker`
- `mouthLeft`, `mouthRight`
- `mouthSmileLeft`, `mouthSmileRight`
- `mouthFrownLeft`, `mouthFrownRight`
- `mouthDimpleLeft`, `mouthDimpleRight`
- `mouthStretchLeft`, `mouthStretchRight`
- `mouthRollLower`, `mouthRollUpper`
- `mouthShrugLower`, `mouthShrugUpper`
- `mouthPressLeft`, `mouthPressRight`
- `mouthLowerDownLeft`, `mouthLowerDownRight`
- `mouthUpperUpLeft`, `mouthUpperUpRight`

### Oculus Viseme Set (alternative to ARKit for lip sync)
- `viseme_sil` — Silent / mouth closed
- `viseme_PP` — p, b, m
- `viseme_FF` — f, v
- `viseme_TH` — th
- `viseme_DD` — t, d
- `viseme_kk` — k, g
- `viseme_CH` — ch, j, sh
- `viseme_SS` — s, z
- `viseme_nn` — n, l
- `viseme_RR` — r
- `viseme_aa` — a (open)
- `viseme_E` — e
- `viseme_I` — i
- `viseme_O` — o
- `viseme_U` — u

## R3F Real-Time Lip Sync

For web real-time (not baked Blender keyframes), drive morph targets directly:

```typescript
import { useFrame } from '@react-three/fiber'

function useLipSync(meshRef, mouthCues, audioRef) {
  useFrame(() => {
    if (!audioRef.current || !meshRef.current) return
    const currentTime = audioRef.current.currentTime
    const cue = mouthCues.find(c => currentTime >= c.start && currentTime < c.end)
    const viseme = RHUBARB_TO_RPM[cue?.value || 'X']

    // Reset all visemes
    for (const v of Object.values(RHUBARB_TO_RPM)) {
      const idx = meshRef.current.morphTargetDictionary[v]
      if (idx !== undefined) meshRef.current.morphTargetInfluences[idx] = 0
    }

    // Activate current
    const idx = meshRef.current.morphTargetDictionary[viseme]
    if (idx !== undefined) meshRef.current.morphTargetInfluences[idx] = 1
  })
}
```

## Notes

- RPM URL must include `?morphTargets=ARKit,Oculus Visemes` to get blend shapes
- Rhubarb requires WAV input — convert MP3 with `ffmpeg -i voice.mp3 voice.wav`
- fps must match between Rhubarb processing and Blender scene (default: 24)
- For smoother transitions, interpolate between visemes over 2-3 frames rather than hard switching
