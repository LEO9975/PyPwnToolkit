# modules/port_scanner.py

import socket

def run():
    print("\n[ Port Scanner Module ]")
    target = input("Enter target IP or hostname: ").strip()
    port_range = input("Enter port range (e.g. 1-1000): ").strip()

    try:
        start, end = map(int, port_range.split('-'))
    except:
        print("Invalid port range.")
        return

    print(f"\nScanning {target} from port {start} to {end}...\n")
    
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
