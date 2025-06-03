# ✅ exec_agent.py (Enhanced for Live Command Execution)
# Handles real-time execution commands and loop integration

import time
import logging
from datetime import datetime

class ExecAgent:
    def __init__(self):
        self.name = "ExecAgent"
        self.last_command_time = None
        self.command_log_path = "logs/exec_agent_commands.txt"
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

    def get_next_command(self):
        # 🔁 Placeholder: Replace with real logic to fetch command from queue, file, or GPT
        return "HOLD"

    def execute_command(self, command):
        # 🧠 Hook: Replace with real execution logic later
        if command == "BUY":
            logging.info("Executing BUY logic...")
        elif command == "SELL":
            logging.info("Executing SELL logic...")
        elif command == "HOLD":
            logging.info("No action taken. HOLD.")
        else:
            logging.warning(f"Unknown command: {command}")

    def log_command(self, command):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.command_log_path, "a") as f:
            f.write(f"[{timestamp}] {command}\n")

    def run(self):
        logging.info(f"[{self.name}] Agent starting up...")
        while True:
            try:
                command = self.get_next_command()
                self.log_command(command)
                self.execute_command(command)
                time.sleep(30)  # Tick rate
            except Exception as e:
                logging.error(f"[ExecAgent Error] {e}")
                time.sleep(10)  # Wait before retry
