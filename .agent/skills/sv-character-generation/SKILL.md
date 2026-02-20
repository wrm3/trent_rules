---
name: sv-character-generation
description: Generate 3D character avatars from reference photos or text descriptions for the Silicon Valley cast. Covers Ready Player Me API, Avaturn API, MB-Lab base body generation, and Blender headless processing. This skill should be used when creating new 3D characters from photos, generating avatar GLBs, or setting up MB-Lab base bodies for the Silicon Valley cast.
triggers:
  - "create character"
  - "character from photo"
  - "photo to avatar"
  - "Ready Player Me"
  - "RPM avatar"
  - "Avaturn"
  - "MB-Lab"
  - "base body"
  - "character GLB"
  - "new character model"
agents:
  - 3d-character-artist
  - full-stack-developer
version: 1.0.0
---

# Silicon Valley Character Generation

Generate rigged, textured 3D character avatars from reference photos or text descriptions. Produces GLB files with humanoid skeleton, morph targets for lip sync, and Mixamo-compatible rig.

## Critical Rules

1. **DO NOT use BlenderMCP** — unstable, blocks execution. Use headless Blender Python scripts via subprocess.
2. **DO NOT use Hyper3D/HunyuaN3D-2 for human characters** — produces fused-limb grotesque models. Only use for props.
3. **DO NOT specify poses in text-to-3D prompts** — "sitting," "arms crossed" cause AI to generate fused geometry.
4. **MB-Lab requires patching for Blender 5.0** — see `reference/blender_patches.md`.
5. **Always request morph targets** from RPM: `?morphTargets=ARKit,Oculus Visemes` in the GLB URL.
6. **Test one character end-to-end** before batch-creating all 14.

## Decision Tree

```
Have reference photos?
  YES → Method A: Ready Player Me API (primary)
        Falls back to Avaturn API (better realism)
  NO  → Method B: RPM outfit + customization API from text description
        Or Method C: MB-Lab in Blender (full control, more manual work)

Target output?
  Web real-time (R3F) → RPM cartoon style, decimate to ~5K verts
  Offline render       → MB-Lab full detail, 18K verts OK
```

## Method A: Photo-to-Avatar (Ready Player Me)

RPM accepts a photo and returns a fully rigged, textured GLB with face likeness, hair, clothing, humanoid rig (Mixamo-compatible), and ARKit morph targets.

```python
import requests, base64, os

RPM_APP_ID = os.environ.get("RPM_APP_ID")

def create_rpm_avatar(photo_path: str, output_dir: str, style: str = "cartoon") -> str:
    """Create avatar from photo via RPM API. Returns path to GLB file."""
    session = requests.Session()
    base_url = "https://api.readyplayer.me/v2"
    headers = {"X-APP-ID": RPM_APP_ID, "Content-Type": "application/json"}

    # Create avatar
    resp = session.post(f"{base_url}/avatars", headers=headers, json={
        "partner": RPM_APP_ID, "gender": "neutral"
    })
    avatar_id = resp.json()["data"]["id"]

    # Upload photo
    with open(photo_path, "rb") as f:
        photo_b64 = base64.b64encode(f.read()).decode()
    session.put(f"{base_url}/avatars/{avatar_id}/photo",
                headers=headers,
                json={"image": f"data:image/jpeg;base64,{photo_b64}"})

    # Finalize
    session.put(f"{base_url}/avatars/{avatar_id}",
                headers=headers, json={"isDraft": False})

    # Download GLB with morph targets
    glb_url = (f"https://models.readyplayer.me/{avatar_id}.glb"
               f"?morphTargets=ARKit,Oculus Visemes"
               f"&textureSizeLimit=1024&textureAtlas=1024")

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{avatar_id}.glb")
    with open(output_path, "wb") as f:
        f.write(requests.get(glb_url).content)
    return output_path
```

**RPM provides out of the box:** Face with photo likeness, hair (AI-matched), skin tone, clothing, full humanoid rig (Mixamo-compatible), morph targets for lip sync.

**Setup (once):** Create free account at https://readyplayer.me/developers → get APP_ID.

### Fallback: Avaturn API (Better Realism)

```python
import requests, time, os

AVATURN_API_KEY = os.environ.get("AVATURN_API_KEY")

def create_avaturn_avatar(photo_path: str, output_dir: str) -> str:
    headers = {"Authorization": f"Bearer {AVATURN_API_KEY}"}
    with open(photo_path, "rb") as f:
        resp = requests.post("https://api.avaturn.me/api/export/create",
                             headers=headers, files={"image": f},
                             data={"export_format": "glb"})
    export_id = resp.json()["export_id"]

    for _ in range(30):
        time.sleep(5)
        status = requests.get(f"https://api.avaturn.me/api/export/{export_id}",
                              headers=headers).json()
        if status.get("status") == "completed":
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "avaturn_avatar.glb")
            with open(output_path, "wb") as f:
                f.write(requests.get(status["url"]).content)
            return output_path
    raise RuntimeError("Avaturn export timed out")
```

## Method B: Text Description to Avatar (No Photo)

Use RPM's outfit + customization API with descriptive parameters when no reference photo is available.

## Method C: MB-Lab Base Bodies (Blender)

For full control over body shape and proportions. Requires Blender 5.0 with patched MB-Lab.

```python
import bpy

scene = bpy.context.scene
scene.mblab_template_name = 'human_male_base'  # or 'human_female_base'
scene.mblab_character_name = 'm_ca01'           # see reference/base_models.md
scene.mblab_use_lamps = False
scene.mblab_use_cycles = True

bpy.ops.mbast.init_character()

scene.mblab_body_mass = 0.50   # 0.0 = thin, 1.0 = heavy
scene.mblab_body_tone = 0.50   # 0.0 = soft, 1.0 = muscular
bpy.ops.mbast.character_generator()
bpy.ops.mbast.finalize_character()
```

**MB-Lab output:** ~18,000 vertices, 71-bone humanoid rig, PBR skin materials. Must decimate for web use (see sv-character-shading skill).

For Silicon Valley cast body presets and facial morph parameters, see `reference/base_models.md`.

## Blender Processing (Headless)

After generating or downloading an avatar, process in headless Blender:

```bash
blender --background --python process_character.py -- --input character.glb --output character_processed.blend
```

See `scripts/process_character.py` for the standard import + setup script.

## Fallback Decision Tree

| Problem | Solution |
|---------|----------|
| RPM API rate limit or auth failure | Fall back to Avaturn API |
| Avaturn fails | Use Meshy.ai API (text-to-3D + photo) |
| GLB has no morph targets | RPM: re-download with `?morphTargets=ARKit,Oculus Visemes` |
| Face doesn't match reference | Use cleaner front-facing photo >500px. Try Avaturn for better likeness |
| MB-Lab won't initialize | Check Blender version, apply patches from `reference/blender_patches.md` |

## Required API Keys

```
RPM_APP_ID=your_ready_player_me_app_id      # free at readyplayer.me/developers
AVATURN_API_KEY=your_avaturn_key             # optional, free tier available
```

## Reference Files

- `reference/base_models.md` — MB-Lab 8 presets, SV cast body params, skeleton info
- `reference/blender_patches.md` — MB-Lab Blender 5.0 compatibility fixes
- `reference/failed_approaches.md` — Anti-patterns: Hyper3D humans, MPFB2, OOM batching
