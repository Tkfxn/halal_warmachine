# loop_commander.py
# File Location: C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine\agents\loop_commander.py

import time
import redis
from datetime import datetime

# Connect to Redis shared memory
r = redis.Redis(host='localhost', port=6379, db=0)

class LoopCommander:
    def __init__(self):
        self.loop_active = True

    def read_flags(self):
        flags = {
            'spoof_alert': r.get('spoof_alert'),
            'high_latency': r.get('latency_alert'),
            'trade_limit_hit': r.get('trade_limit'),
            'error_flag': r.get('error_flag')
        }
        return {k: v.decode() if v else None for k, v in flags.items()}

    def evaluate_flags(self, flags):
        if flags['spoof_alert'] == '1' and flags['high_latency'] == '1':
            print("[LOOP-COMMANDER] 🚑 PAUSE: Spoof + Latency detected!")
            r.set('exec_agent_pause', '1')
        elif flags['trade_limit_hit'] == '1':
            print("[LOOP-COMMANDER] ⛔ Max trades hit, halting until reset.")
            r.set('exec_agent_pause', '1')
        elif flags['error_flag'] == '1':
            print("[LOOP-COMMANDER] 🔧 Error flag detected. Triggering recovery...")
            r.set('patchsmith_trigger', '1')
        else:
            r.set('exec_agent_pause', '0')

    def run(self):
        print("[LOOP-COMMANDER] Meta-agent online...")
        while self.loop_active:
            flags = self.read_flags()
            self.evaluate_flags(flags)
            time.sleep(5)

if __name__ == '__main__':
    commander = LoopCommander()
    commander.run()
