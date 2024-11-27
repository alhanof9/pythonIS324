import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import messagebox
import hashlib
from Student_window import StudentWindow


class SignUp_GUI:

    def __init__(self):

        # gui format
        self.signUp_window = tkinter.Tk()
        self.signUp_window.configure()
        self.signUp_window.title('KSU Workshop')
        self.signUp_window.geometry('370x490')

        # frames
        self.topFrame = tkinter.Frame(self.signUp_window)
        self.nameFrame = tkinter.Frame(self.signUp_window)
        self.idFrame = tkinter.Frame(self.signUp_window)
        self.passwordFrame = tkinter.Frame(self.signUp_window)
        self.emailFrame = tkinter.Frame(self.signUp_window)
        self.phoneFrame = tkinter.Frame(self.signUp_window)
        self.bottomFrame = tkinter.Frame(self.signUp_window)

        # labels
        self.welcomeLabel = tkinter.Label(self.topFrame, bg="light blue", text="Sign up", font=('Times New Roman', 20))
        self.enterInfoLabel = tkinter.Label(self.topFrame, font=('Arial', 10), text="Enter the following:")
        self.FnameLabel = tkinter.Label(self.nameFrame, text="First Name", font=('Arial', 10))
        self.LnameLabel = tkinter.Label(self.nameFrame, text="Last Name", font=('Arial', 10))
        self.idLabel = tkinter.Label(self.idFrame, text="Student ID", font=('Arial', 10))
        self.passwordLabel = tkinter.Label(self.passwordFrame, text="Password", font=('Arial', 10))
        self.emailLabel = tkinter.Label(self.emailFrame, text="Email", font=('Arial', 10))
        self.phoneLabel = tkinter.Label(self.phoneFrame, text="Phone", font=('Arial', 10))
        self.existLabel = tkinter.Label(self.bottomFrame, text="Do you have account already?", font=('Arial', 10),
                                        pady=7)

        # entries
        self.FnameEnter = tkinter.Entry(self.nameFrame, width=12)
        self.LnameEnter = tkinter.Entry(self.nameFrame, width=12)
        self.idEnter = tkinter.Entry(self.idFrame, width=40)
        self.passwordEnter = tkinter.Entry(self.passwordFrame, width=40)
        self.emailEnter = tkinter.Entry(self.emailFrame, width=40)
        self.phoneEnter = tkinter.Entry(self.phoneFrame, width=40)

        # buttons
        self.signUpButton = tkinter.Button(self.bottomFrame, bg="light blue", height=2, width=20, text='Sign up',
                                           font=('Times New Roman', 15), command=self.getInfoFromDBSignUp)
        self.logInButton = tkinter.Button(self.bottomFrame, bg="light blue", height=2, width=20, text='Login',
                                          font=('Times New Roman', 15), command=self.Log_IN)

        # display items
        self.welcomeLabel.pack(fill='both', ipadx=150, ipady=10)
        self.enterInfoLabel.pack(fill='x', side='left', pady=10, padx=14)
        self.FnameLabel.pack(side='left')
        self.FnameEnter.pack(side='left', padx=10)
        self.LnameLabel.pack(side='left')
        self.LnameEnter.pack(side='left', padx=10)
        self.idLabel.pack(side='left', padx=2)
        self.idEnter.pack(padx=10)
        self.passwordLabel.pack(side='left', padx=3)
        self.passwordEnter.pack(padx=10)
        self.emailLabel.pack(side='left', padx=15)
        self.emailEnter.pack(padx=10)
        self.phoneLabel.pack(side='left', padx=14)
        self.phoneEnter.pack(padx=10)
        self.signUpButton.pack()
        self.existLabel.pack()
        self.logInButton.pack()

        # display frames
        self.topFrame.pack()
        self.nameFrame.pack(pady=10)
        self.idFrame.pack(pady=10)
        self.phoneFrame.pack(pady=10)
        self.emailFrame.pack(pady=10)
        self.passwordFrame.pack(pady=10)
        self.bottomFrame.pack(pady=10)

        tkinter.mainloop()

    def Log_IN(self):

        # close sign up window
        self.signUp_window.destroy()

        # gui format
        self.logIn_window = tkinter.Tk()
        self.logIn_window.configure()
        self.logIn_window.title('KSU Workshop')
        self.logIn_window.geometry('370x300')

        # frames
        self.topFrame = tkinter.Frame(self.logIn_window)
        self.idFrame = tkinter.Frame(self.logIn_window)
        self.passwordFrame = tkinter.Frame(self.logIn_window)
        self.bottomFrame = tkinter.Frame(self.logIn_window)

        # labels
        self.welcomeLabel = tkinter.Label(self.topFrame, bg="light blue", text="Login", font=('Times New Roman', 20))
        self.enterInfoLabel = tkinter.Label(self.topFrame, font=('Arial', 10), text="Enter the following:")
        self.idLabel = tkinter.Label(self.idFrame, text="  User ID  ", font=('Arial', 10))
        self.passwordLabel = tkinter.Label(self.passwordFrame, text="Password", font=('Arial', 10))

        # entries
        self.idEnter = tkinter.Entry(self.idFrame, width=40)
        self.passwordEnter = tkinter.Entry(self.passwordFrame, width=40)

        # button
        self.logInButton = tkinter.Button(self.bottomFrame, bg="light blue", height=2, width=20, text='Login',
                                          font=('Times New Roman', 15),
                                          command=self.getInfoFromDBLogIn)  # complete the command

        # display items
        self.welcomeLabel.pack(fill='both', ipadx=150, ipady=10)
        self.enterInfoLabel.pack(fill='x', side='left', pady=10, padx=14)
        self.idLabel.pack(side='left', padx=3)
        self.idEnter.pack(padx=10)
        self.passwordLabel.pack(side='left', padx=3)
        self.passwordEnter.pack(padx=10)
        self.logInButton.pack()

        # display frames
        self.topFrame.pack()
        self.idFrame.pack(pady=10)
        self.passwordFrame.pack(pady=10)
        self.bottomFrame.pack(pady=10)

        tkinter.mainloop()

    def getInfoFromDBSignUp(self):

        # connect to database
        conn = sqlite3.connect("test.db")
        ForTast = conn.execute("SELECT ID ,password FROM Student_INFO")
        IDdec = {}
        for row in ForTast:
            IDdec[row[0]] = row[1]

        # retrieve info
        Fname = self.FnameEnter.get().strip()
        lname = self.LnameEnter.get().strip()
        idDB = self.idEnter.get().strip()
        Pass = self.passwordEnter.get().strip()
        email = self.emailEnter.get().strip()
        phoneNumber = self.phoneEnter.get().strip()

        # check the validation of entries
        if not Fname or not lname or not idDB or not Pass or not email or not phoneNumber:
            messagebox.showwarning("warning", "Please enter all the information")

        elif (Pass.isdigit() or Pass.isalpha() or Pass.isalnum()) and len(Pass) == 6 and len(
                idDB) == 9 and idDB.isdigit():

            if email.endswith('@student.ksu.edu.sa') and len(email) == 27 and phoneNumber.startswith('05') and len(
                    phoneNumber) == 10:
                hashpass = hashlib.sha256(Pass.encode()).hexdigest()
                idDB = int(idDB)

                if idDB in IDdec:
                    messagebox.showinfo("warning", "You already have an account")
                if idDB not in IDdec:
                    conn.execute(
                        "INSERT INTO Student_INFO(FristName,LastName,ID,password,email,phonNumber) VALUES(?,?,?,?,?,?)",
                        (Fname, lname, idDB, hashpass, email, phoneNumber))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Welcome", "Registration completed successfully ")

            elif not (email.endswith('@student.ksu.edu.sa') and len(email) == 27):
                messagebox.showinfo("warning", "Email is wrong (format XXXXXXXX@student.ksu.edu.sa)")
            else:
                messagebox.showinfo("warning", "phone number is wrong (format 05XXXXXXXX)")

        elif not ((Pass.isdigit() or Pass.isalpha() or Pass.isalnum())) and len(Pass) != 6:
            messagebox.showinfo("warning", "Password must be only 6 (letters or numbers)")
        else:
            messagebox.showinfo("warning", "ID must be only 9 digits")

    def getInfoFromDBLogIn(self):

        # connect to database
        conn = sqlite3.connect("test.db")
        ForTast = conn.execute("SELECT ID ,password FROM Student_INFO")
        IDdec = {}
        for row in ForTast:
            IDdec[row[0]] = row[1]

        # retrieve info
        idDB = self.idEnter.get()
        Pass = self.passwordEnter.get()

        # encrypt the password
        hashpass = hashlib.sha256(Pass.encode()).hexdigest()

        # check the validation of entries
        if not idDB or not Pass:
            messagebox.showwarning("warning", "Please enter all the information")

        elif (Pass.isdigit() or Pass.isalpha() or Pass.isalnum()) and len(Pass) == 6 and len(
                idDB) == 9 and idDB.isdigit():
            idDB = int(idDB)
            if idDB not in IDdec:
                messagebox.showinfo("warning", "You do not have an account")
            else:
                if IDdec[idDB] != hashpass:
                    messagebox.showinfo("warning", "The password is wrong")
                else:
                    if idDB == 123456789:
                        messagebox.showinfo("Welcome", "Welcome Admin")
                    else:
                        messagebox.showinfo("Welcome", "Welcome student")
                        self.logIn_window.destroy()
                        StudentWindow(idDB)

        elif not ((Pass.isdigit() and Pass.isalpha() and Pass.isalnum())) and len(Pass) != 6:
            messagebox.showinfo("warning", "Password must be only 6 (letters or numbers)")
        else:
            messagebox.showinfo("warning", "ID must be only 9 digits")

        conn.close()


signUp = SignUp_GUI()
