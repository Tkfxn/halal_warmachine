# main.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\main.py

import subprocess
import time
import threading
from datetime import datetime
import schedule
import os
import sys

# Redirect stderr for main process
os.makedirs("logs", exist_ok=True)
sys.stderr = open("logs/system_crash.txt", "a")

AGENTS = [
    "agents/commander.py",
    "agents/loop_commander.py",
    "agents/log_watcher.py",
    "agents/exec_agent.py",
    "agents/wallet_watcher.py",
    "agents/strategy_evolver.py",
    "agents/spoof_detector.py",
    "agents/pulse_sniper.py",
    "agents/backup_commander.py",
    "agents/intel_harvester.py",
    "dashboard.py"
]

def launch_process(path):
    try:
        log_file = path.replace("/", "_").replace("\\", "_").replace(".py", "").replace("agents_", "")
        stderr_path = os.path.join("logs", f"subprocess_{log_file}.txt")
        subprocess.Popen(["python", path], stderr=open(stderr_path, "a"))
        print(f"[MAIN] ✅ Launched {path}")
    except Exception as e:
        print(f"[MAIN] ❌ Failed to launch {path}: {e}")


def schedule_tasks():
    from core.telegram_alerts import send_daily_summary
    schedule.every().day.at("00:01").do(send_daily_summary)

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(30)

    threading.Thread(target=loop, daemon=True).start()


if __name__ == '__main__':
    print("[MAIN] Starting Halal Warmachine Loop...")
    for agent in AGENTS:
        launch_process(agent)

    schedule_tasks()
    print("[MAIN] All agents launched. Daily scheduler active.")

    while True:
        time.sleep(60)
