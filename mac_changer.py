#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
        exit(1)
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info.")
        exit(1)

    return options

def change_mac(interface, new_mac):
    if interface is None or new_mac is None:
        print("[-] Please specify an interface and a MAC address.")
    exit(1)

    print("[+] Changing MAC address for " + interface + " to " + new_mac)    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)

# This script uses the subprocess module to call system commands to change the MAC address.
# It uses the optparse module to parse command-line options.
# The script first checks if the user has provided the necessary arguments (interface and new MAC address). 


                
# The above code is a simple Python script that changes the MAC address of a network interface on a Linux system.