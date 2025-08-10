import nmap
import socket
from network_scan import ScanResults


def do_scan():
    scan = ScanResults()
    scan.scan_network()

def open_ports(scan_results, ip_addr):
    for protocol in scan_results[ip_addr].all_protocols():
        print(f"Protocol: {protocol}")
        
        port_list = scan_results[ip_addr][protocol].keys()
        for port in port_list:
            print(f"Port: {port}    State: {scan_results[ip_addr][protocol][port]["state"]}")

#search for open ports
my_device = do_scan()
open_ports(my_device.scan_results, my_device.ip_addr)



#search for services





