def listPractice():
    thisList = [1,5.5,"text",[1,2]]
    print(thisList)
    print(thisList[:]) # print all element from index 0 to the end => same result as above

    secondList = list((1,3,4,5,7)) # use list() function to create a new list
    secondList[3:5] = [9,9,9] # the original end on index 4 but when add this line until index 5 also okay
    print(secondList)
    
    num = [1,2,3,4]
    num.insert(0,'a')
    print(num)

    num = (1,2,3,4) # a tuple
    secondList.extend(num)
    print(secondList)

    """ 
    print([x for x in num]) # also the same as

    for x in secondList:
        print(x)
    """

# listPractice()

# comprehension list
# num = [1,2,3,4,5,6,7,8,9]

# print even number
# print([x for x in num if x % 2 == 0])

# print all element
# print([x for x in num])


# practice 1
def animal(list):
    newList = []
    # comprehension 
    newList = [i for i in list if 'i' in i.lower()]
    return newList

    # for loop
    for i in list:
        if "i" in i.lower():
            newList.append(i)
    return newList
        
a = ["cat", "dog", "bird", "giraffee", "Inu"]
# print(a)

# print(animal(a))

# sort and reverse method
b = [1,7,4,5,0,3,2,7,0]
b.sort(reverse=True)
# print(b)

def tuplePractice():
    number = (1,2,3,4) # this is tuple

    # creating new tuple
    number2 = tuple((10,11,12))
    print(number + number2)
    
    # need to add , if there's only one element inside a tuple
    number3 = (1,)
    number4 = (1) # this will return as list or in this case int

    # convert tuple to a list
    number2 = list(number2)
    print(number2) # this way we can use the same functions list have to modify 

    # convert list to tuple
    number2 = tuple(number2)

    # unpack a tuple: assigning variable to each item inside a tuble
    (*ten, eleven, twelve) = number2 # put * will make it a list
    print(ten)

# tuplePractice()

def setPractice():
    aset = {1,2,3,4}
    aset.add(1000) # random order in set
    aset.update(['a','b','c']) # random order in set
    aset.remove('c') # will raise an error if the element you want to remove doesnt exist
    aset.discard(3) # will not raise an error if the element you want to remove doesnt exist
    print(aset)

# setPractice()

def dictPractice():
    dict = {
            'name': "joe",
            'age': 10,
            'job': 'student'
        }
    
    print(len(dict))
    print(dict['age']) # get the value of 10 & we can also assign new value with that as well
    print(dict.get("job")) # same as above
    print(dict.keys()) # return all the keys in dict
    print(dict.values()) # return all the values in dict
    print(dict.items()) # return all items in dict as tuple
    dict.update({"id": 1}) # add another dictionary 
    print(dict)

# dictPractice()

# practice 2
def month(dict):
    newMonth = {}
    x = list(dict.values())
    number = x[0]
    month = x[1]
    for i in range(len(number)):
        # newMonth[number[i]] = month[i] 
        newMonth.update({number[i]:month[i]})
    return newMonth
        

        

        
       
            
a = {
    'month': [1,2,3],
    'name': ['jan','feb', 'mar']
}

print(month(a))