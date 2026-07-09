
# def gcd(a, b):
#     start = min(a, b)
#
#     for n in range(start, 0, -1):
#         if a % n == 0 and b % n == 0:
#             return n

def gcd(a, b):
    small = min(a, b)
    big = max(a, b)

    while small != 0:
        big = big % small
        small, big = min(small, big), max(small, big)

    return big


print(gcd(1767863131786523456576203495872304598273405987230459872340, 1767863131786523456576203495872304598273405987230459872345213414501463455))