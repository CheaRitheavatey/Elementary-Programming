import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Text box to display input and results
textbox = tk.Text(root, height=3, font=('Arial', 13))
textbox.pack()

# Frame for number and operation buttons
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# Function to handle button clicks
def on_button_click(value):
    current_text = textbox.get("1.0", "end-1c")
    textbox.delete("1.0", "end")
    textbox.insert("1.0", current_text + str(value))

# Function to clear the last character (DEL button)
def delete_last_char():
    current_text = textbox.get("1.0", "end-1c")
    textbox.delete("1.0", "end")
    textbox.insert("1.0", current_text[:-1])

# Function to clear all input (AC button)
def clear():
    textbox.delete("1.0", "end")

# Function to evaluate the expression
def calculate():
    try:
        expression = textbox.get("1.0", "end-1c")
        result = eval(expression)  # Evaluate the mathematical expression
        textbox.delete("1.0", "end")
        textbox.insert("1.0", str(result))
    except Exception:
        textbox.delete("1.0", "end")
        textbox.insert("1.0", "Error")

# Add buttons for digits and actions
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('DEL', 3, 0), ('0', 3, 1), ('AC', 3, 2),
]

for (text, row, col) in buttons:
    if text.isdigit():
        btn = tk.Button(buttonframe, text=text, font=('Arial', 13), command=lambda t=text: on_button_click(t))
    elif text == "DEL":
        btn = tk.Button(buttonframe, text=text, font=('Arial', 13), command=delete_last_char)
    elif text == "AC":
        btn = tk.Button(buttonframe, text=text, font=('Arial', 13), command=clear)
    btn.grid(row=row, column=col, sticky=tk.W + tk.E)

buttonframe.pack(fill='x', pady=10)

# Add the "=" button to calculate
btn_equal = tk.Button(root, text="=", font=('Arial', 13), command=calculate)
btn_equal.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
