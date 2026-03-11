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

print("generator")
gen_prime = prime_generator()
for i in range(10):
    print(next(gen_prime), end=" ")
    
    
    
    
# iteration
# if index0 
class PrimeIterator:
    def __init__(self):
        self.primes = []
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        # return cached prime if available
        if self.index < len(self.primes):
            prime = self.primes[self.index]
            self.index += 1
            return prime

        # do next prime
        if not self.primes:
            # first prime
            self.primes.append(2)
            self.index = 1
            return 2

        # check the number after the last prime
        num = self.primes[-1] + 1
        while True:
            if is_prime(num):
                self.primes.append(num)
                self.index += 1
                return num
            num += 1


print("iterator")
prime_iter = prime_generator()
for i in range(5):
    print(next(prime_iter), end=" ")
