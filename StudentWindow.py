import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

class StudentWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Window")
        self.root.geometry("800x600")

        # Tabs for Book a workshop and View my workshops
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)
        self.book_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.book_tab, text="Book a Workshop")
        self.view_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.view_tab, text="View My Workshops")

        self.setup_book_tab()
        self.setup_view_tab()

        self.root.mainloop()
        
    # Return to signup window
    def logout(self):
        from SignUp_GUI import SignUp_GUI

    def setup_book_tab(self):
        # Workshop list
        self.workshop_list = ttk.Treeview(self.book_tab, columns=("ID", "Name", "Location", "Date", "Time"), show="headings")
        self.workshop_list.heading("ID", text="Workshop ID")
        self.workshop_list.heading("Name", text="Name")
        self.workshop_list.heading("Location", text="Location")
        self.workshop_list.heading("Date", text="Date")
        self.workshop_list.heading("Time", text="Time")
        self.workshop_list.pack(fill="both", expand=True)

        self.load_workshops()


        button_frame = tk.Frame(self.book_tab)
        button_frame.pack(pady=10)

        # Book Button
        self.book_button = tk.Button(button_frame, text="Book", command=self.book_workshop)
        self.book_button.pack(side="left", padx=10)

        # Logout Button
        self.logout_button = tk.Button(button_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side="left", padx=10)
        
    def setup_view_tab(self):
        # view workshops list
        self.my_workshop_list = ttk.Treeview(self.view_tab, columns=("Name", "Location", "Date", "Time"), show="headings")
        self.my_workshop_list.heading("Name", text="Name")
        self.my_workshop_list.heading("Location", text="Location")
        self.my_workshop_list.heading("Date", text="Date")
        self.my_workshop_list.heading("Time", text="Time")
        self.my_workshop_list.pack(fill="both", expand=True)

        button_frame = tk.Frame(self.view_tab)
        button_frame.pack(pady=10)

        # Show Button
        self.show_button = tk.Button(button_frame, text="Show", command=self.show_my_workshops)
        self.show_button.pack(side="left", padx=10)
        # Logout Button
        self.logout_button = tk.Button(button_frame, text="Logout", command=self.logout)
        self.logout_button.pack(side="left", padx=10)



     #workshop data from the database
    def load_workshops(self):
        conn = sqlite3.connect("test.db")
       # the database is empty so just for testing I am going to fill it ##

        # conn.execute('''INSERT INTO workshop (ID,Name,Location,Date,Time,Capacity)
        #             VALUES(1,'Python','Riyadh-Aziziyah-building 5','2-1-2025','10:00AM',2)''')
        
        # conn.execute('''INSERT INTO workshop (ID,Name,Location,Date,Time,Capacity)
        #                   VALUES(2,'Java','Jeddah-AlBalad-building 6','3-1-2025','11:00AM',4)''')
        # conn.execute('''INSERT INTO workshop (ID,Name,Location,Date,Time,Capacity)
        #                          VALUES(3,'Javascript','Riyadh-AL Olaya-building 1','10-1-2025','8:00AM',5)''')
        # conn.commit()
        # conn.close()

        # The actual code for the method
        conn = sqlite3.connect("test.db")
        select = conn.execute("SELECT ID,Name,Location,Date,Time from workshop")
        count=0
        for row in select:
            self.workshop_list.insert(parent='',index=count,text='',values=(row[0],row[1],row[2],row[3],row[4]))
            count+=1
        conn.close()

    def book_workshop(self):
        booking_number=0
        conn = sqlite3.connect("test.db")
        capacity = conn.execute("SELECT Capacity from workshop")
        workshop = conn.execute("SELECT ID,Name,Location,Date,Time,Capacity from workshop")
        id = conn.execute("SELECT ID from workshop")

        if self.check_already_booked(workshop,id):
            messagebox.showerror("Error", "You have already booked this workshop.")
        else:
         messagebox.showinfo("Success", "Workshop booked successfully!")

        conn.close()
    def check_already_booked(self, workshop,id):
        conn = sqlite3.connect("test.db")
        view_id = conn.execute("SELECT ID from view")
        ID = {}
        r=workshop.fetchone()
        for row in view_id:
            ID[row[0]] = row[1]

        idWS = id
        if idWS in ID:
            messagebox.showinfo("warning", "You already booked this workshop ")
        if idWS not in ID:
            return

    def show_my_workshops(self):
        conn = sqlite3.connect("test.db")
        workshop = conn.execute("SELECT ID,Name,Location,Date,Time from workshop")
        count = 0
        for row in workshop:
            self.my_workshop_list.insert(parent='', index=count, text='',
                                         values=(row[0], row[1], row[2], row[3], row[4]))
            count += 1

        conn.close()







stu=StudentWindow()








