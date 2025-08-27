import socket
import os
import psutil
from scapy.all import *
conf.verb = 0

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", 31337))
#socket.sendto(b"FLAG:10.0.0.1:31337", ("10.0.0.2", 31338))
#flag, (flag_host, flag_port) = socket.recvfrom(1024)
child_processes = int(50)
port_range = int(65535 / 50)
start_port = 0
for i in range(0,child_processes):
    current_port = start_port
    start_port = current_port+port_range+1
    val = os.fork()
    if val == 0:
        print(f"Starting to scan {start_port}")
        for j in range(current_port, current_port+port_range):
            packet = IP(src = "10.0.0.3", dst = "10.0.0.2") / UDP(sport = 31337, dport = j) / Raw(load=b"FLAG:10.0.0.1:31337")
            send(packet)
        print(f"Finished scanning {start_port}")
print("Started listening")
flag, (flag_host, flag_port) = socket.recvfrom(1024)
print(flag)
