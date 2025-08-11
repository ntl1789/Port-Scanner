import nmap
import csv


#create scanner object from PortScanner class
scanner = nmap.PortScanner()

#run scan of loopback address
scanner.scan()
scanner.scan("192.168.56.1", "22-443")

#the data the above line returns is a dict:
scan_results = {
                'nmap': {
                        'command_line': 'nmap -oX - -p 22-443 -sV 127.0.0.1', 
                        'scaninfo': {
                                    'tcp': {
                                            'method': 'syn', 
                                            'services': '22-443'
                                            }
                                    }, 
                        'scanstats': {
                                    'timestr': 'Sun Aug 10 14:22:30 2025', 
                                    'elapsed': '7.69', 
                                    'uphosts': '1', 
                                    'downhosts': '0', 
                                    'totalhosts': '1'
                                    }
                        }, 
                'scan': {
                        '127.0.0.1': {
                                    'hostnames': [
                                                        {
                                                        'name': 'localhost', 
                                                        'type': 'PTR'
                                                        }
                                                ], 
                                    'addresses': {
                                                'ipv4': '127.0.0.1'
                                                }, 
                                    'vendor': {}, 
                                    'status': {
                                                'state': 'up', 
                                                'reason': 'localhost-response'
                                                }, 
                                    'tcp': {
                                                    135: {
                                                            'state': 'open', 
                                                            'reason': 'syn-ack', 
                                                            'name': 'msrpc', 
                                                            'product': 'Microsoft Windows RPC', 
                                                            'version': '', 
                                                            'extrainfo': '', 
                                                            'conf': '10', 
                                                            'cpe': 'cpe:/o:microsoft:windows'
                                                        }, 
                                                    137: {
                                                            'state': 'filtered', 
                                                            'reason': 'no-response', 
                                                            'name': 'netbios-ns', 
                                                            'product': '', 
                                                            'version': '', 
                                                            'extrainfo': '', 
                                                            'conf': '3', 
                                                            'cpe': ''
                                                        }
                                            }
                                    } 
                        }
            }


#After using scanner.scan() can use scanner. methods to get details about the scan
#hosts = scanner.all_hosts()

#After running the initial scan, can use the scanner obj, specify the IP or hostname, then access various methods
hostname = (scanner["192.168.56.1"].hostname)
state = (scanner["192.168.56.1"].state)

#Can translate the scan data to csv format using:
csv_data = scanner.csv()
with open("nmap_results_mine.csv", "w") as file:
    file.write(csv_data)
