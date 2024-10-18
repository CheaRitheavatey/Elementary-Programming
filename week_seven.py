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
dog.bark()
print(dog)

class Cat(Animal):
    # constructor
    def __init__(self, name, color, age):
        super().__init__(name, color, age)
    def __str__(self):
        return super().__str__()
    def sound(self):
        print(f"{self.name} is meowing")

cat = Cat("titi","blue",1)
cat.sound()

print(cat)