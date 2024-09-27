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

print(same([1,2,3,1]))