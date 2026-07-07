a = int(input("Give me a side length: "))
b = int(input("Give me a side length: "))
c = int(input("Give me a side length: "))

if a + b > c and b + c > a and a + c > b:
    print("That's a valid triangle!")
else:
    print("Not a valid triangle :(")

