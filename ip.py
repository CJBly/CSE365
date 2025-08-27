from scapy.all import *

# Define the Ethernet frame with custom Ether type
ip = send(IP(proto=0xFF,dst="10.0.0.2"))


# Send the Ethernet frame
