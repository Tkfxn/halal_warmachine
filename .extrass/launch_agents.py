
# ✅ launch_agents.py
# Optional tool: opens pinned agents in Chrome
import webbrowser

tabs = [
    "https://chat.openai.com/?agent=pulse-sniper",
    "https://chat.openai.com/?agent=wallet-watcher",
    "https://chat.openai.com/?agent=intel-harvester",
    "https://chat.openai.com/?agent=spoof-detector",
    "https://chat.openai.com/?agent=wallet-cloner",
    "https://chat.openai.com/?agent=task-sentinel"
]

for tab in tabs:
    webbrowser.open(tab)
