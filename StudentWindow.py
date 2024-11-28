import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import logging
import datetime
uid1 = ""


class StudentWindow:
    def __init__(self, userID):
        self.root = tk.Tk()
        self.uid1 = userID
        self.root.title("Student Window")
        self.root.geometry("800x600")
        logging.basicConfig(filename="Transactions.log", filemode='a', format="%(asctime)s - %(message)s",
                            level=logging.INFO)

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
        self.root.destroy()
        from SignUp_GUI import SignUp_GUI

    def setup_book_tab(self):
        # Workshop list
        self.workshop_list = ttk.Treeview(self.book_tab, columns=("ID", "Name", "Location", "Date", "Time"),
                                          show="headings")
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
        self.book_button = tk.Button(button_frame, bg="light blue", height=1, width=25, text="Book",
                                     font=('Times New Roman', 15), command=self.book_workshop)
        self.book_button.pack(side="left", padx=10)

        # Logout Button
        self.logout_button = tk.Button(button_frame, bg="light blue", height=1, width=25, text="Logout",
                                       font=('Times New Roman', 15), command=self.logout)
        self.logout_button.pack(side="left", padx=10)

    def setup_view_tab(self):
        # view workshops list
        self.my_workshop_list = ttk.Treeview(self.view_tab, columns=("Name", "Location", "Date", "Time"),
                                             show="headings")
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

    # workshop data from the database
    def load_workshops(self):
        conn = sqlite3.connect("test.db")
        ## the database is empty so just for testing I am going to fill it ##

        # The actual code for the method
        conn = sqlite3.connect("test.db")
        select = conn.execute("SELECT ID,Name,Location,Date,Time from workshop")
        count = 0
        for row in select:
            self.workshop_list.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
            count += 1
        conn.close()

    def book_workshop(self):
        try:
            conn = sqlite3.connect('test.db')
            c = conn.cursor()
            # workshop id & Student_ID
            selectedworkshop = self.workshop_list.selection()[0]
            reco = self.workshop_list.item(selectedworkshop)['values']
            workshop_ID = str(self.workshop_list.item(selectedworkshop)['values'][0])

            # insert and check if id is exist

            id = c.execute(
                f"SELECT  booked.workshopID,Name,Location,Date,Time from user_info,workshop,booked where user_info.ID=booked.StuID and workshop.ID=booked.workshopID and booked.StuID= {self.uid1} and booked.workshopID={workshop_ID}")
            if len(id.fetchall()) == 0:
                id = c.execute(f"SELECT Capacity from  workshop where ID = {workshop_ID} and Capacity != 0")
                if len(id.fetchall()) == 0:
                    messagebox.showinfo("Book faild", "No more Booking Available")
                else:
                    sql = """INSERT INTO booked VALUES('{}','{}')
                    """.format(self.uid1, workshop_ID)
                    c.execute(sql)
                    c.execute(
                        f"UPDATE workshop set Capacity = Capacity-1, numberOfBook=numberOfBook+1 where  ID={workshop_ID}")
                    conn.commit()
                    messagebox.showinfo("Booking Succeed", "Your booking has been registered")
                    self.log_transaction(reco, "Succeed")


            else:
                messagebox.showinfo("Booking Fail", "this event already booked")
                self.log_transaction(reco, "Fail")
                conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")
            self.log_transaction(reco, "Fail")

    def show_my_workshops(self):
        current_date=datetime.datetime.now().strftime("%Y-%m-%d")
        for item in self.my_workshop_list.get_children():
            self.my_workshop_list.delete(item)
        conn = sqlite3.connect("test.db")
        workshop = conn.execute(
            f"SELECT booked.workshopID,Name,Location,Date,Time from workshop,user_info,booked where user_info.ID=booked.StuID and workshop.ID=booked.workshopID and booked.StuID= {self.uid1} and Date>='{current_date}' ORDER BY Date ASC")
        count = 0
        for row in workshop:
            self.my_workshop_list.insert(parent='', index=count, text='',
                                         values=(row[0], row[1], row[2], row[3], row[4]))
            count += 1

        conn.close()

    def log_transaction(self, rec, status):
        log_message = f"User ID: {self.uid1}, Workshop Name: {rec[1]}, Location: {rec[2]}, " \
                      f"Reservation Date: {rec[3]},Reservation Time:{rec[4]}, Status: {status}"

        logging.info(log_message)

StudentWindow1=StudentWindow("444200934")












