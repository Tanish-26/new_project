#python3
import scapy.all as scapy
import optparse

def get_agruments():
	parser = optparse.optionparser()
	parser.add_option("-t", "--target", dest="target", help="target IP/IP range")
	(options,agruments) = parser.parse_args()
	return options

ip = input("enter the routers ip or the gate way ip")

def scan(IP):
	apr_request = scapy.ARP(pdst=IP)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	apr_request_broatcast = broadcast/apr_request
	answered_list = scapy.srp(apr_request_broatcast, timeout=1, verbo=False)[0]
    
    clients_list = []
    for element in answered_list:
    	clients_dict = {"IP": element[1].psrc, "MAC_Address": element[1].hwdst}
    	clients_list.append(clients_dict)
    	return clients_list

def print_result(result_list):
	print("IP \t\t\t MAC_Address\n ----------------------------------------------------")
	for client in result_list:
		print(client["IP"] + "\t\t" + client["MAC_Address"])

options = get_agruments
scan_result = scan(IP)
print_result(scan_result)		

https://portswigger.net/users/retrieve-password-t7eee598d455d71285cfa0ccc501873ac490a6c80096ee83c36570fe98211c6cf?tid=Et4Q1BIKdJk4P6Iy6VE4oNL4Y5svB2GE7htdj36SBt_8cV62F39ErW0-n7mwkdoK
			
