class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def print(self):
        print( ("*  " * self.width + "\n") * self.height )


r = Rectangle(5, 10)
print(r.area())
print(r.perimeter())
r.print()