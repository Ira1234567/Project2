import sqlite3
con = sqlite3.connect('emails.db')
cur = con.cursor()
cur.execute(
   '''CREATE TABLE IF NOT EXISTS emails (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(130), email varchar(30))''')
con.commit()
con.close()