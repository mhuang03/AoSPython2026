n = int(input("Enter a number: "))
print(n)

while n != 1:
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = 3 * n + 1
    print(n)