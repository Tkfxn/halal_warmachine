# ✅ utils/logging.py (Final)
import os
from datetime import datetime

LOG_PATH = "logs/wallet_watch_log.txt"

def log_wallet_activity(wallet, action, details=""):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_PATH, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {wallet} | {action} | {details}\n"
        f.write(line)
