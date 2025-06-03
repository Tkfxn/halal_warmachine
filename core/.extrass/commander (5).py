# ✅ commander.py
# With Loop-Warden, Task-Sentinel, Telegram alerts, and full recovery
import os
import time
import threading
import traceback
from agents.exec_agent import ExecAgent
from agents.wallet_watcher import WalletWatcher
from agents.pulse_sniper import PulseSniper
from agents.intel_hunter import IntelHunter
from agents.microstructure_agent import MicrostructureAgent
from agents.book_watcher import BookWatcher
from agents.strategy_evolver import StrategyEvolver
from agents.macro_coach import MacroCoach
from agents.log_uploader import LogUploader
from agents.drive_sync_agent import init_drive, upload_logs
from agents.task_sentinel import schedule_tasks
from agents.reserve_agent import ReserveAgent
from agents.wallet_cloner import WalletCloner
from agents.spoof_detector import SpoofDetector
from agents.backup_commander import BackupCommander
from agents.smart_trade_timer import SmartTradeTimer
from utils.telegram_alerts import send_telegram_alert

# Global tracker for agents
agent_threads = {}

# Background agents

def start_drive_sync():
    try:
        def drive_loop():
            drive = init_drive()
            while True:
                upload_logs(drive)
                time.sleep(600)
        t = threading.Thread(target=drive_loop, daemon=True)
        t.start()
        agent_threads['DriveSync'] = t
        print("[Commander] Drive Sync Agent started.")
    except Exception as e:
        print(f"[Commander] Failed to start Drive Sync Agent: {e}")

def start_task_sentinel():
    try:
        t = threading.Thread(target=schedule_tasks, daemon=True)
        t.start()
        agent_threads['TaskSentinel'] = t
        print("[Commander] Task Sentinel started.")
    except Exception as e:
        print(f"[Commander] Failed to start Task Sentinel: {e}")

def restart_agent(agent_name, target):
    try:
        t = threading.Thread(target=target, daemon=True)
        t.start()
        agent_threads[agent_name] = t
        send_telegram_alert(f"🔁 Restarted {agent_name} after crash.")
    except Exception as e:
        print(f"[Commander] Could not restart {agent_name}: {e}")

def monitor_agents():
    while True:
        for name, thread in list(agent_threads.items()):
            if not thread.is_alive():
                print(f"[Loop-Warden] Agent {name} crashed. Restarting...")
                if name == 'DriveSync':
                    restart_agent('DriveSync', lambda: start_drive_sync())
                elif name == 'TaskSentinel':
                    restart_agent('TaskSentinel', lambda: start_task_sentinel())
        time.sleep(60)

# Commander startup sequence
def main():
    print("[Commander] Launching Halal Warmachine...")
    send_telegram_alert("🤖 Halal Warmachine Commander Online")

    agents = [
        ExecAgent(),
        WalletWatcher(),
        PulseSniper(),
        IntelHunter(),
        MicrostructureAgent(),
        BookWatcher(),
        StrategyEvolver(),
        MacroCoach(),
        LogUploader(),
        ReserveAgent(),
        WalletCloner(),
        SpoofDetector(),
        BackupCommander(),
        SmartTradeTimer(),
    ]

    for agent in agents:
        try:
            t = threading.Thread(target=agent.run, daemon=True)
            t.start()
            agent_threads[agent.__class__.__name__] = t
            print(f"[Commander] Launched: {agent.__class__.__name__}")
        except Exception as e:
            err = traceback.format_exc()
            print(f"[Commander] Failed to start {agent.__class__.__name__}: {e}\n{err}")
            send_telegram_alert(f"❌ {agent.__class__.__name__} failed to start.")

    start_drive_sync()
    start_task_sentinel()
    threading.Thread(target=monitor_agents, daemon=True).start()

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
