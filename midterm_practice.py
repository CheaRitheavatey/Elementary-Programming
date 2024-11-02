# task 1
def task1():
    newlist = [i if i % 5 != 0 else '!' for i in range(25)]
    return newlist

# print(task1())

# task 2
def task2():
    while True:
        try:
            num1 = input('Enter first number: ')
            num2 = input('Enter second number: ')

            num1 = int(num1)
            num2 = int(num2)

            result = num1 // num2
            remainder = num1 % num2

            print( f'{num1} / {num2} = {result}, remainder {remainder}')
        except ValueError:
            print("please input integer try again")
            continue
        except ZeroDivisionError:
            print("second number cannot be zero try again")
            continue

        else:
            again = input("Do you want to enter again? (y/n): ")

            if again.lower() == 'y':
                continue
            else:
                break

# task2()

# task 3: find the shortest word in string
def task3(words):
    current = ''
    shortest = None
    for i in words:
        if i == ' ' or i == '-' or i == '_':
            if current: # only consider the non empty word
                if shortest is None or len(current) < len(shortest):
                    shortest = current
            current = ''
        else:
            current += i
    return shortest

# print(task3("i love you 11_111111111"))

# task 4:
def task4(string):
    dict = {}
    for char in string:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict

# print(task4('abaaabbcc'))

# task 5
def task5(list,add):
    list.insert(0,add)
    list.pop()
    return list

# print(task5([1,2,3,4,5],0))

'''
------------------------------------------------
              exercise at home
-------------------------------------------------
'''

"""
task 1: use list comprehension to create a list of number from 1-50. 
if divisbile by 3 add 'fizz' if divisible by 5 add 'buzz' if divisible by both add 'fizzbuzz'
"""

def exercise1():
    newlist = [
        'fizzbuzz' if i % 3 == 0 and i % 5 == 0 else 
        'fizz' if i % 3 == 0 else 
        'buzz' if i % 5 == 0 else
        i for i in range(50)]
    return newlist

# print(exercise1())

"""
task 2: write a one-liner that generate a list of the squares of even number from 1 to 30
"""
def exercise2():
    newlist = [i**2 for i in range(0,31) if i % 2 == 0]
    # newlist = []
    # for i in range(0,31):
    #         i = i**2
    #         newlist.append(i)
    return newlist
print(exercise2())

"""
task 3: create a function that asks the user to enter a minute value between 0-59.
if the input is invalid prompt the user to enter a valid minute until they do
"""
def exercise3():
    while True:
        try:
            user = input('Enter a minute value between 0 and 59: ')

            user = int(user)
            if 0 <= user <= 59:
                print( f'You enter {user} minutes')
            else:
                print('Invalid input')
                continue
        except ValueError:
            print( 'cannot be a string enter again')
        else:
            again = input('Do you want to enter again? (y/n): ')
            if again.lower() != 'y':
                break

# exercise3()
        
"""
task 4: create a class called movie with properties for title, director and release year.
implement the appropriate constructor and method that return a string representation of the movie in the formal: 'Title (Director, Year)'
"""    

class Movie:
    def __init__(self,title,director,release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def __str__(self):
        return f'{self.title} ({self.director}, {self.release_year})'
    

class MoiveCollection:
    def __init__(self):
        self.movies = []

    def add_movie(self,title,director,release_year):
        new_movie = Movie(title,director,release_year)
        self.movies.append(new_movie)
    
    def remove_movie(self,title):
        for movie in self.movies:
            if movie.title == title:
                self.movies.remove(movie)
                return f'{title} has been remove'
        
        return f'{title} not found in the collection'

    def count_movie(self):
        return f'Total movies: {len(self.movies)}'
    
    def show_movies(self):
        if not self.movies:
            return 'No movies in the collection'
        
        return '\n'.join(str(movie) for movie in self.movies)
    def find_movie(self,title):
        for movie in self.movies:
            if movie.title == title:
                return movie
        
        return f'{title} not found in the collecton'
    
collection = MoiveCollection()

# add movies
collection.add_movie("Avatar", "pixar",2022)
collection.add_movie("Inception", "Chirstopher",2001)
collection.add_movie("Mommy", "Joe",2008)

# show movies
print("current movie: \n")
print(collection.show_movies())

# count movies
print(collection.count_movie())

# find movie
print(collection.find_movie("Mommy"))
print(collection.find_movie("Mermaid"))

# remove movie
print(collection.remove_movie("Inception"))
print(collection.remove_movie("Matrix"))

# show movie after remove
print('Update movie collection')
print(collection.show_movies())


"""
task 5: write a function that check if a given number is prime
return true if it is prime and false otherwise
"""

def exercise5(number):
    if number <= 1:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
print(exercise5(11))
print(exercise5(20))