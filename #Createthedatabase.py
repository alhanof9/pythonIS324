#Createthedatabase
# import sqlite3
#
# conn=sqlite3.connect("test.db")
#
#
# conn.execute('''CREATE TABLE INFO
# (ID INT(9) PRIMARY KEY NOT NULL,
# password CHAR NOT NULL);''')
#
# conn.close()
#
# import sqlite3
#
#
# conn=sqlite3.connect("test.db")
# conn.execute('''CREATE IF NOT EXIST TABLE workshop
# (ID INT(9) PRIMARY KEY NOT NULL,
#  Name TEXT NOT NULL,
#  Location CHAR,
#  Date DATE,
#  Time CHAR,
#  Capacity INT);''')

# conn.close()

# import sqlite3
# conn=sqlite3.connect("test.db")
# conn.execute('''CREATE TABLE view
# (ID INT(9) PRIMARY KEY NOT NULL,
# Name TEXT NOT NULL,
# Location CHAR,
# Date DATE,
# Time CHAR,
# Capacity INT);''')
# conn.close()

# conn.execute('''DROB TABLE INFO;''')
# conn.close()

conn.execute('''CREATE TABLE INFO
(FristName CHAR,
LastName CHAR,
 ID INT(9) PRIMARY KEY NOT NULL,
password CHAR NOT NULL,
email CHAR,
phonNumber CHAR  );''')

