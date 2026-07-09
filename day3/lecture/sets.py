# sets are unordered collections of unique elements, and defined by curly brackets.
# sets do not allow duplicate elements, if you try to add a duplicate element, it will be ignored.
# sets are useful for storing unique elements and performing set operations

# create a set
fruits = {'apple', 'banana', 'cherry'}
print(fruits) # {'banana', 'apple', 'cherry'}

# you can also use the set() constructor to create a set
empty_set = set()
numbers = set([1, 2, 3, 4, 5])

# you can get the length of a set using the len() function
print(len(fruits)) # 3

# check if an element is in a set
print('apple' in fruits) # True
print('orange' in fruits) # False

# add elements to a set
fruits.add('orange')
print(fruits) # {'banana', 'apple', 'orange', 'cherry'}

# remove elements from a set
fruits.remove('banana')
print(fruits) # {'apple', 'orange', 'cherry'}

# discard() removes an element from a set if it is a member
fruits.discard('apple')
print(fruits) # {'orange', 'cherry'}
fruits.discard('apple') # no error if element is not in set

# pop() removes and returns an arbitrary element from a set
popped = fruits.pop()
print(popped) # orange
print(fruits) # {'cherry'}

# you can iterate through a set
fruits.add('apple')
fruits.add('banana')
for fruit in fruits:
    print(fruit)
# all elements are printed, but the order is not guaranteed



# set operations
more_fruits = {'banana', 'mango', 'pear'}

# union of two sets
all_fruits = fruits.union(more_fruits)
print(all_fruits) # {'apple', 'banana', 'cherry', 'mango', 'pear'}

# intersection of two sets
common_fruits = fruits.intersection(more_fruits)
print(common_fruits) # {'banana'}

# difference between two sets
diff_fruits = fruits.difference(more_fruits)
print(diff_fruits) # {'apple', 'cherry'}