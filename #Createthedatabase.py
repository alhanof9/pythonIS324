#Createthedatabase
import sqlite3

conn=sqlite3.connect("test.db")


conn.execute('''CREATE TABLE INFO
(ID INT(9) PRIMARY KEY NOT NULL,
password CHAR NOT NULL);''')

conn.close()
