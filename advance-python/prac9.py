# metaprogramming = create class dynamically

# many python tools are built on this like decorators, dataclass, enum, orm, django, validation libraries, testing frameworks, plugin system

# metaprogramming mean do sth like modify or create other part of program

# reminder 1: class is an object
class Student:
    school = "univeristy of pecs"
    def __init__(self, name,neptun):
        self.name= name,
        self.neptun = neptun
        
    def introduce(self):
        return f"my name is {self.name} with neptun {self.neptun}"
        
s = Student('joe', 'abd123')

    # s is an instance of student
    # student is an instance of type
    # type is the default "class factory" aka metaclass
    
print(type(Student))
print(Student.__dict__) # they are not the same
print(s.__dict__) 


# class can be modify at runtime cuz class is an object
class Person:
    pass

print(Person.__dict__)
# adding new class attribute
Person.speciecs = "human"
print(Person.speciecs)

# add new method
def say_hello(self):
    return f"hello {self.name}"

Person.say_hello = say_hello

p = Person()
p.name = 'Anna' # adding attribute
print(p.say_hello())


def add_describe_method(cls):
    def describe(self):
        return f"{cls.__name__} object with attribute {self.__dict__}"
    
    cls.describe = describe
    return cls

@add_describe_method
class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price
@add_describe_method
class Course:
    def __init__(self, title, credit):
        self.title = title
        self.credit = credit
        
        
product=  Product('laptop',1000)
course=  Course('math',4)

print(product.describe())
print(course.describe())

# the @add_describe is a class decorator that take class a parameter instead of function


# dataclass
# is a function -> automatic modification of classes
# add dunder method based on the field

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    
b = Book('book1', 'author1', 2002)

# we didint write init method and its not empty constructor but we can use it
# why? cuz dataclass annotation, it automatically generate the method

# type
# type can be used in 2 ways:
#     1. type(obj) -> tell us the type of object
#     2. type(class_name, bases, namespace) have 3 parameters -> dynamically create a new class
    
# so class keyword is not the only way to create a class
class Animal:
    species = "unknown"
    def speak(self):
        return "some sound"
    
a = Animal()
print(a.speak())
print(type(Animal))

# the above is the regular or usual way we create class

# now lets do the same with type
def speak(self):
    return "some sound using type"

AnimalDin = type("AnimalDin", # this is the class name 
(), # this is the base which is a tuple (classes it inherit from)
 {"speak": speak,
                  "species": speices # class namespace
                  }
                 )

ad = AnimalDin()


import math
def circle_init(self,r):
    self.r = r
def circle_area(self):
    return math.pi * self.r **2
def circle_circunference(self):
    return math.pi * self.r *2

CircleDin = type(
    "CircleDin",
    (),
    {
        "__init__": circle_init,
        "area": circle_area,
        "circumfernce": circle_circunference
        
    }
)

cir = CircleDin(12)
print(cir.area())
print(cir.circumfernce())
print(cir.__dict__)

# how is class create?
# read name of the class -> read baes class (inherit or sth) -> create a namespace for class body -> execute the code in class body inside that namespace
# -> python create teh class object based on that namespace

# by default the class object is created by type

# custom metaclass
# when do we write our custom metaclass? when we want to control the creation of classes centrally
# example, we want class automatically recieve an id attribute if programmer forgot to define one
class RequireId(type):
    def __new__(cls, name, bases, namespace):
        print(f"creating class {name}")
        if "id" not in namespace:
            namespace["id"] = None
        return super().__new__(cls, name, bases, namespace)
    
class Product(metaclass=RequireId):
    name = "unknown"
    
class User(metaclass=RequireId):
    name = "anonymous"
    
print(Product.id)
print(User.id)

# class decorator vs metaclass
# both use for modify classes
# but they are not meant for the same purpose

# deorator: simpler, modifies a class that already been create, generally this is what we gonna use

# metaclass: more complicate, intervenes in teh process of class creation, useful when we want to centrally control the creation of many classes

# decorator classes = a class that decorate function
# decorator class != class decorator

class Logger:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args, **kwargs):
        print(f"log: {self.fn__name__} called")
        return self.fn(*args, **kwargs)
    
@Logger
def say_hello():
    return "hello"
print(type(say_hello)) # __main__.Logger