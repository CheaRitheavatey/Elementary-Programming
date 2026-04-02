# # challenge5:
# # write a custom class that has one (number) attribute
# # and give this attribute an initial value
# # using a descriptor class, implement it in such as way
# # that the value of the attribute can only be modified
# # if the new value is greater than the previous one


# # using exception what we learn
class NumberError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class LessThanNumberError(NumberError):
    def __init__(self, message):
        super().__init__(message)
        
class NotANumberError(NumberError):
    def __init__(self, message):
        super().__init__(message)

class Increase:
    def __set__(self, instance, value):
        if isinstance(value, str):
            raise NotANumberError("not a number")
        current = instance.__dict__.get("number")
        
        if current is None or value > current:
            instance.__dict__["number"] = value
        else:
            raise LessThanNumberError("number is less than initial number")

class Number:
    number = Increase()
    def __init__(self, initial):
        self.number = initial

n = Number(5)
print(n.number)   # 5
n.number = 8      # OK
print(n.number)   # 8
try:
    n.number = 3  # number error
except NumberError as e:
    print("error:", e)