from scapy.all import *

# Define the Ethernet frame with custom Ether type
eth = Ether(type=0xFFFF)/IP(dst="10.0.0.2")

# Send the Ethernet frame
sendp(eth)
