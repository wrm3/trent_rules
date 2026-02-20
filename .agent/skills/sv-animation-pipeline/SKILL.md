---
name: sv-animation-pipeline
description: Apply animations to rigged 3D characters via Mixamo clips, BVH motion files, and bone retargeting. Covers the 18-state animation system, animation state machine, crossfade blending, and GLB export with embedded clips. This skill should be used when rigging character animations, retargeting Mixamo FBX clips, applying BVH motion data, or configuring the character animation state machine.
triggers:
  - "animation"
  - "Mixamo"
  - "BVH animation"
  - "retarget"
  - "bone map"
  - "walk cycle"
  - "animation clip"
  - "animation state"
  - "character animation"
  - "animation pipeline"
  - "motion capture"
agents:
  - animation-engineer
  - full-stack-developer
version: 1.0.0
---

# Silicon Valley Animation Pipeline

Apply and manage animations for 3D characters. Covers Mixamo clip acquisition, BVH motion file application, bone retargeting, the 18-state animation system, and GLB export with embedded animation clips.

## Critical Rules

1. **DO NOT upload to Mixamo for rigging** if the model is already rigged (RPM/Avaturn output is pre-rigged). Only use Mixamo for animation clips.
2. **DO NOT re-rig with Rigify** unless explicitly told to — character generators output pre-rigged models.
3. **RPM and Mixamo use the same skeleton** — Mixamo animations apply directly to RPM characters without retargeting.
4. **Run Blender headless** — `blender --background --python script.py`, never BlenderMCP.
5. **Enable "In Place" in Mixamo** or apply root motion baking to prevent sliding feet.

## Three-Layer Animation Architecture

```
Layer 1: Behavior Engine (2D logic)
  ↓ Emits activity states (coding, thinking, talking, etc.)
Layer 2: useCharacter3DAnimation (bridge hook)
  ↓ Maps activities → 3D waypoints + animation states
Layer 3: GLB Model Animations (Three.js useAnimations)
  ↓ Plays Mixamo clips (walk, sit, type, idle, etc.)
```

For Layer 2 and 3 integration details, see `sv-r3f-integration` skill.

## Method A: Mixamo FBX Clips (Primary)

### Required Animations per Character

| Clip Name | Mixamo Search | Loop | Use Case |
|-----------|--------------|------|----------|
| `Idle` | "Breathing Idle" | Yes | Default standing |
| `Walking` | "Walking" | Yes | Movement between waypoints |
| `Typing` | "Typing" | Yes | Working at computer |
| `Sitting_Idle` | "Sitting Idle" | Yes | Seated rest |
| `Talking` | "Talking" | Yes | In conversation |
| `Thinking` | "Weight Shift" | Yes | At whiteboard/kanban |
| `Standing_Up` | "Standing Up" | No | Transition desk→standing |
| `Sitting_Down` | "Sitting Down" | No | Transition standing→desk |

### Mixamo Workflow

1. Visit mixamo.com, sign in with Adobe account
2. Upload FBX (exported from Blender, one-time per character)
3. For each animation: search → preview → download as "FBX Binary (.fbx)"
4. Settings: "Without Skin" for all except first (needs "With Skin")
5. Import back into Blender, combine into single GLB

### Export for Mixamo

```python
import bpy

bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.type in ('MESH', 'ARMATURE'):
        obj.select_set(True)

bpy.ops.export_scene.fbx(
    filepath="character_for_mixamo.fbx",
    use_selection=True,
    add_leaf_bones=False,
    bake_anim=False,
)
```

### Retarget Mixamo Animations in Blender

```bash
blender --background --python retarget_animations.py -- --blend character.blend --anim_dir animations/ --output final.blend
```

