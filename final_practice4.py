import tkinter as tk
from tkinter import messagebox
# simple logic form 
class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x200')

        self.name = tk.Label(self.root, text="Name ")
        self.name.pack()

        self.entryName = tk.Entry(self.root)
        self.entryName.pack()

        self.password = tk.Label(self.root, text="Password ")
        self.password.pack(pady=10)

        self.entryPassword = tk.Entry(self.root, show='*')
        self.entryPassword.pack(pady=10)

        self.button = tk.Button(self.root, text='Submit',command=self.submit)
        self.button.pack(pady=10)
        
        self.names = []
        self.passwords = []
        self.root.mainloop()

    def submit(self):
        try:
            if self.entryName.get() != "" and self.entryPassword.get() != "":
                messagebox.showinfo('Submitted', 'Thank You your information has been record has been recorded')
                self.names.append(self.entryName.get().lower())
                self.passwords.append(self.entryPassword.get())

                self.entryName.delete(0,tk.END)
                self.entryPassword.delete(0,tk.END)

                self.loginto()
            else:
                messagebox.showwarning('Warning','Cannot leave the box empty')
        except Exception as e:
            print(type(e))
    def loginto(self):
        
        self.root = tk.Tk()
        self.root.geometry('200x200')
        
        self.root.title('Login form')
        self.name = tk.Label(self.root, text="Name ")
        self.name.pack()

        self.entryName = tk.Entry(self.root)
        self.entryName.pack()

        self.password = tk.Label(self.root, text="Password ")
        self.password.pack(pady=10)

        self.entryPassword = tk.Entry(self.root, show='*')
        self.entryPassword.pack(pady=10)

        self.button = tk.Button(self.root, text='Submit',command=self.checklogin)
        self.button.pack(pady=10)
        self.root.mainloop()
    def checklogin(self):
        if self.name in self.names and self.password == self.passwords:
            index = self.names.index(self.name)
            if self.passwords[index] == self.password:
                messagebox.showinfo('Login', 'You are login!\n Welcome!')
            else:
                messagebox.showinfo('Not Login', 'Incorrect password')
        else: 
            messagebox.showinfo('Not Login', 'Username not found')
           
Login()


# file handling
def file_handling(filepath,word,newword):
    file = open(filepath,'r')
    print(file.read()) #read

    # count a specific word and print that specific line
    count = 0
    lines = file.readlines()
    for i in range(len(lines)):
        if word in lines[i]:
            count += 1
        print(f"count: {count}\nThe line say: {lines[i]}")
    file.close()

    # replace a specific word
    file = open(filepath,'r')
    content = file.read()

    modify = content.replace(word,newword)

    file1 = open(filepath, 'w')
    file1.write(modify)
    file1.close()
    file.close()

    file.open(filepath, 'r')
    print(file.read())
    file.close()

