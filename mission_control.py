# === mission_control.py ===
# Central orchestrator that launches all components and monitors their state

import subprocess
import threading
import time
import os
import sys

MODULES = [
    ("Commander", "core/commander.py"),
    ("Exec Agent", "core/exec_agent.py"),
    ("Dashboard", "dashboard.py"),
    ("Strategy Evolver", "core/strategy_evolver.py"),
    ("Pulse Sniper", "agents/pulse_sniper.py"),
    ("Wallet Watcher", "agents/wallet_watcher.py"),
    ("Book Watcher", "agents/book_watcher.py"),
    ("Macro Coach", "core/macro_coach.py"),
    ("Log Uploader", "core/log_uploader.py"),
]

LOG_FILE = "logs/system_launch_log.txt"
CMD_LOG_FILE = "logs/system_stdout.txt"


def launch_module(name, path):
    def _launch():
        try:
            with open(CMD_LOG_FILE, "a") as out:
                subprocess.Popen([sys.executable, path], stdout=out, stderr=out)
            print(f"🚀 Launching {name}...")
        except Exception as e:
            print(f"❌ Failed to launch {name}: {e}")

    thread = threading.Thread(target=_launch)
    thread.start()
    return thread


def log_start():
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Warmachine Boot at {time.ctime()} ---\n")
    with open(CMD_LOG_FILE, "a") as f:
        f.write(f"\n--- CMD Output Boot at {time.ctime()} ---\n")


def main():
    log_start()
    for name, path in MODULES:
        launch_module(name, path)
        time.sleep(2)  # delay between module launches
    print("✅ All modules launched. War machine is operational.")


if __name__ == "__main__":
    main()
