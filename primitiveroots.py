import parameter, prime
import math, sys

n = 5
n = parameter.handle(sys.argv, (n, True))

def relativeprimes(n):
    primes = []
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            primes.append(i)
    return primes

def isprimitiveroot(g, n):
    if g < 2 or g >= n:
        return False
    if prime.isprime(n):
        for i in range(1, n - 1):
            if g**i % n == 1 or g**i % n == 0:
                return False
    else:
        relative = relativeprimes(n)
        primes = []
        for i in range(len(relative)):
            primes.append(g**i % n)
        if set(primes) == set(relative):
            return True
        return False
    return True

def primitiveroots(n):
    if n == 2:
        return [1]
    roots = []
    for i in range(n):
        if isprimitiveroot(i, n):
            roots.append(i)
    return roots

def powersmod(g, n):
    for i in range(n):
        print(g**i % n)



