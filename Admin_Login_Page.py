from tkinter import messagebox
from Admin_Register_Page import *

admin_login = Tk()
admin_login.title("Admin Login")
admin_login.minsize(width=200, height=200)
admin_login.maxsize(width=750, height=750)
admin_login.resizable(width=False, height=False)

def login_success():
    messagebox.showinfo("Welcome", "Login Successful!")

def login_failed():
    messagebox.showerror("Alert", "Login Failed! Please Try Again!")


def show():
    u=E1.get()
    p=E2.get()
    if u == "kenji" and p == "123":
        login_success()
    else:
        login_failed()


ADMIN = Label(admin_login, text = "WELCOME, PLEASE LOGIN FIRST...", font=(500))
ADMIN.pack(side = TOP)

L1 = Label(admin_login, text="Username")
L1.pack(side = LEFT)
E1 = Entry(admin_login, bd=2)
E1.pack(side = LEFT)

L2 = Label(admin_login, text="Password")
#L2.grid(row = 3, column = 0)
L2.pack(side = LEFT)
E2 = Entry(admin_login, bd=2, show="*")
#E2.grid(row = 3, column = 1)
E2.pack(side = LEFT)

login = Button(admin_login, text = "LOGIN", font=(100), command=show)
login.pack(side = BOTTOM)

register = Button(admin_login, text = "REGISTER", font = (100), command = admin_register)
register.pack(side = BOTTOM)

admin_login.mainloop()