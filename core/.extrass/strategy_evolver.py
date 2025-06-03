
import os
import json
import datetime
from telegram_alerts import send_telegram_message

TRADE_LOG_PATH = "logs/trade_reviews.json"
EVOLUTION_LOG_PATH = "logs/evolution_log.json"

def run():
    print("[EVOLVER] Starting evolution scan...")

    if not os.path.exists(TRADE_LOG_PATH):
        print("[EVOLVER] No trades found.")
        return

    with open(TRADE_LOG_PATH, "r") as f:
        trades = json.load(f)

    if not trades:
        print("[EVOLVER] No trade data to evolve.")
        return

    metrics = {
        "total_trades": len(trades),
        "last_trade": trades[-1],
        "symbols_traded": list(set(t["symbol"] for t in trades if "symbol" in t)),
        "side_counts": {
            "BUY": sum(1 for t in trades if t.get("side") == "BUY"),
            "SELL": sum(1 for t in trades if t.get("side") == "SELL")
        }
    }

    evolution = {
        "timestamp": datetime.datetime.now().isoformat(),
        "metrics": metrics
    }

    if os.path.exists(EVOLUTION_LOG_PATH):
        with open(EVOLUTION_LOG_PATH, "r") as f:
            existing = json.load(f)
    else:
        existing = []

    existing.append(evolution)
    with open(EVOLUTION_LOG_PATH, "w") as f:
        json.dump(existing, f, indent=2)

    send_telegram_message(f"📊 Strategy evolved at {evolution['timestamp']}")
    print("[EVOLVER] Evolution complete.")
