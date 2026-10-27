from math import ceil

def primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [i for i in range(2, n + 1) if sieve[i]]

for n in range(999999999999999999999):

    triangle = int((n+1)*(n+2)*0.5)

    pf = []

    current = triangle
    for p in primes(ceil(triangle**0.5)):
        while current % p == 0:
            current /= p
            pf.append(p)

    done = []
    exponents = []

    i = 0
    while i < len(pf):
        if pf[i] not in done:
            count = 0
            j = 0
            while i+j < len(pf):
                if pf[i+j] == pf[i]:
                    count += 1
                    j += 1
                else: break
            exponents.append(count)
            done.append(pf[i])
        i += j
        

    divisors = 1
    for item in exponents:
        divisors *= item+1

    print(triangle, divisors)

    if divisors > 500: break
        
        
   