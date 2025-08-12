import nmap
import socket
from dict2xml import dict2xml
from xml.dom.minidom import parseString
import xmltodict
from xml.etree.ElementTree import Element, tostring


class MachineData():
    
    def __init__(self) -> None:
        self.hostname = socket.gethostname()
        self.ip_addr = socket.gethostbyname(self.hostname)
        self.open_ports = {}
        self.os_list = []
        self.protocols = []


    def initial_scan(self, port_start: int, port_end: int):
        """Performs initial scan"""
        scanner = nmap.PortScanner()
        results = scanner.scan(ports=f"{port_start}-{port_end}", arguments="-O", hosts=self.ip_addr)
        self.save_results(results, scanner)

    def save_results(self, results, scanner):
        for os in results["scan"][self.ip_addr]["osmatch"]:
            self.os_list.append(os["name"])

        for protocol in scanner[self.ip_addr].all_protocols():
            self.protocols.append(protocol)

            ports = scanner[self.ip_addr][protocol].keys()
            for port in ports:
                state = results["scan"][self.ip_addr][protocol][port]["state"]
                self.open_ports[port] = state





