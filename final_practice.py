from random import randint
# file handling practice
# task 1: create a python script that writes a list of your favorite movies to a text file, one movie per line.
import os
import tkinter as tk
from tkinter import messagebox
def task1(filepath):
    movies = ["movie1", "movie2", "movie3"]
    myfile = open(filepath, "w")

    # write file
    for i in movies:
        myfile.write(i+'\n')
    
    myfile.close()

    # read file
    myfile = open(filepath, "r")
    print(myfile.read())
    myfile.close()

    # append file
    myfile = open(filepath, 'a')
    myfile.write("movie4"+'\n')
    myfile.close()

    # count line
    myfile = open(filepath, 'r')
    print(len(myfile.readlines()))
    myfile.close()

    # copy a file
    myfile = open(filepath, 'r')
    newfile = open('newfile.txt', 'w')

    for i in myfile.readlines():
        newfile.write(i)
    newfile.close()
    myfile.close()

    # check if file exist
    print(os.path.exists(filepath))

    # exception handling
    try:
        file = open(filepath)
        print(file.read())
    except FileNotFoundError:
        print("File not found")
    finally:
        file.close()

    # file statistic
    file = open(filepath, 'r')
    count = 0
    longest_movie = ""

    for i in file:
        title = i.strip() # remove extra white space
        count += 1
        if len(title) > len(longest_movie):
            longest_movie = title
    
    print(f"Number of movies: {count}")
    print(f"Longest movie: {longest_movie}")

    file.close()

# task1('name.txt')

def task2():
    first_list = []
    second_list = []

    # generate 26 random number
    for i in range(5):
        first_list.append(randint(1,5))
    print(first_list)

    # initial second list length
    second_list = [0] * len(first_list)

    # after generate 5 random number we add the number in fib sequence
    second_list[0] = first_list[0]
    for i in range(len(first_list)-1):
        second_list[i+1] = first_list[i] + first_list[i+1]
    print(second_list) 
        

# task2()

# calculate factorial number
def task3(num):
    # recursive method
    if num == 0 or num == 1:
        return 1
    return num * task3(num-1)

# print(task3(1))

# count the number of word in the text file
def task4(filepath):
    file = open(filepath, 'r')
    # read the file
    text = file.read()
    # split the text and return the length
    count = len(text.split())
    return count

# print(task4("name.txt"))


class todoList:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.geometry("200x200")
        self.tk.title("To Do List")

        # entrybox
        self.entrybox = tk.Entry(self.tk)
        self.entrybox.pack(fill='x', padx=10, pady=10)

        # hold task in list
        self.task = []

        # button
        self.tk.button = tk.Button(self.tk,text= "Add Task",command=self.addTask)
        self.tk.button.pack(padx=10,pady=10,side= "bottom")	  

        self.tk.mainloop()



    def addTask(self):
        if self.entrybox.get() != "":
            # check state of the checkbox
            var = tk.IntVar()
            # checkbox
            checkbox = tk.Checkbutton(self.tk,text=self.entrybox.get(),command=self.check_state,variable=var)
            self.task.append((checkbox,var))
            checkbox.pack(anchor=tk.W, padx=10, pady=10)

            # clear entrybox
            self.entrybox.delete(0,tk.END)
        else:
            messagebox.showwarning("Warning","Please enter a task")

    def check_state(self):
        if all (var.get() == 1 for _,var in self.task):
            messagebox.showinfo("Info","All tasks are done") 
            
todoList() 


