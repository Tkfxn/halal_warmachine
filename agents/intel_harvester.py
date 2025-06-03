# intel_harvester.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\intel_harvester.py

import requests
import time
import json
import os
from datetime import datetime

OUTPUT_DIR = "logs/intel_harvests"
os.makedirs(OUTPUT_DIR, exist_ok=True)

HEADERS = {"User-Agent": "IntelHarvester/1.0"}

SOURCES = [
    "https://api.github.com/search/repositories?q=crypto+trading+bot&sort=stars&order=desc",
    "https://hn.algolia.com/api/v1/search?query=crypto+trading",
    "https://api.marktechpost.com/api/news/?q=crypto",
    # Add more sources as needed
]

def fetch_sources():
    results = {}
    for url in SOURCES:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            if resp.status_code == 200:
                results[url] = resp.json()
            else:
                results[url] = {"error": f"HTTP {resp.status_code}"}
        except Exception as e:
            results[url] = {"error": str(e)}
    return results

def save_report(data):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(OUTPUT_DIR, f"intel_report_{ts}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[INTEL HARVESTER] Report saved to {path}")

if __name__ == "__main__":
    while True:
        intel = fetch_sources()
        save_report(intel)
        time.sleep(1800)  # Every 30 minutes
