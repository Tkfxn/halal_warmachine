# strategy_evolver.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\strategy_evolver.py

import json
import os
from pattern_scorer import update_pattern_score

MEMORY_FILE = "memory/evolver_memory.json"

if not os.path.exists("memory"):
    os.makedirs("memory")

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)


def evolve_logic(trade_result):
    """
    Updates strategy logic based on trade outcome
    trade_result: dict with keys 'outcome' ('win'/'loss'), 'pattern_tag', etc.
    """
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except:
        memory = {}

    tag = trade_result.get("pattern_tag")
    outcome = trade_result.get("outcome")

    if tag and outcome:
        update_pattern_score(tag, outcome)

    memory.setdefault(tag, {"total": 0, "wins": 0, "losses": 0})
    memory[tag]["total"] += 1
    if outcome == "win":
        memory[tag]["wins"] += 1
    elif outcome == "loss":
        memory[tag]["losses"] += 1

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

    print(f"[EVOLVER] Updated logic for pattern: {tag} - {memory[tag]}")


def get_pattern_scores():
    """
    Return pattern scores as dict
    """
    try:
        with open("memory/pattern_scores.json", "r") as f:
            return json.load(f)
    except:
        return {}


if __name__ == "__main__":
    sample_trade = {
        "pattern_tag": "spoof_whiplash",
        "outcome": "loss"
    }
    evolve_logic(sample_trade)
