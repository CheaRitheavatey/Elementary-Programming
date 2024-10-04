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
    
    
    
    - tuple: ordered, unchangable, allow duplicate member

    - set: unordered unablechange no duplicate member unindexed
    - dictionary: ordered changeable no duplicate memebr