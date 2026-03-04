# review last lessons
# square all numbers
nums = [1,2,3,4]
new_nums =list(map(lambda x: x**2,nums))
print(new_nums)

# convert all names to upper case
names = ["vatey", "anna", "john"]
new_names = list(map(lambda x: x.upper(), names))
print(new_names)

# convert list of price to price with 10% tax
prices = [100, 200, 50]
new_price = list(map(lambda x: x+ (x*0.1), prices))
print(new_price)

# keep only even number
nums = [1,2,3,4,5,6]
filter_num = list(filter(lambda x: x % 2==0, nums))
print(filter_num)

# keep words longer than 5 letters
words = ["apple", "banana", "kiwi", "strawberry"]
filter_word = list(filter(lambda x: len(x) > 5, words))
print(filter_word)

# keep student who passed
grades = [30, 75, 60, 45, 90]
filter_grade = list(filter(lambda x : x >= 50, grades))
print(filter_grade)

# find product of all number
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x,y: x*y, nums)
print(product)

# find max number
nums = [5, 2, 9, 1]
max_num = reduce(lambda x, y: x if x > y else y,nums)
print(max_num)


# count total char in list of word
words = ["hi", "functional", "python"]
total = reduce(lambda x,y:x +len(y) ,words, 0)
# or sum(map(len, words))
print(total)

# square only even number:
nums = [1,2,3,4,5,6]
even_square = list(map(lambda x : x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_square)

# sum of squares of odd numbers
nums = [1,2,3,4,5]
sqo = reduce(lambda x,y : x + y, map(lambda x : x**2, filter(lambda x : x % 2 !=0, nums)))
print(sqo)

# get total grade of student who pass
students = [
    {"name":"Anna", "grade":80},
    {"name":"Bob", "grade":40},
    {"name":"Cara", "grade":90}
]

grade= reduce(lambda x,y : x + y['grade'], filter(lambda x: x['grade'] >= 50, students),0)
print(grade)

"""
callable object = any object ou can call using ()
- functions are callable
- classes can be callable too using __call__

"""

class Multiplier:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return x * self.n

double = Multiplier(2)

print(double(5))   # 10


x = 10  # global

def outer():
    y = 5  # enclosing
    
    def inner():
        z = 2  # local
        print(x, y, z)
    
    inner()

outer()


# non local
def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

c = counter()
print(c())
print(c())


# decorator
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


# create a decorator that count how many time func is call
def count(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"called {count} times")
        return func(*args, **kwargs)
    return inner

@count
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()


"""
closure = function remember outer variable
decorator = function that wrap another function
"""