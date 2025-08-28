#!/usr/bin/env python3
# InzelSec - ICMP Ping (continuous)
# Usage:
#   sudo python3 ping.py 192.168.1.1
#   sudo python3 ping.py 192.168.1.0/24 [delay_seconds]
# Ctrl+C to stop.

import ipaddress
import socket
import struct
import sys
import threading
import time
import os

ICMP_ECHO_REQUEST = 8
stop_flag = False

def checksum(data: bytes) -> int:
    if len(data) % 2:
        data += b"\x00"
    s = sum((data[i] << 8) + data[i+1] for i in range(0, len(data), 2))
    s = (s & 0xFFFF) + (s >> 16)
    s = (s & 0xFFFF) + (s >> 16)
    return ~s & 0xFFFF

def build_packet(ident: int, seq: int) -> bytes:
    header = struct.pack("!BBHHH", ICMP_ECHO_REQUEST, 0, 0, ident, seq)
    payload = b"Q" * 56
    csum = checksum(header + payload)
    header = struct.pack("!BBHHH", ICMP_ECHO_REQUEST, 0, csum, ident, seq)
    return header + payload

def send_pings(target, delay):
    ident = os.getpid() & 0xFFFF
    seq = 1
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    except PermissionError:
        print("[-] Need root privileges for raw ICMP sockets.")
        sys.exit(1)

    while not stop_flag:
        packet = build_packet(ident, seq)
        send_time = time.time()
        try:
            s.sendto(packet, (str(target), 0))
        except Exception:
            pass
        seq += 1
        time.sleep(delay)
    s.close()

def listen_replies(target_ip):
    global stop_flag
    try:
        r = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        r.settimeout(0.5)
    except PermissionError:
        print("[-] Need root privileges for raw ICMP sockets.")
        sys.exit(1)

    while not stop_flag:
        try:
            pkt, addr = r.recvfrom(1024)
        except socket.timeout:
            continue

        src_ip = addr[0]
        if src_ip != target_ip:
            continue

        icmp_type = pkt[20]
        if icmp_type == 0:  # Echo Reply
            recv_time = time.time()
            ttl = pkt[8]
            print(f"{len(pkt)} bytes from {src_ip}: ttl={ttl} time={(recv_time - start_time)*1000:.2f} ms")
            # reset start_time so next reply time is correct
            globals()['start_time'] = recv_time
    r.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: sudo python3 {sys.argv[0]} <IP> [delay_seconds]")
        sys.exit(1)

    target_arg = sys.argv[1]
    delay = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0

    try:
        # Only accept single IP for classic ping-like behavior
        ip = socket.gethostbyname(target_arg)
    except socket.gaierror:
        print("[-] Invalid target.")
        sys.exit(1)

    print(f"PING {ip} (ICMP) with 56 bytes of data:")

    alive_hosts = []
    start_time = time.time()

    t_listener = threading.Thread(target=listen_replies, args=(ip,))
    t_listener.daemon = True
    t_listener.start()

    try:
        send_pings(ip, delay)
    except KeyboardInterrupt:
        stop_flag = True
        print("\n--- ping statistics ---")
        sys.exit(0)
