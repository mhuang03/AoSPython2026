# strings in python are surrounded by either single quotation marks (' ')
# or double quotation marks (" ").
# strings are immutable, meaning they cannot be changed after they are created.

# the plus (+) operator can be used to concatenate (join) strings:
print('hello' + 'world') # helloworld

# variable assignments can be combined with string concatenation as shorthand:
x = 'hello'
x += 'world' # equivalent to x = x + 'world'
print(x) # helloworld

# the asterisk (*) can be used to repeat a string:
print('hello' * 3) # hellohellohello

# strings can be indexed, with the first character having an index of 0:
s = 'hello'
print(s[0])  # h
print(s[1])  # e
print(s[-1]) # o

# strings can also be sliced, with the first number being the start index (inclusive)
# and the second number being the end index (exclusive):
print(s[1:3]) # el
print(s[1:])  # ello
print(s[:2])  # he

# the len() function can be used to get the length of a string:
print(len(s)) # 5

# the in operator can be used to check if a string contains a certain substring:
print('e' in s) # True
print('a' in s) # False

# f-strings (formatted strings) can be used to insert variables into strings:
name = 'Alice'
age = 25
print(f'{name} is {age} years old') # Alice is 25 years old