# 1 task - list comprehension
fruits = ["apple", "banana", "cherry", "orange", "lemon"]

result = [fruit for fruit in fruits if 'a' in fruit]
print(result)


nums = list(range(1,51))
new_list = [i**2 for i in nums if i % 2 == 0]
print(new_list)

draws = [
    [1, 5, 10, 20, 30],
    [3, 5, 7, 10, 88],
    [1, 3, 5, 7, 9]
]
new_draws1 = []

for i in draws:
    for j in i:
        if j >10:
            new_draws1.append(j)

new_draws = [j for i in draws for j in i if j > 10]
print(new_draws)
print(new_draws1)

# keep fruits of length 6
new_fruit = [fruit for fruit in fruits if len(fruit) >= 6]
print(new_fruit)
import random
for _ in range(3):
    numberrr = random.sample(range(1,9),5)
    print(' '.join(str(i) for i in numberrr))

# exercise 2 lottery simulation
def draw_lottery_numbers(filename='winning_number.txt', n=100):
    with open(filename, 'a') as l:
        for _ in range(n):
            number = random.sample(range(1,91),5)
            print(' '.join(str(i) for i in number), file=l)
                
lst = []
from collections import Counter
def count_frequencies(filename='winning_number.txt'):
    with open(filename, 'r') as l:
        for i in l:
            item = i.split()
            lst.extend(item)
    counter = Counter(lst)
    print(counter.most_common())
        
# immutable object = int float string tuple bool
# mutable object = list dict set 
a = [1,2]
b = a[:]
a.append(3)
print(a)
print(b)

c = 5
f = c
c +=3
print(f)
print(c)

# unpacking
nums = [1,2,3,4,5]
a, *middle, b = nums
print(a)      # 1
print(middle) # [2,3,4]
print(b)      # 5


pairs = [(1,2), (3,4), (5,6)]
for x, y in pairs:
    print(x,y)
    
    
d = {"a":1, "b":2}

for key, value in d.items():
    print(key, value)
    
    
a = [1,2,3]
b = a
b[0] = 100
print(a)


def add_student(students):
    students.append("Alice")
    return students

classroom = ["Tom", "Emma"]
new_classroom = add_student(classroom[:])

print(classroom)
print(new_classroom)

x = (1,2,3)
y = x
x = x + (4,)
print(y)

def min_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_max([10,2,1,3,4])
print(smallest, largest)

students = [
    ("Tom", 20),
    ("Anna", 22),
    ("Sam", 19)
]
for i in students:
    name, age = i
    print(f"{name} is {age} years old")