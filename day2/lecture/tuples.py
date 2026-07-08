# tuples are immutable (cannot be changed)

# create a tuple
fruits = ('apple', 'banana', 'cherry')
print(fruits) # ('apple', 'banana', 'cherry')

# you can get the length of a tuple using the len() function
print(len(fruits)) # 3

# access items (items are indexed starting from 0)
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # cherry

# negative indexing (last item has index -1, second last item has index -2, and so on)
print(fruits[-1]) # cherry

# slicing can be used
print(fruits[:2]) # ('apple', 'banana')

# tuple unpacking
fruit1, fruit2, fruit3 = fruits
print(fruit1) # apple
print(fruit2) # banana
print(fruit3) # cherry