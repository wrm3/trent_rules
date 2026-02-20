---
name: sv-asset-pipeline
description: Source, download, normalize, and place 3D assets for Silicon Valley environments. Covers Poly Pizza API, KennyNL free assets, HunyuaN3D-2 custom prop generation, Blender batch normalization (scale, orientation, poly count), and furniture placement from scene definitions. This skill should be used when sourcing 3D props and furniture, normalizing downloaded assets, generating custom props with AI, or placing assets in room scenes.
triggers:
  - "3D assets"
  - "Poly Pizza"
  - "KennyNL"
  - "asset sourcing"
  - "normalize assets"
  - "furniture"
  - "props"
  - "HunyuaN3D"
  - "asset pipeline"
  - "download models"
  - "GLB assets"
agents:
  - 3d-environment-artist
  - full-stack-developer
version: 1.0.0
---

# Silicon Valley Asset Pipeline

Source, normalize, and place 3D props and furniture for the Silicon Valley environment. All assets must be CC0/free license for commercial use.

## Critical Rules

1. **Always find free CC0 alternatives first** — never use paid asset stores (Fab, TurboSquid).
2. **HunyuaN3D-2 is for props ONLY** — never use for human characters.
3. **Normalize all downloaded assets** before placing in scene — wrong scale/orientation is the #1 issue.
4. **Run Blender headless** — `blender --background --python script.py`.
5. **Target poly budgets**: Props ~5K tris, furniture ~8K tris, large items ~10K tris.

## Decision Tree

```
Need a specific prop?
  Common (desk, chair, laptop) → Poly Pizza API or KennyNL
  Branded/Custom (Pied Piper server rack) → HunyuaN3D-2 from reference image
  Not found anywhere → Simple Blender primitives (boxes, cylinders)

Asset downloaded?
  YES → Normalize (scale, orient, decimate) → Place in scene
```

## Source 1: Poly Pizza API (CC0, Best for Office Props)

```python
import requests, pathlib

POLY_PIZZA_SEARCH = "https://api.poly.pizza/v1/search"

def search_and_download(query: str, output_dir: str, limit: int = 3) -> list:
    """Search Poly Pizza for CC0 models, download GLBs."""
    r = requests.get(POLY_PIZZA_SEARCH, params={"q": query, "format": "glb", "limit": limit})
    results = r.json().get("results", [])
    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    downloaded = []
    for item in results:
        download_url = item.get("Download")
        if not download_url:
            continue
        name = item["Title"].replace(" ", "_").lower()
        dest = output_dir / f"{name}.glb"
        dest.write_bytes(requests.get(download_url).content)
        downloaded.append(str(dest))
    return downloaded
```

### Batch Asset Sourcing

```python
asset_queries = [
    ("office chair", "assets/furniture"),
    ("laptop computer", "assets/props"),
    ("desk", "assets/furniture"),
    ("whiteboard", "assets/props"),
    ("arcade machine", "assets/props"),
    ("couch sofa", "assets/furniture"),
    ("coffee maker", "assets/props"),
    ("ping pong table", "assets/props"),
]

for query, folder in asset_queries:
    search_and_download(query, folder, limit=2)
```

## Source 2: KennyNL Assets (CC0, Game-Ready)

Direct download, no API needed:

```
https://kenney.nl/assets/furniture-kit    — desks, chairs, shelves
https://kenney.nl/assets/office-kit       — computers, phones, plants
https://kenney.nl/assets/game-kit         — arcade machines, game items
```

Download ZIP, extract GLBs directly.

## Source 3: HunyuaN3D-2 Custom Props

When you can't find a specific prop, generate from a reference image:

```python
import bpy

def generate_prop_from_image(image_path: str, output_path: str, prompt: str = ""):
    """Use HunyuaN3D-2 Blender addon to generate mesh from reference image."""
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.select_set(True)
    bpy.ops.object.delete()

    bpy.ops.hunyuan3d.generate(image_path=image_path, prompt=prompt, output_mesh=True)

    # Clean up generated mesh
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.remove_doubles(threshold=0.001)
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.object.mode_set(mode='OBJECT')
            # Decimate for web
            mod = obj.modifiers.new(name="Decimate", type='DECIMATE')
            mod.ratio = 0.3  # target ~5K tris
            bpy.ops.object.modifier_apply(modifier="Decimate")

    bpy.ops.export_scene.gltf(filepath=output_path, export_format='GLB',
                               export_apply=True, export_yup=True)
```

