# the following are the basic math operations in python (+,-,*,/):
print(3 + 4) # 7
print(3 - 4) # -1
print(3 * 4) # 12
print(3 / 4) # 0.75

# two asterisks represent exponentiation:
print(2 ** 3) # 8, since 2^3 = 8

# the modulo operator (%) returns the remainder of the division of the number to the left by the number on its right:
print(10 % 3) # 1, since 10 divided by 3 is 3 with a remainder of 1

# two forward slashes represent integer division, meaning the result is rounded down to the nearest whole number:
print(10 // 4) # 2, since 10 divided by 4 is 2.5, rounded down to 2

# the order of operations is the same as normal:
print(3 + 4 * 5) # 23

# parentheses can be used to specify the order of operations:
print((3 + 4) * 5) # 35

# variable assignments can be combined with math operations as shorthand:
x = 5
x += 3 # equivalent to x = x + 3
print(x) # 8
x *= 2 # equivalent to x = x * 2
print(x) # 16