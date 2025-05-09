import psutil
from .logger import log_scan_results

SUSPICIOUS_KEYWORDS = [
    "cheat",
    "trainer",
    "injector",
    "hack",
    "debug",
    "engine",
    "olly",
    "x64dbg",
    "wireshark"
]

def scan_processes():
    suspicious_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in pname:
                    suspicious_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    log_scan_results(suspicious_processes)
    return suspicious_processes
