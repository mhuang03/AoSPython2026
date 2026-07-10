# An object in python is an instance of a class. A class is a blueprint for creating objects.
# An object has properties (attributes) and methods (functions) associated with it.

# Define a class
class Person:
    # __init__ is a special method that is called when an object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self refers to the current instance of the class (the object itself)

    # a method to greet the person
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # a method to increase the age of the person
    def birthday(self):
        self.age += 1

# Create an object of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access the properties of the object
print(person1.name) # Alice
print(person2.age) # 25

# Call the methods of the object
person1.greet() # Hello, my name is Alice and I am 30 years old.
person2.birthday()
print(person2.age) # 26