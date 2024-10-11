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

# practice 3
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

# divide()

# raise Exception
# usually we use raise exception in funciton and when we try to use that function we put it in try block
def practice4():
    try:
        num = input("enter number: ")
        num = int(num)
        if num<0:
            raise TypeError("positive integer only")
    except TypeError as e:
        print(type(e))

# practice4()

# practice 5

def practice5():
    day = {
    'one': 'monday',
    'two': 'tuesday',
    'three': 'wednesday',
    'four': 'thursday',
    'five': 'friday',
    'six': 'saturday',
    'seven': 'sunday'
    }
    
    while True: 
        try:
            user = input("enter number as text from one-seven: ")
            user = user.lower()
            print("day of the week is: ", day[user])
        except KeyError as e:
            print("enter from one-seven")
        else:    
            again = input("want to enter again? (y/n): ")
            if again.lower() != 'y':
                break
    
# practice5()

# practice 6: bmi calculation
# bmi()

def practice5():
    while True:
        try:
            weight = input("enter weight (kg): ")
            height = input("enter height (m): ")
            
            weight = float(weight)
            height = float(height)
            
            bmi = round((weight/height),2)
        except ValueError as e:
            print(e)

        else:
            print(f"bmi: {bmi}")
            if  18.5 < bmi < 24.9:
                print(f"{bmi} is within the healthy range")
            elif bmi > 25:
                print( f"{bmi} is in the overweight range")
            else:
                print( f"{bmi} is within the underweight range")

            again = input("want to enter again? (y/n): ")
            if again != 'y':
                break

practice5()