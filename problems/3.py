from math import sqrt, ceil, floor

t = 600851475143

primes = [2, 3, 5]
pf = []
for n in primes:
    if t % n == 0:
        pf.append(n)
for n in range(t):
    try: print(f'{floor(n*100/t)}%', n, pf)
    except: print('error')
    if n in {0, 1, 2, 3, 4, 5}: continue
    elif n % 2 == 0: continue
    elif n % 5 == 0: continue
    for p in primes:
        if n % p == 0: break
        elif p == primes[len(primes)-1]:
            primes.append(n)
            if t % n == 0:
                pf.append(n)
    product = 1
    for item in pf: product *= item
    if product == t:
        print('DONE')
        break
        