from utils.process_scanner import scan_processes

def main():
    print("[*] Running Lightweight Anti-Cheat PoC...")
    suspicious = scan_processes()
    if suspicious:
        print("[!] Suspicious processes detected:")
        for proc in suspicious:
            print(f" - PID {proc['pid']}: {proc['name']}")
    else:
        print("[+] No suspicious processes found. System looks clean!")

if __name__ == "__main__":
    main()
