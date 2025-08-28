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
git clone https://github.com/<your-user>/icmp-ping.git
cd icmp-ping
chmod +x ping.py
```

## Usage

sudo python3 ping.py 8.8.8.8
sudo python3 ping.py example.com
# custom interval (seconds)
sudo python3 ping.py 8.8.8.8 0.5


## Output example:
PING 8.8.8.8 (ICMP) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=24.13 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=23.94 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=117 time=24.01 ms
^C
--- ping statistics ---
3 packets transmitted, 3 received, 0.0% packet loss, time 3002ms

