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
