from tkinter import *
from tkinter import messagebox

def clear_entrybox():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    password2_entry.delete(0, END)
    savedata_button.config(font=("Helvetica", fontsize), text="Save Data", state=ACTIVE)

def admin_username():
    global file_username
    file_username = open("admin_username.txt", "a")

def admin_password():
    global file_password
    file_password = open("admin_password.txt", "a")

def save_admin_data():
    check_username = open("admin_username.txt", "r")
    check_username2 = check_username.readlines()
    username_list = []
    password_list = []
    admin_username()
    admin_password()
    username_saved = username_entry.get()
    username_list.append(username_saved+"\n")
    password_saved = password_entry.get()
    password_list.append(password_saved+"\n")
    password2_saved = password2_entry.get()
    if password_saved == password2_saved and len(password_saved) > 0 and len(password2_saved)>0 and len(username_saved)>0 and username_saved+"\n" not in check_username2:
        file_username.writelines(username_list)
        file_password.writelines(password_list)
        savedata_button.config(font=("Helvetica", fontsize), text = "Data Saved!", state = DISABLED)
        reset_button.config(state= DISABLED)
        username_list = []
        password_list = []
        file_username.close()
        file_password.close()
    else:
        savedata_button.config(font=("Helvetica", fontsize), text = "INVALID DATA! / USERNAME IS TAKEN \n PRESS RESET FIRST!", state = DISABLED)


fontsize = 12
def admin_register():
    global username_entry, password_entry, password2_entry, savedata_button, reset_button

    register_admin = Toplevel()
    register_admin.after(1, lambda: register_admin.focus_force())

    register_admin.title("Register New Admin")
    username_label = Label(register_admin, text = "Username")
    username_label.grid(row = 1, column = 1, pady = 10, padx = 10, sticky = W)
    username_label.config(font = ("Helvetica", fontsize))
    username_entry = Entry(register_admin, bd = 2)
    username_entry.grid(row = 1, column = 2, pady = 10, padx = 10)

    password_label = Label(register_admin, text = "Password")
    password_label.grid(row = 2, column = 1, pady = 10, padx = 10, sticky = W)
    password_label.config(font=("Helvetica", fontsize))
    password_entry = Entry(register_admin, bd = 2, show = '*')
    password_entry.grid(row = 2, column = 2, pady = 10, padx = 10)

    password2_label = Label(register_admin, text = "Confirm Password")
    password2_label.grid(row = 3, column = 1, pady = 10, padx = 10, sticky =  W)
    password2_label.config(font=("Helvetica", fontsize))
    password2_entry = Entry(register_admin, bd = 2, show = '*')
    password2_entry.grid(row = 3, column = 2, pady= 10, padx = 10)

    savedata_button = Button(register_admin, text = "Save Data", command = save_admin_data)
    savedata_button.grid(row = 4, column = 2, pady = 10, padx = 10)
    savedata_button.config(font=("Helvetica", fontsize))

    reset_button = Button(register_admin, text="Reset", command=clear_entrybox)
    reset_button.grid(row=4, column=1, pady=10, padx=10)
    reset_button.config(font=("Helvetica", fontsize))

    register_admin.bind('<Return>', lambda press_key: save_admin_data())

    register_admin.mainloop()
