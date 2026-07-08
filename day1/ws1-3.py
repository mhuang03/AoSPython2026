# Problem 3: Factorial
# Write a program that asks the user for a number n and then calculates the factorial of that number.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# Hint: Use a loop to multiply the numbers from 1 to n together.

n = int(input("Enter a positive integer: "))

product = n
n -= 1

while n > 1:
    print(f"Multiplying {product} by {n}")
    product *= n
    n -= 1
print(f"The factorial is {product}")