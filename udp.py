import socket
import os
import psutil

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", 31337))
socket.sendto(b"FLAG:10.0.0.1:31337", ("10.0.0.2", 31338))
flag, (flag_host, flag_port) = socket.recvfrom(1024)
print(flag)
