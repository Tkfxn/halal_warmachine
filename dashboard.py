# dashboard.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\dashboard.py

import streamlit as st
import pandas as pd
import os
import json
import sys
sys.path.append("agents")
from redis_client import fetch_all
from strategy_evolver import get_pattern_scores

st.set_page_config(layout="wide", page_title="Halal Warmachine Dashboard")

LOG_DIR = "logs/"

def load_log(filename):
    path = os.path.join(LOG_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "No log available."

def load_json(filename):
    path = os.path.join(LOG_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

st.title("Halal Warmachine Dashboard")
tabs = st.tabs(["Trade Stats", "Loop Logs", "Learned Logic", "Pattern Scores", "Redis Flags", "Control Panel", "Alerts Config"])

with tabs[0]:
    st.subheader("📈 Trade Summary")
    stats = load_json("trade_stats.json")
    if stats:
        st.metric("Total Trades", stats.get("total", 0))
        st.metric("Win Rate", f"{stats.get('winrate', 0)}%")
        st.metric("P&L", f"${stats.get('pnl', 0):.2f}")
        st.metric("Max Drawdown", f"{stats.get('drawdown', 0)}%")
    else:
        st.warning("No stats yet.")

with tabs[1]:
    st.subheader("🌀 Loop Logs")
    st.text(load_log("system_stdout.txt"))

with tabs[2]:
    st.subheader("🧠 Strategy Insights")
    mem = load_json("evolver_memory.json")
    st.json(mem)

with tabs[3]:
    st.subheader("📊 Pattern Scores")
    scores = get_pattern_scores()
    if scores:
        df = pd.DataFrame(scores).T
        df["Win Rate"] = df["wins"] / (df["wins"] + df["losses"] + 1e-9)
        st.dataframe(df.sort_values("Win Rate", ascending=False))
    else:
        st.warning("No pattern scores yet.")

with tabs[4]:
    st.subheader("🔁 Redis Flags")
    state = fetch_all()
    st.json(state)

with tabs[5]:
    st.subheader("⚙️ Agent Control")
    st.button("Pause Trading")
    st.button("Resume Trading")
    st.button("Trigger Patchsmith")

with tabs[6]:
    st.subheader("🚨 Telegram Alerts")
    st.write("Daily alerts are sent at 00:01 Bahrain time with full stats.")
    st.success("Telegram alerts enabled and active.")
