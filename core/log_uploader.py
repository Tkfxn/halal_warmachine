# ✅ log_uploader.py (Final Patched Version)
# Handles secure upload of key logs and outputs to Google Drive

import logging
import os
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class LogUploader:
    def __init__(self):
        self.name = "LogUploader"
        self.target_folder = "logs"
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')
        self.drive = None

    def authenticate(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            logging.error("❌ No valid credentials. Please re-authenticate.")
            return False
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile("mycreds.txt")
        self.drive = GoogleDrive(gauth)
        return True

    def upload_logs(self):
        if not self.authenticate():
            return
        for filename in os.listdir(self.target_folder):
            if filename.endswith(".txt") or filename.endswith(".log"):
                filepath = os.path.join(self.target_folder, filename)
                file_drive = self.drive.CreateFile({'title': filename})
                file_drive.SetContentFile(filepath)
                file_drive.Upload()
                logging.info(f"✅ Uploaded {filename} to Google Drive")

    def run(self):
        logging.info(f"[{self.name}] Uploader active...")
        while True:
            try:
                self.upload_logs()
                time.sleep(600)  # Every 10 minutes
            except Exception as e:
                logging.error(f"[{self.name} Error] {e}")
                time.sleep(60)
