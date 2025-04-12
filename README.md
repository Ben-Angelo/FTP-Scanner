# FTP & Telnet Vulnerability Scanner

This is a simple Python tool that scans a target IP for two insecure services:

- *FTP (port 21)* — Checks if anonymous login is allowed.
- *Telnet (port 23)* — Attempts login using common weak credentials.

## Features

- Fast socket connection scanning
- Anonymous FTP login check
- Telnet weak password test (optional)
- Easy to use

## How It Works

1. You provide the target's IP address.
2. The script checks if ports 21 and 23 are open.
3. If open:
   - It attempts anonymous login on FTP.
   - It tries default login on Telnet.

## Example

```bash
python scanner.py 192.168.43.101
