#! python3
import subprocess

interface = input("enter the interface >>")
new_mac = input("enter New Mac-Address >>")

print("Changing Mac-Address for " + interface " to " + new_mac)

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface " hw ether" + new_mac)
subprocess.call("ifconfig " + interface + " up")
