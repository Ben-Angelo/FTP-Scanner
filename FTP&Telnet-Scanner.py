import socket
from ftplib import FTP
import telnetlib

# Common credentials to try on Telnet
common_creds = [
    ('admin', 'admin'),
    ('root', 'root'),
    ('user', '1234'),
    ('admin', '12345')
]

# Function to check if a port is open
def is_port_open(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=3):
            return True
    except:
        return False

# Check for anonymous FTP login
def check_ftp(ip):
    try:
        ftp = FTP(ip, timeout=5)
        ftp.login()
        print(f"[+] Anonymous FTP login allowed on {ip}")
        ftp.quit()
    except Exception as e:
        print(f"[-] FTP anonymous login failed on {ip}: {e}")

# Try weak Telnet login
def check_telnet(ip):
    for username, password in common_creds:
        try:
            tn = telnetlib.Telnet(ip, 23, timeout=5)
            tn.read_until(b"login: ", timeout=3)
            tn.write(username.encode('ascii') + b"\n")
            tn.read_until(b"Password: ", timeout=3)
            tn.write(password.encode('ascii') + b"\n")
            response = tn.read_some()
            if b"Last login" in response or b"$" in response or b"#" in response:
                print(f"[+] Telnet login SUCCESS: {username}:{password} on {ip}")
                tn.close()
                return
            tn.close()
        except Exception as e:
            continue
    print(f"[-] Telnet login failed on {ip}")

# Main scanner
def scan(ip):
    print(f"Scanning {ip}...\n")

    if is_port_open(ip, 21):
        print("[*] FTP port (21) is open.")
        check_ftp(ip)
    else:
        print("[-] FTP port (21) is closed.")

    if is_port_open(ip, 23):
        print("[*] Telnet port (23) is open.")
        check_telnet(ip)
    else:
        print("[-] Telnet port (23) is closed.")

# Example IP to scan
target_ip = "192.168.1.1"
scan(target_ip)