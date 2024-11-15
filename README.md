# Elementary-Programming 
week 2: lesson summary
-----------------------

# comment: use to explain the code using "#"
"""
comment for long line (instruction)
"""

variable:
- variable containers for storing data value
- can only contain aplpha-numeric characters and underscores (a-z,0-9,_)
- cannot start with number
- is case sensitive

camelCase
PascalCase
snake_case


function:
- print(): put out on terminal
- can use , to separate what we want to print
- parameter: what we pass into
- argument: the value itself
- example: def func(a):
    a = parameter 
    value of a is the argument

type of programming language:
- static: when we declare a variable we need to specify its type
        example, java, c++, c#...
- dynamic: when we do not have to declare a variable to specify its type
        example, javascript, python, ruby

- compile time error: happen when writing the code
- runtime error/logic error: happen when running the code


data type:
- text: str, char
- numeric type: int, float, complex
- sequence types: dict, array
- mapping
- set: set, 
- boolean: true, false
- binary: binaryType
- none Type: noneType

- print(type(variable)) -- to tell you the what type it is

Immutable: cannot change
- example, number, str, boolean
- why? because when you change the value there will be a new memory space for that new assigned value
- print(id(argument)) -- to find out the memory address 

Mutable: can change
- example, List, Dictionary, and Sets

FINAL in java, in Python is writing what you want not to change in all uppercase
- example, PI

function: applicable in all case like print()
method: only applicable for only a project, or class

Scape sequence:
# -> comment
\* -> "
\' -> '
\\ -> \ (example: C:\\document\\desktop)
\n -> new line

str method
.lower() -- lowercase
.upper() -- uppercase
.title() -- first char to uppercase
.strip() -- trim whitespace
.lstrip() -- trim whitespace beginning
.rstrip() -- trim whitespace at the end
.find("") -- return index of what you want to find

number methods:
- round()
- ceil()
- floor()
- bin()
- hex()

input() -- for taking input from users

Type of conversion:
- int()
- float()
- bool()
- str()

truth and false value
- return false when:
    "" -- empty string
    0 -- zero
    [] -- empty list
    None -- absence of number

comparision operator
(NOTE: = is for assigning value NOT equivalent)
> -- bigger
< -- smaller
>= -- bigger or equal
<= -- smaller or equal
== -- equal
!= -- not equal
-----------------------

week 3: Conditional statement
----------------------
- use if statement

if condition:
    // do something here //
elif other condition:
    // do something here //
else:
    // do something here //


- ternary operator: put everything in one line
format: statement + if condition + else + statement
example, print("a equal b") if a == b else print("a is not equal to b")

- logical operation: use to combine statement: 
and 
or 
not (and)
== 
!= 

- pass: if for any reason you have to leave one empty, you can do it by puttin in the pass statement
(just like when prof give code to write and put pass)
example, def abc():
            pass

- for loops: use for iteraeting over a sequence or any object that is iterable (that is either a list, a tuple, a dictionary, a set, or a string)
example,
for x in "python":
    print(x)
    <!-- it going to print each character in "python" -->

- range
example,
1. for i in range(5):
    print(i) <!-- print 0 until 4-->

2. for i in range(0,4,1):
    print(i) <!-- same as above but its java style-->

- break statement: use to jump out of a loop for perfrmance reasons.
example,
name = ["smith", "joe", "jonh", "jack"]
for i in name:
    if i == "joe":
        print("{i} is founded")
        break
else:
    print("name not founded")


- continue statement: stop the current iteraction of the loop, and continue with the next
example,
for i in range(10):
if i == 5:
    continue
print(i)
<!-- its going to print number from 0 to 10 except 5 -->


- while loop: execute a set of statement as long as condition is ture.
example, 
i = 1
while i > 6:
    print()
    i += 1
 *** remember to increment or decrement or it will be an infinite loop

- len(list([1,2,3,4,5])) 
<!-- will display: 5 as it is the length of the list -->

- for loop inside for loop: used to iterate 2 lists like a matrix
---------------------------------

week 4: function
---------------------------------
def functionName(parameter):

- to call function:
functionName(parameter)

example,
def functionName(age): # this age is a parameter
    print(f"You are {age} years old")

functionName(12) # 12 that passed in is an argument

- for arbitary argument: use * when we dont know how many argument users going to passed in
def arbitary(*parameter):

