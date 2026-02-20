# Blender 5.0 Compatibility Patches

## MB-Lab 1.8.1 Patch

MB-Lab was built for Blender 2.80-4.x. Blender 5.0 removed/renamed some APIs.

### Fix: `use_contact_shadow` removed from AreaLight

**File**: `<blender_addons>/MB-Lab/object_ops.py`
**Error**: `AttributeError: 'AreaLight' object has no attribute 'use_contact_shadow'`

```python
# Line ~437 in object_ops.py
# BEFORE (broken):
mblight01.use_contact_shadow = True

# AFTER (fixed):
pass  # use_contact_shadow removed in Blender 5.0
```

There are 3 occurrences in the file. Replace all.

### Automated Patch Script

```python
import os

file_path = r"<blender_addons>/MB-Lab/object_ops.py"
with open(file_path, 'r') as f:
    content = f.read()

patched = content.replace(
    'use_contact_shadow = True',
    'pass  # use_contact_shadow removed in Blender 5.0'
).replace(
    'use_contact_shadow = False',
    'pass  # use_contact_shadow removed in Blender 5.0'
)

with open(file_path, 'w') as f:
    f.write(patched)
```

### MB-Lab Installation Path

```
C:\Users\<user>\AppData\Roaming\Blender Foundation\Blender\5.0\scripts\addons\MB-Lab\
```

## MPFB2 v2.0.8 — NOT Compatible with Blender 5.0

MPFB2 (MakeHuman Plugin for Blender 2) uses the old add-on format. Blender 5.0's new extension system rejects it with:

```
Error: The "package" does not name an extension
```

**Workaround**: None currently. Wait for MPFB2 update or use Blender 4.x for MPFB2.

## MB-Lab Add-on Installation (Blender 5.0)

The standard `addon_install()` method won't work with the GitHub source zip because the directory name contains hyphens. Manual installation required:

```python
import zipfile, shutil, os

# 1. Download from GitHub
zip_url = "https://github.com/animate1978/MB-Lab/archive/refs/tags/1_8_1.zip"

# 2. Extract to temp directory
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(temp_dir)

# 3. Copy to addons as "MB-Lab"
addon_dir = bpy.utils.user_resource('SCRIPTS', path='addons')
shutil.copytree(
    os.path.join(temp_dir, "MB-Lab-1_8_1"),
    os.path.join(addon_dir, "MB-Lab")
)

# 4. Enable add-on
bpy.ops.preferences.addon_enable(module="MB-Lab")

# 5. Apply Blender 5.0 patches (see above)

# 6. Reload
bpy.ops.preferences.addon_disable(module="MB-Lab")
bpy.ops.preferences.addon_enable(module="MB-Lab")
```

## Tips for Blender 5.0 Add-on Compatibility

- Blender 5.0 uses a new "extension" system alongside legacy "add-ons"
- Legacy add-ons with `bl_info` dict still work IF they don't use deprecated APIs
- `blender_manifest.toml` files conflict with the legacy system — remove them
- Always set `mblab_use_lamps = False` to avoid lighting API issues
- Test one character creation before batching
