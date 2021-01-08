import math


def primes(n):
    numbers = list(range(0, n))
    for x in range(n):
        numbers[x] = 1
    numbers[0] = 0
    numbers[1] = 0
    p = 2
    while p * p <= n:
        if numbers[p] == 1:
            for i in range(p * p, n, p):
                numbers[i] = 0
        p += 1
    prime = []
    for x in range(n):
        if numbers[x] == 1:
            prime.append(x)

    for x in range(1000):
        print(prime[x])


primes(10000)