example, 
def getList(*objectList):
    return objectList

print(getList(1,2,3,"hi","hello",1.4))
// the arugment passed will be stored in tuple

example,

def getUser(*name):
    for i in name:
        print(i)

getUser("joe", "jonh", "jack")

-> output:
joe
jonh
jack
// not a tuple anymore if we use for loop to print

- arbitrary keyword argument (**keywordArgument): use when we dont know how many information they going to passed in and the return type: dictionary
example,
def save_user(**user):
    return(user)

print(save_user(id=123,name="joe"),job="abc")

- local variable: accessible within function scope
- global variable: accessible within file scope
- but we can assign local into global as well by using "global" keyword
- example,

// global variable
message = 'global variable'
def send():
    message1 = 'local variable'
    global message = 'local variable turn into global variable when we use global keyword'
    print(message)

-----------------------------
week 5: collection
----------------------------
- there are 4 build-in data types in python used to store collectoins of data:
    
    - lists: ordered, changeable, allow duplicate member
        - example, colorList = ['green', 'blue', 'yellow']
        - first index: colorList[0]
        - last index: colorList[-1]

        - if you dont specify the new element where you want to add, it will add at the end of list

        - len(list): determine the length of the list
        - newList = list(('a','b','c')): create a new list

        - access a range of indexes:
        example, colorList = ['green', 'blue', 'yellow']
        colorList[1:2] -> print out the second and third elements
        colorLList[:] -> print out all elements
        colorList[:1] -> print out first and until index 2
        colorList[1:] -> print out from index 1 until the end

        - check if element in list:
        if 'yellow' in colorList:
            return True

        - change range of items value:
            example, 
            colorList = ['green', 'blue', 'yellow']
            colorList[1:2] = ['orange', 'white']
            print(colorList) -> output: ['green', 'orange', 'white']
        
        - .insert(index, newElement): insert new element in specific index. the exisiting element in that index will not be replace but move to the next index
            example, num = [1,2,3,4]
            num.insert(0,'a') -> output: ['a',1,2,3,4]

        - .append(newElement): add new element at the last index of the list
            example, num.append(100) -> output: [1,2,3,4,100]
        
        - .extend(): add iterable object into another list
            example, 
            num = (1,2,3,4) # a tuple
            colorList.extend(num)
        - .pop(): remove the last item if you dont pass an argument, but if you pass index it will remove item in   that index

        - .remove(element): remove that element
        - .clear(): remove all element inside list only empty list remain

        - comprehension list:
            newList = [expression for item in iterable if condition == True]

            we can write that instead of for loop they both are the same

        - .sort(): sort list alphabetically or in ascending order
        - .reverse(): reverse the list from back to front
        - .copy(): copy the list
            example,
            b = [1,7,4,5,0,3,2,7,0]
            b.sort(reverse=True)
            print(b)
        - .count(element inside list): count how many element inside that list exist
            example,  b = [1,7,4,5,0,3,2,7,0]
            b.count(7) -> output: 2 because it exists 2 times

    
    - tuple: ordered, unchangable, allow duplicate member
        - similar to list its just that its unchangeable (immutable) 
        - can convert to list and modify and use the functions and methods of list and then convert it back to tuple

    - set: unordered unablechange no duplicate member unindexed
        example, aSet = {1,3,4,5}
        - create a set: aSet = set({1,2,3,4})
        - .add(value): just like append() it is just for set its just for set its not ordered so the new value will be anywhere in set
        - .update(element): add list, another set, or tuple in a set
        - .remove(element): delete an element inside set but will raise error if the element you want to remove doesnt exist
        - .discard(element): same as .remove() but will not raise an error
        - .pop(): dont need argument but will remove element randomly
        - .clear(): remove all element inside set and will have empty set remain    


    - dictionary: ordered changeable no duplicate memebr
        - stored data in key:value pairs
        example, dict = {
            'name': "joe",
            'age': 10
        }

        - len(dict): print out how many item inside the dictionary
        example, len(dict) -> output: 2
        - .get(): same as dict[key]
        - .keys(): return all the key in dict
        - .values(): return all the value in dict
        - .items(): return in item in dict as a tuple
        - .update(): 

        - del: keyword for delete collection completely will have nothing not even empty list or dict or set or tuple...
            example, del dictName

-------------------------------------
week 6: Exception
------------------------------------

