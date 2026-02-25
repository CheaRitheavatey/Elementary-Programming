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
# result = reduce(lambda x, y: x+y,
#                 map(lambda x: x**2,
#                     filter(lambda x: x & 2 == 0)**2, nums))

"""class work"""
my_list = [5,8,4]

def sq(x):
    return list(map(lambda y: y**2, x))


# or another way 
def sq1(x):
    return x**2

my_sq_list = list(map(sq1,my_list))

# adding two lists element wise with map
list1 = [1,2,3,4]
list2 = [1,2,3,4,5]

def add2_list(x,y):
    return x+y

new_lists = list(map(add2_list, list1,list2)) # only add the name of the function no need parenthesis()
print(new_lists)

# recursive factorial
def factorial(n):
    return 1 if n <=1 else n * factorial(n-1)

# compute serveral factorial at once with map
fact_result = list(map(factorial, range(6)))

# adding three list elemtwise with a lambda
l1 = [1,2,3,4]
l2 = [10,20,30,40]
l3 = [100,200,300,400]

result = list(map(lambda x,y,z: x+y+z, l1,l2,l3)) # number of lambda x y z mean 3 so iterable l1,l2 l3 kor trov 3 too
print(result)

"""note: if use helper method then the map no need to use lambda"""
# extra FP-wizard example: adding an arbitrary number of lists
def add_all(*args):
    return sum(args)

result = list(map(add_all,l1,l2,l3, my_list,list1,list2)) # if len of all the list is different then it will only do the shortest one

# filter = is a predicate aka return true or false and the filter keep only the true element

# print out the number between 32 and 97 that are divisble by 3
list_div3 = list(filter(lambda x: x % 3 ==0, range(32,97)))

# filter without a function use truthy/falsy values
# if func is None, Fase, 0,0.0, '',[], {} --> Falsy 
# everything else is --> Truthy

list_nofunc = list(filter(None,[1,2,3,'a','c', '', True, False, None]))
print(list_nofunc)

# realistic example of cleaning list of name
name = ['anna', '', 'bill', None,'john', ' ', 'eve']
# def is_non_empty_name(name):
#     return bool(name.strip())

# res = list(filter(is_non_empty_name,name))
# print(res)

# reduce
sum_result = reduce(lambda x,y: x+y, list1)
product_result = reduce(lambda x,y: x*y, list1)
fact_result = reduce(lambda x,y: x*y, range(1,6))

# max search with reduce
list3 = [4,5,6,78,9,2]
max_search = reduce(lambda x, y: x if x>y else y,list3 )
min_search = reduce(lambda x, y: x if x<y else y,list3 )
print(max_search)
print(min_search)

# mini reduce - how reduce work internally


_max = lambda x,y : x if x > y else y
_min = lambda x,y : x if x < y else y
_sum = lambda x,y : x + y

def max_seq(seq):
    result = seq[0]
    for i in seq[1:]:
        result = _max(result,i)
    return result

def min_seq(seq):
    result = seq[0]
    for i in seq[1:]:
        result = _min(result,i)
    return result

def sum_seq(seq):
    result = seq[0]
    for i in seq[1:]:
        result = _sum(result,i)
    return result

# write our own reduce func
def _reduce(func,seq):
    result = seq[0]
    for i in seq[1:]:
        result = func(result, i)
    return result

# flattening list using reduce
list5 = [[1,2], [3,4], [5,6]]

# for normal version
flat_manual = []
for i in list5:
    flat_manual += i # concatenate
print(flat_manual)
# using reduce
flat_reduce = list(reduce(lambda x,y : x + y, list5, []))
print(flat_reduce)

# reduce advance pipe() with for loop
# goal: define a function that take an initial value and a seq of func, and applies them one after another
# example, pipe(5,add_one,times_two, to_str)

# loop version
def pipe(value, *func):
    result = value
    for i in func:
        result = i(result)
    return result


# now using pipe()
# pipe(5,add_one,times_two, to_str)

# reduce pipe: same as pipe but implemented with reduce instead of for loop

def pipe_reduce(value, *func):
    return reduce(lambda acc, f: f(acc), func,value)