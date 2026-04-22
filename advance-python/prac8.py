""" 
enumerations

- immutable collection of constant
- difference: values can also be assigned to constants
but those values themeselves can be mutable

- special enum: IntEnum, Flag, IntFlag

"""
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
    # Color: the enumeration itself
    # Color.RED: a member of the enumeration
    # member have assigned values
    # the type of the member matches the type of the enumeration
    # 'is' and 'in' also work here
    # Color.RED in Color -> True
    # Color.RED is Color.BLUE -> False
    

class Status(Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'
    
class UnitVector(Enum):
    # can also be a tuple
    V1D = (1,) #  need , to make it a tuple
    V2D = (1,1)
    V3D = (1,1,1)
    
print(Color.RED)
print(Color.RED.value)
print(UnitVector.V2D)
print(UnitVector.V2D.value)
print(Status.PENDING)       # name
print(type(Status.PENDING)) # type
print(Status.PENDING.value) # value

a = Status.PENDING
print(a is Status.PENDING) # 'is' and == work here for both

# print(Color.RED < Color.BLUE) # give type error
print(Color.RED.value < Color.BLUE.value)

# enum is iterable 
for member in Status:
    print(repr(member)) # repr() = representation of the member
    # output will be both name and value 
    # <Status.PENDING: 'pending'>
    # <Status.RUNNING: 'running'>
    # <Status.COMPLETED: 'completed'>
    
    
    print(member) # will give only name

print(Color.__members__) # will print all member
print(list(Status)) # item will be in the same order
print(list(Status)[0] is Status.PENDING)


# interitance: enum can be extend but only if it has no member yet

"""
Exception handling - custom exception class

heirarchy: base exception is the mother and other inherit from base exception
but some of the child is for hardware, 
so normally we use exception class
"""

# custom exception
# days are represented by numbers: monday - 1, tue - 2, ...
# write 2 custom exception: one for invalid day (e.g. day = 0, -1, 10)
# and prevent weekend booking 

class InvalidDayError(Exception):
    def __init__(self, message):
        super().__init__(message)
        

class DayOutOfRangeError(InvalidDayError):
    def __init__(self, message):
        super().__init__(message)
        
class Date:
    def __init__(self,day):
        self.day = day
    
    def reserve_day(self):
        if self.day < 1 or self.day > 7:
            raise InvalidDayError("there is no such day")
        
        if self.day == 6 or self.day == 7:
            raise DayOutOfRangeError("you cannot make a reservation for the weekend")
        
        else:
            match(self.day): # similar to switch case
                case 1: print("your reserved day is monday")
                case 2: print("your reserved day is tuesday")
                case 3: print("your reserved day is wednesday")
                case 4: print("your reserved day is thursday")
                case 5: print("your reserved day is friday")

date1 = Date(5)
try: # need a try block
    date1.reserve_day()
except InvalidDayError as e:
    print(e)

# example
# virtual banking application, where custom exception class handle different type of transaction error
# type of error:
class TransactionError(Exception): # super class
    def __init__(self, message):
        super().__init__(message)
        

class InsufficientFundErrorClass(TransactionError): # withdrawal related problem
    def __init__(self, amount, balance):
        message = f"Insufficient funds to complete transaction, Amount: {amount}, Balance: {balance}"
        super().__init__(message)
        
class InvalidTransactionError(TransactionError):
    def __init__(self, transcation_id):
        message = f"Invalid Transaction, Transaction ID: {transcation_id}"
        super().__init__(message)

class BankAccount:
    valid_transaction_id = ('1100', '1111')
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundErrorClass(amount, self.balance)
        
        self.balance -= amount
        print(f"withdrawal of {amount} successful")
        
    def transaction(self, transaction_id):
        if transaction_id not in BankAccount.valid_transaction_id:
            raise InvalidTransactionError(transaction_id)
        

account1 = BankAccount(1000)
try:
    account1.withdraw(50)
except TransactionError as e:
    print(e)
    
try:
    account1.transaction('1111')
except TransactionError as e:
    print(e)
    
    
# challenge5:
# write a custom class that has one (number) attribute
# and give this attribute an initial value
# using a descriptor class, implement it in such as way
# that the value of the attribute can only be modified
# if the new value is greater than the previous one

class NumberError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class LessThanNumberError(NumberError):
    def __init__(self, message):
        super().__init__(message)
        
class NotANumberError(NumberError):
    def __init__(self, message):
        super().__init__(message)
class Number:
    # initial number
    number = 10
    def __init__(self):
        pass
            
    def setNumber(self, num):
        if isinstance(num, str):
            raise NotANumberError("It is not a number")
        
        if num < self.number:
            raise LessThanNumberError(f"number is less than initial number {self.number}")
        else:
            self.number = num
            print(f"new number: {self.number}")
        
 

# case 1: number less than 10 it should raise error
num1 = Number()
try:
    num1.setNumber(1)
except NumberError as e:
    print(e)

print()
# case 2: number more than 10 it should be ok
num2 = Number()
try:
    num2.setNumber(100)
except NumberError as e:
    print(e)

print()

# case 3: number is not a number it should raise error
num3 = Number()
try:
    num3.setNumber('jjj')

except NumberError as e:
    print(e)

print()

# case 4: set num2 which is valid (100) to 3 which less than a 100 it should raise error
try:
    num2.setNumber(3)
except NumberError as e:
    print(e)

        


class Increasing:
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("must be int/float")
        current = instance.__dict__.get("number")
        if current is None or value > current:
            instance.__dict__["number"] = value
        else:
            raise ValueError("new value must be greater than previous value")

class Number:
    number = Increasing()
    def __init__(self, initial):
        self.number = initial
# demo
n = Number(5)
print(n.number)   # 5
n.number = 8      # OK
print(n.number)   # 8
try:
    n.number = 3  # ValueError
except ValueError as e:
    print("error:", e)