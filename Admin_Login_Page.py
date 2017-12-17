from tkinter import messagebox
from Admin_Register_Page import *
from tkinter import *
from Scan import *
import time

admin_login = Tk()

admin_login.title("Admin Login")
admin_login.minsize(width=200, height=200)
admin_login.maxsize(width=750, height=750)
admin_login.resizable(width=False, height=False)

def login_success():
    admin_login.destroy()
    scan()

def login_failed():
    messagebox.showerror("Alert", "Login Failed! Please Try Again!")


def show():
    uname_clean = []
    psw_clean = []
    file_username = open("admin_username.txt", "r")
    file_password = open("admin_password.txt", "r")
    fu = file_username.readlines()
    fp = file_password.readlines()

    uname=E1.get()
    psw=E2.get()

    for element in fu:
        element = element.strip()
        uname_clean.append(element)

    for element2 in fp:
        element2 = element2.strip()
        psw_clean.append(element2)

    try:
        name_index = uname_clean.index(uname)
        psw_index = psw_clean.index(psw)
        if len(E1.get()) == 0:
            login_failed()
        elif str(name_index) == str(psw_index):
            login_success()
    except ValueError:
        login_failed()

    E1.delete(0, END)
    E2.delete(0, END)


ADMIN = Label(admin_login, text = "WELCOME! PLEASE LOGIN FIRST.\nBINUSIAN Parking System")
ADMIN.config(font=("Helvetica", 16))
ADMIN.grid(row = 1, column = 1, pady = 10, padx = 10, sticky = W)

L1 = Label(admin_login, text="Username")
L1.grid(row = 3, column = 1, pady = 1, padx = 10, sticky = W)
L1.config(font=("Helvetica", 15))
E1 = Entry(admin_login, font=("Helvetica, 20"))
E1.grid(row = 4, column = 1, pady = 1, padx = 10, sticky = W, ipady = 5)


L2 = Label(admin_login, text="Password")
L2.config(font=("Helvetica", 15))
L2.grid(row = 5, column = 1, pady = 1, padx = 10, sticky = W)
E2 = Entry(admin_login, font=("Helvetica, 20"), show = "•")
E2.grid(row = 6, column = 1, pady = 1, padx = 10, sticky = W, ipady = 5)

login = Button(admin_login, text = "LOGIN", font=("Helvetica", 20, "bold"), command = show)
login.grid(row = 7, column = 2,pady=5, padx = 10, sticky = W)

register = Button(admin_login, text = "REGISTER",font=("Helvetica", 14, "bold"), command = admin_register)
register.grid(row = 8, column = 2,pady = 5, padx = 10, sticky = W)


time1 = ''
clock = Label(admin_login, font=('Helvetica', 25, 'bold'))
clock.grid(row = 9, column = 0)
def liveclock():
    global time1, time2
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, liveclock)
liveclock()

admin_login.bind('<Return>', lambda press_key: show())

admin_login.mainloop()
