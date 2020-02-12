import sqlite3

conn = sqlite3.connect("midway.db")

cur = conn.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS registration(name text,address text,gender text,marital_status text,class_duration text,time_reference text,date_registered text)")

cur.execute("INSERT INTO registration VALUES('Modou Lamin Jatta','Wellingara','Male','Single','One Week','9AM','28/Jan/20')")

cur.execute("CREATE TABLE IF NOT EXISTS logins(username text,password text)")

cur.execute("CREATE TABLE IF NOT EXISTS admins(name text,surname text,contact integer,address text,username text,password text)")

cur.execute("INSERT INTO admins VALUES('midway','driving school',7933540,'manjai','midwaydrivingschool3@gmail.com','kanaland123')")

#names = "modou"
#santa = "jatta"
#
#cur.execute("INSERT INTO admins (name,surname) VALUES (?,?)",(names,santa))

conn.commit()

conn.close()


