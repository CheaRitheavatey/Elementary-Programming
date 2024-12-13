from random import randint
# practice
"""
Task 1: create 26 random numbers between 1 and 5. sotre the number in a list:
    1. the first element is the first random number
    2. the seoncd elemnt is the first element + second random number
    3. the third element is the second element + third random number...
    4. the element number N is the element [number N-1] + the Nth random number
    5. print all the lement of the list, each elemnt in a new line 
"""
def task1():
    
    list = []
    i = 1
    
    first = randint(1,5)
    list.append(first)
    print("First element: ", first)

    while i <5:
        random = randint(1,5)
        print("Random: ",random)
        random += list[i-1]
        print(f"Element {i}: ", random)
        list.append(random)
        i+=1

    return list

# print(task1())

# teacher answer
# so first you have to generate all the random number first then you create another list and add it
# so it look sth like this [2,5,3,6,1] then you just create a new list and add the element -> [2,7,8,9,7]
def res1():
    while True:
        try:
            a = input("lowest number (1-3): ")
            b = input("highest number (4-5): ")

            a = int(a)
            b = int(b)

            if (a in range(1,4)) and (b in range(4,6)):
                randlist = [randint(a,b) for i in range(5)]
                print("random list: ",randlist)
                randlistupdate = []
                randlistupdate.append(randlist[0])
                for i in range(1,len(randlist)):
                    randlistupdate.append(randlist[i]+ randlist[i-1])

                for i in randlistupdate:
                    print(i)
                break
            else: 
                print("invalid")
                continue       
        except ValueError:
            print("Invalid")
            continue
        
            

# res1()


def task2():
    while True:
        try:
            a = int(input("lowest: "))
            if 1 <= a <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("wrong input, try again")
    
    while True:
        try:
            b = int(input("highest: "))
            if 4 <= b <= 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("wrong input, try again")
    
    print(f"lowest {a} and highest {b}")
    randlist = [randint(a,b) for i in range(5)]
    print("random list: ",randlist)
    randlistupdate = []
    randlistupdate.append(randlist[0])
    for i in range(1,len(randlist)):
        randlistupdate.append(randlist[i]+ randlist[i-1])
    
    print(randlistupdate)
    
    for x in range(len(randlistupdate)):
        for i in randlistupdate:
                print(
                    f"{i} {'-'*i} \\ {'skier' if i == randlistupdate[x] else ''} "
                    )
                
task2()