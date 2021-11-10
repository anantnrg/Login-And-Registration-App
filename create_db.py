import sqlite3

db = sqlite3.connect('user_creds.db')
c = db.cursor()

c.execute(""" CREATE TABLE users (
			usr_code text,
			full_name text,
			usr_name text,
			usr_passwd text )""")

			
db.commit()
db.close()
