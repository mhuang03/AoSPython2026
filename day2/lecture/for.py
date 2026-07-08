# the for loop in python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# the range() function is used to generate a sequence of numbers.

# range(stop) goes from 0 to stop - 1
for i in range(10): # 0 to 9
    print(i)

# range(start, stop) goes from start to stop - 1
for i in range(1, 10): # 1 to 9
    print(i)

# range(start, stop, step) goes from start to stop - 1 with an increment value of step
for i in range(1, 10, 2): # 1, 3, 5, 7, 9
    print(i)

# iterate over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# iterate over a string
for letter in 'hello':
    print(letter)
