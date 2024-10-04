# function

# example 1
def functionName(age):
    print(f"You are {age} years old")

# functionName(12)

# example 2
def assignColor(redObj, yellowObj, greenObj):
    print(f"red {redObj}\nyellow {yellowObj}\ngreen {greenObj}")

# assignColor("flower","sun","tree")

# example 3
def increment(number, by=1):
    return number + 1

# print(increment(12))

# example 4
# arbitary argument: used when you dont know how many arugment are going to get passed to your function *
def getList(*objectList):
    return objectList

# print(getList(1,2,3,"hi","hello",1.4))


# example 5
def getUser(*name):
    for i in name:
        print(i)

# getUser("joe", "jonh", "jack")


# example 6
def sumNum(*number):
    total = 0
    for i in number:
        total += i
    return total

# print(sumNum(1,2,3,4,5))

# exercise 1
def multiplyNumber(*number):
    total = 1
    for i in number:
        total *= i
    return f"total: {total}"

# print(multiplyNumber(2,4,2,5))

# example 7
# arbitarary keyword argument
# use ** when we dont know how many kind/type of information users going to put in
def save_user(**user):
    return(user["id"])

# print(save_user(id=123,name="joe",job="abc")) 


# exercise 2
def noDuplicate(list):
    uniqueList = []
    for i in range(0,len(list)):
        if list[i] not in uniqueList:
            uniqueList.append(list[i])

    return uniqueList
# print(noDuplicate([1,2,3,1,3,4,4,4,4,3,7]))


# global variable
message = 'global variable'
def send():
    global message 
    message = 'local variable -> global variable'

    message = 'local variable'
    return(message)

# print(message)
# send()

# exercise 3
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else: 
        return input

# print(fizz_buzz(90))


# exercise 4
def removeN(str,num):
    return(str[num:])

# print(removeN("python",2))


# exercise 5
def same(parameter):
    for i in range(0,len(parameter)):
        if parameter[0] != parameter[-1]:
            return False
    else:
        return True

# print(same([1,2,3,1]))


def prime(number):
    newlist = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            newlist.append(divisor)
            number = number // divisor
        divisor += 1
    return newlist

# print(prime(70))


def get_cofactor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def matrix1(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * matrix(get_cofactor(matrix, 0, c))
    return det

# Test cases
matrix_2x2 = [[4, 6], [3, 8]]
matrix_3x3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]

# print(matrix(matrix_2x2))  # Output: 14
# print(matrix(matrix_3x3))  # Output: -306

import numpy as np

def matrix(matrix):
    return np.linalg.det(matrix)

array = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
# print(matrix(array))


def plusMinus(arr):
    postive = 0
    negative = 0
    zero = 0
    total = len(arr)
    for i in arr:
        if i > 0:
            postive+= 1
        elif i < 0:
            negative+=1
        else:
            zero +=1
    postiveRatio = postive/total
    negativeRatio = negative/total
    zeroRatio = zero/total

    formattedP = f"{postiveRatio:.6f}"
    formattedN = f"{negativeRatio:.6f}"
    formatted0 = f"{zeroRatio:.6f}"

    return formattedP, formattedN, formatted0

# print(plusMinus([1,-1,0,-1,1]))



# home practice start 

# exercise 1 palindrome checker: check if a given string is a palindrome (read the saem forwards and backward)
def palindrome(str):
    str = str.lower().replace(" ", "")
    return str == str[::-1]

# print(palindrome("aba"))


# exercise 2: fibonacci sequence: write a function that return the nth fibonacci number
def fibonacci(n):
    # base case
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibonacci(n-2) + (fibonacci(n-1))

# print(fibonacci(4))

# exercise 3 check for prime number
def primeChecker(num):
    if num <= 1:
        return False
    
    # loop over possible divisor to check if num is diviible by any of them
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True
# print(primeChecker(3))


# exercise 4: write a function that check if two string are anagrams of each other
def anagram(str1, str2):
    # convert them into lowercase and store them in a sorted list using sorted() functino
    return sorted(str1.lower()) == sorted(str2.lower())

# sorted("listen") results in ['e', 'i', 'l', 'n', 's', 't']

# home practice end