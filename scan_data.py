import nmap
import socket
from network_scan import ScanResults


def open_ports(scan_results, ip_addr):
    for protocol in scan_results[ip_addr].all_protocols():
        print(f"Protocol: {protocol}")
        
        port_list = scan_results[ip_addr][protocol].keys()
        for port in port_list:
            print(f"Port: {port}    State: {scan_results[ip_addr][protocol][port]["state"]}")

def get_protocols(scan_results, ip_addr):
    print("All Protocols:")
    for protocol in scan_results[ip_addr].all_protocols():
        print(protocol)
#search for services





