import tkinter as tk
from tkinter import messagebox 
# write a function add_course that adds a course to a dictionary. the function should include:
# the course name (string)
# the instuctor name (string)
# credit value (integer) that must be between 1 and 6. raise an error if the credits are out of this range
# example
# courses = {}
# add_course(courses, 'Data Science', 'Dr. Smith', 4)
def add_course(courses ,course_name, instructor, credit):
    if not 1 <= credit <= 6:
        raise ValueError("credit must be in range 1-6")
        
    dictionary = {
        'course name': course_name,
        'instructor': instructor,
        'credit': credit
    }

    courses[course_name] = dictionary

course = {}
add_course(course,'data structure', 'joe', 4)
# print(course)

    


# file word count: create a function count_word_in_file(file_path, word) that counts the occurrences of a specific word in a given text file.
# handle possible exception such as filenotfounderror and permissionerror
# count_word_in_file('document.txt', 'python')
def count_word(filepath, word):
    try:
        
        file = open(filepath,'r')
        count = 0
        line = file.readlines()

        for i in range(len(line)):
            if word in line[i].lower():
                count += 1
                print(line[i]) # print the line
                print(i) # print the number of line that have that word
        return count
    except FileNotFoundError:
        print("file cannot be found")
    except PermissionError:
        print("do not have permission")
    except Exception:
        print("Unexpected thing happend")
# print(count_word('log.txt','cannot'))


# develop a small application that asks user for their favorite color. provide a button to submit the answer. 
# if the entry is empty show a warning otherwise display a message confirming their favorite color.
class Favorite_color:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        
        self.root.configure(bg='cyan')

        # label
        self.label = tk.Label(self.root,text="What is your favorite color? ")
        self.label.pack()

        # entry box
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10,pady=10)

        # button
        self.button = tk.Button(self.root,text="Submit",command=self.changecolor)
        self.button.pack()
        self.root.mainloop()
    
    def changecolor(self):
        if self.entry.get() != "":
            self.root.configure(bg=f'{self.entry.get().lower()}')
            messagebox.showinfo('submitted',f'your answer is {self.entry.get()}') 
            
        else:
            messagebox.showwarning('warning', 'cannot be empty')
# Favorite_color()

# --------------------------------------------------------------------------------------------------------
# exercise 1: student record management
# create a function add_student(students, name, age, grade) to add a student record to a dictionary. 
# the name is string
# the age is an integer between 5 and 18
# the grade is a float between 0.0 and 100.0 raise an error if any of these conditions are not met
# students = {}
# add_student(students, 'Alice', 16, 88.5)
def add_student(students, name, age, grade):
    if not 5 <= age <= 18:
        raise ValueError("age must be between 5 and 18")
    
    dictionary = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students[name] = dictionary
students = {}
add_student(students, 'Alice', 16, 88.5)
# print(students)

# exercise 2: write a function analyze_log_file(filepath) that read a log file and print each line that contain the word warning along with its line number. handle potential file access errors
# example, analyze_log_file('server.log')

def analyze_file(filepath):
    try:
        file = open(filepath, 'r')
        lines = file.readlines()
        for i in range(len(lines)):
            if 'warning' in lines[i].lower():
                print(f"the word 'warning' is found in line {i} and the whole line is: {lines[i]}")
        else:
            print("The word warning is not found")
    except FileNotFoundError:
        print("file not found")
    except Exception:
        print("Error")

# analyze_file('log.txt')
# exercise 3: basic calculator gui: create a tkinter application that acts as a basic calculator for addition. the gui should have two entry field for numbers and a button to calculate their sum. display the result in a message box.
        
# --------------------------------------------------------------------------------------------------------------------
# exercise 1: develop a function add_item(inventory, item_name, quantity, price) that adds an item to an inventory dictionary. 
# ensure the item name is a string, the quanity is a positive integer. 
# the price is a float greater than zero. 
# raise an error if any of these condition are violated.
# inventory = {}
# add_item(inventory, 'Apples', 50, 0.5)

def add_item(inventory, item_name, quanity, price):
    try: 
        dict = {
            'item name': item_name,
            'quanity': quanity,
            'price': price
        }

        inventory[item_name] = dict
    except ValueError:
        print("Value error")
    except Exception:
        print("exception error")

inventory = {}
add_item(inventory, 'book', 2, 1200)
print(inventory)



# exercise 2: write a function read_line(filepath) that reads and prints lines from a file. if the file cannot be read, handle and print appropriate error messages for filenotfounderror and ioerror
# example read_lines('data.txt')
def read_line(filepath):
    try:
        file = open(filepath,'r')
        print(file.read())
    except Exception as e:
        print(type(e))

# read_line('log.txt')

# exercise 3: user input gui: create a tkinter application that prompts the user to enter their age. 
# if the input is not a valid intefer or is negative show a warning, 
# otherwise display a message comfirming their age.

class Age:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x200")
        self.root.configure(bg='pink')

        self.label = tk.Label(self.root, text="what is your age? ")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, command=self.printage, text='submit')
        self.button.pack(fill='x')

        self.root.mainloop()

    def printage(self):
        try:
            if self.entry.get() != "":
                answer = int(self.entry.get())
                messagebox.showinfo('Your age', f"you enter {answer}")
            else:
                messagebox.showwarning('warning', 'cannnot be empty')
        except ValueError:
            messagebox.showwarning('warning', 'please enter number')
        except Exception as e:
            print(type(e))
Age()
