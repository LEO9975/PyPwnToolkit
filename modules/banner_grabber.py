# modules/banner_grabber.py

import socket

def run():
    print("\n[ Banner Grabber ]")
    target = input("Enter IP or hostname: ").strip()
    port = int(input("Enter port number: ").strip())

    try:
        with socket.socket() as s:
            s.settimeout(2)
            s.connect((target, port))
            banner = s.recv(1024)
            print(f"[+] Banner from {target}:{port}:\n{banner.decode().strip()}")
    except Exception as e:
        print(f"[-] Error grabbing banner: {e}")
