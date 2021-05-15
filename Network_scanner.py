#!user/bin/env/python

import scapy.all as scapy

def scan(ip):
    arp_requset = scapy.ARP(pdst=ip)
    broadcast =  scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requset_broadcast = broadcast/arp_requset
    answered_list, unanswered_list = scapy.srp(arp_requset_broadcast, timeout=1)
    print(answered_list.summary())

scan("ip/ciddr")


