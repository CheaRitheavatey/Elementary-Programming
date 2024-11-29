import tkinter as tk
from tkinter import messagebox
class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text='Your Message',font=('Arial',13))
        self.label.pack(padx=10,pady=10)
        
        self.textbox = tk.Text(self.root,height=5,font=('Arial',13))
        self.textbox.pack(padx=10,pady=10)

        self.checkstate = tk.IntVar()

        self.check = tk.Checkbutton(self.root,text='Show message on another frame',variable=self.checkstate)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text='button',command=self.showMessage, activebackground='pink')
        # active background is changing the color of the button when press
        self.button.pack()

        # button to clear the content inside textbox
        self.clearbutton = tk.Button(self.root,text='Clear',command=self.clear)
        self.clearbutton.pack(padx=10,pady=10)
        self.entry = tk.Entry(self.root)
        self.entry.bind("<KeyPress>",self.enter) # when press enter it will show a message
        self.entry.pack(padx=10,pady=10)

        self.menubar = tk.Menu(self.root)

        # one small menu inside big menu bar
        self.smallmenu = tk.Menu(self.menubar,tearoff=0)
        self.smallmenu2 = tk.Menu(self.menubar,tearoff=0)

        self.smallmenu.add_command(label='close',command=self.closing)
        self.smallmenu.add_separator()
        self.smallmenu.add_command(label='close A',command=exit)
        
        # another small menu inside big menu bar
        self.action = tk.Menu(self.menubar,tearoff=0)
        self.action.add_command(label='Show message',command=self.showMessage)

        
        # add the menurbar to the root
        self.root.config(menu=self.menubar)
        self.menubar.add_cascade(menu=self.smallmenu, label='Small Menu 1')
        self.menubar.add_cascade(menu=self.action, label='Actions')
        self.root.protocol("WM_DELETE_WINDOW",self.closing) # when press the x button it will do sth in this case i want to ask user if they sure they want to close it
        self.root.mainloop()
    def showMessage(self):
        if self.checkstate.get() == 0: # .get() is to get the input form the checkbox if i check the box it will show 1 on the terminal and if i dont check the box then it will show 0 on the terminal
            print(self.textbox.get('1.0',tk.END)) # print from the beginning till the end
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0',tk.END))

    def enter(self,event):
        if event.keycode == 13 and event.keysym == 'Return':
            messagebox.showinfo(message=self.entry.get())
    
    def closing(self):
        if messagebox.askyesno(title='Quit?', message="Are you sure?"):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0',tk.END)
MyGui()