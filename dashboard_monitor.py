# dashboard_monitor.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\dashboard_monitor.py

import os
import time
import subprocess

WATCH_FILE = "dashboard.py"
CHECK_INTERVAL = 5  # seconds

last_modified = None
streamlit_proc = None


def file_changed():
    global last_modified
    if not os.path.exists(WATCH_FILE):
        return False
    current = os.path.getmtime(WATCH_FILE)
    if last_modified is None:
        last_modified = current
        return False
    if current != last_modified:
        last_modified = current
        return True
    return False


def start_dashboard():
    print("[DASHBOARD-MONITOR] Starting Streamlit dashboard...")
    with open("logs/streamlit_error.txt", "w") as errlog:
        return subprocess.Popen(
            ["streamlit", "run", WATCH_FILE],
            stdout=subprocess.DEVNULL,
            stderr=errlog,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )


def kill_dashboard():
    global streamlit_proc
    if streamlit_proc:
        print("[DASHBOARD-MONITOR] Restarting Streamlit...")
        streamlit_proc.kill()
        streamlit_proc = None


if __name__ == '__main__':
    print("[DASHBOARD-MONITOR] Watching for changes to dashboard.py")
    streamlit_proc = start_dashboard()

    while True:
        if file_changed():
            kill_dashboard()
            time.sleep(1)
            streamlit_proc = start_dashboard()
        time.sleep(CHECK_INTERVAL)
