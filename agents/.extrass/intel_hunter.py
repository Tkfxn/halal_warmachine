# === intel_hunter.py ===
# Scans GitHub + KDnuggets for new AI agent upgrades

import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os

OUTPUT_FILE = "data/upgrade_queue.json"
GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
KDNUGGETS_URL = "https://www.kdnuggets.com/category/news/index.html"

HEADERS = {"Accept": "application/vnd.github+json"}
GITHUB_KEYWORDS = ["crypto agent", "trading bot", "langgraph", "agent framework"]

# --- GitHub Repo Search ---
def search_github():
    results = []
    for keyword in GITHUB_KEYWORDS:
        params = {"q": keyword, "sort": "stars", "order": "desc", "per_page": 3}
        r = requests.get(GITHUB_SEARCH_URL, headers=HEADERS, params=params)
        if r.status_code == 200:
            for item in r.json().get("items", []):
                results.append({
                    "source": "GitHub",
                    "title": item["name"],
                    "desc": item.get("description", "-"),
                    "url": item["html_url"],
                    "stars": item["stargazers_count"],
                    "timestamp": datetime.utcnow().isoformat()
                })
    return results


# --- KDnuggets Scraper ---
def scrape_kdnuggets():
    r = requests.get(KDNUGGETS_URL)
    soup = BeautifulSoup(r.content, "html.parser")
    articles = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        if re.search(r"agent|AI|strategy|framework|autonomous", text, re.I):
            articles.append({
                "source": "KDnuggets",
                "title": text,
                "url": href,
                "timestamp": datetime.utcnow().isoformat()
            })
    return articles[:5]

# --- Run Full Sweep ---
def run_hunter():
    print("[intel_hunter] Scanning web for upgrade ideas...")
    upgrades = search_github() + scrape_kdnuggets()

    if not os.path.exists("data"):
        os.makedirs("data")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(upgrades, f, indent=2)

    print(f"[intel_hunter] {len(upgrades)} new ideas added to upgrade queue.")

if __name__ == "__main__":
    run_hunter()
