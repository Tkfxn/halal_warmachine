
# commander.py
import threading
import time
from core import exec_agent, macro_coach, strategy_evolver, log_uploader
from core import microstructure_agent, bookwatcher
from batch_auto_patcher import run_auto_patcher

# Background loop agents
def start_exec():
    exec_agent.run()

def start_macro():
    macro_coach.run()

def start_strategy():
    strategy_evolver.run()

def start_log_uploader():
    log_uploader.run()

def start_microstructure():
    microstructure_agent.run()

def start_bookwatcher():
    bookwatcher.run()

def main():
    print("[Commander] Launching Halal Warmachine...")

    threading.Thread(target=run_auto_patcher, daemon=True).start()
    threading.Thread(target=start_exec, daemon=True).start()
    threading.Thread(target=start_macro, daemon=True).start()
    threading.Thread(target=start_strategy, daemon=True).start()
    threading.Thread(target=start_log_uploader, daemon=True).start()
    threading.Thread(target=start_microstructure, daemon=True).start()
    threading.Thread(target=start_bookwatcher, daemon=True).start()

    while True:
        time.sleep(999)

if __name__ == "__main__":
    main()
