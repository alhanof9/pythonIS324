import sqlite3

conn=sqlite3.connect("myDataBase.db")


conn.execute('''CREATE TABLE INFO
(FristName CHAR,
LastName CHAR,
 ID INT(9) PRIMARY KEY NOT NULL,
password CHAR NOT NULL,
email CHAR,
phonNumber CHAR  );''')


conn.close()
