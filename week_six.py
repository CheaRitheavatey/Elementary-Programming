# print(x) NameError exception cause the variable x is not define
def testTryExcept():
    try:
        print(x)
    except NameError:
        print("NameError has occur")
    except:
        print("second except") # should use specific type of error in the first and more general below


# testExeception()

def differentWayToWrite():
    try:
        print(12/0)
    except BaseException as err:
        print(f"unexpceted {err}, {type(err)=}")
        

# differentWayToWrite()


# practice 1
# we have a list, ask user for an input which is the index valuse we want to access
# run the code until we get the right input from user

def practice1():
    myList = [12,48,55,1,222]


    while True:
        user = input("which index? ")
        try:
            print(myList[int(user)])
            break
        except IndexError as e:
            print(e)
        except ValueError as e:
            print(e)

# practice1()

# practice 2
# create a variable which holds a number input from the user
# concatenate it with an integer and put it in the same variable and print the new value

def practice2():
    while True:
        number = input("enter a number: ")
        try:
            number = int(number) # concatenate to int
            print(f"number: {number}")
            
        except ValueError:
            print("enter an integer number")
        except Exception as e:
            print(f"something wrong with the input {type(e)}")

        again = input("want to enter again? (y/n): ")
        if again.lower() != "y":
            break

# concatenate is different from upcast and downcast
# practice2()

# testTryExcept()

def testExeception():
    try:
        number1, number2, = eval(input("Enter two numbers, separated by a comma: "))
        result = number1 / number2
        print("Result: ", result)
    except ZeroDivisionError:
        print("division by 0")
    except SyntaxError:
        print("a comma may be missing")
    except:
        print("something is wrong with the input")
    finally:
        print("finally clause executed")

# testExeception()

# practice
def divide():
    while True:
        try:
            a = input("enter number x: ")
            b = input("enter numebr y: ")
            a = float(a)
            b = float(b)
            print(f"result of x/y: {a/b}")
        except ValueError as e:
            print("one or both of the input is not numberic value")
        except ZeroDivisionError as e:
            print("y cannot be 0")
        
        else:
            # this will executed only if try block executed successfully
            again = input("want to enter again? (y/n): ")
            if again.lower() != "y":
                break
        # finally:
            # this is will executed no matter what
            # print("program exited! ")

divide()