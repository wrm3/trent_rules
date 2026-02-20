Animate a 3D character: $ARGUMENTS

## What This Command Does

Applies Mixamo animation clips to a character GLB and optionally adds voice + lip sync.

## Workflow

### 1. Apply Animation Clips
- Export character FBX for Mixamo (if not already done)
- Download required clips: walk, sit, type, idle, talk, think, stand up, sit down
- Import FBX clips into Blender, retarget if needed
- Bake and embed animations into character GLB

### 2. Voice & Lip Sync (Optional)
- Generate dialogue via ElevenLabs
- Run Rhubarb lip sync analysis
- Map visemes to morph targets
- Keyframe or prepare for real-time playback

### 3. R3F Integration
- Verify character loads with animations in Character3D
- Test animation crossfade (0.3s blend)
- Configure behavior store with character personality

## Skills Used
- sv-animation-pipeline
- sv-voice-lipsync (if voice requested)
- sv-r3f-integration

## What I Need From You
- Character name
- Path to character GLB (if not already in standard location)
- Whether voice + lip sync is needed
- Dialogue text (if voice is needed)
