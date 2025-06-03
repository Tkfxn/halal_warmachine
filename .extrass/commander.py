# === commander.py ===
# Central brain that launches all core and agent modules

import subprocess
import threading
import time
import os
import webbrowser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.join(ROOT_DIR, "agents")
CORE_DIR = os.path.join(ROOT_DIR, "core")

MODULES_TO_LAUNCH = [
    os.path.join(CORE_DIR, "execution_agent.py"),
    os.path.join(CORE_DIR, "log_uploader.py"),
    os.path.join(CORE_DIR, "intel_hunter.py"),
    os.path.join(CORE_DIR, "microstructure_agent.py"),
    os.path.join(CORE_DIR, "mission_control.py"),
    os.path.join(AGENTS_DIR, "macro_coach.py"),
    os.path.join(AGENTS_DIR, "pulse_sniper.py"),
    os.path.join(AGENTS_DIR, "wallet_watcher.py")
]

def run_module(path):
    subprocess.Popen(["python", path], creationflags=subprocess.CREATE_NEW_CONSOLE)

def main():
    print("💻 Launching GPT crypto war machine loop...")
    time.sleep(1)
    for module in MODULES_TO_LAUNCH:
        print(f"🚀 Launching: {module}")
        threading.Thread(target=run_module, args=(module,)).start()
        time.sleep(1)
    
    print("🌐 Opening dashboard...")
    time.sleep(2)
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    main()
