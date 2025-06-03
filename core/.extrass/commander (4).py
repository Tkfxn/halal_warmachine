
import sys, os
import time
import threading
import traceback
from telegram_alerts import send_telegram_message

class DualLogger:
    def __init__(self, filepath):
        self.terminal = sys.__stdout__
        self.log = open(filepath, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = sys.stderr = DualLogger("logs/commander_startup_log.txt")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("[Commander] Starting...", flush=True)

try:
    print("[Commander] Importing exec_agent...", flush=True)
    import exec_agent
except Exception as e:
    print(f"[Commander] Failed to import exec_agent: {e}", flush=True)

try:
    print("[Commander] Importing macro_coach...", flush=True)
    import macro_coach
except Exception as e:
    print(f"[Commander] Failed to import macro_coach: {e}", flush=True)

try:
    print("[Commander] Importing strategy_evolver...", flush=True)
    import strategy_evolver
except Exception as e:
    print(f"[Commander] Failed to import strategy_evolver: {e}", flush=True)

try:
    print("[Commander] Importing log_uploader...", flush=True)
    import log_uploader
except Exception as e:
    print(f"[Commander] Failed to import log_uploader: {e}", flush=True)

try:
    print("[Commander] Importing microstructure_agent...", flush=True)
    import microstructure_agent
except Exception as e:
    print(f"[Commander] Failed to import microstructure_agent: {e}", flush=True)

try:
    print("[Commander] Importing book_watcher...", flush=True)
    import book_watcher
except Exception as e:
    print(f"[Commander] Failed to import book_watcher: {e}", flush=True)

try:
    print("[Commander] Importing batch_auto_patcher...", flush=True)
    from batch_auto_patcher import run_auto_patcher
except Exception as e:
    print(f"[Commander] Failed to import batch_auto_patcher: {e}", flush=True)

def safe_run(target, name):
    def wrapper():
        try:
            target()
        except Exception as e:
            err_msg = f"[Commander] {name} crashed: {str(e)}\n" + traceback.format_exc()
            print(err_msg, flush=True)
            with open("logs/system_stdout.txt", "a", encoding="utf-8") as f:
                f.write(err_msg + "\n")
    return wrapper

def main():
    print("[Commander] Launching agents...", flush=True)

    threads = [
        threading.Thread(target=safe_run(run_auto_patcher, "AutoPatcher"), daemon=True),
        threading.Thread(target=safe_run(exec_agent.run, "Execution Agent"), daemon=True),
        threading.Thread(target=safe_run(macro_coach.run, "Macro Coach"), daemon=True),
        threading.Thread(target=safe_run(strategy_evolver.run, "Strategy Evolver"), daemon=True),
        threading.Thread(target=safe_run(log_uploader.run, "Log Uploader"), daemon=True),
        threading.Thread(target=safe_run(microstructure_agent.run, "Microstructure Agent"), daemon=True),
        threading.Thread(target=safe_run(book_watcher.run, "Bookwatcher"), daemon=True)
    ]

    for t in threads:
        t.start()

    send_telegram_message("✅ Loop is live and agents launched successfully.")

    while True:
        time.sleep(999)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[FATAL] Commander startup failed: {e}", flush=True)
