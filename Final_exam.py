import tkinter as tk
from tkinter import colorchooser
from random import randint
# exercise 1
def exercise1():
    # conver the tuple into list
    # give 2 tuples
    myTup = (1,3,4)
    myTupp = (1,4,8)

    # convert them into list
    list1 = list(myTup)
    list2 = list(myTupp)

    # add both list into one big list
    list3 = list1+list2
    
    # convert the list into set because set do not allow duplicate
    aset = set(list3)
    
    # convert the set back to tuple
    tupe = tuple(aset)

    # return tuple
    return tupe

print(exercise1())

# exercise 2
# generate 5 random number
def exercise2(filepath):
    list = []
    for i in range(5):
        x = randint(1,90)
        list.append(x)
    print(list)

    # store the list in text file
    file = open(filepath, 'w')
    for i in list:
        file.write(str(i)+'\n')
    file.close()

    # print the chosen number in terminal
    file = open(filepath, 'r')
    print(f"The random number generated: {file.read()}in file")
    file.close()

exercise2('name.txt')
        
# exercise 3
class exercise3:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x200')

        # black background
        self.root.configure(bg='black')

        # button
        self.button = tk.Button(self.root,text='Click here!', command=self.changeColor)

        self.button.pack(pady=10)
        self.root.mainloop()
    
    def changeColor(self):
        # change the color of the button
        self.color = colorchooser.askcolor()
        self.colorHex = self.color[1]
        self.button.configure(background=self.colorHex)
        self.button.pack()


# exercise3()