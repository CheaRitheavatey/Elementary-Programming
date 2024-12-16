from tkinter import *
#from tkinter import font
from tkinter import colorchooser

def add():
    listbox.insert(listbox.size(), entryBox.get())

    listbox.config(height= listbox.size())
    entryBox.delete(0, END)

def submit(event): #added for event binding
    foodList = []
    #curselection returns the index of the selection
    for i in listbox.curselection():
        foodList.insert(i, listbox.get(i))

    label = Label(window, 
                  text=f"You ordered: {[f for f in foodList]}", 
                  font=("Arista Pro", 20))
    label.pack()

def delete():
    #because of the change of indexes after each delete we loop from end
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    
    listbox.config(height= listbox.size())

def submitScale():
    return Label(window, text=f"Submitted scale value: {scale.get()}").pack()

window = Tk()
#print(font.families())
window.geometry('500x500')
window.title("GUI Practice")

def chooseColor():
    #this will return a range with 1: rgb value 2: hex value
    color = colorchooser.askcolor()
    colorHex = color[1]
    listbox.config(fg=colorHex)
    scale.config(troughcolor=colorHex)



listbox = Listbox(window,
                  bg= "yellow",
                  font=("Arista Pro", 20),
                  width= 12,
                  selectmode= MULTIPLE,
                  activestyle= NONE
                )
listbox.pack()
listbox.insert(0, "Pizza")
listbox.insert(1, "Pasta")
listbox.config(height= listbox.size())

entryBox= Entry(window)
entryBox.pack()

addButton = Button(window, text="Add", command=add).pack()
submitButton = Button(window, text="Submit", command=submit)
submitButton.pack(expand=True)
deleteButton= Button(window, text="Delete", command=delete).pack()

scale = Scale(window,
              from_=100,
              to=0,
              orient="horizontal",
              length=300,
              font=("Candara", 10),
              #showvalue=0,
              tickinterval=10,
              resolution=0.5,
              troughcolor="yellow",
              fg="Lime",
              bg="black")
scale.pack()
#set the default value the scale shows
scale.set((scale["from"]-scale["to"])/2+scale["to"])

scaleButton = Button(window, 
                     text="Submit scale value", 
                     command=submitScale).pack()


Button(window, command= chooseColor, text="Choose Color").pack()

window.bind('<Return>', submit)
submitButton.bind('<Button>', submit)

window.mainloop()