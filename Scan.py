from tkinter import *
from Admin_Register_Page import *
from Karcis import *
import os

def destroyscan():
    scan_id.destroy()
    karcis()

def keluar():
    messagebox.showinfo('See you later!','Bye - Bye')
    exit()

def scan():
    global scan_id

    scan_id = Tk()
    scan_id.after(1, lambda: scan_id.focus_force())
    scan_id.title("Silahkan Scan Binusian Card Anda")
    scan = Button(scan_id, text = "SCAN", command = destroyscan,height = 5, width = 15 )
    scan.grid(row = 1, column = 1,pady =70, padx = 70)
    scan.config(font=("Helvetica", 15))
    scan_id.bind('<Return>', lambda pk: destroyscan())
    exit_button = Button(scan_id, text="EXIT", command=keluar)
    exit_button.grid(row=2, column=1, pady=70, padx=70)
    exit_button.config(font=("Helvetica", 15))
    scan_id.mainloop()
