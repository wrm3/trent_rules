---
name: sv-character-shading
description: Apply toon shaders, materials, mesh optimization, hair, and clothing to 3D character avatars. Covers Blender EEVEE toon shading, solidify-based outlines, decimate for web, mesh-based hair, clothing from body mesh, and cartoonified proportions. This skill should be used when styling raw character GLBs with toon shading, optimizing character meshes for web rendering, or adding hair and clothing.
triggers:
  - "toon shader"
  - "character shading"
  - "decimate mesh"
  - "mesh hair"
  - "character clothing"
  - "outline shader"
  - "cartoon style"
  - "optimize character"
  - "web optimization"
  - "character materials"
agents:
  - 3d-character-artist
  - frontend-developer
version: 1.0.0
---

# Silicon Valley Character Shading & Optimization

Transform raw avatar GLBs into stylized, web-optimized characters with toon shading, outlines, mesh-based hair, clothing, and cartoonified proportions.

## Critical Rules

1. **DO NOT leave raw unshaded grey mesh** — always apply a toon shader before delivering.
2. **DO NOT use particle hair** — particle systems don't export to GLB. Use mesh-based hair only.
3. **Always decimate for web** — 18K verts → ~5K verts for 60fps R3F rendering.
4. **Run headless** — `blender --background --python script.py`, never BlenderMCP.
5. **Apply transforms before export** — location, rotation, scale must be applied.

## Decision Tree

```
Starting from a raw avatar GLB?
  YES → Phase 1: Import + Toon Shader

Need web performance?
  YES → Phase 2: Decimate (18K → 5K verts)
  NO  → Skip decimate (offline render)

Character needs hair?
  Mesh hair from Sketchfab → Phase 3A: Import + fit
  Sculpted hair            → Phase 3B: Blender curves → mesh

Character needs clothing?
  Simple (t-shirt, pants)  → Phase 4A: Body mesh duplicate method
  Complex (suit, dress)    → Phase 4B: Import from Sketchfab

Want cartoon proportions?
  YES → Phase 5: Bone scale adjustments (bigger head/eyes)
```

## Phase 1: Toon Shader Setup

Run as headless Blender script:

```bash
blender --background --python toon_setup.py -- --glb "/path/to/avatar.glb" --output "/path/to/output.blend"
```

### Core Toon Shader

```python
import bpy

def apply_toon_shader(obj):
    """Apply toon BSDF shader with solidify-based outline to a mesh object."""
    for slot in obj.material_slots:
        mat = slot.material
        if mat is None:
            mat = bpy.data.materials.new(name="ToonMat")
            slot.material = mat

        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        nodes.clear()

        output = nodes.new('ShaderNodeOutputMaterial')
        toon = nodes.new('ShaderNodeBsdfToon')
        toon.inputs['Size'].default_value = 0.8     # Band width (0.0-1.0)
        toon.inputs['Smooth'].default_value = 0.05   # Edge softness

        links.new(toon.outputs['BSDF'], output.inputs['Surface'])

    # Solidify-based outline
    if not any(m.type == 'SOLIDIFY' for m in obj.modifiers):
        solidify = obj.modifiers.new(name="Outline", type='SOLIDIFY')
        solidify.thickness = 0.003
        solidify.offset = 1.0
        solidify.use_flip_normals = True
        solidify.use_rim = False
        solidify.material_offset = len(obj.material_slots)

        outline_mat = bpy.data.materials.new(name="Outline")
        outline_mat.use_nodes = True
        outline_mat.node_tree.nodes["Principled BSDF"].inputs['Base Color'].default_value = (0, 0, 0, 1)
        outline_mat.use_backface_culling = True
        obj.data.materials.append(outline_mat)
```

### Toon Lighting

```python
def setup_toon_lighting():
    """Three-point lighting optimized for toon shading."""
    # Key light (sun)
    bpy.ops.object.light_add(type='SUN', location=(5, -5, 8))
    key = bpy.context.active_object
    key.data.energy = 3.0
    key.rotation_euler = (0.8, 0.2, 0.5)

    # Fill light (area)
    bpy.ops.object.light_add(type='AREA', location=(-4, 2, 4))
    fill = bpy.context.active_object
    fill.data.energy = 1.5
    fill.data.size = 5
```

### EEVEE Configuration

```python
bpy.context.scene.render.engine = 'BLENDER_EEVEE'
bpy.context.scene.eevee.use_bloom = True
```

### Shader Tuning

| Parameter | Effect | Default | Range |
|-----------|--------|---------|-------|
| `Size` | Band width — higher = more lit area | 0.8 | 0.0-1.0 |
| `Smooth` | Edge softness — lower = sharper toon edge | 0.05 | 0.0-1.0 |
| `thickness` (solidify) | Outline width | 0.003 | 0.001-0.01 |

If the toon shader appears too dark/light, adjust `Size`. For thicker cartoon outlines, increase solidify `thickness`.

## Phase 2: Decimate for Web

Target: 18,000 → ~5,000 vertices for web. ~2-5 MB GLB final size.

```python
def decimate_for_web(obj, target_ratio=0.28):
    """Decimate mesh to ~5K verts from 18K MB-Lab output."""
    mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
    mod.ratio = target_ratio  # 0.28 ≈ 5K from 18K
    bpy.ops.object.modifier_apply(modifier="Decimate")
```

### Target File Sizes

| Character Type | Vertices | Textures | Target GLB |
|---------------|----------|----------|------------|
| Main cast (7) | 5,000 | 1K maps | 2-5 MB |
| Supporting (7) | 3,000 | 512 maps | 1-3 MB |
| Background | 2,000 | 256 maps | 0.5-1 MB |

## Phase 3: Mesh-Based Hair

### 3A: Import Pre-Made Hair

Source mesh hair from Sketchfab (free CC0), import into Blender, scale and position to fit character head, parent to head bone.

### 3B: Curves to Mesh

```python
# Create Bezier curves for hair strands
# Convert curves to mesh: Object → Convert → Mesh
# This gives exportable geometry
```

## Phase 4: Clothing

### 4A: Body Mesh Duplicate Method (Simple)

```python
# Duplicate body mesh
# Delete vertices below waist / above neck
# Scale slightly outward (1.02x)
# Apply Shrinkwrap modifier targeting body
# Assign clothing material/color
```

### 4B: External Clothing Import

Source clothing meshes from Sketchfab, fit to character body, parent to armature with automatic weights.

## Phase 5: Cartoonified Proportions (Optional)

```python
def cartoonify_proportions(armature):
    """Scale bones for cartoon look — bigger head, bigger eyes."""
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    for bone_name in ['LeftEye', 'RightEye', 'leftEye', 'rightEye']:
        bone = armature.pose.bones.get(bone_name)
        if bone:
            bone.scale = (1.3, 1.3, 1.3)
    bpy.ops.object.mode_set(mode='OBJECT')
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Toon shader too dark | Increase `Size` parameter (e.g., 0.9) |
| Toon shader too flat | Decrease `Size` (e.g., 0.5), increase `Smooth` slightly |
| Outline too thick on close-up | Reduce solidify `thickness` to 0.001 |
| Hair clips through head | Adjust hair mesh position, add Shrinkwrap modifier |
| Decimate destroys face | Use weighted vertex groups — protect face vertices from decimation |
| Export loses materials | Ensure `export_materials='EXPORT'` in glTF export settings |
