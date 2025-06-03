import json
import os
from datetime import datetime

MEMORY_FILE = "logs/evolver_memory.json"

class EvolverMemory:
    def __init__(self):
        self.memory = []
        self.load()

    def load(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                self.memory = json.load(f)
        else:
            self.memory = []

    def save(self):
        with open(MEMORY_FILE, 'w') as f:
            json.dump(self.memory[-100:], f, indent=2)

    def remember(self, pattern, outcome, context=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "pattern": pattern,
            "outcome": outcome,
            "context": context
        }
        self.memory.append(entry)
        self.save()

    def recall_failures(self):
        return [m for m in self.memory if m['outcome'] == 'fail']

    def recall_successes(self):
        return [m for m in self.memory if m['outcome'] == 'profit']


# Example usage
if __name__ == "__main__":
    mem = EvolverMemory()
    mem.remember("morning breakout", "fail", "Volatility spike after entry")
    mem.remember("double bottom", "profit", "Reversal clean at support")

    print("FAILED PATTERNS:", mem.recall_failures())
    print("WINNING PATTERNS:", mem.recall_successes())
