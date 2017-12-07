from tkinter import *
username_list = []
password_list = []

def admin_username():
    file_username = open("admin_username.txt", "a")
    file_username.writelines(username_list)

def admin_password():
    file_password = open("password_username.txt", "a")
    file_password.writelines(password_list)

def save_admin_data():
    admin_username()
    admin_password()
    username_saved = username_entry.get()
    #username_list.append(username_saved+"\n")
    password_saved = password_entry.get()
    #password_saved.append(username_saved+"\n")
    savedata_button.config(font=("Helvetica", fontsize), text = "Data Saved!", state = DISABLED)



fontsize = 12
def admin_register():
    global username_entry, password_entry, savedata_button

    register_admin = Tk()
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
    register_admin.mainloop()