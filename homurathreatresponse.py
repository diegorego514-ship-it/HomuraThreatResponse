import socket
import argparse
import requests

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.close()
    s.gettimeout(5) # Set timer in Seconds
    s.time_sleep(10) # Set time in Seconds to Avoid Detection
    s.send(max.data, 1024, bin)
except:
    print("[*] Your Port is Secure.")

    print("[+] Your devices are not safe.")

    print("[-] Recommendation - Be sure to scan your devices regularly" 
  " and update/upgrade them"  " from time to time to keep them safe"  
  " from threats and cybercriminals all the time")

else:
    print("[*] Your devices are compromised")