# the random module helps us generate randomness.
import random

# the randint() function generates a random integer between the two arguments, inclusive
a = random.randint(1, 12) # can generate any integer between 1 and 12
b = random.randint(1, 12) # can generate any integer between 1 and 12, not necessarily the same as a

# the shuffle function shuffles a list in place
fruits = ['apple', 'banana', 'cherry']
random.shuffle(fruits)
print(fruits)

# the choice function returns a random element from a list
random_fruit = random.choice(fruits)
print(random_fruit)

# the random function returns a random float between 0 and 1
random_float = random.random() # returns a decimal number between 0 and 1
print(random_float)