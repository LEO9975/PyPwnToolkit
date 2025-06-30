# modules/ping_sweep.py

import socket
import ipaddress

def run():
    print("\n[ Ping Sweep ]")
    subnet = input("Enter subnet (e.g. 192.168.1.0/24): ").strip()
    
    try:
        net = ipaddress.ip_network(subnet, strict=False)
    except:
        print("Invalid subnet.")
        return

    print(f"\nScanning subnet {subnet}...\n")
    for ip in net.hosts():
        try:
            socket.setdefaulttimeout(0.5)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((str(ip), 80))
            if result == 0:
                print(f"[+] Host {ip} is up (port 80 open)")
            s.close()
        except:
            pass
