product = 1
for n in range(100): product*=(n+1)
array = []
for d in str(product):
    array.append(int(d))
print(sum(array))