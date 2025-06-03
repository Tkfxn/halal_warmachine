# ✅ File: agents/drive_sync_agent.py
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, time

def init_drive():
    gauth = GoogleAuth()
    if os.path.exists("mycreds.txt"):
        try:
            gauth.LoadCredentialsFile("mycreds.txt")
            gauth.Refresh()
            print("[DriveSync] Loaded and refreshed existing credentials.")
        except Exception as e:
            print(f"[DriveSync] Refresh failed: {e}")
            os.remove("mycreds.txt")
            return init_drive()
    else:
        gauth.LocalWebserverAuth()
        gauth.SaveCredentialsFile("mycreds.txt")
        print("[DriveSync] New credentials saved.")
    return GoogleDrive(gauth)

def upload_logs(drive):
    log_folder = "logs"
    for filename in os.listdir(log_folder):
        filepath = os.path.join(log_folder, filename)
        if not os.path.isfile(filepath):
            continue
        try:
            file_drive = drive.CreateFile({"title": filename})
            file_drive.SetContentFile(filepath)
            file_drive.Upload()
            print(f"[DriveSync] Uploaded: {filename}")
        except Exception as e:
            print(f"[DriveSync] Failed to upload {filename}: {e}")

# ✅ Patch Commander to launch this agent in background
import threading

def start_drive_sync():
    try:
        from agents.drive_sync_agent import init_drive, upload_logs
        def drive_loop():
            drive = init_drive()
            while True:
                upload_logs(drive)
                time.sleep(600)  # every 10 minutes
        t = threading.Thread(target=drive_loop, daemon=True)
        t.start()
        print("[Commander] Drive Sync Agent started.")
    except Exception as e:
        print(f"[Commander] Failed to start Drive Sync Agent: {e}")
