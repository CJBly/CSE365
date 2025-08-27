from scapy.all import *

def print_packet(packet):
    if packet.haslayer(IP):
        ip_s = packet[IP].src
        ip_d = packet[IP].dst
        if packet.haslayer(TCP):
            s_port = packet[TCP].sport
            d_port = packet[TCP].dport
            seq = packet[TCP].seq
            ack = packet[TCP].ack
            print(f"IP: {ip_s} -> {ip_d}, Port: {s_port} -> {d_port}, Seq: {seq}, Ack: {ack}")
            return seq

# Define the Ethernet frame with custom Ether type
#send(IP(dst="10.0.0.2")/TCP(sport = 31337, dport=31337, seq=31337, ack=31337, flags="S"))
sequence = sr1(IP(dst="10.0.0.2")/TCP(sport = 31337, dport = 31337, seq=31337, ack=31337, flags="S"))
print(f"This is the : {sequence}")
print(f"This is the sequence: {sequence[TCP].seq + 1}")
send(IP(dst="10.0.0.2")/TCP(sport = 31337, dport= 31337, seq = sequence[TCP].ack, ack=sequence[TCP].seq + 1, flags="A"))
# Send the Ethernet frame
