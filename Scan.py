from tkinter import *
from Admin_Register_Page import *
from Karcis import *
import os
def scan():
    def exit():
        os.system('Admin_Register_Page.py')

    global scan_id
    scan_id = Tk()
    scan_id.title("Silahkan Scan Binusian Card Anda")
    scan = Button(scan_id, text = "SCAN", command = karcis,height = 5, width = 15 )
    scan.grid(row = 1, column = 1,pady =70, padx = 70)
    scan.config(font=("Helvetica", 15))
    scan_id.bind('<Return>', lambda pk: karcis())
    exit_button = Button(scan_id, text="LOGOUT", command=exit)
    exit_button.grid(row=2, column=1, pady=70, padx=70)
    exit_button.config(font=("Helvetica", 15))
    scan_id.mainloop()



