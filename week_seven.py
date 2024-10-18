class Point:
    # constructor
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    # string representative
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    # getter and setter
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def setX(self,x):
        self.x = x
    def setY(self, y):
        self.y = y
    
    # methods


point = Point(10,12)
# print(point)

point.z = 100 # create a new property outside the class 
# print(point.z)
# del point.z # deleting point z
# print(point.z) # will cause error because z has already been deleted


# inheritance

# parent class
class Animal:
    # constructor
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    # act as like printing method
    def __str__(self):
        return f"animal: \nname: {self.name}\ncolor: {self.color}\nage: {self.age}"
    
    # method
    def walk(self):
        print(f"{self.name} is walking")

class Dog(Animal): # this is like extends
    # constructor
    def __init__(self, name, color, age, breed):
        super().__init__(name,color,age) # calling constructor of parent class constructor
        self.breed = breed
    
    def __str__(self):
        return f"{super().__str__()}\nbreed: {self.breed}"
    
    def bark(self):
        print(f"{self.name} is barking")


dog = Dog("toto","white",3,"chiwawa")
# dog.bark()
# print(dog)

class Cat(Animal):
    # constructor no need to create again because it is thes same as parent
    def sound(self):
        print(f"{self.name} is meowing")

cat = Cat("titi","blue",1)
# cat.sound()

# print(cat)

class Jaguar(Animal):
    def __init__(self, name ,age):
        super().__init__(name, color="black", age=age)
        

jaguar = Jaguar("jak",4)
# jaguar.color = "white"
print(jaguar)


from math import pi
from math import pow
class Circle:
    # constructor
    def __init__(self,radius):
        self.radius = radius
    
    def parameter(self):
        parameter = 2 * pi * self.radius
        return parameter
    
    def area(self):
        area = pi * pow(self.radius,2)
        return area
    
    def __str__(self):
        return f"circle has raidus {self.radius}\nparameter: {self.parameter()}\narea: {self.area()}"

circle = Circle(5)
# print(circle)


class Food:
    # constructor
    def __init__(self,name,calories):
        self.name = name
        self.calories = calories
    
    def getKcal(self):
        return self.calories/1000
    
    def __str__(self):
        return f"food name: {self.name} \ncalories: {self.calories} \ngetKcal method:{self.getKcal()}"
    

class Vegetable(Food):
    def __init__(self, name, calories=0):
        super().__init__(name, calories)

    def getKcal(self):
        return super().getKcal() + 10

vegetable = Vegetable("carrot")
vegetable.calories = 200
print(vegetable)

# practice
class Bank:
    # constructor
    def __init__(self,name,accountNumber,balance,):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
    # methods
    def withdraw(self,withdrawAmount):
        if withdrawAmount > self.balance or self.balance == 0:
            return "not enough balance to withdraw"
        else:
            self.balance = self.balance - withdrawAmount
            return f": withdraw amount: {withdrawAmount}\ntotal balance: {self.balance}"
    
    def deposit(self,depositAmount):
        self.balance += depositAmount
        return f"depoist: {depositAmount}\ntotal balance: {self.balance}"
    
bank = Bank("abc",1,1200)
print(bank.deposit(200))
print(bank.withdraw(4000))

