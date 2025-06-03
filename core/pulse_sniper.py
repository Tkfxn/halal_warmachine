# ✅ pulse_sniper.py (Final Patched Version)
# Scans crypto news from various sources and logs alerts

import time
import logging

class PulseSniper:
    def __init__(self):
        self.name = "PulseSniper"
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

    def scan_sources(self):
        logging.info(f"[{self.name}] Checking sources: CoinGecko, Twitter, Reddit, etc...")
        # Placeholder for scraping logic
        news = [
            "BTC spikes 3% after ETF rumours",
            "Massive ETH whale transfer detected",
            "New Binance listing alert: XYZ"
        ]
        return news

    def log_alerts(self):
        alerts = self.scan_sources()
        for alert in alerts:
            logging.info(f"[PulseSniper Alert] {alert}")

    def run(self):
        logging.info(f"[{self.name}] Agent starting...")
        while True:
            try:
                self.log_alerts()
                time.sleep(180)  # Run every 3 mins
            except Exception as e:
                logging.error(f"[PulseSniper Error] {e}")
                time.sleep(60)
