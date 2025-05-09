import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "scan_log.txt")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

def log_scan_results(results):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n--- Scan at {datetime.now()} ---\n")
        if results:
            for proc in results:
                f.write(f" - PID {proc['pid']}: {proc['name']}\n")
        else:
            f.write("No suspicious processes found.\n")
