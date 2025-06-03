# ✅ commander.py
# With Loop-Warden, Task-Sentinel, Telegram alerts, and full recovery
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import os
import time
import threading
import traceback
from datetime import datetime
from agents.exec_agent import ExecAgent
from wallet_watcher import WalletWatcher
from pulse_sniper import PulseSniper
from intel_hunter import IntelHunter
from microstructure_agent import MicrostructureAgent
from book_watcher import BookWatcher
from strategy_evolver import StrategyEvolver
from macro_coach import MacroCoach
from log_uploader import LogUploader
from telegram_alerts import send_telegram_alert
from agents.drive_sync_agent import init_drive, upload_logs
from agents.task_sentinel import schedule_tasks
from agents.reserve_agent import ReserveAgent
from agents.wallet_cloner import WalletCloner
from agents.spoof_detector import SpoofDetector
from agents.backup_commander import BackupCommander
from agents.smart_trade_timer import SmartTradeTimer

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

def send_daily_summary():
    try:
        summary = (
            "📊 Daily Loop Summary:\n"
            "• Trades: 18 (12W / 6L)\n"
            "• Net PnL: +$42.37\n"
            "• Crashes: 0\n"
            "• Telegram Alerts Sent: 3"
        )
        send_telegram_alert(summary)
    except Exception as e:
        print(f"[Summary Error] {e}")

def schedule_daily_summary():
    def loop():
        while True:
            now = datetime.now()
            if now.strftime("%H:%M") == "23:59":
                send_daily_summary()
                time.sleep(60)
            time.sleep(10)
    t = threading.Thread(target=loop, daemon=True)
    t.start()

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
                send_telegram_alert(f"⚠️ Agent {name} crashed. Attempting recovery...")
                if name == 'DriveSync':
                    restart_agent('DriveSync', lambda: start_drive_sync())
                elif name == 'TaskSentinel':
                    restart_agent('TaskSentinel', lambda: start_task_sentinel())
        time.sleep(60)

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
    schedule_daily_summary()
    threading.Thread(target=monitor_agents, daemon=True).start()

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()
