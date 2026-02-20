# Asset Sources Reference

## Poly Pizza (Primary — CC0)

**API**: `https://api.poly.pizza/v1/search`
**License**: CC0 (public domain, commercial use OK)
**Format**: GLB direct download
**Quality**: Low-poly, clean meshes, web-ready

### API Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `q` | string | Search query |
| `format` | string | "glb" or "gltf" |
| `limit` | int | Max results (1-20) |

### Response Structure

```json
{
  "results": [
    {
      "Title": "Office Chair",
      "Download": "https://poly.pizza/download/...",
      "Author": "...",
      "License": "CC0"
    }
  ]
}
```

### Recommended Searches for Silicon Valley Office

| Query | Category | Expected Results |
|-------|----------|-----------------|
| "office chair" | Furniture | Rolling desk chairs |
| "desk" | Furniture | Office/work desks |
| "laptop computer" | Props | Open laptops |
| "monitor screen" | Props | Desktop monitors |
| "whiteboard" | Props | Wall-mounted boards |
| "couch sofa" | Furniture | Seating |
| "arcade machine" | Props | Retro arcade cabinets |
| "coffee maker" | Props | Kitchen appliances |
| "ping pong table" | Props | Game table |
| "bookshelf" | Furniture | Book storage |
| "plant pot" | Props | Indoor plants |
| "pizza box" | Props | Food items |
| "server rack" | Props | IT equipment |
| "keyboard" | Props | Computer peripherals |

## KennyNL (Secondary — CC0)

**URL**: https://kenney.nl/assets
**License**: CC0 (public domain)
**Format**: GLB, FBX, OBJ in ZIP downloads
**Quality**: Game-ready, consistent low-poly style

### Relevant Asset Packs

| Pack | URL | Contents |
|------|-----|----------|
| Furniture Kit | kenney.nl/assets/furniture-kit | Desks, chairs, tables, shelves |
| Office Kit | kenney.nl/assets/office-kit | Computers, phones, plants, filing cabinets |
| Game Kit | kenney.nl/assets/game-kit | Arcade machines, game items |
| Food Kit | kenney.nl/assets/food-kit | Pizza, drinks, snacks |

Download ZIP, extract, use GLB files directly. No API needed.

## HunyuaN3D-2 (Custom Props Only)

**Method**: Blender addon, image-to-3D
**When to use**: Branded or custom props not found in free libraries
**Never for**: Human characters (produces fused-limb grotesque models)

### Best Practices

- Provide clear, well-lit reference images with white/neutral background
- Keep prompts simple: "kanban board with sticky notes" not "office kanban board with colorful sticky notes arranged in columns with headers"
- Always post-process: `remove_doubles(threshold=0.001)` + `normals_make_consistent`
- Decimate to ~5K tris for props
- Noisy meshes: increase remove_doubles threshold to 0.005

### Good Prompts

```
✅ "server rack with blinking lights"
✅ "whiteboard with diagrams"
✅ "retro arcade cabinet"
✅ "coffee mug"
```

### Bad Prompts

```
❌ "person sitting at desk" (human character)
❌ "hand holding coffee cup" (body part)
❌ "group of people standing" (multiple humans)
```

## Sketchfab (Manual — One-Time)

**URL**: https://sketchfab.com
**License**: Mixed (filter for CC0 or CC-BY)
**Quality**: Varies widely, some excellent

Use for specific detailed props that can't be found on Poly Pizza or KennyNL. Requires manual download (no batch API for free tier).

## Normalization Requirements

All downloaded assets MUST be normalized before scene placement:

1. **Scale**: Longest dimension = 1.0 meter (caller applies explicit scale)
2. **Origin**: Center of bounding box, bottom at Z=0
3. **Orientation**: Y-up (GLB standard)
4. **Poly count**: ≤8K tris for furniture, ≤5K for props
5. **Transforms**: Applied (no pending rotation/scale)
6. **Materials**: Preserved from source

Run: `blender --background --python normalize_assets.py -- input_dir/ output_dir/`
