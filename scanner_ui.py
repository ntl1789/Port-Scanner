from tkinter import ttk, Tk
import scan_data

class ScannerApp():

    def __init__(self):
        self.window = Tk()
        self.window.title("Network Scanner")

        self.scan_button = ttk.Button(text="Scan Your Machine", command=scan_data.do_scan)
        self.scan_button.grid(row=0, column=0)

        self.scan_complete = ttk.Label(text="")

        self.window.mainloop()