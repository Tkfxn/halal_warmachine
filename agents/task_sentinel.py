# ✅ task_sentinel.py (Patched with schedule_tasks entrypoint)
import schedule
import threading
import time
import logging
import os
from datetime import datetime

def weekly_patch_check():
    logging.info("🔁 Weekly patch check triggered.")
    # Future: Pull updates from repo or cloud

def daily_log_backup():
    logging.info("💾 Daily log backup saved.")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.system(f"xcopy logs logs_backup\{timestamp} /E /I /Y")

def review_trade_results():
    logging.info("📊 Reviewing daily trade results...")
    # Future: Load CSV, analyse PnL, trigger patch

def sync_google_drive():
    logging.info("☁️ Syncing Google Drive")
    os.system("python core/drive_sync_agent.py")

def health_check():
    logging.info("🩺 System health check running")
    # Future: Ping commander log, detect stalls

def schedule_tasks():
    logging.info("📅 Task Sentinel Scheduler Starting")
    schedule.every().day.at("01:00").do(weekly_patch_check)
    schedule.every().day.at("02:00").do(daily_log_backup)
    schedule.every().day.at("03:00").do(review_trade_results)
    schedule.every(10).minutes.do(sync_google_drive)
    schedule.every(15).seconds.do(health_check)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    t = threading.Thread(target=run_schedule)
    t.daemon = True
    t.start()
    logging.info("✅ Task scheduling launched")
