import math

# task 1:
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nStock: {self.stock}"

# child class
class DigitalProduct(Product):
    def __init__(self, name, price, download_url,file_size):
        super().__init__(name, price, stock=None)
        self.download_url = download_url
        self.file_size = file_size
    
    def __str__(self):
        return f"{super().__str__()} \nDownload URL: {self.download_url}\nFile Size: {self.file_size}"

# example
productOne = Product('Laptop',2100,5)
print(productOne)

productTwo = DigitalProduct('E-book',15,'http://lib.com/ebook',5)
print(productTwo)

# task 2
def task2():
    try:
        vowel= "aeiou"
        vowel_string = ''

        user = input("Enter a text: ")
        count = len(user.split(" "))

        # dictionary to store vowel
        dict = {}
        for char in user:
            if char in vowel:
                vowel_string += char

        for i in vowel_string:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        
        return f"Number of word: {count}\nVowel: {dict}"
    except AttributeError:
        print("The text cannot be empty")
        
print(task2())

# task 3
def task3(x,y):
    try:
        x = list(x)
        y = list(y)

        distance = math.sqrt(((x[1] - x[0])**2) + ((y[1] - y[0])**2))
        return f"Distance: {distance}"

    except TypeError:
        print("Invalid input")

point1 = (1,2)
point2 = (4,6)
print(task3(point1,point2))