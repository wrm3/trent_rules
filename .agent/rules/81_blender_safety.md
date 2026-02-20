---
description: "Safety rules for Blender Python scripts. Enforces headless mode, prevents dangerous patterns."
activation: "always_on"
---

# Blender Python Safety Rules

## Mandatory

1. **Always run headless**: `blender --background --python script.py`
2. **Never use BlenderMCP** — unstable, blocks execution, causes hangs
3. **Never use MB-Lab for facial likeness** — produces faceless base meshes only
4. **Never use Hyper3D/HunyuaN3D-2 for human characters** — produces fused-limb models
5. **Never load 10+ models into Blender simultaneously** — causes OOM crashes
6. **Always apply transforms** before export: `bpy.ops.object.transform_apply()`
7. **Always set `export_yup=True`** in glTF export for web compatibility

## Batch Processing

- Process models in groups of 3-4
- Clear scene between batches: `bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete()`
- Monitor file sizes — flag GLBs >10MB for review

## Script Pattern

```python
#!/usr/bin/env python3
"""script_name.py — Run as: blender --background --python script_name.py -- [args]"""
import bpy, sys

args = sys.argv[sys.argv.index('--') + 1:]
# ... script logic ...
```

## Export Checklist

Before exporting any GLB:
- [ ] Transforms applied (location, rotation, scale)
- [ ] Poly count within budget (5K chars, 8K furniture)
- [ ] Materials assigned (no grey meshes)
- [ ] Y-up orientation (`export_yup=True`)
- [ ] Animations included if character (`export_animations=True`)
- [ ] Morph targets included if character (`export_morph=True`)
