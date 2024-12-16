import tkinter as tk
from tkinter import messagebox 
import os
"""
exercise about nested dictionary START
"""
# EXERCISE 1

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


# EXERCISE 2

# student record management
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


# EXERCISE 3
# develop a function add_item(inventory, item_name, quantity, price) that adds an item to an inventory dictionary. 
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


# EXERCISE 4
def add_student_grades(students, student_name, subject, grade):
    # Check if the student already exists in the dictionary
    if student_name not in students:
        students[student_name] = {}  # Create a new dictionary for the student
    
    # Add or update the subject grade for the student
    students[student_name][subject] = grade

def get_student_average(students, student_name):
    # Check if the student exists
    if student_name in students:
        grades = students[student_name].values()  # Get all grades for the student
        return sum(grades) / len(grades)  # Calculate and return the average
    else:
        return None  # Student not found

# Example Usage
students = {}
add_student_grades(students, 'Alice', 'Math', 85)
add_student_grades(students, 'Alice', 'Science', 90)
add_student_grades(students, 'Bob', 'Math', 75)

print(get_student_average(students, 'Alice'))  # Output: 87.5
print(get_student_average(students, 'Bob'))    # Output: 75.0
print(get_student_average(students, 'Charlie'))  # Output: None


# exercise 6
# Create a nested dictionary to represent a library system where each category of books contains a list of books with their details.

# Structure:
# The outer dictionary will have categories as keys (e.g., "Fiction", "Non-Fiction", "Science").
# Each category will have a list of books, where each book is represented as a dictionary containing:
# title: The title of the book.
# author: The author of the book.
# year: The year the book was published.
# available: A boolean indicating if the book is available.
def add_book(library, category, title, author, year):
    if category not in library:
        library[category] = []  # Create a new list for the category if it doesn't exist
    
    book = {
        'title': title,
        'author': author,
        'year': year,
        'available': True  # Set the book as available by default
    }
    
    library[category].append(book)

# nested dictionary


def remove_book(library, category, title):
    if category in library:
        library[category] = [book for book in library[category] if book['title'] != title]

def list_books(library, category):
    if category in library:
        return library[category]
    else:
        return []

def check_availability(library, category, title):
    if category in library:
        for book in library[category]:
            if book['title'] == title:
                return book['available']
    return None

# Example Usage
library = {}

add_book(library, 'Fiction', 'The Great Gatsby', 'F. Scott Fitzgerald', 1925)
add_book(library, 'Fiction', '1984', 'George Orwell', 1949)
add_book(library, 'Science', 'A Brief History of Time', 'Stephen Hawking', 1988)

print(list_books(library, 'Fiction'))
print(check_availability(library, 'Fiction', '1984'))
remove_book(library, 'Fiction', '1984')
print(list_books(library, 'Fiction'))

"""
exercise about nested dictionary END
"""

"""
exercise about file START
"""

# EXERCISE 1
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


# EXERCISE 2
# write a function analyze_log_file(filepath) that read a log file and print each line that contain the word warning along with its line number. handle potential file access errors
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

# EXERCISE 3
# write a function read_line(filepath) that reads and prints lines from a file. if the file cannot be read, handle and print appropriate error messages for filenotfounderror and ioerror
# example read_lines('data.txt')
def read_line(filepath):
    try:
        file = open(filepath,'r')
        print(file.read())
    except Exception as e:
        print(type(e))

# read_line('log.txt')

# EXERCISE 4
# replace
def replace_word_in_file(file_path, target_word, replacement_word):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace the target word with the replacement word
        modified_content = content.replace(target_word, replacement_word)

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f"All occurrences of '{target_word}' have been replaced with '{replacement_word}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
file_path = 'example.txt'  # Make sure this file exists
target_word = 'oldword'
replacement_word = 'newword'

replace_word_in_file(file_path, target_word, replacement_word)

# EXERCISE 5
# replace file
def replace_file(source_file_path, target_file_path):
    try:
        # Check if the target file exists
        if os.path.exists(target_file_path):
            os.remove(target_file_path)  # Remove the target file if it exists

        os.rename(source_file_path, target_file_path)  # Rename source to target
        print(f"'{source_file_path}' has been replaced with '{target_file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{source_file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to replace '{target_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
source_file_path = 'source.txt'  # Ensure this file exists
target_file_path = 'target.txt'   # The file you want to replace

replace_file(source_file_path, target_file_path)


# EXERCISE 6
def replace_file_contents(source_file_path, target_file_path):
    try:
        # Read the contents of the source file
        with open(source_file_path, 'r') as source_file:
            content = source_file.read()

        # Write the contents to the target file, replacing its contents
        with open(target_file_path, 'w') as target_file:
            target_file.write(content)

        print(f"Contents of '{target_file_path}' have been replaced with contents from '{source_file_path}'.")

    except FileNotFoundError:
        print(f"Error: One of the files '{source_file_path}' or '{target_file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{target_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example Usage
source_file_path = 'source.txt'  # Ensure this file exists
target_file_path = 'target.txt'   # The file whose contents you want to replace

replace_file_contents(source_file_path, target_file_path)

"""
exercise about file END
"""

"""
exercise about GUI START
"""

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


# EXERCISE 2
# user input gui: create a tkinter application that prompts the user to enter their age. 
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
# Age()

# EXERCISE 3
class ColorScaleExample:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Scale Example")
        self.root.geometry("400x300")

        # Create a frame to display the color
        self.color_frame = tk.Frame(root, width=300, height=200)
        self.color_frame.pack(pady=20)

        # Create scales for Red, Green, and Blue
        self.red_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Red", command=self.update_color)
        self.red_scale.pack(fill=tk.X, padx=20)

        self.green_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=self.update_color)
        self.green_scale.pack(fill=tk.X, padx=20)

        self.blue_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=self.update_color)
        self.blue_scale.pack(fill=tk.X, padx=20)

        # Initial color update
        self.update_color()

    def update_color(self, event=None):
        # Get the current scale values
        r = self.red_scale.get()
        g = self.green_scale.get()
        b = self.blue_scale.get()

        # Update the frame color
        self.color_frame.config(bg=f'#{r:02x}{g:02x}{b:02x}')

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorScaleExample(root)
    root.mainloop()

"""
exercise about GUI END
"""

