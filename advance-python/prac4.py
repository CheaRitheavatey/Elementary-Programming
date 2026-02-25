from functools import reduce
# built in higher order function
nums = [1,2,3,4]
result = list(map(lambda x: x*2, nums))

# equivalent
result1 = [x*2 for x in nums]
print(result)
print(result1)


# filter 
num2 = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2==0, num2))
print(evens)

# reduce
total = reduce(lambda a, b: a+b, nums)
print(total)


nums = [1,2,3,4,5]
result = list(map(lambda x : x**2, nums))
print(result)


words = ["apple", "banana", "pear", "kiwi", "orange"]
result = list(filter(lambda x : len(x) > 4, words))
print(result)

nums = [5, 10, 15]
result = (reduce(lambda x,y: x*y, nums))
print(result)

def apply_n_times(f,value,n):
    return f(value) * n

print(apply_n_times(lambda x: x+1, 0, 5))


def add_item(data, x):
    return data + [x]


def make_adder(n):
    def add_n(m):
        return m+n
    return add_n

add5 = make_adder(5)
print(add5(10))

nums = [1,2,3,4,5,6]
result = reduce(lambda x, y: x+y,
                map(lambda x: x**2,
                    (filter(lambda x: x & 2 == 0))**2, nums))