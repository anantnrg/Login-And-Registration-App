# Imports
from tkinter import *
from tkinter import messagebox
import sqlite3

# Make Window
loginApp = Tk()
loginApp.title("Login App")
loginApp.geometry("340x150")
loginApp.eval('tk::PlaceWindow . center')

# Variables
input_passwd = ""
input_username = ""


# Functions
def check_credentials():
    input_username = txtbox_username.get()
    input_passwd = txtbox_password.get()
    conn = sqlite3.connect('user_creds.db')
    c = conn.cursor()
    c.execute("SELECT usr_name FROM users WHERE usr_name =  ? AND usr_passwd = ?" ,(input_username,input_passwd))
    data = c.fetchone()

    if data is None:
        messagebox.showerror("Incorrect Password", "You have entered an incorrect password. Please correct it.")
    else:
        messagebox.showinfo("Login successfull", "Your Login is successfull")
        loginApp.destroy()


    conn.commit()
    conn.close()


lbl_1 = Label(loginApp, text="")
lbl_2 = Label(loginApp, text="")
lbl_username = Label(loginApp, text="Username", padx=10, pady=5)
lbl_password = Label(loginApp, text="Password", padx=10, pady=20)
txtbox_username = Entry(loginApp, width=30)
txtbox_password = Entry(loginApp, width=30, show="*")
btn_login = Button(loginApp, text="Login", command=check_credentials)
btn_cancel = Button(loginApp, text="Cancel")

lbl_1.grid(row=0, column=0)
lbl_2.grid(row=0, column=4)
lbl_username.grid(row=3, column=1)
lbl_password.grid(row=5, column=1)
txtbox_username.grid(row=3, column=4)
txtbox_password.grid(row=5, column=4)
btn_cancel.grid(row=10, column=3)
btn_login.grid(row=10, column=4)

loginApp.mainloop()
