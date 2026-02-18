"""
functional programming: 
- treat function like value
- small composable function

"""


# nested functon
def outer(x):
    def inner(y):
        return y*2
    return inner(x)


def make_multiplier(factor):
    def multiply(x):
        print(f"x: {x}")
        print(f"factor: {factor}")
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(5))  # 10


# higher order function: take function as in input or return another functon
def apply_function(f, value):
    return f(value)

def square(x):
    return x * x

print(apply_function(square, 5))

# built in hofs
nums = [1,2,3,4]

result = list(map(lambda x: x*2, nums))
print(result)

# pure function: depend only on input
# pure
def add(a, b):
    return a + b

# not pure
total = 0

def add_to_total(x):
    global total
    total += x


pairs = [(1,3), (2,1), (5,2)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)


# exercise
# write function that apply f function twice
def apply_twice(f,value):
    return f(f(value))

print(apply_twice(lambda x: x+3,5))

# write a function return a function that raise number to the power n
def power_factory(n):
    def raise_n(x):
        return x **n
    return raise_n


squa = power_factory(2)
print(squa(5))  # 25


# rewrite to be pure
def add_num(x):
    return [x]

# lambda + filter: create a list of only even number using filter()
nums = [1,2,3,4,5,6,7,8]
even = list(filter(lambda x : x % 2 == 0, nums))
print(even)


def counter():
    counts = 0
    def increment():
        nonlocal counts
        count = counts + 1
        return count
    return increment
c = counter()
print(c())


def outer():
    x = 10
    def inner():
        return x * 2
    return inner

f = outer()
print(f())


"""
class lessons
"""

# nested function 

# nested function procedural
def greeting(name):
    def inner():
        print(f'hello {name}!')
    inner()

greeting('joe')


# nested function that have return
def greetings(name):
    def inner():
        return f'hello {name}'
    return inner()

print(greetings('joe'))


def add(x):
    def inner_add(y):
        return x + y
    return inner_add


# higher order function: can return function and accept function

# recursion
def factor(n):
    # edge case
    if n <= 1:
        return 1
    
    return n * factor(n-1)


def fibonacci(n):
    # edge case
    if n <= 1:
        return n
    
    return   fibonacci(n - 1) +fibonacci(n - 2)


def print_recursion(func, n):
    for i in range(1,n+1):
        print(f"{i}: {func(i)}")
        
        
print_recursion(factor, 3)
print_recursion(fibonacci, 3)

import random
# list generator function
# generate a list of random numbers with a given length
# filter - even number only and odd number only
# user can also define the random number range (value1, value2)
def even_number(n):
    if n % 2 == 0:
        return n
    

def odd_number(n):
    if n % 2 != 0:
        return n

def list_generator(n, func, value1, value2):
    lst = []
    while len(lst) < n:
        number = random.randint(value1,value2)
        val = func(number)
        if val is not None:
            lst.append(number)
        
        # if func(number):
        #     lst.append(number)
            
    return lst

print(list_generator(10, even_number,0,2 ))


# lambda expression
square = lambda x : x**2 # square is a function
print(square(5))

reverse = lambda x : x[::-1] # 3 s: start, stop, step
print(reverse('apple'))


even = lambda x : x % 2 ==0
print(even(234))

# lambda and sorting
l = [10,25,-9,74,65,-50]
print(sorted(l))

s = ['B', 'c', 'D', 'a', 'F', 'x', 'S']
print(sorted(s, key=lambda x: x.upper()))

# sort by length
words = ['apples', 'peach', 'lemon', 'strawberry']
print(sorted(words, key=lambda x: len(x)))

#  count words in a string
my_string = 'this is an example. a short text for the task.'
result = lambda x: len(x.split())
print(result(my_string))


# sort a dictionary
d = {
    'a': 30,
    'x': 500,
    'c': 200
}

print(sorted(d))
# sort by value
print(sorted(d, key=lambda x: d[x]))