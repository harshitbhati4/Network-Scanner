# 🔍 **PortSniffer Xtreme** 🚀  
*Blazing-fast port scanner that uncovers hidden network entry points like a digital bloodhound!*  

![Banner](https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif)

---

## 🌟 **Features** ✨
- ⚡ Lightweight but powerful Python scanner
- 🎯 Scans all 65,535 ports in one go
- 🕵️‍♂️ Hostname-to-IP resolution built-in
- ⏱️ Execution time tracking
- 🛡️ Proper error handling for network issues

```python
#!/usr/bin/env python3
# The heart of PortSniffer Xtreme
import sys
import socket
from datetime import datetime

target = socket.gethostbyname(sys.argv[1])  # DNS magic!
print(f"🔭 Scanning target: {target}")
print(f"⏰ Started: {datetime.now()}")
print('-' * 50)

try:
    for port in range(1,65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f"🚪 Port {port} is OPEN!")
except KeyboardInterrupt:
    print("\n🛑 Scan aborted by user!")
    sys.exit()
```
---

## 🛠️ **Implementation**

```bash
# Clone the beast
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner

# Make it executable
chmod +x port_scanner.py
```
---

## 💻 **Usage**

```bash
./port_scanner.py example.com       # Scan a domain
python3 port_scanner.py 192.168.1.1 # Scan an IP
```
---
## ⌨️ **Command Cheat Sheet**

| Command          | What It Does                          |
|------------------|---------------------------------------|
| `CTRL+C`         | 🚨 Emergency stop!                    |
| Any hostname     | 🔄 Auto-converts to IP                |
| `--fast`         | ⚡ Quick scan (top 1000 ports)        |
| `--verbose`      | 🔍 Show all scan attempts             |
| `--output FILE`  | 💾 Save results to specified file     |

---
## 🎨 **Sample Output**

```text
🔭 Scanning target: 127.0.0.1
⏰ Started: 2023-11-15 14:30:45.123456
--------------------------------------------------
🚪 Port 22 is OPEN!     # SSH
🚪 Port 80 is OPEN!     # HTTP
🚪 Port 443 is OPEN!    # HTTPS
💀 Port 666 is OPEN!    # Uh oh...
```
---
## ⚠️ **Ethical Notice** 
![Warning GIF](https://media.giphy.com/media/J3urE5oNvSmsI5ZI8j/giphy.gif)

> 🔒 **Legal Disclaimer**:  
> This tool is for **authorized** security testing and educational purposes only.  
> Unauthorized scanning may violate:  
> - Computer Fraud and Abuse Act (CFAA)  
> - Local cybersecurity laws  
> - Network usage policies  

Unauthorized use = 🚔 Legal consequences + 🏛️ Fines + 🔓 Reputation damage

---

## 🤝 **Want to improve This ?**
- 🍴 Fork it
- 🌱 Create your feature branch
- 💾 Commit changes
- 📤 Push to the branch
- 🔃 Create a PR

---

## 📜 **License**

MIT © [Harshit Bhati] - Hack responsibly!
[![GitHub Stars](https://img.shields.io/github/stars/harshitbhati4/port-scanner?style=for-the-badge)](https://github.com/harshitbhati4/port-scanner)
[![Python Version](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)](https://python.org)

---

### 🎉 **Happy (ethical) hacking!** 🎉
![Hacker GIF](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif)
