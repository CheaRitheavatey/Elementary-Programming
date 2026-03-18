"""Advanced OOP"""

# attribute
class Student:
    school = 'pecs university'
    def __init__(self, name, grade):
        self.name =name
        self.grade = grade
    
    # getter and setter
    def get_grade(self):
        return self.get_grade
    
    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.grade = grade
        return self.grade
s1 = Student('joe', 12)
print(s1.name)
print(s1.school)
print(s1.grade)

s1.school = "Other School" # This creates a new instance attribute, NOT changing the class one.
print(s1.school)


# or another way to setter and getter
""""  @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            print("Invalid grade")"""
            
            
# class method
class Student:
    school = "UP"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name
        
        
Student.change_school("New University")

# factory method
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, data):
        name, grade = data.split(",")
        return cls(name, int(grade))

s = Student.from_string("Anna,90")

# static method = no self no cls
# when to use static method?
# when logic belongs to class
# doesnt need object or class
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(2,3))

class Student:
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade   # private

    # property (getter)
    @property
    def grade(self):
        return self._grade

    # property (setter)
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            print("Invalid grade")

    # class method (factory)
    @classmethod
    def from_string(cls, data):
        name, grade = data.split(":")
        return cls(name, int(grade))

    # static method
    @staticmethod
    def is_passing(grade):
        return grade >= 50
    
    
s1 = Student("Anna", 80)

# property
print(s1.grade)
s1.grade = 95
s1.grade = 150   # invalid

# class method
s2 = Student.from_string("Bob:40")
print(s2.name, s2.grade)

# static method
print(Student.is_passing(s1.grade))  # True
print(Student.is_passing(s2.grade))  # False


"""
CLASS CODE: OOP 1

"""
class Person:
    __slots__ = ('name', 'id') # to prohibit the dynamic way of ptyhon, now the person2.profession will give error
    
    species = 'Homo sapiens' # class variable is static variable but they are inherited
    # python have only 1 constructor unlike java cuz python cannot do overriding
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    
    @classmethod
    def print_species_classmethod(cls):
        print(cls.species)
    
    @staticmethod
    def print_species_staticmethod():
        print(Person.species)
        
    @classmethod
    def from_json(cls, input_str):
        split_text = input_str.split(',')
        name = split_text[0]
        id = split_text[1]
        return cls(name, id)
    
# even if nothing is inside the person class we can still instaniate it
person1 = Person('joe', 1)
print(person1.__dir__())

# when we class Person() like person1 = Person('joe')
# this is what run in the background
person2 = object.__new__(Person)
person2.__init__('james',2)

person3 = Person.from_json('jack,12')
print(person3.name)
print(person3.id)

# in this case the profsesion is only link to person2 
# this is the dynamic property of python
# person2.profession = 'developer'
# print(person2.profession)

"""class methods and static methods
class method = can be use as an alternative constructor
             = to create a new instance or object


"""
class MyNewClass:
    # instance method
    def instance_method(self):
        print(f"hello instance: {self}")
        
        
    # class method
    @classmethod
    def class_method(cls):
        print(f'hello class {cls}')
        
    # static method
    @staticmethod
    def static_method():
        print('hello static method')
        

        
        
mn = MyNewClass()
mn.instance_method() # will return memory address

mn.class_method() # hello class <class '__main__.MyNewClass'>
# we can use class method through class=> class method can be reach through object and class itself
MyNewClass.class_method()

mn.static_method()
MyNewClass.static_method() # same with static method

"""inheritance"""
class User(Person):
    species = 'another species'
    def __init__(self, name, id, login_name):
        super().__init__(name, id) # super() is a proxy object
        self.login_name = login_name
        
        
user1 = User('jack',3,'jackkkss')
print(user1.name)
print(user1.id)
print(user1.login_name)

user1.print_species_staticmethod()
user1.print_species_classmethod()

# how to check which class instance belong to
# type() will give the class it instancitate from but wont show the one they inherited
print(type(person1)) # output: <class '__main__.Person'>
print(type(user1)) # output: <class '__main__.User'>

# isinstance() -> will check the class they inherited too
print(isinstance(user1, User))
print(isinstance(user1, Person))

# multiple inheritance
class Student:
    def __init__(self, student_id):
        self.student_id = student_id

class NeptunUser(User, Student):
    
    def __init__(self,name, id,login_name, student_id, neptun_code):
        User.__init__(self, name, id, login_name)
        Student.__init__(self, student_id)
        self.neptun_code = neptun_code
    
        
neptun_user1 = NeptunUser('joey', 4, 'joeeyy', 999,'1h1h1h')
print(neptun_user1.neptun_code)

"""MRO: method resolution order
    A 
  /   \
 B      C
 \     /
    D
    
this diamond shape: if we instanitate from class D then it will be D field/method -> B, C field/method -> lastly A
"""

class A:
    num = 10 # class variable

class B(A):
    num = 20 # class variable
    
class C(A):
    num = 30 # class variable
# class C:
#     num = 30 # class variable 
# if class C is not inherited from the same class as B then it will backtrack to class A first then C is the last

class D(B,C):
    pass


print(D.num)
print(D.mro())