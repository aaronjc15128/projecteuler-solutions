def collatz(n):
    chain = [n]
    while chain[-1] != 1:
        last = chain[-1]
        if last % 2 == 0: chain.append(last//2)
        else: chain.append(last*3+1)
    return len(chain)

longest = 0
target = 0
for starting in range(1000000):
    if starting == 0: continue
    length = collatz(starting)
    if length > longest: target, longest = starting, length 
    print(starting, length)

print(f'final: {longest} n={target}')