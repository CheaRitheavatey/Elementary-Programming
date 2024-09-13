# comment: use to explain the code using "#"
"""
comment for long line (instruction)
"""
# variable
x = 1
a,b,c = 2,3,4 # 3 variable have to be 3 value
y = '   yes   '

# basic functions
print(a,y)
print(id(b))
print("hello \"yes\" hello")
print(f"a is {a} ")

# str method
print(y[:])
print(y[2:])
print(y[:4])
print(y.strip())
print(y.rstrip())
print(y.lstrip())
print(y.lower())
print(y.upper())
print(y.replace("y", "Y"))


"""
-----------------------------------------
"""
# name = "joe"
# age = 12
# print(f"{name} is {age} years old")

def calculateAge(year):
     year = int(year)
     return 2024 - year


while(True):
    name = input("Name: ")
    year = input("Year born: ")

    if year.isdigit():
        
        print(f"{name} is {calculateAge(year)} years old")
    else:
        print("enter integer for age")
        continue

    
    break