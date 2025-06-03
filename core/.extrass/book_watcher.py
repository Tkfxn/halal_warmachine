# === bookwatcher.py ===
# Live Binance order book monitor with spoofing + imbalance detection

import websocket
import json
import threading
from datetime import datetime

SYMBOL = "btcusdt"
DEPTH_STREAM = f"wss://stream.binance.com:9443/ws/{SYMBOL}@depth"

book_state = {
    "bid_volume": 0.0,
    "ask_volume": 0.0,
    "imbalance": 0.0,
    "spoof_detected": False,
    "last_update": None
}

log_file = "logs/bookwatch_log.json"

# --- Logic ---
def analyse_orderbook(data):
    try:
        bids = data["b"][:5]
        asks = data["a"][:5]

        bid_vol = sum(float(b[1]) for b in bids)
        ask_vol = sum(float(a[1]) for a in asks)

        imbalance = (bid_vol - ask_vol) / max((bid_vol + ask_vol), 1)
        spoof = bid_vol > ask_vol * 3 or ask_vol > bid_vol * 3

        book_state.update({
            "bid_volume": bid_vol,
            "ask_volume": ask_vol,
            "imbalance": imbalance,
            "spoof_detected": spoof,
            "last_update": datetime.utcnow().isoformat()
        })

        log_snapshot(book_state)
    except Exception as e:
        print(f"[bookwatcher] Error analysing orderbook: {e}")


def log_snapshot(snapshot):
    with open(log_file, "a") as f:
        f.write(json.dumps(snapshot) + "\n")


# --- WebSocket Setup ---
def on_message(ws, message):
    data = json.loads(message)
    analyse_orderbook(data)


def on_error(ws, error):
    print(f"[bookwatcher] WebSocket error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("[bookwatcher] WebSocket closed.")


def run_bookwatcher():
    print("[bookwatcher] Launching...")
    ws = websocket.WebSocketApp(DEPTH_STREAM, on_message=on_message, on_error=on_error, on_close=on_close)
    thread = threading.Thread(target=ws.run_forever)
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
    run_bookwatcher()
    while True:
        pass
