def primes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [i for i in range(2, n + 1) if sieve[i]]

from itertools import combinations
from math import prod

def divisors(factors):
    divisors = set()

    for i in range(len(factors) + 1):
        for combo in combinations(factors, i):
            divisors.add(prod(combo))

    return sorted(divisors)

def d(n):
    pf = []
    p = primes(n)

    current = n

    i = 0
    while current != 1:
        if current % p[i] == 0:
            pf.append(p[i])
            current //= p[i]
        else:
            i += 1

    return sum(divisors(pf)[:-1]) 

amicable = []

da = [0]

for i in range(1, 10000):
    da.append(d(i))

i = 1
while i < len(da):
    j = i+1
    while j < len(da):
        print(i, j)
        if i == da[j] and j == da[i]:
            amicable.append([i, j])
        j += 1
    i += 1

uniques = []
for a in amicable:
    if a not in uniques:
        uniques.append(a)

a = []
b = []

for u in uniques:
    a.append(u[0])
    b.append(u[1])

au, bu = [], []
for n in a:
    if n not in au:
        au.append(n)
for n in b:
    if n not in bu:
        bu.append(n)


print(amicable, uniques, a, b, au, bu)
print(sum(au) + sum(bu))