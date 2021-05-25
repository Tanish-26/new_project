#!user/bin env pyhton
import subprocess
import optparse
import re

 def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dust="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--interface", dust="new_mac", help="New MAc Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error ("[-] please specify an interface, use --help for more info. ")
    elif not options.new_mac:
        parser.error ("[-] please specify a new mac, use --help for more info. ")
    return options
 def chnage_mac(interface, new_mac):
    print(" changing mac address for " + interface + " to " + new_mac)
    Second why which is much better and effective
    subprocess.call(["ifconfig" , interface, "down"])
    subprocess.call(["ifconfig" , interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig" , interface, "up"])
 def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface, new_mac])
    mac_address_serach_result = re.search(r"\w\w\:\w\w\:\w\w\:\w\w\:\w\w\:\w\w\", ifconfig_result )
    if mac_address_search_result:
        print(mac_address_serach_result.group(0))
    else:
        print("[-] could not read MAC address.")


options = get_arguments()

currnet_mac = get_current_mac(options.interface)
print("currnet_mac" + str(currnet_mac))

chnage_mac(options.interface, options.new_mac)

currnet_mac = get_current_mac(options.interace)
if currnet_mac == options.new_mac:
    print("[-] MAC addess was successfully changed to" + currnet_mac)
else:
    print("[-] MAc address did not get changed")






