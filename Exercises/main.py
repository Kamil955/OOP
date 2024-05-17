import math

class Rectangle:
    def __init__(self, name, a, b):
        if a<=0 or b<=0:
            raise ValueError("length must be a positive number.")
        self.name = name
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def circuit(self):
        return 2 * self.a + 2 * self.b
    def get_name(self):
        return self.name

class Circle:
    def __init__(self, name, radius):
        if radius<=0:
            raise ValueError("radius must be a positive number.")
        self.name = name
        self.radius = radius
    def area(self):
        return self.radius**2 * math.pi
    def circuit(self):
        return 2 * self.radius * math.pi

    def get_name(self):
        return self.name

class IsoscekesTriangle:
    def __init__(self, name, a, b):
        if a<=0 or b<=0:
            raise ValueError("length must be a positive number.")
        self.name = name
        self.a = a
        self.b = b

    def area(self):
        p  =(self.a + self.a + self.b)/2
        s= math.sqrt(p *(p-self.a)* (p- self.a) *(p-self.b))
        return s

    def circuit(self):
        return 2* self.a + self.b

    def get_name(self):
        return self.name

figures = ["Rectangle", "Circle", "IsoscelesTriangle", "Stop"]

while True:
    figure_input = input(f"Enter name of the figure that you want to use ({figures}): ")

    if figure_input.capitalize() in figures:
        if figure_input.capitalize() == "Rectangle":
            name = input("Enter name of the rectangle: ")
            length = float(input("Enter length of the rectangle: "))
            width = float(input("Enter width of the rectangle: "))
            try:
                rectangle = Rectangle(name, length, width)
                print("Area:", rectangle.area())
                print("Circuit:", rectangle.circuit())
                print("Name:", rectangle.get_name())
            except ValueError as e:
                print("Error:", e)

        elif figure_input.capitalize() == "Circle":
            name = input("Enter name of the circle: ")
            radius = float(input("Enter radius of the circle: "))
            try:
                circle = Circle(name, radius)
                print("Area:", circle.area())
                print("Circuit:", circle.circuit())
                print("Name:", circle.get_name())
            except ValueError as e:
                print("Error:", e)

        elif figure_input.capitalize() == "IsoscelesTriangle":
            name = input("Enter name of the isosceles triangle: ")
            side = float(input("Enter length of the equal side of the triangle: "))
            base = float(input("Enter length of the base of the triangle: "))
            try:
                isosceles_triangle = IsoscekesTriangle(name, side, base)
                print("Area:", isosceles_triangle.area())
                print("Circuit:", isosceles_triangle.circuit())
                print("Name:", isosceles_triangle.get_name())
            except ValueError as e:
                print("Error:", e)

        elif figure_input.capitalize() == "Stop":
            print("Stopping program...")
            break

    else:
        print("Input correct value")






