import os
# file handling
myfile = open("file_handling.txt","r") 

# we can also write "xb" just continue what kind if its text (t) or binary (b) when we write "x" its already mean "xt"
# myfile = open("C:\\Users\\Admin\\Desktop\\elementaryProgram.txt","x")


# will create file if its doesnt exist and replace the content inside to write a new one
# myfile = open("file_handling.txt","w") 

# when you want to append something and want to keep whats already inside the file
# myfile = open("file_handling.txt","a") 


# read the content
# print(mifile.read(4)) # put number inside to specify how many char you want to read in that file
# print(mifile.readline())

# write the content
# myfile.write("- recursion problem \n1. give description and ask to write code in recursion (want to see the base case and the recursion steps) fib, triangular number")
# loop through the content inside
# for line in myfile:
    # print(line) 

# remove the file
# os.remove("file_handling.txt")

# check if the file exist or not
# print(os.path.exists("file_handling.txt"))

# print(myfile.close())

# create folder
# os.mkdir("folder")

# delete folder
# os.rmdir("folder")

# practice 1
# create a function to store each line from a file as an item in a list adn removing the white space or any \n from it
def exercise1(path):
    file = open(path)
    contentlist = file.readlines()
    
    # use comprehension list
    newlist = [i.strip() for i in contentlist]

    # normal for loop
    # for i in contentlist:
    #     newlist.append(i.strip())
    file.close()
    return (newlist)

    # if tehy only want to remove just \n from the end then
    # x = i.replace('\n','')

# print(exercise1("file_handling.txt"))


# practice 2
def exercise2():
    list = ["apple", "banana", "cranberry", "durian"]

    if not os.path.exists("file_handling.txt"):
        afile = open("file_handling.txt","x")
    else:
        afile = open("file_handling.txt","w")
    
    for i in list:
        afile.write(i+'\n')
    afile.close()    
    afile = open("file_handling.txt")
    print(afile.read())
    afile.close()

# exercise2()


# practice 3
# read a random line from a file and print it
from random import choice
def exercise3(filepath):
    # another way to open a file is using keyword "with" "with" will open and close automatically but you have to define scope more carefully 
    with open(filepath,'a') as myfile:
        myfile.write("Orange")
    
    myfile = open(filepath)
    list = myfile.readlines()
    random = choice(list).strip()
    myfile.close()
    return random


# print(exercise3("file_handling.txt"))

# practice 4 (not file related)
# ask user for name year of birth and country they are from make sure the year enter is in the correct format (4 digit numbers)
# in case of an inccorect input give user enough information so they know what should they enter
# and program keep asking until it gets the right format after getting the information welcome the user like: welcome name, you were born in year and from country

def exercise4():
    name = input("Enter Name: ")
    country = input("Enter Country: ")

    while True:
        try:
            year = input("Enter Year: ")
            
            if len(str(year)) != 4 or int(year) > 2024:
                print("invalid input year")
                continue
            else:
                year = int(year)
                age = 2024 - year
                print( f"Welcome {name}, You are {age} years old and from {country}")
        except ValueError:
            print("invalid input")
            
# print(exercise4())


# practice 5
# create a function to add user informaiton received from the previous function to the names.txt file if the user with the same year of birth and country doesnt not 
# if the name.txt file couldn not be found create the file and add the user there
# this shouldnt be case sensitive
# keep the writing in the file as it is 
# let the user know if they are added to the file or they were alrady listed
def exercise5():
    dict = {'name': '',
            'year': '',
            'country':''}
    
    if not os.path.exists("names.txt"):
        file = open("names.txt","x")
    else:
        file = open("names.txt", "w")

    for i in dict:    
        file.write(i+' ')
    file.close()

    # append in the last function
   
    exercise4()
    name = ""
    year = 0
    country = ""

    user = f"{name} {year} {country}\n"
    if user in exercise4():
        file = open("names.txt","a")
        file.write(user)
        print("you are added to the list")

exercise5()
