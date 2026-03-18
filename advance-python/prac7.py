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