**When to use HunyuaN3D-2 vs Poly Pizza:** Use Poly Pizza first — faster, cleaner meshes. Fall back to HunyuaN3D-2 for custom branded props.

## Batch Normalization

Downloaded assets often have wrong scale, axis orientation, or excessive polys. Normalize all in one pass:

```bash
blender --background --python normalize_assets.py -- assets/ assets/normalized/
```

### normalize_assets.py

```python
import bpy, pathlib, sys

TARGET_MAX_DIMENSION = 1.0  # longest axis = 1 meter, caller scales in scene

def normalize_glb(input_path: str, output_path: str, target_tris: int = 8000):
    # Clear scene
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    bpy.ops.import_scene.gltf(filepath=input_path)
    objs = [o for o in bpy.context.scene.objects if o.type == 'MESH']
    if not objs:
        return False

    # Join all meshes
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objs:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    combined = bpy.context.active_object

    # Apply transforms
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    # Normalize scale
    dims = combined.dimensions
    max_dim = max(dims.x, dims.y, dims.z)
    if max_dim > 0:
        scale_factor = TARGET_MAX_DIMENSION / max_dim
        combined.scale = (scale_factor, scale_factor, scale_factor)
        bpy.ops.object.transform_apply(scale=True)

    # Center at origin, bottom at z=0
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    combined.location = (0, 0, combined.dimensions.z / 2)
    bpy.ops.object.transform_apply(location=True)

    # Decimate if over budget
    current_tris = sum(len(p.vertices) - 2 for p in combined.data.polygons)
    if current_tris > target_tris:
        mod = combined.modifiers.new("Decimate", 'DECIMATE')
        mod.ratio = target_tris / current_tris
        bpy.ops.object.modifier_apply(modifier="Decimate")

    # Export
    pathlib.Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=output_path, export_format='GLB',
                               export_apply=True, export_yup=True)
    return True

# CLI: blender --background --python normalize_assets.py -- input_dir/ output_dir/
args = sys.argv[sys.argv.index('--') + 1:]
for glb in pathlib.Path(args[0]).rglob("*.glb"):
    out = pathlib.Path(args[1]) / glb.relative_to(args[0])
    normalize_glb(str(glb), str(out))
```

## Furniture Placement from Scene Definition

Place normalized assets at positions defined in `scene_definition.json`:

```python
ZONE_PROP_MAP = {
    "workstation":      ["desk.glb", "office_chair.glb", "laptop.glb"],
    "interactive_wall": ["whiteboard.glb"],
    "seating":          ["couch.glb"],
    "arcade":           ["arcade_machine.glb"],
    "game_table":       ["ping_pong_table.glb"],
    "appliance":        ["coffee_maker.glb"],
}
```

```bash
blender --background --python place_furniture.py -- scene_definition.json output/furniture_placed.glb
```

## Environment Assets Checklist

**Main Office:** desk ×4, office chair ×4, laptop ×4, couch, whiteboard, kanban board, SWOT board

**Garage/Arcade:** arcade cabinet(s), ping pong table, server rack, cables, boxes

**Kitchen:** coffee maker, counter/sink, bar stools

**Atmosphere props:** houseplants, pizza boxes, energy drinks, sticky notes, motivational posters

## Full Build Pipeline

```bash
# 1. Source assets
python source_assets.py

# 2. Normalize all downloaded GLBs
blender --background --python normalize_assets.py -- assets/ assets/normalized/

# 3. Build room geometry
blender --background --python build_rooms.py -- scene_definition.json output/rooms.glb

# 4. Place furniture
blender --background --python place_furniture.py -- scene_definition.json output/furniture_placed.glb
```

## Reference Files

- `reference/asset_sources.md` — Complete Poly Pizza API reference, KennyNL asset catalog, HunyuaN3D-2 usage guide
