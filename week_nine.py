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
for line in myfile:
    print(line) 

print(myfile.close())