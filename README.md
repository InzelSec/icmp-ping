# ICMP Ping

A minimal Python implementation of the classic **ping** command using raw 
sockets.  
It sends ICMP Echo Requests and prints replies with `icmp_seq`, `ttl`, and 
RTT in ms.

⚠️ Requires **root privileges** (or `CAP_NET_RAW`) to run.

---

## Installation

Clone the repository and make the script executable:

```bash
git clone https://github.com/<your-user>/icmp-ping.git
cd icmp-ping
chmod +x ping.py


## Usage

# classic 1-second interval
sudo python3 ping.py 1.1.1.1

# custom interval (seconds)
sudo python3 ping.py 8.8.8.8 0.5

# hostname works too
sudo python3 ping.py example.com

