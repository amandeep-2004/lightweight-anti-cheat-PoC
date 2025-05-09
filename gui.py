import tkinter as tk
from tkinter import ttk, scrolledtext
from utils.process_scanner import scan_processes
import threading
import time

# Global flag for auto-scan
auto_scan_active = False

def run_scan(output_box):
    suspicious = scan_processes()
    output_box.delete('1.0', tk.END)
    if suspicious:
        output_box.insert(tk.END, "Suspicious processes detected:\n\n")
        for proc in suspicious:
            output_box.insert(tk.END, f" - PID {proc['pid']}: {proc['name']}\n")
    else:
        output_box.insert(tk.END, "No suspicious processes found. System looks clean!\n")

def auto_scan_loop(output_box, interval):
    global auto_scan_active
    while auto_scan_active:
        run_scan(output_box)
        time.sleep(interval)

def start_auto_scan(output_box, interval_entry):
    global auto_scan_active
    if not auto_scan_active:
        auto_scan_active = True
        try:
            interval = int(interval_entry.get())
        except ValueError:
            interval = 10  # default 10 seconds
        t = threading.Thread(target=auto_scan_loop, args=(output_box, interval), daemon=True)
        t.start()

def stop_auto_scan():
    global auto_scan_active
    auto_scan_active = False

def main():
    root = tk.Tk()
    root.title("Lightweight Anti-Cheat PoC")
    root.geometry("600x500")

    title_label = ttk.Label(root, text="Lightweight Anti-Cheat Scanner", font=("Helvetica", 16))
    title_label.pack(pady=10)

    scan_button = ttk.Button(root, text="Run Single Scan", command=lambda: run_scan(output_box))
    scan_button.pack(pady=5)

    # Auto-scan controls
    auto_frame = ttk.Frame(root)
    auto_frame.pack(pady=5)

    interval_label = ttk.Label(auto_frame, text="Auto-Scan Interval (sec):")
    interval_label.pack(side=tk.LEFT, padx=5)

    interval_entry = ttk.Entry(auto_frame, width=5)
    interval_entry.insert(0, "10")  # default 10 seconds
    interval_entry.pack(side=tk.LEFT)

    start_button = ttk.Button(auto_frame, text="Start Auto-Scan", command=lambda: start_auto_scan(output_box, interval_entry))
    start_button.pack(side=tk.LEFT, padx=5)

    stop_button = ttk.Button(auto_frame, text="Stop Auto-Scan", command=stop_auto_scan)
    stop_button.pack(side=tk.LEFT, padx=5)

    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=18)
    output_box.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
