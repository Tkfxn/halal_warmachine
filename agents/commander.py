# commander.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\commander.py

import time
import random
from agents.strategy_evolver import evolve_logic

print("[COMMANDER] Live Trading Loop Starting...")

while True:
    try:
        # Simulated trade outcome (replace with live result logic)
        result = random.choice(["win", "loss"])
        tag = random.choice(["spoof_whiplash", "momentum_surge", "volume_drain"])

        trade_result = {
            "pattern_tag": tag,
            "outcome": result
        }

        evolve_logic(trade_result)

        print(f"[COMMANDER] Trade executed: {trade_result}")
        time.sleep(10)

    except Exception as e:
        print(f"[COMMANDER] ERROR: {e}")
        time.sleep(5)
