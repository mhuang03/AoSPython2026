def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def print_primes(k):
    count = 0
    i = 2
    while count < k:
        # find the next prime
        if is_prime(i):
            print(i)
            count += 1
        i += 1


print_primes(1000)