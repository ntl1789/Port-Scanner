from tkinter import Tk, Button, Text, Label, END, Entry, Frame
from network_scan import MachineData

class ScannerApp():

    def __init__(self, machine_obj: MachineData):
        self.root = Tk()
        self.root.title("Network Scanner")
        self.root.config(bg="#FFF2E0", padx=20, pady=20)

        self.border_colour = Frame(bg="#898AC4")
        self.border_colour.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.scan_button = Button(master=self.border_colour, text="Scan Your Machine", bg="#C0C9EE", relief="flat", width=20, command=lambda: self.scan(machine_obj), font=("helvetica", 12, "normal")) 
        self.scan_button.grid(row=0, column=0, pady=1, padx=1)

        self.progress_label = Label(font=("helvetica", 12, "normal"))
        self.progress_label.grid(row=1, column=0, columnspan=2)

        self.ip_label = Label(text="Your IP Address: ", bg="#C0C9EE", font=("helvetica", 12, "normal"))
        self.ip_label.grid(row=2, column=0, pady=20, sticky="E")

        self.ip_entry = Entry(width=30, font=("helvetica", 12, "normal"), relief="flat")
        self.ip_entry.grid(row=2, column=1, pady=20, padx=20, sticky="W")

        self.ports = Label(text="Ports:" , bg="#C0C9EE", font=("helvetica", 12, "normal"))
        self.ports.grid(row=3, column=0, sticky="E")
        self.ports_text = Text(height=10, relief="flat", font=("helvetica", 12, "normal"), width=50)
        self.ports_text.grid(row=3, column=1, pady=20)

        self.os_label = Label(text="Operating Systems: ", bg="#C0C9EE", font=("helvetica", 12, "normal"), )
        self.os_label.grid(row=4, column=0, sticky="E")
        self.os_text = Text(height=10, relief="flat", font=("helvetica", 12, "normal"), width=50)
        self.os_text.grid(row=4, column=1, padx=20, pady=20)

        self.root.mainloop()


    def scan(self, machine_obj: MachineData):
        self.progress_label.config(text="Scanning....")
        self.progress_label.update_idletasks()
        
        machine_obj.initial_scan(1, 1000)

        self.progress_label.config(text="Done")

        self.ip_entry.insert(END, machine_obj.ip_addr)
        self.ip_entry.config(state="readonly")

        port_keys = list(machine_obj.open_ports.keys())
        i = 0
        for value in machine_obj.open_ports.items():
            self.ports_text.insert(END, f"Port: {port_keys[i]}  State: {value[1]}\n")
            i += 1
        self.ports_text.config(state="disabled")

        for os in machine_obj.os_list:
            self.os_text.insert(END, f"{os}\n")
        self.os_text.config(state="disabled")

        self.scan_button.config(state="disabled")
