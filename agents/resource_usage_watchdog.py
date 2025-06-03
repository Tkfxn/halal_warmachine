import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 85  # percent
RAM_THRESHOLD = 80  # percent

MONITORED_PROCS = ["commander.py", "dashboard.py"]


def get_proc_stats():
    stats = {}
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            for match in MONITORED_PROCS:
                if match in ' '.join(proc.info['cmdline']):
                    cpu = proc.cpu_percent(interval=0.5)
                    mem = proc.memory_percent()
                    stats[proc.info['pid']] = (match, cpu, mem)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return stats


def watchdog():
    print("[RESOURCE-WATCHDOG] Monitoring process usage...")
    while True:
        stats = get_proc_stats()
        for pid, (name, cpu, mem) in stats.items():
            if cpu > CPU_THRESHOLD or mem > RAM_THRESHOLD:
                print(f"[RESOURCE-WATCHDOG] ⚠️ {name} (PID {pid}) is consuming high resources at {datetime.now()} | CPU: {cpu:.2f}%, RAM: {mem:.2f}%")
                # Future: throttle agents or trigger restart
        time.sleep(30)


if __name__ == "__main__":
    watchdog()
