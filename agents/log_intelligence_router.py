import os
import time
import re
from datetime import datetime

LOG_FILES = [
    "logs/commander_console_log.txt",
    "logs/system_stdout.txt"
]

SUMMARY_FILE = "logs/log_summary.txt"
CATEGORY_PATTERNS = {
    "ERROR": re.compile(r"\b(ERROR|EXCEPTION|CRASH|Traceback)\b", re.IGNORECASE),
    "TRADE": re.compile(r"\b(BUY|SELL|TP|SL|TRADE|ENTRY|EXIT)\b", re.IGNORECASE),
    "LOOP": re.compile(r"\b(loop|restart|cycle|tick)\b", re.IGNORECASE),
    "AGENT": re.compile(r"\b(agent|task|patch|strategy|watcher)\b", re.IGNORECASE),
}

CACHE_LINES = set()


def classify_line(line):
    for category, pattern in CATEGORY_PATTERNS.items():
        if pattern.search(line):
            return category
    return "OTHER"


def summarise_logs():
    summary_lines = []
    for filepath in LOG_FILES:
        if not os.path.exists(filepath):
            continue
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line in CACHE_LINES:
                    continue
                CACHE_LINES.add(line)
                category = classify_line(line)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                summary_lines.append(f"[{timestamp}] [{category}] {line}")

    if summary_lines:
        with open(SUMMARY_FILE, 'a') as out:
            out.write("\n".join(summary_lines) + "\n")
            print(f"[ROUTER] {len(summary_lines)} new entries routed to {SUMMARY_FILE}")


if __name__ == "__main__":
    while True:
        summarise_logs()
        time.sleep(300)  # every 5 mins
