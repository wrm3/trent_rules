---
name: sv-voice-lipsync
description: Generate character voices via ElevenLabs TTS and apply Rhubarb lip sync data to 3D character morph targets. Covers voice synthesis, voice cloning, phoneme-to-viseme mapping, ARKit/Oculus morph target keyframing, and audio+video combining. This skill should be used when generating character dialogue audio, creating lip sync data, mapping visemes to blend shapes, or combining rendered video with voice audio.
triggers:
  - "voice"
  - "lip sync"
  - "ElevenLabs"
  - "Rhubarb"
  - "viseme"
  - "morph targets"
  - "character voice"
  - "TTS"
  - "text to speech"
  - "shape keys"
  - "dialogue audio"
agents:
  - voice-artist
  - animation-engineer
version: 1.0.0
---

# Silicon Valley Voice & Lip Sync

Generate character dialogue audio via ElevenLabs and apply precise lip sync to 3D character morph targets using Rhubarb.

## Pipeline Overview

```
Text Dialogue
     |
[Step 1] ElevenLabs TTS → .mp3/.wav audio
     |
[Step 2] Rhubarb Lip Sync → mouth_cues.json (phoneme timing)
     |
[Step 3] Map cues to RPM viseme morph targets → keyframed shape keys in Blender
     |
[Step 4] (Optional) Render + combine audio+video via ffmpeg
```

## Prerequisites

```bash
pip install requests elevenlabs
# Rhubarb: https://github.com/DanielSWolf/rhubarb-lip-sync/releases
```

**API Keys (.env):**
```
ELEVENLABS_API_KEY=your_key    # free tier: 10k chars/month
```

## Step 1: Voice Generation (ElevenLabs)

### Using the Python Client

```python
from elevenlabs.client import ElevenLabs
from elevenlabs import save

def generate_voice(text: str, voice_name: str, output_path: str, api_key: str) -> str:
    """Generate voice audio from text. Returns path to audio file."""
    client = ElevenLabs(api_key=api_key)
    audio = client.generate(text=text, voice=voice_name, model="eleven_multilingual_v2")
    save(audio, output_path)
    return output_path
```

### Using the REST API Directly

```python
import requests, os

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

VOICE_PRESETS = {
    "confident_male": "TxGEqnHWrfWFTfGW9XjX",
    "energetic_female": "EXAVITQu4vr4xnSDxMaL",
    "calm_narrator": "21m00Tcm4TlvDq8ikWAM",
    "young_male": "AZnzlk1XvdvUeBnXmlld",
    "young_female": "MF3mGyEYCl7XYWbV9V6O",
}

def generate_voice_rest(text: str, voice_id: str, output_path: str) -> str:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}
    }
    resp = requests.post(url, json=payload, headers=headers)
    with open(output_path, "wb") as f:
        f.write(resp.content)
    return output_path
```

### Voice Cloning (Custom Character Voices)

For better character match, clone a voice from 1-5 min audio sample:

```python
client = ElevenLabs(api_key=api_key)
voice = client.clone(name="Richard_Hendricks", files=["richard_sample.mp3"])
```

## Step 2: Rhubarb Lip Sync

Rhubarb analyzes audio and produces frame-accurate mouth shape timing.

```bash
./rhubarb -f json -o mouth_cues.json --recognizer phonetic voice.wav
```

**Important:** Rhubarb requires WAV format. Convert MP3 first:

```bash
ffmpeg -i voice.mp3 voice.wav
```

### Python Wrapper

```python
import subprocess, json

def generate_lipsync(audio_path: str, output_json: str, rhubarb_path: str = "rhubarb") -> list:
    """Generate lip sync data from audio. Returns list of mouth cues."""
    result = subprocess.run([
        rhubarb_path, "-f", "json", "-o", output_json,
        "--recognizer", "phonetic", audio_path
    ], capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Rhubarb failed: {result.stderr}")

    with open(output_json) as f:
        return json.load(f)['mouthCues']
```

### Rhubarb Output Format

```json
{
  "mouthCues": [
    {"start": 0.00, "end": 0.05, "value": "X"},
    {"start": 0.05, "end": 0.27, "value": "D"},
    {"start": 0.27, "end": 0.31, "value": "C"},
    {"start": 0.31, "end": 0.43, "value": "B"}
  ]
}
```

## Step 3: Map Visemes to Morph Targets

RPM avatars include ARKit and Oculus Viseme blend shapes. Map Rhubarb phoneme codes to these:

### Rhubarb → RPM Viseme Mapping

```python
RHUBARB_TO_RPM = {
    'A': 'viseme_aa',   # Open mouth (ah)
    'B': 'viseme_PP',   # Lips together (b, m, p)
    'C': 'viseme_I',    # Ee sound
    'D': 'viseme_E',    # Eh sound
    'E': 'viseme_O',    # Oh sound
    'F': 'viseme_FF',   # F/V sound (teeth on lip)
    'G': 'viseme_U',    # Oo sound
    'H': 'viseme_CH',   # Sh/Ch sound
    'X': 'viseme_sil',  # Silence (closed mouth)
}
```

For the complete mapping table with ARKit equivalents, see `reference/viseme_mapping.md`.

### Apply to Blender Shape Keys

```python
import bpy

def apply_lipsync_to_character(mouth_cues: list, mesh_obj, fps: int = 24):
    """Keyframe morph targets on a mesh based on Rhubarb mouth cues."""
    shape_keys = mesh_obj.data.shape_keys
    if not shape_keys:
        return
    key_blocks = shape_keys.key_blocks

    for cue in mouth_cues:
        frame_start = int(cue['start'] * fps)
        frame_end = int(cue['end'] * fps)
        viseme = RHUBARB_TO_RPM.get(cue['value'], 'viseme_sil')

        # Zero all visemes at frame start
        for key_name in RHUBARB_TO_RPM.values():
            key = key_blocks.get(key_name)
            if key:
                key.value = 0.0
                key.keyframe_insert('value', frame=frame_start)

        # Activate target viseme
        key = key_blocks.get(viseme)
        if key:
            key.value = 1.0
            key.keyframe_insert('value', frame=frame_start)
            key.value = 0.0
            key.keyframe_insert('value', frame=frame_end)
```

## Step 4: Render + Combine (Optional)

For offline video output, render the animated character then combine with audio:

```python
import bpy

def render_character_video(output_path: str, frame_end: int = 120):
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = frame_end
    scene.render.fps = 24
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.image_settings.file_format = 'FFMPEG'
    scene.render.ffmpeg.format = 'MPEG4'
    scene.render.ffmpeg.codec = 'H264'
    scene.render.filepath = output_path
    bpy.ops.render.render(animation=True)
```

### Combine Audio + Video

```bash
ffmpeg -i character_render.mp4 -i voice.mp3 -c:v copy -c:a aac -shortest character_final.mp4
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No shape keys on GLB | RPM: re-download with `?morphTargets=ARKit,Oculus Visemes` |
| Voice doesn't match character | Use voice cloning with 1-5 min sample |
| Lip sync timing is off | Check fps match between Rhubarb and Blender scene |
| Rhubarb can't read audio | Convert to WAV first via ffmpeg |
| ElevenLabs rate limited | Free tier: 10k chars/month. Upgrade or batch wisely |

## Reference Files

- `reference/viseme_mapping.md` — Complete Rhubarb→ARKit→Oculus→RPM morph target mapping table
