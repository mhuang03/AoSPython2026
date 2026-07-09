# functions allow us to group code that we want to reuse, and call it whenever we need it
# functions are defined using the def keyword, followed by the function name and parentheses

# this function takes no arguments and prints a message
def greet():
    print("Hello!")

greet() # Hello!


# this function takes one argument and prints a message with the argument
def greet_name(name):
    print(f"Hello {name}!")

greet_name("Alice") # Hello Alice!


# this function takes two arguments and returns the sum of the arguments
def add(a, b):
    return a + b

print(add(3, 5)) # 8


# functions can have default values for their arguments
def greet_default(name="World"):
    print(f"Hello {name}!")

greet_default() # Hello World!
greet_default("Bob") # Hello Bob!


# functions can have an arbitrary number of arguments
def greet_many(*names):
    for name in names:
        print(f"Hello {name}!")

greet_many("Alice", "Bob", "Charlie")
# Hello Alice!
# Hello Bob!
# Hello Charlie!


# functions can return multiple values
def add_subtract(a, b):
    return a + b, a - b

sum_result, diff_result = add_subtract(5, 3)
print(sum_result) # 8
print(diff_result) # 2
print(add_subtract(5, 3)) # (8, 2)


# functions can call other functions
def greet_all(names):
    for name in names:
        greet_name(name)

greet_all(["Alice", "Bob", "Charlie"])
# Hello Alice!
# Hello Bob!
# Hello Charlie!


# functions can be recursive, calling themselves
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120
print(factorial(0)) # 1