# === pulse_sniper.py ===
# Aggregates crypto news and sentiment from various sources

import requests
import time
import json
import os
from datetime import datetime

SAVE_PATH = "intel/news_feed.json"

class PulseSniper:
    def __init__(self):
        self.sources = [
            "https://api.coingecko.com/api/v3/status_updates",
            "https://cryptopanic.com/api/v1/posts/?auth_token=demo&public=true",
            # You can add more free sources or scraped links here
        ]

    def fetch_news(self):
        headlines = []
        for url in self.sources:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    headlines.append({
                        "source": url,
                        "data": response.json(),
                        "fetched_at": datetime.utcnow().isoformat()
                    })
                else:
                    print(f"⚠️ Failed to fetch from {url} - Status: {response.status_code}")
            except Exception as e:
                print(f"❌ Error fetching from {url}: {e}")

        return headlines

    def save_to_file(self, data):
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        with open(SAVE_PATH, "w") as f:
            json.dump(data, f, indent=2)

    def run(self):
        print("📡 Pulse Sniper fetching crypto news...")
        news_data = self.fetch_news()
        self.save_to_file(news_data)
        print(f"✅ Fetched {len(news_data)} sources and saved to {SAVE_PATH}")


if __name__ == "__main__":
    sniper = PulseSniper()
    sniper.run()
