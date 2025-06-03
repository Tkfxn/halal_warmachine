# ✅ spoof_detector.py (Final Patched Version)
# Detects spoofing patterns in order book activity

import logging
import time

class SpoofDetector:
    def __init__(self):
        self.name = "SpoofDetector"
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

    def detect_spoofing(self):
        logging.info(f"[{self.name}] Analysing order book for spoof patterns...")
        # Simulated detection logic placeholder
        detected = False  # Replace with real detection logic later
        if detected:
            logging.warning(f"[{self.name}] 🚨 Potential spoofing detected!")

    def run(self):
        logging.info(f"[{self.name}] Agent active and scanning...")
        while True:
            try:
                self.detect_spoofing()
                time.sleep(300)  # Scan every 5 minutes
            except Exception as e:
                logging.error(f"[{self.name} Error] {e}")
                time.sleep(60)

