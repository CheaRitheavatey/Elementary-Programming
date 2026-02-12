# 2 type of pass: reference and value
# immutable object = int float string tuple bool
# mutable object = list dict set 
var = 521
print(id(var)) # use id() to know the address
print(hex(id(var))) # use hex() to know hexadecimal number of id() or address

var1 = var # point to the same address as var aka shared reference

# object are created on heap

# count reference
import sys
print(f"references to var: {sys.getrefcount(var)}" ) # when function call itself it also count so its not 2 but whenever we mention var it will count

# delete var1
del var1
print(f"references to var: {sys.getrefcount(var)}" )

var = 350 # when assign new value it overwrite the old one so new id
print(id(var))

# list
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

# 1 object for num1 and num2
num1 = 896
num2 = 896 
print(id(num1)) # same address
print(id(num2))
# between -5 - 256 python use the same address cuz it knows that its the same number 
# print(f"references to var: {sys.getrefcount(num1)}" )


# 2 object for list1 and list2
list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))

""" references type: 
# shared references, 
# strong references: function name, variable name,...
# weak references: do not keep object alive. it only point to the obj and if the obj not use anymore it can be free for garbage collector
# circular: bug & cause memory leak 
# example for circular references """
class Circular:
    def __init__(self):
        self.obj = None
        
        
obj1 = Circular()
obj2 = Circular()

#circular 
obj1.obj = obj2
obj2.obj = obj1
    

# weak references
import weakref

# creating weak reference
class MyClass:
    def __init__(self, value):
        self.value = value
        
obj3 = MyClass("hello") #obj3 is a strong references
obj4 = weakref.ref(obj3) # obj4 is a weak references

if obj4() is not None:
    print("object is still alive")
else:
    print("object has been freed")
    
    
# now delete the strong ref
del obj3

if obj4() is not None:
    print("object is still alive")
else:
    print("object has been freed")


""" unpacking: python allows any iterable to be unpacked into multiple variables at once """
a = 10
b = 20

a , b = b , a # this is tuple
print(a,b)

# string
a, b , c = 'xyz'
print(a,b,c)


# set
s = {'h', 'i'}

a1, a2 = s
print(a1, a2)

# dict
dict = {'key1' : 'value1',
        'key2': 'value2',
        'key3': 'value3'}

k1,k2,k3 = dict # only the key
print(k1,k2,k3)

v1, v2, v3 = dict.values() # only values
print(v1,v2,v3)

i1, i2, i3 = dict.items() # tuple of key and value
print(i1,i2,i3)

# nested unpacking
list3 = [1,2,3,4,5,6,7]
a , *middle, b, c = list3
print(a, middle, b, c)

list4 = [1,2,3]
list5 = [5,6,7]
list_sum = [list4 , list5] # output: [[1, 2, 3], [5, 6, 7]]
list_sum = [list4 + list5] # output: [[1, 2, 3, 5, 6, 7]]
list_sum = [*list4 , *list5] # output: [1, 2, 3, 5, 6, 7] # one dimensional unpacking

nested = [1,2,[3,4]]
o, b, (m1,m2) = nested
print(o,b, m1,m2)

list6 = [1,2,3, 'xyz']
b1, *b2, (b3,b4,b5) = list6
print(b1,b2,b3,b4,b5)


def func1(a,b,*args): #positional parameter
    print(f'a={a}, b={b}, c={args}')
    
func1(1,2,3,4,5,'j')

# keyword parameter
# *c = arbitrary parameter
def func2(a,b,*c,d=0):
    print(f'a={a}, b={b}, c={c}, d={d}')
    
func2(1,2,3,4,5)
# or func2(1,2,3,4,d=5) if the parameter is just d

def func3(**kwargs): #kwargs will be dictionary
    for key, arg in kwargs.items():
        print(f"key={key}, arg={arg}")
        
func3(a=7, b=3.5, c='hi', d=(10,11))
print(type(a))

a = {'a': 1,
     'b': 2,
     'c': 3
     }

print(len(a))

average = sum(a.values())/len(a)
print(average)
print(a.values())
# challenge 1: 
# write a function that accept any number and any type of parameter use the unpacking
# if the function receives a dictionary calculate the average of the values
# if the passed parameter contain non-numeric element convert to 0
my_data = {"key": "value"}
if isinstance(my_data, dict):
    print("It's a dictionary!")

# def func4(*args, **kwargs):
#     # thought process: 
#     # goal: only want number to calculate average
#     # store num in list -> calculate average
#     result = []
#     for i in args:
#         if isinstance()
        
# def flexible_average(*args, **kwargs):
#     values = []
#     # Process positional args
#     for arg in args:
#         if isinstance(arg, dict):
#             for v in arg.values():
#                 try:
#                     values.append(float(v))
#                 except (ValueError, TypeError):
#                     values.append(0.0)
#         else:
#             try:
#                 values.append(float(arg))
#             except (ValueError, TypeError):
#                 values.append(0.0)
#     # Process keyword args values
#     for v in kwargs.values():
#         try:
#             values.append(float(v))
#         except (ValueError, TypeError):
#             values.append(0.0)
#     return sum(values) / len(values) if values else 0.0

# print(flexible_average({"a": 10, "b": 20, "c": "x"}))
