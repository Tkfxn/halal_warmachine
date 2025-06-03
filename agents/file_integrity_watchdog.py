import os
import hashlib
import time
from datetime import datetime

WATCHED_FILES = [
    "commander.py",
    "dashboard.py",
    "launcher.bat",
    "config/settings.yml",
    "config/client_secrets.json"
] + [f"agents/{f}" for f in os.listdir("agents") if f.endswith(".py")]

HASH_RECORD = "logs/file_hashes.txt"


def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_previous_hashes():
    hashes = {}
    if not os.path.exists(HASH_RECORD):
        return hashes
    with open(HASH_RECORD, 'r') as f:
        for line in f:
            if '|' in line:
                path, hashval = line.strip().split('|')
                hashes[path] = hashval
    return hashes


def save_hashes(hashes):
    with open(HASH_RECORD, 'w') as f:
        for path, hashval in hashes.items():
            f.write(f"{path}|{hashval}\n")


def watchdog():
    print("[INTEGRITY] Watching for file changes...")
    last_hashes = load_previous_hashes()
    while True:
        current_hashes = {f: file_hash(f) for f in WATCHED_FILES if os.path.exists(f)}
        for f, h in current_hashes.items():
            if f in last_hashes and last_hashes[f] != h:
                print(f"[INTEGRITY] ⚠️ File modified: {f} at {datetime.now()}")
                # Optional: Trigger Telegram alert or restore from backup
        save_hashes(current_hashes)
        last_hashes = current_hashes.copy()
        time.sleep(60)


if __name__ == "__main__":
    watchdog()
