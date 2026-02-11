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
        
