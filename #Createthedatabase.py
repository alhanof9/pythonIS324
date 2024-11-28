# #Createthedatabase
import sqlite3
import hashlib

conn=sqlite3.connect("test.db")




conn.execute('''CREATE TABLE IF NOT EXISTS workshop
(ID INT(5) PRIMARY KEY NOT NULL,
Name TEXT NOT NULL,
Location CHAR,
Date DATE,
Time CHAR,
Capacity INT,
numberOfBook INT);''')


conn.execute('''CREATE TABLE IF NOT EXISTS booked
(
StuID      INT(9),
workshopID INT(9) ,
PRIMARY KEY(StuID,workshopID),
FOREIGN KEY(StuID) REFERENCES student(StuID) ,
FOREIGN KEY(workshopID) REFERENCES workshop(ID) );''')

conn.execute('''CREATE TABLE IF NOT EXISTS user_info
(FristName CHAR,
LastName CHAR,
 ID INT(9) PRIMARY KEY NOT NULL,
password CHAR NOT NULL,
email CHAR,
phonNumber CHAR  );''')

hashpass = hashlib.sha256("areej1".encode()).hexdigest()

##admin
# conn.execute("INSERT INTO  user_info(FristName,LastName,ID,password,email,phonNumber) VALUES(?,?,?,?,?,?)",
#                         ("areej", "AbdulJabbar", 123456789, hashpass, "areej111@gmail.com", "0555555555"))



             

# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (1, 'Python', 'Riyadh-Aziziyah-building 5', '2025-01-02', '10:00AM', 2,0)''')

# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (2, 'Java', 'Jeddah-AlBalad-building 6', '2025-01-03', '11:00AM', 4,0)''')

# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (3, 'Javascript', 'Riyadh-AL Olaya-building 1', '2025-01-10', '8:00AM', 5,0)''')

# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (4, 'C++', 'Riyadh-AL Olaya-building 1', '2025-01-09', '8:00AM', 5,0)''')
# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (5, 'C', 'Riyadh-AL Olaya-building 1', '2024-11-28', '8:00AM', 5,0)''')
#
# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity,numberOfBook)
#                  VALUES (6, 'HTML', 'Riyadh-AL Olaya-building 1', '2024-11-27', '8:00AM', 5,0)''')


conn.commit()
conn.close()

