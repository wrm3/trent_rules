# Bone Retargeting Maps

## CMU Motion Capture → Mixamo/RPM

Use this map when applying Carnegie Mellon University BVH files to RPM or Mixamo-rigged characters.

```python
CMU_TO_MIXAMO = {
    "Hips": "mixamorig:Hips",
    "Spine": "mixamorig:Spine",
    "Spine1": "mixamorig:Spine1",
    "Spine2": "mixamorig:Spine2",
    "Neck": "mixamorig:Neck",
    "Head": "mixamorig:Head",
    "LeftShoulder": "mixamorig:LeftShoulder",
    "LeftArm": "mixamorig:LeftArm",
    "LeftForeArm": "mixamorig:LeftForeArm",
    "LeftHand": "mixamorig:LeftHand",
    "RightShoulder": "mixamorig:RightShoulder",
    "RightArm": "mixamorig:RightArm",
    "RightForeArm": "mixamorig:RightForeArm",
    "RightHand": "mixamorig:RightHand",
    "LeftUpLeg": "mixamorig:LeftUpLeg",
    "LeftLeg": "mixamorig:LeftLeg",
    "LeftFoot": "mixamorig:LeftFoot",
    "RightUpLeg": "mixamorig:RightUpLeg",
    "RightLeg": "mixamorig:RightLeg",
    "RightFoot": "mixamorig:RightFoot",
}
```

## Retarget Function

```python
def retarget_bones(source_armature, target_armature, bone_map: dict):
    """Remap fcurve bone names from source skeleton to target skeleton."""
    for fcurve in source_armature.animation_data.action.fcurves:
        for bone_src, bone_tgt in bone_map.items():
            if bone_src in fcurve.data_path:
                fcurve.data_path = fcurve.data_path.replace(bone_src, bone_tgt)
```

## MB-Lab → Mixamo

MB-Lab uses different bone naming. Key mappings:

| MB-Lab Bone | Mixamo Bone |
|-------------|-------------|
| `hip` | `mixamorig:Hips` |
| `spine01` | `mixamorig:Spine` |
| `spine02` | `mixamorig:Spine1` |
| `spine03` | `mixamorig:Spine2` |
| `head` | `mixamorig:Head` |
| `shoulder_L` | `mixamorig:LeftShoulder` |
| `upperarm_L` | `mixamorig:LeftArm` |
| `lowerarm_L` | `mixamorig:LeftForeArm` |
| `hand_L` | `mixamorig:LeftHand` |
| `thigh_L` | `mixamorig:LeftUpLeg` |
| `calf_L` | `mixamorig:LeftLeg` |
| `foot_L` | `mixamorig:LeftFoot` |

(Same pattern for `_R` suffixes.)

## RPM Skeleton

RPM characters use the Mixamo skeleton directly — no retargeting needed when applying Mixamo animation FBX files.

## Bandai Namco BVH → Mixamo

Bandai Namco research BVH files use similar naming to CMU. Use `CMU_TO_MIXAMO` map.

## Notes

- Always set `automatic_bone_orientation=True` when importing FBX animations
- Set `ignore_leaf_bones=True` to avoid duplicate end bones
- Bake animations after retargeting: `bpy.ops.nla.bake()`
