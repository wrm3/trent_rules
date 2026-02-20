# Failed Approaches — What Didn't Work and Why

Consult this document before re-attempting any of these approaches.

---

## Hyper3D Text-to-3D for Human Characters

**Date**: February 2026

Models came out looking like "human centipede" — limbs fused, contorted poses, animal-like proportions. Even simple standing poses had poor anatomy. No recognizable actor likeness achieved.

**Why it failed**: Text-to-3D AI models are trained on objects, not articulated humans. Pose specification in prompts causes the AI to fuse the pose into geometry rather than creating a riggable mesh.

**Rule**: Never use text-to-3D for human characters. Only use for props, furniture, architecture, vehicles.

---

## MPFB2 (MakeHuman Plugin for Blender 2)

**Date**: February 2026

Blender 5.0's new extension system rejects MPFB2 v2.0.8 with "The 'package' does not name an extension." No current workaround — wait for update or use Blender 4.x.

---

## Batch Hyper3D + Blender Import (OOM Crash)

**Date**: February 2026

Generating 14 character models in parallel and importing all into one Blender scene caused OOM crash. The machine has 128GB RAM but the Cursor IDE process has lower limits.

**Rule**: Batch in groups of 3-4 models. Import, export, clear scene, repeat.

---

## Wrong MB-Lab Character Type Initialization

Must set BOTH properties before initialization:
```python
scene.mblab_template_name = 'human_male_base'  # Category filter
scene.mblab_character_name = 'm_ca01'           # Actual selector
bpy.ops.mbast.init_character()
```

The `character_name` is the actual selector. The `template_name` is just a filter.

---

## ReadyPlayerMe (Considered, Not Attempted Initially)

Was initially skipped because avatar style is cartoony/VRChat-style. However, RPM has since been adopted as the primary pipeline for speed — the cartoon style works well with toon shading.

---

## Unreal Engine / MetaHuman (Not Adopted)

Produces photorealistic characters but requires Unreal Engine (incompatible with R3F/Three.js pipeline), would need Pixel Streaming, and cannot be scripted by AI.

---

## Character Creator 4 / Reallusion ($200)

AI cannot interact with it (GUI-only, no API/scripting). Manual creation only.
