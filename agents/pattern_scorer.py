# pattern_scorer.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\pattern_scorer.py

import json
import os
from collections import defaultdict

SCORES_PATH = "memory/pattern_scores.json"

if not os.path.exists("memory"):
    os.makedirs("memory")

# Initialise score dict if needed
if not os.path.exists(SCORES_PATH):
    with open(SCORES_PATH, "w") as f:
        json.dump({}, f)


def update_pattern_score(pattern_tag: str, outcome: str):
    """
    Updates win/loss score for a given pattern
    """
    with open(SCORES_PATH, "r") as f:
        scores = json.load(f)

    if pattern_tag not in scores:
        scores[pattern_tag] = {"wins": 0, "losses": 0}

    if outcome == "win":
        scores[pattern_tag]["wins"] += 1
    elif outcome == "loss":
        scores[pattern_tag]["losses"] += 1

    with open(SCORES_PATH, "w") as f:
        json.dump(scores, f, indent=2)

    print(f"[PATTERN SCORER] Updated {pattern_tag}: {scores[pattern_tag]}")


if __name__ == "__main__":
    # Test example
    update_pattern_score("momentum_surge", "win")
    update_pattern_score("spoof_whiplash", "loss")
