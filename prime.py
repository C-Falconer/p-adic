from math import ceil

def isprime(n):
    for i in range(2, ceil(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factors(n):
    factors = []
    for i in range(2, ceil(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return sorted(set(factors))

if __name__ == '__main__':
    print("Running Prime File")
