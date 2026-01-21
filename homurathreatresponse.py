import socket
import argparse
import requests

SERVER_HOST = "192.168.0.21"
SERVER_PORT = 1024
SERVER_LIST = SERVER_HOST, SERVER_PORT

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    s.gettimeout(5) # Set timer in Seconds
    s.time_sleep(10) # Set time in Seconds to Avoid Detection
    s.send(max.data, 1024, bin)

except:
    print("[*] Your Port is Secure.")

    print("[+] Your devices are not safe.")

    print("[-] Recommendation - Be sure to scan your devices regularly")

    print("[+] Be sure to update your devices regularly and from time to time.")

    print("[*] To avoid cyber threats and cyber criminal attacks from happening be sure to also scan your devices properly and mainly update/upgrade your systems from now on.")

else:
    print("[*] Your devices are compromised")
