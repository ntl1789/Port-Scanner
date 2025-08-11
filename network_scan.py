import nmap
import socket

class ScanResults():
    
    def __init__(self) -> None:
        self.hostname = socket.gethostname()
        self.ip_addr = socket.gethostbyname(self.hostname)
        self.scan_results = None

    def scan_network(self):
        scanner = nmap.PortScanner()
        scanner.scan(self.ip_addr)
        self.scan_results = scanner

    # save scan results to xml?
    # def save_to_xml(self):
    #     xml = dicttoxml.dicttoxml(self.scan_results, attr_type=False) # type: ignore
    #     with open(f"{self.hostname}_scan_results.xml", "w") as file:
    #         file.write(xml) # type: ignore
   

#Add options to add own ip_addr and hostname?