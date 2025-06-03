
import os
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PATCH_DIR = os.path.join(ROOT_DIR, "patches", "auto")

def apply_patch(patch):
    if 'target_file' not in patch:
        print("[PATCHER] Skipped: missing 'target_file'")
        return False
    try:
        file_path = os.path.join(ROOT_DIR, patch['target_file'])
        with open(file_path, 'a', encoding='utf-8') as f:
            for line in patch['patch_lines']:
                f.write("\n" + line)
        print(f"[PATCHER] Patch applied to {patch['target_file']}")
        return True
    except Exception as e:
        print(f"[PATCHER] Error applying patch: {e}")
        return False

def run_auto_patcher():
    if not os.path.exists(PATCH_DIR):
        print("[PATCHER] ⚠️ No patches/auto directory found. Skipping.")
        return

    for fname in os.listdir(PATCH_DIR):
        if fname.endswith(".json"):
            try:
                with open(os.path.join(PATCH_DIR, fname), 'r', encoding='utf-8') as f:
                    patch = json.load(f)
                apply_patch(patch)
            except Exception as e:
                print(f"[PATCHER] Error reading {fname}: {e}")
