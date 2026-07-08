# Problem 2: Quadratic Formula
# Ask the user for the coefficients a,b,c of a quadratic in ax^2+bx+c=0 form.
# Then, compute the real roots of the equation and print them out.
# If you don't know the quadratic formula, either Google it or skip this one for now.
# Hint: use the discriminant to determine whether solutions are real.
import math
math.sqrt(9)  # == 3, square root function

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"Two real solutions: {x1} and {x2}")
elif discriminant == 0:
    x = (-b)/(2*a)
    print(f"One real solution: {x}")
else:
    print("No real solutions")