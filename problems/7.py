from math import sqrt, ceil, floor

primes = [2, 3, 5]
for n in range(999999999999999999):
    try: print(f'{floor(len(primes)*100/10001)}%', n)
    except: print('error')
    if len(primes) == 10001: break
    elif n in {0, 1, 2, 3, 4, 5}: continue
    elif n % 2 == 0: continue
    elif n % 5 == 0: continue
    for p in primes:
        if n % p == 0: break
        elif p == primes[len(primes)-1]:
            primes.append(n)

print(primes[len(primes)-1])
        