#Createthedatabase
# import sqlite3

# import sqlite3
#
#
# conn=sqlite3.connect("test.db")
# conn.execute('''CREATE TABLE workshop
# (ID INT(9) PRIMARY KEY NOT NULL,
# Name TEXT NOT NULL,
# Location CHAR,
# Date DATE,
# Time CHAR,
# Capacity INT);''')
#
# conn.close()


# import sqlite3
# conn=sqlite3.connect("test.db")
# conn.execute('''CREATE TABLE booked
# (
# StuID      INT(9),
# workshopID INT(9) ,
# PRIMARY KEY(StuID,workshopID),
# FOREIGN KEY(StuID) REFERENCES student(StuID) ,
# FOREIGN KEY(workshopID) REFERENCES workshop(ID) );''')
# conn.close()

# conn.execute('''CREATE TABLE Student_INFO
# (FristName CHAR,
# LastName CHAR,
#  ID INT(9) PRIMARY KEY NOT NULL,
# password CHAR NOT NULL,
# email CHAR,
# phonNumber CHAR  );''')
# conn.close()

# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity)
#                  VALUES (1, 'Python', 'Riyadh-Aziziyah-building 5', '2025-01-02', '10:00AM', 2)''')
#
# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity)
#                  VALUES (2, 'Java', 'Jeddah-AlBalad-building 6', '2025-01-03', '11:00AM', 4)''')
#
# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity)
#                  VALUES (3, 'Javascript', 'Riyadh-AL Olaya-building 1', '2025-01-10', '8:00AM', 5)''')
#
# conn.execute('''INSERT INTO workshop (ID, Name, Location, Date, Time, Capacity)
#                  VALUES (4, 'C++', 'Riyadh-AL Olaya-building 1', '2025-01-09', '8:00AM', 5)''')
#
# conn.commit()
# conn.close()

