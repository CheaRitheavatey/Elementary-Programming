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
