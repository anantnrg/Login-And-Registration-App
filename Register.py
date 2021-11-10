from tkinter import *
import pickle
import sqlite3
import datetime
from tkinter import messagebox

# Make window
regApp = Tk()
regApp.title("Add New User")
regApp.geometry("400x180")
regApp.eval('tk::PlaceWindow . center')

# variables  

full_name = ""
usr_name = ""
usr_passwd = ""
usr_passwd_confirm = ""

### Functions
# Save credentials
global usr_id
usr_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') 

def check_not_blank():
	if txtbox_usr_name.get() == "" and txtbox_usr_passwd.get() == "" and txtbox_full_name.get() == "":
		messagebox.showerror("No credentials", "No username, password or full name was given. Please enter the correct credentials.")
	else:
		check_both_passwds()

def check_both_passwds():
	if txtbox_usr_passwd.get() == txtbox_usr_passwd_confirm.get():
		save_credentials()
	else:
		messagebox.showerror("Password Error", "The entered passwords are not the same. Please enter the correct passwords in both fields.")

def save_credentials():
	conn = sqlite3.connect('user_creds.db')
	c = conn.cursor()
	
	c.execute("INSERT INTO users VALUES (:usr_code, :full_name,:usr_name, :usr_passwd)",
			{
				'usr_code' : usr_id,
				'full_name' : txtbox_full_name.get(),
				'usr_name' : txtbox_usr_name.get(),
				'usr_passwd' : txtbox_usr_passwd.get()

			})
	conn.commit()
	conn.close()



def show_users():
	conn = sqlite3.connect('user_creds.db')
	c = conn.cursor()
	c.execute("SELECT * FROM users")
	data = c.fetchall()
	print(data)
	conn.commit()
	conn.close()


#### WIDGETS
# Labels
lbl_full_name = Label(regApp, text="Full Name", padx=60, pady=5)
lbl_usr_name = Label(regApp, text="User Name", padx=60, pady=5)
lbl_usr_passwd = Label(regApp, text="Password", padx=60, pady=5)
lbl_usr_passwd_confirm = Label(regApp, text="Confirm Password", padx=60, pady=5)

# Entries
txtbox_full_name = Entry(regApp, width=20)
txtbox_usr_name = Entry(regApp, width=20)
txtbox_usr_passwd = Entry(regApp, width=20, show="*")
txtbox_usr_passwd_confirm = Entry(regApp, width=20, show="*")

# Buttons
btn_ok = Button(regApp, text="Save", pady=10, padx=20, width=10, command=check_not_blank)
btn_show_users = Button(regApp, text="Show users", pady=10, padx=20, width=10, command=show_users)



# Shove it on the screen
lbl_full_name.grid(column=2, row=2)
lbl_usr_name.grid(column=2, row=4)
lbl_usr_passwd.grid(column=2, row=6)
lbl_usr_passwd_confirm.grid(column=2, row=8)

txtbox_full_name.grid(column=6, row=2)
txtbox_usr_name.grid(column=6, row=4)
txtbox_usr_passwd.grid(column=6, row=6)
txtbox_usr_passwd_confirm.grid(column=6, row=8)

btn_ok.grid(column=6, row=10)
btn_show_users.grid(column=2, row=10)


regApp.mainloop()
