class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def area(self):
        # Area of all sides of the parallelepiped
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()  # Call the display method from Rectangle
        print(f"Height: {self.height}")
        print(f"Volume: {self.volume()}")


# Example usage
if __name__ == "__main__":
    rect = Rectangle(4, 5)
    rect.display()
    
    
    para = Parallelepiped(4, 5, 6)
    para.display()