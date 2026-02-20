# Base Model Reference

## 8 Base Models (MB-Lab Generated)

All stored at: `docker/frontend/public/models/characters/bases/`

| File | Preset | Vertices | Bones | Size |
|------|--------|----------|-------|------|
| `base_male_caucasian.glb` | m_ca01 | 17,996 | 71 | 37.5 MB |
| `base_male_african.glb` | m_af01 | 17,996 | 71 | 37.5 MB |
| `base_male_asian.glb` | m_as01 | 17,996 | 71 | 37.5 MB |
| `base_male_latino.glb` | m_la01 | 17,996 | 71 | 37.5 MB |
| `base_female_caucasian.glb` | f_ca01 | 18,210 | 71 | 37.3 MB |
| `base_female_african.glb` | f_af01 | 18,210 | 71 | 37.3 MB |
| `base_female_asian.glb` | f_as01 | 18,210 | 71 | 37.3 MB |
| `base_female_latino.glb` | f_la01 | 18,210 | 71 | 37.3 MB |

## Character → Base Mapping

### Male Characters

| Character | Base Model | Mass | Tone | Ethnicity Match |
|-----------|-----------|------|------|-----------------|
| Richard Hendricks | base_male_caucasian | 0.40 | 0.45 | Direct |
| Gilfoyle | base_male_caucasian | 0.45 | 0.50 | Direct |
| Erlich Bachman | base_male_caucasian | 0.78 | 0.30 | Direct (heavy) |
| Jared Dunn | base_male_caucasian | 0.35 | 0.40 | Direct (thin/tall) |
| Big Head | base_male_caucasian | 0.55 | 0.40 | Direct |
| Gavin Belson | base_male_caucasian | 0.55 | 0.55 | Direct |
| Russ Hanneman | base_male_caucasian | 0.50 | 0.55 | Direct |
| Peter Gregory | base_male_caucasian | 0.45 | 0.40 | Direct |
| Dinesh Chugtai | base_male_latino | 0.45 | 0.50 | Closest (Pakistani) |
| Jian Yang | base_male_asian | 0.42 | 0.45 | Direct |

### Female Characters

| Character | Base Model | Mass | Tone | Ethnicity Match |
|-----------|-----------|------|------|-----------------|
| Monica Hall | base_female_caucasian | 0.45 | 0.50 | Direct |
| Carla Walton | base_female_caucasian | 0.45 | 0.50 | Direct |
| Laurie Bream | base_female_caucasian | 0.40 | 0.45 | Direct |
| Sophia (AI) | base_female_caucasian | 0.42 | 0.55 | Modified (robotic) |

## Skeleton Bone List (71 bones)

Key bones for animation:
- `head` — Head rotation, lip sync
- `spine01`, `spine02`, `spine03` — Torso movement
- `hip` — Root bone, center of mass
- `shoulder_L`, `shoulder_R` — Shoulder rotation
- `upperarm_L/R`, `lowerarm_L/R` — Arm bending
- `hand_L`, `hand_R` — Hand/wrist
- `thigh_L/R`, `calf_L/R` — Legs
- `foot_L`, `foot_R` — Feet placement
- `toes_L`, `toes_R` — Toe flex

## Mixamo Animation Compatibility

The MB-Lab skeleton is compatible with Mixamo auto-rigging. When uploading:
1. Export as FBX (binary)
2. Mixamo detects humanoid skeleton automatically
3. Place markers on: chin, wrists, elbows, knees, groin
4. Download animations as "FBX Binary" with "Without Skin" (except first)

## Post-Processing Pipeline

```
Base GLB (37 MB)
  ↓ Decimate (ratio 0.28)
~5,000 vertices (est. 3-5 MB)
  ↓ Add hair mesh
  ↓ Add clothing mesh
  ↓ Bake textures to 1K maps
  ↓ Export FBX for Mixamo
  ↓ Apply 8 animation clips
  ↓ Re-import to Blender
  ↓ Export final GLB
Target: 2-5 MB per character with animations
```
