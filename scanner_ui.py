from tkinter import Tk, Button, Canvas, Text, Label, END, Entry
import nmap
from network_scan import MachineData

class ScannerApp():

    def __init__(self, machine_obj: MachineData):
        self.root = Tk()
        self.root.title("Network Scanner")
        self.root.config()

        self.scan_button = Button(text="Scan Your Machine", width=20, command=lambda: self.scan(machine_obj)) # type: ignore
        self.scan_button.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        self.progress_label = Label()
        self.progress_label.grid(row=1, column=0, columnspan=2)

        self.ip_label = Label(text="Your IP Address: ")
        self.ip_label.grid(row=2, column=0, pady=20)

        self.ip_entry = Entry(width=30)
        self.ip_entry.grid(row=2, column=1, pady=20, padx=20, sticky="W")

        self.ports = Label(text="Ports:" )
        self.ports.grid(row=3, column=0)
        self.ports_text = Text(height=10)
        self.ports_text.grid(row=3, column=1, pady=20)

        self.os_label = Label(text="Operating Systems Detected: ")
        self.os_label.grid(row=4, column=0)
        self.os_text = Text(height=10)
        self.os_text.grid(row=4, column=1, padx=20, pady=20)

        
        #convernt state to normal before you need to change the text
        

        self.root.mainloop()

  
        


    def scan(self, machine_obj: MachineData):
        self.progress_label.config(text="Scanning....")
        self.progress_label.update_idletasks()
        
        machine_obj.initial_scan(1, 1000)

        self.progress_label.config(text="Done")

        self.ip_entry.insert(END, machine_obj.ip_addr)
        self.ip_entry.config(state="readonly")

        self.ports_text.insert(END, str(machine_obj.open_ports))
        self.ports_text.config(state="disabled")

        self.os_text.insert(END, str(machine_obj.os_list))
        self.os_text.config(state="disabled")

        self.scan_button.config(state="disabled")
