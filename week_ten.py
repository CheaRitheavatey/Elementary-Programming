# GUI
import tkinter as tk

# one variable for frame
root = tk.Tk() # create a frame or window 
root.geometry("500x500") # width and height of the window
root.title("TITLE") #set title

# another variable for label
label = tk.Label(root, text="Hello world",font=('Arial',12)) # set label
label.pack(padx=20, pady=20) # basically put it in root or window and can also paste in padding 

# another variable for textbox
textbox = tk.Text(root, height=3,font=('Arial',13)) # specify where is the textbox located obviously its in root, then set height or font 
textbox.pack()

# another variable for entry. it also similar to textbox
entry = tk.Entry(root)
entry.pack(padx=10)

# another variable for button
button = tk.Button(root, text="Enter",font=('Arial',13))
button.pack(padx=10,pady=10)

# muliltple button in grid like calculator
buttonframe = tk.Frame(root) # use .Frame(root)
buttonframe.columnconfigure(0,weight=1) # if there are 10 button then you have to write it again and again 0 times
buttonframe.columnconfigure(1,weight=1) # the 0,1,2... is the col
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe,text='1',font=('Arial',13))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E) # where this btn1 is located

btn2 = tk.Button(buttonframe,text='2',font=('Arial',13))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E) # tk.W + tk.E is do make sure that the button stretch from end of the frame and not in the middle

btn3 = tk.Button(buttonframe,text='3',font=('Arial',13))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E) # where this btn1 is located

btn4 = tk.Button(buttonframe,text='1',font=('Arial',13))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E) # where this btn1 is located

btn5 = tk.Button(buttonframe,text='2',font=('Arial',13))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E) # where this btn1 is located

btn6 = tk.Button(buttonframe,text='3',font=('Arial',13))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E) # where this btn1 is located

# just pack the button frame then it will be all
buttonframe.pack(fill='x') # make sure that it strectch in the x dimension

# we can also use place to make a button as well
button1 = tk.Button(root, text='Button 1')
button1.place(x=200,y=300,height=100,width=100)
root.mainloop() # call the constructor

