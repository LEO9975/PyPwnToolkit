# main.py

import os
import sys
from modules import port_scanner, brute_forcer, banner_grabber, ping_sweep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("""
    =====================================
        PyPwnToolkit - by Om Shinde
    =====================================
    [1] Port Scanner
    [2] Web Login Brute Forcer
    [3] Banner Grabber
    [4] Ping Sweep (Live Hosts)
    [0] Exit
    """)

    choice = input("Select a module: ").strip()
    
    if choice == '1':
        port_scanner.run()
    elif choice == '2':
        brute_forcer.run()
    elif choice == '3':
        banner_grabber.run()
    elif choice == '4':
        ping_sweep.run()
    elif choice == '0':
        print("Exiting toolkit.")
        sys.exit()
    else:
        print("Invalid choice. Try again.")

    input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    while True:
        main_menu()
