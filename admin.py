from random import randint
import re
import tkinter
import sqlite3
import random
import csv
from tkinter import messagebox
root=tkinter.Tk()



class admin:
    def __init__(self):
        self.main_window = root
        self.main_window.configure()
        self.main_window.title('KSU Workshop')
        self.main_window.geometry('370x470')

        # Frames
        self.topFrame = tkinter.Frame(self.main_window)
        self.workshopnameFrame = tkinter.Frame(self.main_window)
        self.locationFrame = tkinter.Frame(self.main_window)
        self.capacityFrame = tkinter.Frame(self.main_window)
        self.dateFrame = tkinter.Frame(self.main_window)
        self.timeFrame = tkinter.Frame(self.main_window)
        self.bottomFrame = tkinter.Frame(self.main_window)

        # Labels
        self.welcomeLabel = tkinter.Label(self.topFrame, bg="light blue", text="Admin", font=('Times New Roman', 20))
        self.enterInfoLabel = tkinter.Label(self.topFrame, font=('Arial', 10), text="Enter the following:")
        self.workshopnameLabel = tkinter.Label(self.workshopnameFrame, text="Workshop Name", font=('Arial', 10),width=15)
        self.locationLabel = tkinter.Label(self.locationFrame, text="Workshop Location", font=('Arial', 10), width=15)
        self.capacityLabel = tkinter.Label(self.capacityFrame, text="Capacity", font=('Arial', 10), width=15)
        self.dateLabel = tkinter.Label(self.dateFrame, text="Date", font=('Arial', 10), width=15)
        self.timeLabel = tkinter.Label(self.timeFrame, text="Time", font=('Arial', 10), width=15)

        # Entry fields
        self.workshopnameEnter = tkinter.Entry(self.workshopnameFrame, width=30)
        self.locationEnter = tkinter.Entry(self.locationFrame, width=30)
        self.capacityEnter = tkinter.Entry(self.capacityFrame, width=30)
        self.dateEnter = tkinter.Entry(self.dateFrame, width=30)
        self.timeEnter = tkinter.Entry(self.timeFrame, width=30)

        # Buttons
        self.CreateButton = tkinter.Button(self.bottomFrame, bg="light blue", height=1, width=25, text='Create',font=('Times New Roman', 12), command=self.Create)

        self.BackupButton = tkinter.Button(self.bottomFrame, bg="light blue", height=1, width=25, text='Backup',  font=('Times New Roman', 12), command=self.Backup)

        self.LogoutButton = tkinter.Button(self.bottomFrame, bg="light blue", height=1, width=25, text='Logout',   font=('Times New Roman', 12), command=self.logout)


        # Pack items into frames
        self.welcomeLabel.pack(fill='both', ipadx=150, ipady=10)
        self.enterInfoLabel.pack(fill='x', side='left', pady=10, padx=14)

        self.workshopnameLabel.pack(side='left',padx=10)
        self.workshopnameEnter.pack(side= 'left', padx=10)
        self.locationLabel.pack(side='left',padx=10)
        self.locationEnter.pack(side= 'left', padx=10)
        self.capacityLabel.pack(side='left',padx=10)
        self.capacityEnter.pack(side='left',padx=10)
        self.dateLabel.pack(side='left',padx=10)
        self.dateEnter.pack(side='left',padx=10)
        self.timeLabel.pack(side='left',padx=10)
        self.timeEnter.pack(side='left',padx=10)

        # Pack buttons
        self.CreateButton.pack(pady=5)
        self.BackupButton.pack(pady=5)
        self.LogoutButton.pack(pady=5)

        # Pack frames
        self.topFrame.pack()
        self.workshopnameFrame.pack(pady=10)
        self.locationFrame.pack(pady=10)
        self.capacityFrame.pack(pady=10)
        self.dateFrame.pack(pady=10)
        self.timeFrame.pack(pady=10)
        self.bottomFrame.pack(pady=10)

        tkinter.mainloop()

    def Create(self):

        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()

            ID = int(random.randint(10000, 99999))
            Name = str(self.workshopnameEnter.get())
            Location = str(self.locationEnter.get())
            Capacity = (self.capacityEnter.get())

            Date = (self.dateEnter.get())
            #vlidate date
            reangDate="^[0-9]{4}-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$"
            forTastDate= re.search(re.compile(reangDate), Date)
            if not forTastDate:
                messagebox.showinfo("invalid Date format",
                                    "Entred date must be yyyy/mm/dd")
                return
            
             #validate time
            Time = str(self.timeEnter.get())            
            reangTime = "^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
            fortastTime = re.search(re.compile(reangTime), Time)
            if not fortastTime:
                messagebox.showinfo("invalid Time format",
                                    "Entred Time must be in form of hh:MM")
                return
            

            cursor.execute("INSERT INTO workshop(ID, Name,Location,Date,Time,Capacity,numberOfBook) VALUES(?,?,?,?,?,?,?)",(ID, Name,Location,Date,Time,Capacity,0))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Workshop created successfully!")
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("Database Error", f"An error occurred: {e}")
            conn.close()

    def Backup(self):
        tkinter.messagebox.showinfo("Success", "All data has been saved successfully")

        conn = sqlite3.connect("test.db")

        fileCSV= open('backup.cs','w',newline='\n')
        csvwriter=csv.writer(fileCSV)

        csvwriter.writerow(" the all info workshop ".split("_"))
        workshopRows=conn.execute("SELECT * FROM workshop")
        csvwriter.writerows(workshopRows)

        csvwriter.writerow("")
        csvwriter.writerow(" the all info booked ".split("_"))
        bookedRows=conn.execute("SELECT * FROM booked")
        csvwriter.writerows(bookedRows)

        csvwriter.writerow("")
        csvwriter.writerow(" the all info user_info ".split("_"))
        user_infoRows=conn.execute("SELECT * FROM userInfo")
        csvwriter.writerows(user_infoRows)

        fileCSV.close()
        

       



    def logout(self):
        self.main_window.destroy() 
        from KSU_Workshop import SignUp_GUI

gui=admin()