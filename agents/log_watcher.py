# log_watcher.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\log_watcher.py

import time
import os
import redis

LOG_DIR = "logs"
ERROR_PATTERNS = ["error", "exception", "failed", "traceback"]
STREAMLIT_LOG = os.path.join(LOG_DIR, "streamlit_error.txt")
SYSTEM_LOG = os.path.join(LOG_DIR, "system_stdout.txt")

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


def scan_file(path):
    if not os.path.exists(path):
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()[-50:]  # scan only last 50 lines
            for line in lines:
                for pattern in ERROR_PATTERNS:
                    if pattern in line.lower():
                        print(f"[LOG-WATCHER] Error detected in {path}: {line.strip()}")
                        return True
    except Exception as e:
        print(f"[LOG-WATCHER] Could not read {path}: {e}")
    return False


while True:
    try:
        if scan_file(SYSTEM_LOG) or scan_file(STREAMLIT_LOG):
            r.set("error_flag", "1")
        time.sleep(5)
    except Exception as e:
        print(f"[LOG-WATCHER] Exception: {e}")
        time.sleep(10)
