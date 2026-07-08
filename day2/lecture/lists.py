# lists store multiple items in a single variable
# lists are ordered, changeable and allow duplicate values
# lists are defined by square brackets

things = ["apple", "banana", "cherry"]
print(things) # ['apple', 'banana', 'cherry']

# you can get the length of a list using the len() function
print(len(things)) # 3

# access items (items are indexed starting from 0)
print(things[0]) # apple
print(things[1]) # banana
print(things[2]) # cherry

# negative indexing (last item has index -1, second last item has index -2, and so on)
print(things[-1]) # cherry
print(things[-2]) # banana
print(things[-3]) # apple

# slicing can be used to get a range of items
# the first index is included, the last index is not included
# the syntax is list[start:end], but if either start or end is omitted, it will go to the beginning or end of the list
print(things[:2]) # ['apple', 'banana']
print(things[1:3]) # ['banana', 'cherry']
print(things[1:]) # ['banana', 'cherry']


# change item value
things[1] = "orange"
print(things) # ['apple', 'orange', 'cherry']
things[2] = "grape"
print(things) # ['apple', 'orange', 'grape']

# append items to the end of the list
things.append("mango")
print(things) # ['apple', 'orange', 'grape', 'mango']

# insert items at a specific index
things.insert(1, "kiwi")
print(things) # ['apple', 'kiwi', 'orange', 'grape', 'mango']

# remove items
things.remove("kiwi")
print(things) # ['apple', 'orange', 'grape', 'mango']

# pop() removes and returns an item at a specific index
popped = things.pop(1)
print(things) # ['apple', 'grape', 'mango']
print(popped) # orange

# del removes an item at a specific index
del things[1]
print(things) # ['apple', 'mango']

# joining lists
more_things = ["pear", "peach"]
all_things = things + more_things
print(all_things) # ['apple', 'mango', 'pear', 'peach']

# sorting lists in-place
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers) # [1, 2, 3, 4]

# sorting lists without changing the original list
numbers = [4, 2, 1, 3]
sorted_numbers = sorted(numbers)
print(numbers) # [4, 2, 1, 3]
print(sorted_numbers) # [1, 2, 3, 4]

# reverse the order of a list
numbers.reverse()
print(numbers) # [3, 1, 2, 4]

reversed(numbers)