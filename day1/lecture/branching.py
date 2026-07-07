# we use if/elif/else to make decisions in Python

# if statement
x = 10
if x > 5:
    print('x is greater than 5')
else:
    print('x is not greater than 5')

# if/elif/else statement
y = 3
if y > 5:
    print('y is greater than 5')
elif y < 5:
    print('y is less than 5')
else:
    print('y is equal to 5')

# only the first branch that matches will run
z = 5
if z >= 5:
    print('z is greater than or equal to 5')
elif z == 5:
    print('z is equal to 5') # this code will not run, since the first branch already matched
else:
    print('z is less than 5')