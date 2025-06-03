# === dashboard.py ===
# Streamlit dashboard for monitoring and control

import streamlit as st
import os
import time
import threading

st.set_page_config(page_title="Halal War Machine Panel", layout="centered")
st.title("📃 Halal War Machine Dashboard")

LOG_FILE = "logs/system_stdout.txt"

# Control buttons
col1, col2, col3 = st.columns(3)
start_clicked = col1.button("\u25b6\ufe0f Start System")
stop_clicked = col2.button("🛑 Stop System")
upload_clicked = col3.button("\u2601\ufe0f Upload Logs (Backup)")

log_placeholder = st.empty()
st.markdown("---")

# === System Log Tailer ===
def tail_logs():
    log_placeholder.markdown("**Live System Logs:**")
    log_area = log_placeholder.empty()
    last_pos = 0
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                f.seek(last_pos)
                new_data = f.read()
                last_pos = f.tell()
                if new_data:
                    log_area.code(new_data, language="bash")
        time.sleep(2)

def run_mission_control():
    os.system("python mission_control.py")

def upload_logs():
    os.system("python core/log_uploader.py")

# === Button Handlers ===
if start_clicked:
    threading.Thread(target=run_mission_control).start()

if stop_clicked:
    st.warning("Manual stop is not implemented yet. Close terminal to stop agents.")

if upload_clicked:
    upload_logs()

# === Start live log tailing ===
threading.Thread(target=tail_logs).start()

st.markdown("---")
st.caption("Made by GPT, managed by Talha 🧠")
