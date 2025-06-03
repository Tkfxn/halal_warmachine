import psutil
import time
from datetime import datetime

KNOWN_CMDS = set()


def get_cmd_windows():
    windows = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if 'cmd.exe' in proc.info['name'].lower() or 'python.exe' in proc.info['name'].lower():
                windows.append((proc.info['pid'], ' '.join(proc.info['cmdline'])))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return windows


def sentinel():
    print("[SENTINEL] Scanning for new terminal windows...")
    global KNOWN_CMDS
    while True:
        current = set(get_cmd_windows())
        new_cmds = current - KNOWN_CMDS
        if new_cmds:
            for pid, cmd in new_cmds:
                print(f"[SENTINEL] 🆕 New CMD window detected (PID {pid}): {cmd} at {datetime.now()}")
                # Optional: register log path or alert Loop-Warden
        KNOWN_CMDS = current
        time.sleep(15)


if __name__ == "__main__":
    sentinel()
