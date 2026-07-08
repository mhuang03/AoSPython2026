# Problem 1: FizzBuzz
# Write a program that asks the user for a number n and then prints:
# - "Fizz" if the number is divisible by 3
# - "Buzz" if the number is divisible by 5
# - "FizzBuzz" if the number is divisible by both 3 and 5
# - The number itself if it is neither divisible by 3 nor 5.
# For example, if the user enters 15, the program should print "FizzBuzz".
# Hint: Use the modulo operator (%).

n = int(input("Enter a number: "))

# if n % 3 == 0:
#     if n % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print("Fizz")
# else:
#     if n % 5 == 0:
#         print("Buzz")
#     else:
#         print(n)

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
