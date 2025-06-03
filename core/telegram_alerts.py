# telegram_alerts.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\core\telegram_alerts.py

import os
import json
import requests
from datetime import datetime
import sys
sys.path.append("agents")
from strategy_evolver import get_pattern_scores

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

LOG_DIR = "logs"

def load_json(filename):
    path = os.path.join(LOG_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def send_telegram_message(text):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("[TELEGRAM] Missing token or chat ID")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"[TELEGRAM] Failed: {response.text}")
    except Exception as e:
        print(f"[TELEGRAM] Error: {e}")

def send_daily_summary():
    stats = load_json("trade_stats.json")
    patterns = get_pattern_scores()

    text = f"*📊 Daily Report — {datetime.now().strftime('%Y-%m-%d')}*\n"
    text += f"*Trades:* {stats.get('total', 0)}\n"
    text += f"*Win Rate:* {stats.get('winrate', 0)}%\n"
    text += f"*P&L:* ${stats.get('pnl', 0):.2f}\n"
    text += f"*Drawdown:* {stats.get('drawdown', 0)}%\n\n"

    if patterns:
        text += "*Pattern Scores:*\n"
        for tag, score in patterns.items():
            wins = score.get("wins", 0)
            losses = score.get("losses", 0)
            wr = wins / (wins + losses + 1e-9)
            text += f"• `{tag}` — {wins}W / {losses}L ({wr:.0%})\n"
    else:
        text += "No pattern scores recorded.\n"

    send_telegram_message(text)

if __name__ == "__main__":
    send_daily_summary()
