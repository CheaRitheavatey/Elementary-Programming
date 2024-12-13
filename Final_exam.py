import tkinter as tk
from tkinter import messagebox
# exercise1 create a function that information to dictionary of subject and it should include the subject name, hours in range 13-78 if not in range raise an error,  
# example addSubject(subjects, 'Elementary Programming', 'Ínformatics' ,50 )

def add_subject(subjects, subject_name, department, hours):
    # Check if hours are in the valid range
    if not (13 <= hours <= 78):
        raise ValueError("Hours must be in the range of 13 to 78.")

    # Create a subject dictionary
    subject_info = {
        'subject_name': subject_name,
        'department': department,
        'hours': hours
    }

    # Add the subject to the subjects dictionary
    subjects[subject_name] = subject_info

# Example usage
subjects = {}

try:
    add_subject(subjects, 'Elementary Programming', 'Informatics', 50)
    print(subjects)
except ValueError as e:
    print(e)

add_subject(subjects, 'Elementary Programming', 'Ínformatics' ,50 )
    
# exercise 2
def check_for_errors_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if "error" in line.lower():
                    print(f"Error found on line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = 'your_file.txt'  # Change this to your file path
check_for_errors_in_file(file_path)

check_for_errors_in_file('log.txt')
# exercise 3
class exercise3:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("200x200")

        # set background color
        self.root.configure(bg="cyan")
        # label
        self.label = tk.Label(self.root, text="2 + 2 = ?")
        self.label.pack()

        # entry
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # button
        self.button = tk.Button(self.root,text="Submit",command=self.submitAnswer)
        self.button.pack(padx=10, pady=10)
        self.root.mainloop()

    def submitAnswer(self):
        try:
            if self.entry.get() != "":
        
                if int(self.entry.get()) == 4:
                    messagebox.showinfo(title="Submitted", message="Your answer is correct")
                elif int(self.entry.get()) != 4:
                    messagebox.showinfo(title="Submitted", message="Your answer is not correct")
            else:
                messagebox.showwarning(title="Warning", message="Cannot be empty")
        except ValueError:
            messagebox.showwarning(title="Warning", message="Please enter a number")
# exercise3()