- error detected during execution are called "exception"
- there are different type of exception
- to handle exeception:
    use try and except block

    - try block let you test a block of code for errors or tell teh program to do sth in that block that may cause the error
    - except block let you handle that error that may arise
    - else block let you execute code when there is no error.
    - finally block let you execute code, regardless of the result of the try and except block. (this will be executed no matter what)
        ex. close a file, it doesnt matter if the program cause error or not you want to close a file

    - raise statement allow the programmer to force a specific exeception to occur. 

    - if an exception occurs during execution of the try clause, the rest of the clause will be skip, then exception clause will be raise and then finally clause will execute

    try:
        <body>
    except <ExceptionType 1>:
        <handler>
    ...
    except <ExceptionType N>:
        <handlerN>
    finally:
        <process_finally> will execute to matter what


    - we can also write this way if we want to use a lot of exception:

    except(TypeError, ZeroDivisionError)

    - all exception inherit from BaseException so if we dont know what exception we will get we can use BaseException

    - can also write this way:

    try:
        <>
    except BaseException as err:
    print("unexpceted {err}, type(err) =")

Exception Hierarchy:

BaseException:
    SystemExit
    KeyboardInterrupt
    Exception
        StopIteration
        StopAsyncIteration
        ArithmeticError
            FloatingPointError
            ConnectionAbortedError
            ConnectionRefusedError
            ConnectionRoseError
        FileExistsError
        FileNotFoundError
        InterruptedError

    OSError: this exception is raise when a system fucntion returns a system related error
    TypeError: raise wehn an operation or function is applied to an object of inappropriate type. ex try to concatinate int and str
    SyntaxError: when you write sth wrong
    RuntimeError: error occur during runtime like zero division error. ex 1/0 is in runtime error
    NameError: when local or global name is not found
    FileExistError: when you want to create a file that already exist
    ValueError occurs when a function is called with the proper argument type but with the wrong value. 

- raise an exception (usually in a function)
- try to use the function
- Handle the exception

---------------------------------------
week 7: OOP
---------------------------------------

- python is an object oriented programming
- class = is like an object constructor or a blueprint for creating an object
- object = will have properties and method
- class keyword for creating class
- self parameter is a reference to the current instand of the class

- create an instance or object of the class
    x = MyClass()
    x.draw() # as draw is one of the method in class name MyClass

- can also create a new variable, or propterty outside like this:

    class MyClass:
        x = 1
        def move(self):
            print("move")

    x = MyClass()
    x.m = 20 # the property m does not exist in the class name MyClass but we can add a new one like this
    print(x.m) # the output will be 20

- constructor: get called everythime we create an object
- __init__() always executed when the class is being initaiated
- use __init__() fuction to assign values to object properties or other operations that are necessary to do when the object is being created

- del keyword: specify something you want to delete

- INHERITANCE: allow us to define class that inherits all the modthods and properties from another class
    - parent class is the class being inherited from
    - child class is the class that inherit from another class

    - super() put this inside the child class constrcutor so that child class will inherit the property inside

    - use import to import class from different file.
    example, 
    import module_name
    module_name.name_of_the_method

    __main__ is set to __main__ when rand directly
    __name__ is set to file name when ran indrectly as a module

    if __name__ == "__main__":
        account.deposit(3000000)
    else:
        print("invalid")

-------------------------------------------------
week 9: file handling
-------------------------------------------------

- open() is the key function for working with files in python
    file that can be used here is text or
    - mode:
        - 'r' = reading text mode
        - 'w' = writing (truncating the file if it already exist)
        - 'x' = creating and writing to new file
        - 'a' = appending (when you want to keep the content inside and want to write more inside)

        - 'b' = binary mode
        - 't' = text mode (default)

    - file going to raise an error when file doesnt exist and you try to open it

    - methods:
        - .read(): read content of the file it return the whole text
        - .readline(): read the content but one line at a time return one line at a time
        - .readlines(): will put each line in a list
        - .close(): close file do this especially when you want to change the 
        
        - os.remove("filename"): to remove file but first you have to remove file
            example, 
            import os
            myfile = open("filename.txt")
            os.remove("filename.txt")
            and then run

        - os.path.exists("filename"): return boolean if the file exist or not can  be use in condition to check if the file exist
        
        - os.rmdir("folder name"): remove folder if folder empty but if the directory or file is not empty then it will show an error

        - os.mkdir("folder name"): create a new folder

    
