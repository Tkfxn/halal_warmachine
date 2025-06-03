import streamlit as st
import os
import subprocess
import webbrowser
import threading
import yaml

st.set_page_config(page_title="Halal War Machine Control Panel", layout="wide")

with open("settings.yml", "r") as f:
    settings = yaml.safe_load(f)

BINANCE_MODE = settings.get("binance_mode", "testnet")
AUTO_UPLOAD = settings.get("auto_upload_logs", True)

def run_system():
    subprocess.Popen(["python", "mission_control.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def upload_logs():
    subprocess.Popen(["python", "core/log_uploader.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def open_dashboard():
    webbrowser.open("http://localhost:8501", new=2)

# === Title and Controls ===
st.title("🧠 Halal War Machine Control Panel")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Start System"):
        st.success("System launching...")
        threading.Thread(target=run_system).start()

with col2:
    if st.button("📤 Upload Logs Manually"):
        st.warning("Uploading logs manually...")
        threading.Thread(target=upload_logs).start()

with col3:
    st.markdown(f"**Exchange Mode:** `{BINANCE_MODE}`")

# === Log Panel ===
st.subheader("📄 Live CMD Output Log")
log_file = "logs/system_stdout.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.read()
    st.text_area("Console Output", logs, height=400)
else:
    st.warning("Log file not found. System might not have started yet.")

# === Auto Upload Trigger ===
if AUTO_UPLOAD:
    threading.Thread(target=upload_logs).start()
    st.success("Auto log upload triggered ✅")
