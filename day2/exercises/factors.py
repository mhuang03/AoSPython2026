n = int(input("Enter a positive integer: "))

factor_count = 0
for factor in range(1, n+1):
    if n % factor == 0:
        print(factor)
        factor_count += 1

if factor_count == 2:
    print(f"{n} is prime!")