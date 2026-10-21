fib = [1, 2]
for n in range(9999999999999):
    item = fib[n]+fib[n+1]
    if item <= 4000000: fib.append(item)
    else: break
sum = 0
for n in fib:
    if n % 2 == 0: sum += n
print(sum)