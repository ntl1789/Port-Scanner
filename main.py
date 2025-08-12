#from scanner_ui import ScannerApp
from network_scan import MachineData

program_on = True
inner_menu = True

while program_on:
    print("This is a simple port scanner to use on your own machine.")
    scan_confirm = int(input("Please choose an option [1 or 2]:\n"
    "[1] Perform a scan\n"
    "[2] Exit\n"))
    if scan_confirm == 1:
        print("Scanning.....")
        machine = MachineData()
        machine.initial_scan(1, 1000)
        print("Scan Complete")
        while inner_menu:
            option = int(input("Please choose an option [1, 2, 3, 4, or 5]:\n"
            "[1] View IP address and hostname\n"
            "[2] View open and filtered ports\n"
            "[3] View all protocols in use\n"
            "[4] View OS detected\n"
            "[5] Exit\n"))
            
            if option == 1:
                print(f"IP address: {machine.ip_addr}\nHostname: {machine.hostname}")
            elif option == 2:
                for key, value in machine.open_ports.items():
                    print(f"{key}: {value}")
            elif option == 3:
                for protocol in machine.protocols:
                    print(protocol)
            elif option == 4:
                for os in machine.os_list:
                    print(os)
            elif option == 5:
                exit_choice = input("Are you sure you want to exit? All scan data will be lost. [yes/no]\n").lower()
                if exit_choice == "yes" or "y":
                    inner_menu = False
                    program_on = False
                else:
                    continue
            else:
                print("Invalid option. Enter a number between 1 and 5.\n")
    elif scan_confirm == 2:
        program_on = False
    else:
        print("Invalid option. Enter either 1 or 2.\n")


#TODO: Any functionality to save the scan to a file, then load the data from that file in.
#TODO: Add other scanning functions like protocol versions. 
#TODO: Add error checking, e.g. for value errors. 
#TODO: Create a tkinter GUI for the program. 
#TODO: Allow users to enter their own IP address/hostname, e.g. enter loopback address. 



