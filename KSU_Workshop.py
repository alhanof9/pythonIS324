import tkinter
import tkinter.messagebox
class SignUp_GUI:

    def __init__(self):
        #gui format
        self.main_window = tkinter.Tk()
        self.main_window.configure()
        self.main_window.title('KSU Workshop')
        self.main_window.geometry('370x490')

        #frames
        self.topFrame = tkinter.Frame(self.main_window)
        self.nameFrame  = tkinter.Frame(self.main_window)
        self.idFrame = tkinter.Frame(self.main_window)
        self.passwordFrame = tkinter.Frame(self.main_window)
        self.emailFrame = tkinter.Frame(self.main_window)
        self.phoneFrame = tkinter.Frame(self.main_window)
        self.bottomFrame = tkinter.Frame(self.main_window)

        #labels
        self.welcomeLabel = tkinter.Label(self.topFrame, bg= "light blue", text= "Sign up" , font=('Times New Roman', 20))
        self.enterInfoLabel = tkinter.Label(self.topFrame, font=('Arial', 10), text= "Enter the following:")
        self.FnameLabel = tkinter.Label(self.nameFrame, text= "First Name", font=('Arial',10))
        self.LnameLabel = tkinter.Label(self.nameFrame, text= "Last Name", font=('Arial',10))
        self.idLabel = tkinter.Label(self.idFrame, text= "Student ID", font=('Arial',10))
        self.passwordLabel = tkinter.Label(self.passwordFrame, text= "Password", font=('Arial',10))
        self.emailLabel = tkinter.Label(self.emailFrame, text= "Email", font=('Arial',10))
        self.phoneLabel = tkinter.Label(self.phoneFrame, text= "Phone", font=('Arial',10))
        self.existLabel = tkinter.Label(self.bottomFrame, text= "Do you have account already?", font=('Arial',10), pady=7)

        #enter info
        self.FnameEnter = tkinter.Entry(self.nameFrame, width=12)
        self.LnameEnter = tkinter.Entry(self.nameFrame, width=12)
        self.idEnter = tkinter.Entry(self.idFrame, width=40)
        self.passwordEnter = tkinter.Entry(self.passwordFrame, width=40)
        self.emailEnter = tkinter.Entry(self.emailFrame, width=40)
        self.phoneEnter = tkinter.Entry(self.phoneFrame, width=40)

        #buttons
        self.signUpButton = tkinter.Button(self.bottomFrame, bg= "light blue", height=2, width=20, text= 'Sign up', font=('Times New Roman', 15), command='') #complete the command
        self.logInButton = tkinter.Button(self.bottomFrame, bg= "light blue", height=2, width=20, text='Login', font=('Times New Roman', 15), command=self.Log_IN)  # complete the command

        #display items
        self.welcomeLabel.pack(fill='both', ipadx=150, ipady=10)
        self.enterInfoLabel.pack(fill = 'x', side='left', pady=10, padx=14)
        self.FnameLabel.pack(side= 'left')
        self.FnameEnter.pack(side= 'left', padx=10)
        self.LnameLabel.pack(side= 'left')
        self.LnameEnter.pack(side= 'left', padx=10)
        self.idLabel.pack(side= 'left', padx=2)
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

        #display frames
        self.topFrame.pack()
        self.nameFrame.pack(pady=10)
        self.idFrame.pack(pady=10)
        self.phoneFrame.pack(pady=10)
        self.emailFrame.pack(pady=10)
        self.passwordFrame.pack(pady=10)
        self.bottomFrame.pack(pady=10)

        tkinter.mainloop()

    def Log_IN(self):
        self.main_window = tkinter.Tk()
        self.main_window.configure()
        self.main_window.title('KSU Workshop')
        self.main_window.geometry('370x300')

        #frames
        self.topFrame = tkinter.Frame(self.main_window)
        self.idFrame = tkinter.Frame(self.main_window)
        self.passwordFrame = tkinter.Frame(self.main_window)
        self.bottomFrame = tkinter.Frame(self.main_window)


        self.welcomeLabel = tkinter.Label(self.topFrame, bg= "light blue", text= "Login" , font=('Times New Roman', 20))
        self.enterInfoLabel = tkinter.Label(self.topFrame, font=('Arial', 10), text= "Enter the following:")
        self.idLabel = tkinter.Label(self.idFrame, text="          ID", font=('Arial', 10))
        self.passwordLabel = tkinter.Label(self.passwordFrame, text="Password", font=('Arial', 10))

        self.idEnter = tkinter.Entry(self.idFrame, width=40)
        self.passwordEnter = tkinter.Entry(self.passwordFrame, width=40)

        self.logInButton = tkinter.Button(self.bottomFrame, bg= "light blue", height=2, width=20, text='Login', font=('Times New Roman', 10), command='')  # complete the command

        self.welcomeLabel.pack(fill='both', ipadx=150, ipady=10)
        self.enterInfoLabel.pack(fill='x', side='left', pady=10, padx=14)

        self.idLabel.pack(side='left', padx=3)
        self.idEnter.pack(padx=10)
        self.passwordLabel.pack(side='left', padx=3)
        self.passwordEnter.pack(padx=10)
        self.logInButton.pack()

        self.topFrame.pack()
        self.idFrame.pack(pady=10)
        self.passwordFrame.pack(pady=10)
        self.bottomFrame.pack(pady=10)



        tkinter.mainloop()

signUp = SignUp_GUI()
