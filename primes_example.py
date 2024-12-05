from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_n_primes(n):
    primes = []
    i = 2
    while len(primes) != n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes


lst = get_n_primes(10000)
for elem in lst:
    print(elem)