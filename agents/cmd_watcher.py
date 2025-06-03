import time
import os
import threading
from datetime import datetime

ERROR_KEYWORDS = ["[ERROR]", "[EXCEPTION]", "[CRASH]", "Traceback", "Invalid", "ConnectionError", "Binance", "Restarting"]

LOG_FILES = [
    "logs/commander_console_log.txt",
    "logs/system_stdout.txt"
]

CHECK_INTERVAL = 5  # seconds
IDLE_TIMEOUT = 60  # seconds with no new line before triggering fallback

last_modified_times = {}
last_line_cache = {}

def tail(filepath):
    try:
        with open(filepath, 'r') as f:
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                yield line.strip()
    except Exception as e:
        print(f"[CMD-WATCHER] Failed to tail {filepath}: {e}")

def watch_log(filepath):
    print(f"[CMD-WATCHER] Watching {filepath}...")
    last_activity = time.time()
    for line in tail(filepath):
        last_activity = time.time()
        if any(keyword in line for keyword in ERROR_KEYWORDS):
            print(f"[CMD-WATCHER] 🚨 Error detected: {line}")
            trigger_patchsmith(filepath, line)
        last_line_cache[filepath] = line

        # Could optionally send to Telegram or strategy_evolver here

        # Idle fallback trigger
        if time.time() - last_activity > IDLE_TIMEOUT:
            print(f"[CMD-WATCHER] ⏳ No output detected from {filepath} for {IDLE_TIMEOUT} seconds — triggering backup recovery.")
            trigger_backup_commander(filepath)
            last_activity = time.time()

def trigger_patchsmith(filepath, line):
    print(f"[CMD-WATCHER] → Patch-Smith notified from {filepath}: {line}")
    # PatchSmith.handle_issue(filepath, line)  # Placeholder for agent call

def trigger_backup_commander(filepath):
    print(f"[CMD-WATCHER] → BackupCommander triggered for {filepath}")
    # BackupCommander.restart_loop(filepath)  # Placeholder for agent call

def start_watcher():
    for file in LOG_FILES:
        thread = threading.Thread(target=watch_log, args=(file,), daemon=True)
        thread.start()

if __name__ == "__main__":
    start_watcher()
    print("[CMD-WATCHER] Online and scanning logs...")
    while True:
        time.sleep(10)
