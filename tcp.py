from scapy.all import *

# Define the Ethernet frame with custom Ether type
send(IP(dst="10.0.0.2")/TCP(sport = 31337, dport=31337, seq=31337, ack=31337, flags="APRSF"))

# Send the Ethernet frame
