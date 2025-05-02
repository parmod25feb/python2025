# Define a Python class named Circle with an attribute for its radius. 
# Include a method area that calculates and returns the area of the circle. (Use π≈3.14159).

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        pi=3.14159
        ar = pi*(self.radius**2)
        print(f"Area of a circle with radius {self.radius} is - {ar}")

a1 = Circle(5)
a1.area()
    