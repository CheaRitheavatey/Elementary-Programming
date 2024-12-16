import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x200')

        self.name_label = tk.Label(self.root, text="Name ")
        self.name_label.pack()

        self.entryName = tk.Entry(self.root)
        self.entryName.pack()

        self.password_label = tk.Label(self.root, text="Password ")
        self.password_label.pack(pady=10)

        self.entryPassword = tk.Entry(self.root, show='*')
        self.entryPassword.pack(pady=10)

        self.submit_button = tk.Button(self.root, text='Submit', command=self.submit)
        self.submit_button.pack(pady=10)
        
        self.names = []
        self.passwords = []

        self.root.mainloop()

    def submit(self):
        name = self.entryName.get().lower()
        password = self.entryPassword.get()

        if name != "" and password != "":
            self.names.append(name)
            self.passwords.append(password)

            messagebox.showinfo('Submitted', 'Thank you! Your information has been recorded.')

            # Clear the entry fields
            self.entryName.delete(0, tk.END)
            self.entryPassword.delete(0, tk.END)

            # Proceed to login
            self.loginto()
        else:
            messagebox.showwarning('Warning', 'Cannot leave the box empty')

    def loginto(self):
        login_window = tk.Tk()
        login_window.geometry('200x200')
        login_window.title('Login Form')

        name_label = tk.Label(login_window, text="Name ")
        name_label.pack()

        entryName = tk.Entry(login_window)
        entryName.pack()

        password_label = tk.Label(login_window, text="Password ")
        password_label.pack(pady=10)

        entryPassword = tk.Entry(login_window, show='*')
        entryPassword.pack(pady=10)

        login_button = tk.Button(login_window, text='Login', 
                                 command=lambda: self.check_login(entryName.get().lower(), entryPassword.get(), login_window))
        login_button.pack(pady=10)

    def check_login(self, name, password, login_window):
        if name in self.names and password in self.passwords:
            index = self.names.index(name)
            if self.passwords[index] == password:
                messagebox.showinfo('Login', 'You are logged in!\nWelcome!')
                login_window.destroy()  # Close the login window
            else:
                messagebox.showerror('Login Failed', 'Incorrect password.')
        else:
            messagebox.showerror('Login Failed', 'Username not found.')

Login()