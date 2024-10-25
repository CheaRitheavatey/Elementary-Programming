# practice for exam

# task 1: use comprehension list to add range numbers to the list if its not divisible by 5 and add ! if it is
def task1():
    # newlist = [i if i % 5 != 0 else 'i' for i in range(25)] my code
    newlist = ['!' if i % 5== 0 and i !=0 else i for i in range(25)] #teacher code
    return newlist

# print(task1())

# task 2: divide first by second number and also show the  remainder also handle error
def task2():
    print("Enter 2 integers number")
    while True:
        try: 
            x = input("Integer one: ")
            y = input("Integer two: ")
            
            x = int(x)
            y = int(y)

            z = x & y
            divide = x // y

            return f"{x} divded by {y} equal to {divide} and {z} remains"
        
        except ValueError as e:
            print(f"{e} try again")
            # continue
        except ZeroDivisionError as e:
            print(f"{e} try again")
            # continue
            

# print(task2())

# task 3: write a function that find the longest word in a string
def task3(words):
    # way 1 to do this
    currentWord = ''
    longestword = ''
    for char in words:
        if char == ' ' or char == '-' or char == '_':
            if len(currentWord) > len(longestword):
                longestword = currentWord
            currentWord = ''
        else:
            currentWord += char

    return longestword

    # way 2 to do this
    word = words.split(" ")
    return max(word,key=len)


# print(task3("hello_worlddddddd! 111111111 this is a python class!"))

# task 4: write a function that put elements and frequencey of a string into a dictionary 
def task4(setence):

    dict = {}
    for char in setence:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
            
    return dict

# print(task4("aaa bbb"))

# task 5: write a function that add an element to the begining of a list, remove an element from the end of the list and then print lis
def task5(add,list):
    # [1,2,3]
    list.insert(0,add)
    list.pop()

    return list

# print(task5(2,[1,2,3]))

# task 6: write code in one line:
age= 0
# print("adult") if age > 18 else print("teenager") if age >= 13 else print("child")

# task 7: create a function and ask the user to enter an hour between 0-23
def task7():
    hours = {
        range(4,11): 'morning',
        range(11,16): 'noon',
        range(16,20): 'evening',
        range(20,24): 'night',
        range(0,4): 'past midnight' 
    }
    try:
        user = input("Enter an hour between 0-23: ")
        user = int(user)

        for i in hours.keys():
            if user in i:
                return hours[i]
        else:
            print("invalid")

    
    except ValueError as e:
        print(e)
    
# print(task7())
        

# task 8: create a book class with title anuthor and isbn properites. create the apporriate construcotr and string representative
class Book:
    def __init__(self, title, author, isbn, genre=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        # self.dict = dict

    
    def __str__(self):
        genreInfo = f"\nGenre: {self.genre}" if self.genre else ''

        return f"Titile: {self.title} \nAuthor: {self.author} \nISBN: {self.isbn}{genreInfo}"
    
    # def addBook(self, title, author, isbn):
    #     self.dict.update({title:author})
    
book = Book("abc", "xyz", 11111111111,"00")
print(book)


    