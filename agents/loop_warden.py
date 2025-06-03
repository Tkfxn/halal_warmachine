import os
import time
from redis_client import set_flag

LOG_FILE = "logs/system_stdout.txt"
TIMEOUT_SECONDS = 30

class LoopWarden:
    def __init__(self):
        self.last_modified = None

    def file_mtime(self):
        if os.path.exists(LOG_FILE):
            return os.path.getmtime(LOG_FILE)
        return None

    def run(self):
        print("[LOOP-WARDEN] Monitoring system_stdout.txt for freeze detection...")
        while True:
            current_mtime = self.file_mtime()
            now = time.time()

            if self.last_modified and current_mtime == self.last_modified:
                print("[LOOP-WARDEN] 🧊 Freeze detected. Loop not writing logs.")
                set_flag("error_flag", "1")

            self.last_modified = current_mtime
            time.sleep(TIMEOUT_SECONDS)


if __name__ == '__main__':
    warden = LoopWarden()
    warden.run()
