# === pulse_sniper.py ===
# Gathers crypto news and sentiment from public sources

import requests
import json
import time
from datetime import datetime

NEWS_LOG = "logs/news_stream.json"

# Sources: CoinGecko + CryptoPanic Free API (optional)
def fetch_coingecko_trending():
    url = "https://api.coingecko.com/api/v3/search/trending"
    try:
        r = requests.get(url)
        data = r.json()
        trending = [coin["item"]["name"] for coin in data["coins"]]
        return {"source": "CoinGecko", "trending": trending, "timestamp": datetime.utcnow().isoformat()}
    except:
        return {"source": "CoinGecko", "error": "Failed to fetch", "timestamp": datetime.utcnow().isoformat()}

def fetch_crypto_panic():
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&public=true"
    try:
        r = requests.get(url)
        data = r.json()
        items = [x['title'] for x in data['results'][:5]]
        return {"source": "CryptoPanic", "headlines": items, "timestamp": datetime.utcnow().isoformat()}
    except:
        return {"source": "CryptoPanic", "error": "Failed to fetch", "timestamp": datetime.utcnow().isoformat()}

def write_news_entry(entry):
    if not entry:
        return
    try:
        with open(NEWS_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[pulse_sniper] Logged news from {entry.get('source')}.")
    except Exception as e:
        print(f"[pulse_sniper] Error writing log: {e}")

if __name__ == "__main__":
    print("[pulse_sniper] Gathering crypto intel...")
    gecko = fetch_coingecko_trending()
    panic = fetch_crypto_panic()
    write_news_entry(gecko)
    write_news_entry(panic)
    time.sleep(10)
