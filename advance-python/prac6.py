"""ITERATION"""
# iteration = is an object that implement iterator protocol
# consist of 2 methods: __iter__() and __next__()

# example of iterator class
class NumberSequence:
    def __iter__(self):
        self.a = 1 # start value for iteration
        return self
    
    def __next__(self):
        x = self.a # x will be the next element of the sequence
        self.a += 1
        return x
    
numbers = NumberSequence()
myiter = iter(numbers) # iter(numbers) call numbers.__iter__()

for i in range(10):
    print(next(myiter))
    
# note: the iter(obj) method is called auto matically by the for loop after initialzing the iterator the __iter__()
# will return any object that implement __next__()

class Fib:
    def __init__(self, max):
        self.max = max
        
    def __iter__(self):
        self.a = 0 # inital value
        self.b = 1
        return self
    
    def __next__(self):
        x = self.a # next element of seq
        if x > self.max:
            raise StopIteration
        
        self.a, self.b = self.b, self.a + self.b
        return x
    
fib = Fib(100)
iter_fib = iter(fib)
for i in range(12):
    print(next(iter_fib))
    
    
    
# because Fib class is an iterable object itself we can do this too
for n in fib:
    print(n, end=" ")
    
"""when iteration class use for?
    - structure: separate data from iteration logic
    - usability: same iterationlogi can be use elsewhere
    - readability: encapsulating iteration logic improve clarity
    - protocol support: work with any python iterative construct
    
    
    iterator class use when:
    1. iteration logic is complex
    2. building custom data structure
    
"""

"""
GENERATOR
also iterator but they deined using unctions that contain the 'yield' keyword

generator function itself is like a factory its NOT A GENERATOR
"""

def my_genfunc(): # this method is not a generator itself
    yield 1
    yield 2
    yield 'hah?'
    
gen = my_genfunc() # gen: the generator object
print(type(gen))
print(dir(gen))

# print(next(gen))
# print(next(gen))
# print(next(gen))


"""
return vs yield

return:
- immediately exits the function
- provide a single value

yield:
- produce a sequence of values
- function execution is paused not terminated
- state is preserved between yields

""" 

def square_generator(nums):
    for i in nums:
        yield i * i
        
square = square_generator([1,2,3,4,5])
for sq in square:
    print(sq)
    
    
square1 = square_generator(range(10))
for sq in square1:
    print(sq)
    
# using iterators and generator to compute factorials
import math

class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0 # index where we are
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        
        result = math.factorial(self.i)
        self.i += 1
        return result
    
fact_iter = FactIter(10)
# print(list(fact_iter))
# print(list(fact_iter)) # this will return [] cuz it already exhausted in the first print


# now for generator
def fact(n):
    for i in range(n+1):
        yield math.factorial(i)

fact_gen = fact(5)
# print(list(fact_gen))

# fib generator
def fib_generator(n):
    fib0 = 0
    yield fib0
    fib1 = 1
    yield fib1
    for i in range(n - 2):
        fib0, fib1 = fib1, fib0 + fib1
        yield fib1
        
gen_fib = fib_generator(20)
for i in gen_fib:
    print(i, end=" ")
        

# generator compare to reduce , recursion, loop it is much faster
"""
advantage:
- effciency: they consume minial memory
- convenience: much simpler syntax than iterator classes
- flexibility: easy to create ininte sequence or dynamic logic
- single pass nature: they can only be iteratd once which is ideal or large datasets

"""


# challenge 3 and 4:
# implement prime number generation using both
# a generator 
#  and an iterator class

# thought process:
# number is !prime if its <= 1, even number and odd number , x^2 <= n if n / x = 0 or n / x+2 = 0
# continue from 5
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while (i**2 <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+= 6
    return True

# generator
def prime_generator():
    num = 3
    yield 2
    while True:
        if is_prime(num):
            yield num
        num+= 2

gen_prime = prime_generator()
for i in range(10):
    print(next(gen_prime), end=" ")
    
# iteration
# example, [2 3 4 5 6 7 8 9]
# if index0 
class PrimeIterator:
    def __init__(self):
        self.primes = []
        self.index = 0
        
    def __iter__(self):
        return self
    
        
    def __next__(self):
        if self.index < len(self.primes):
            prime = self.primes[self.index]
            self.index += 1
            return prime
        else:
            # add next prime
            if not self.primes:
                self.primes.append(2)
                self.index = 1
                return 2
            num = self.primes[-1] + 2
            while True:
                if is_prime(num):
                    self.primes.append(num)
                    self.index += 1
                    return num
                num += 2


print("Using Iterator Class:")
prime_iter = PrimeIterator()
for _ in range(10):
    print(next(prime_iter), end=" ")
print()








# # generator
# def prime_genertor