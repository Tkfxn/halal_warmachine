# patch_smith.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\patch_smith.py

import os
import sys
sys.path.append("agents")

from redis_client import get_flag, set_flag
import time
import json

PATCH_DIR = "patches"
LOG_FILE = "logs/patch_smith_log.txt"
FLAG = "patchsmith_trigger"

os.makedirs("logs", exist_ok=True)

def log(message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
    print(f"[PATCH-SMITH] {message}")

def apply_patch():
    try:
        patch_files = [f for f in os.listdir(PATCH_DIR) if f.endswith(".py")]
        for pf in patch_files:
            src = os.path.join(PATCH_DIR, pf)
            dst = os.path.join(".", pf)
            with open(src, "r", encoding="utf-8") as sf:
                code = sf.read()
            with open(dst, "w", encoding="utf-8") as df:
                df.write(code)
            log(f"Patched {pf} -> {dst}")
    except Exception as e:
        log(f"Patch failed: {e}")

if __name__ == '__main__':
    log("Patch-Smith running...")
    while True:
        if get_flag(FLAG) == '1':
            log("Patch triggered!")
            apply_patch()
            set_flag(FLAG, '0')
        time.sleep(5)
