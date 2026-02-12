# challenge 1: 
# write a function that accept any number and any type of parameter use the unpacking
# if the function receives a dictionary calculate the average of the values
# if the passed parameter contain non-numeric element convert to 0

def func4(*args, **kwargs):
    # thought process: goal is to take all the num and give average
    # store all num in one place and set other to 0
    # some edge case i can think of like '4' -> try to convert it to float
    
    # store number
    result = []
    
    for i in args:
        if isinstance(i, dict): # check if its a dict type
            for j in i.values():
                try:
                    result.append(float(j))
                except (ValueError, TypeError):
                    result.append(0)
                    
        else:
            try:
                result.append(float(i))
            except (ValueError, TypeError):
                result.append(0)
                
    # key word value
    for i in kwargs.values():
        try:
            result.append(float(i))
        except (ValueError, TypeError):
            result.append(0)
            
    return sum(result)/ len(result) if result else 0

print(func4(1,2,3))
print(func4(1,2,3, 'adj', '5'))
print(func4([1, '2', 3.5], x=4, y='foo'))
print(func4(5))
print(func4('df'))
print(func4({"a":10}))
print(func4(1,2,'dd',{"a":10}))
print(func4(x=5, y=10))


