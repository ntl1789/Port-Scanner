#from scanner_ui import ScannerApp
from network_scan import ScanResults
import scan_data

program_on = True
inner_menu = True

while program_on:
    print("This is a simple port scanner to use on your own machine.")
    scan_confirm = int(input("Please choose an option [1 or 2]:\n"
    "[1] Perform a scan\n"
    "[2] Exit\n"))
    if scan_confirm == 1:
        print("Scanning.....")
        scanner_obj = ScanResults()
        scanner_obj.scan_network()
        print("Scan Complete")
        while inner_menu:
            option = int(input("Please choose an option [1, 2, 3 or 4]:\n"
            "[1] View IP address and hostname\n"
            "[2] View open ports\n"
            "[3] View all protocols in use\n" \
            "[4] Exit\n"))
            
            if option == 1:
                print(f"IP address: {scanner_obj.ip_addr}\nHostname: {scanner_obj.hostname}")
            elif option == 2:
                scan_data.open_ports(scanner_obj.scan_results, scanner_obj.ip_addr)
            elif option == 3:
                scan_data.get_protocols(scanner_obj.scan_results, scanner_obj.ip_addr)
            elif option == 4:
                exit_choice = input("Are you sure you want to exit? All scan data will be lost. [yes/no]\n").lower()
                if exit_choice == "yes" or "y":
                    inner_menu = False
                    program_on = False
                else:
                    continue
    elif scan_confirm == 2:
        program_on = False


#TODO: Any functionality to save the scan to a file, then load the data from that file in.
#TODO: Add other scanning functions like protocol versions. 
#TODO: Add error checking, e.g. for value errors. 
#TODO: Create a tkinter GUI for the program. 
#TODO: Allow users to enter their own IP address/hostname, e.g. enter loopback address. 


