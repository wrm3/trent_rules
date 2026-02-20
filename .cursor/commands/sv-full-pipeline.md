Run the full character pipeline: $ARGUMENTS

## What This Command Does

End-to-end pipeline: photo → 3D avatar → toon shading → animation → voice → lip sync → R3F integration.

## Pipeline Stages

```
[1] Generate avatar from photo (RPM/Avaturn)
[2] Apply toon shader + optimize for web
[3] Apply 8 Mixamo animation clips
[4] Generate voice audio (ElevenLabs)
[5] Create lip sync data (Rhubarb)
[6] Apply viseme morph targets
[7] Export final GLB
[8] Register in R3F scene
```

## Skills Used
- sv-character-generation
- sv-character-shading
- sv-character-roster
- sv-animation-pipeline
- sv-voice-lipsync
- sv-r3f-integration

## What I Need From You
- Character name
- Reference photo path
- Dialogue lines (at least one for voice/lip sync)
- Voice preset preference (or use roster default)
