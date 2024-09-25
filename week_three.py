import random
# conditional statement - if
"""
a = 8
b = 32
if a > b:
    print("a is bigger than b")
elif a < b:
    print("a is smaller than b")
else: 
    print("a is equal to b")
"""

# ternary operator
# print("a is bigger than b") if a > b else print("a is smaller than b") if a < b else print("a equal to b")

# logical operator: and, or, not
"""
age = 70
if age > 18 and age < 55:
    print("eligible")
elif age < 18 or age >= 55:
    print("not eligible")
"""

# using not
"""
if not (age > 18 and age < 55):
    print("not eligible")
elif not (age < 18 or age >= 55):
    print("eligible")
"""

# pass statement
def abc():
    # enter code here
    pass

 
"""
practice 1

write a program to check whether the number enter by user even or odd
"""
def exercise1():
    # take user input
    # if the input is a number convert that to int, else ask them to enter it again
    # if the input number % 2 == 0 it is an even number, else it an odd number
    while True:
        number = input("enter integer number: ")
        if number.isdigit():
            number = int(number)
        
            if number == 0:
                print("number is 0")
                break

            if number % 2 == 0:
                print(f"{number} is an even number")
            else:
                print(f"{number} is an odd number")
            break
        else:
            print("please enter integer")
            continue

    # ternary
    print("the number is 0") if number == 0 else print(f"{number} is an odd number") if number % 2 != 0 else print(f"{number} is an even number")

"""
practice 2: write a program to check if the last digit of a number entered by user is divisible by 3 or not
"""

def exercise2():
    # take user input
    # if the input is a number convert that to int, else ask them to enter it again
    # if the input number % 10 == 3 it is divisible by 3, else it is not
    while True:
        number = input("enter integer number: ")
        if number.isdigit():
            number = int(number)
            lastDigit = number % 10

            if lastDigit % 3 == 0:
                print(f"last digit: {lastDigit} is divisible by 3")
            else:
                print(f"last digit: {lastDigit} is not divisible by 3")
            break
        else:
            print("please enter integer")
            continue

# exercise2()


# for loop
# for x in range(5):
#     print(x)

# for j in range(0,5,1):
#     print(j)


# range
"""
for i in range(1,6,1):
    print(f"2 x {i} = {2 * i}")
"""

# break
"""
user = input("search name: ")
name = ["smith", "joe", "jonh", "jack"]

for i in name:
    if i == user:
        print(f"{i} is founded")
        break
else:
    print("name not founded")

for i in range(10):
    if i == 5:
        continue
    print("i above: ", i)
print("i below ", i) # print the last i
"""


# while loops
# i = 1
# while i <6:
#     print()
#     i += 1

"""
practice 3:
calculate the sum of number from a list, using a while loop
"""

myList = [22,14,3]
# iterate all the element inside list
# add the sum to a new variable
sum  = 0
i = 0
while i < len(myList):
    sum += myList[i]
    i+=1
# print(sum)

def exercise3():
    # ask user to guess number and if the numeber match with the guess print it is right
    answer = 100
    count = 0
    while True:
        guess = input("enter guess: ")
        if guess == answer:
            print(f"you guess: {count} times and the answer is {answer}")
            break
        else:
            count += 1
            continue 
        
    
# exercise3()

def exercise4():
    # print a pyramid
    num = 1
    for i in range(1):
        for j in range(1,6,1):
            print("* "*j)

            

# exercise4()
    
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

# homework 
for i in range(1,6):
    for j in range(i,6,1):
        print(j,end=" ")
    print()

# output:
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

# homework 
for i in range(5, 0, -1): 
    for j in range(i, 0, -1):  
        print(j, end=" ")  
    print()

# output:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1