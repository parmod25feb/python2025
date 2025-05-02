'''Object-Oriented Programming (OOP): Define a simple Python class called Dog 
with an __init__ method that initializes the dog's name and breed attributes. 
Also, define a method called bark that prints "Woof!". Create an instance of the 
Dog class and call its bark method.'''

class Dog:
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(f"{self.name} belongs to {self.breed} breed")

d1=Dog("Jakson","Italian")
d1.bark()
d2=Dog("Romeo","French")
d2.bark()