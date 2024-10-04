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
    u = [print(x) for x in secondList] # also the same as
    print(u)
    
    for x in secondList:
        print(x)
    """

# listPractice()

# comprehension list
num = [1,2,3,4]
print([x for x in num])