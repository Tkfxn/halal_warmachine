
# === log_uploader.py ===
# Handles log uploads to Google Drive automatically + manually

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import time

def authenticate():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("drive_creds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("drive_creds.txt")
    return GoogleDrive(gauth)

def upload_logs():
    drive = authenticate()
    folder_path = "logs"
    if not os.path.exists(folder_path):
        print("No logs folder found to upload.")
        return
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            file_drive = drive.CreateFile({"title": filename})
            file_drive.SetContentFile(filepath)
            file_drive.Upload()
            print(f"Uploaded {filename} to Drive")

def manual_upload():
    print("[log_uploader] Manual upload started")
    upload_logs()

def run():
    print("[log_uploader] Auto upload starting...")
    upload_logs()
    print("[log_uploader] Auto upload complete")

if __name__ == "__main__":
    run()