```python
import bpy, sys, os, glob

def retarget_fbx_animations(blend_path: str, anim_dir: str, output_path: str):
    bpy.ops.wm.open_mainfile(filepath=blend_path)
    char_armature = next((o for o in bpy.data.objects if o.type == 'ARMATURE'), None)
    if not char_armature:
        raise RuntimeError("No armature found")

    for fbx_path in glob.glob(os.path.join(anim_dir, "*.fbx")):
        anim_name = os.path.splitext(os.path.basename(fbx_path))[0]
        bpy.ops.import_scene.fbx(
            filepath=fbx_path, use_anim=True,
            automatic_bone_orientation=True, ignore_leaf_bones=True)

        imported = [o for o in bpy.context.selected_objects if o.type == 'ARMATURE']
        if not imported:
            continue

        anim_armature = imported[0]
        if anim_armature.animation_data and anim_armature.animation_data.action:
            action = anim_armature.animation_data.action
            action.name = anim_name
            if not char_armature.animation_data:
                char_armature.animation_data_create()
            char_armature.animation_data.action = action

            bpy.context.view_layer.objects.active = char_armature
            bpy.ops.nla.bake(
                frame_start=int(action.frame_range[0]),
                frame_end=int(action.frame_range[1]),
                only_selected=False, visual_keying=True,
                clear_constraints=False, use_current_action=True,
                bake_types={'POSE'})

        bpy.data.objects.remove(anim_armature, do_unlink=True)

    bpy.ops.wm.save_as_mainfile(filepath=output_path)
```

## Method B: BVH Animation Files

Download BVH packs once, store locally, apply via script. Useful when Mixamo is unavailable.

### Free BVH Sources

- Carnegie Mellon Motion Capture: http://mocap.cs.cmu.edu/
- Bandai Namco Research: https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset
- Mixamo BVH exports (download once manually)

### Apply BVH

```python
import bpy

def apply_bvh(blend_path: str, bvh_path: str, output_path: str):
    bpy.ops.wm.open_mainfile(filepath=blend_path)
    armature = next(obj for obj in bpy.data.objects if obj.type == 'ARMATURE')
    bpy.context.view_layer.objects.active = armature
    bpy.ops.import_anim.bvh(filepath=bvh_path, use_fps_scale=True, use_cyclic=False)
    bpy.ops.wm.save_as_mainfile(filepath=output_path)
```

### Bone Retargeting (CMU → Mixamo/RPM)

For bone map tables, see `reference/bone_maps.md`.

## All 18 Animation States

| State | GLB Clip | Loop | Description |
|-------|----------|------|-------------|
| `idle` | Idle | Yes | Default standing |
| `talking` | Talking | Yes | In conversation |
| `typing` | Typing | Yes | At keyboard |
| `thinking` | Weight Shift | Yes | Contemplating |
| `walking` | Walking | Yes | Moving |
| `eating` | Eating | Yes | With food/drink |
| `coding` | Typing | Yes | Same as typing |
| `presenting` | Gesture | Yes | At whiteboard |
| `celebrating` | Victory | No | Jump/cheer |
| `frustrated` | Head Down | Yes | Upset |
| `sleeping` | Sleeping | Yes | Asleep |
| `reading` | Reading | Yes | At screen |
| `arguing` | Arguing | Yes | Heated debate |
| `laughing` | Laughing | No | Amused |
| `whispering` | Lean In | No | Secretive |
| `panicking` | Panic | Yes | Stressed |
| `bored` | Bored | Yes | Unengaged |
| `excited` | Excited | Yes | Energized |

## Final GLB Export with Animations

```python
import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.export_scene.gltf(
    filepath="character_final.glb",
    use_selection=True,
    export_format='GLB',
    export_apply=True,
    export_animations=True,
    export_morph=True,
)
```

## Performance Considerations

- **Max animated characters on screen**: 7-10 (browser dependent)
- **LOD**: Distant characters use simpler animations or freeze
- **Animation update rate**: 30fps for distant, 60fps for close
- **Crossfade duration**: 0.3 seconds between states
- **Skeleton sharing**: Characters with same base can share skeleton definition

## Reference Files

- `reference/animation_system.md` — Full 3-layer architecture, state machine, movement system, character-specific idles
- `reference/bone_maps.md` — CMU→Mixamo, RPM bone names, retarget lookup tables
