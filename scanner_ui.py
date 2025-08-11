from tkinter import Tk, Button, Canvas, Text, Label
import scan_data
import nmap

class ScannerApp():

    def __init__(self):
        self.root = Tk()
        self.root.title("Network Scanner")
        self.root.config(bg="#FFEAEA")

        self.scan_button = Button(text="Scan Your Machine", width=20)
        self.scan_button.grid(row=0, column=0, padx=20, pady=20)

        self.ip_label = Label(text="Your IP Address: ")
        self.ip_label.grid(row=0, column=1, pady=20)

        self.ip_text = Text(width=30, height=1)
        self.ip_text.grid(row=0, column=2, pady=20)

        self.scan_text = Text()
        self.scan_text.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        self.root.mainloop()