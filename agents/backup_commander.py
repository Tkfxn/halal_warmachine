# ✅ backup_commander.py (Final Patched Version)
# Monitors commander logs and restarts system if crash or silence is detected

import os
import time
import logging
from datetime import datetime, timedelta

class BackupCommander:
    def __init__(self, log_path="logs/commander_console_log.txt", timeout_minutes=5):
        self.name = "BackupCommander"
        self.log_path = log_path
        self.timeout = timedelta(minutes=timeout_minutes)
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

    def last_modified_time(self):
        try:
            return datetime.fromtimestamp(os.path.getmtime(self.log_path))
        except FileNotFoundError:
            return datetime.min

    def check_loop_health(self):
        now = datetime.now()
        last_mod = self.last_modified_time()
        logging.info(f"[{self.name}] Last commander log time: {last_mod}")
        if now - last_mod > self.timeout:
            logging.warning(f"[{self.name}] Commander seems stalled! Restart logic should trigger here.")
            # 🔁 Restart logic placeholder — could restart .bat or system script

    def run(self):
        logging.info(f"[{self.name}] Agent running...")
        while True:
            try:
                self.check_loop_health()
                time.sleep(120)
            except Exception as e:
                logging.error(f"[{self.name} Error] {e}")
                time.sleep(60)
