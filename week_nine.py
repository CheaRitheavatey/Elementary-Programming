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

print(exercise1("file_handling.txt"))
    