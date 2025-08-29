<p align="center">
  <img src="https://github.com/user-attachments/assets/14b2c4c2-4a11-4bea-85de-fa660dfe591e" alt="InzelSec Logo" width="150"/>
</p>


# ICMP Ping

A Python implementation of the **ping** command using raw 
sockets.  
It sends ICMP Echo Requests and prints replies with `icmp_seq`, `ttl`, and 
RTT in ms.

⚠️ Requires **root privileges** to run.

---

## Installation

Clone the repository and make the script executable:

```bash
git clone https://github.com/InzelSec/icmp-ping.git
cd icmp-ping
chmod +x ping.py
```

## Usage
```
sudo python3 ping.py 8.8.8.8
```
```
sudo python3 ping.py example.com
```
custom interval (seconds):
```
sudo python3 ping.py 8.8.8.8 0.5
```

## Output example:

<img width="477" height="108" alt="Screenshot 2025-08-29 at 09 14 45" src="https://github.com/user-attachments/assets/e7e5af52-9b5f-4c67-bd16-ff602a9c9865" />
