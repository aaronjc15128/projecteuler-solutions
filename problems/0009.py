triplets = []
c = 997
while c > 0:
    absum = 1000-c
    i = 1
    while absum-i > i:
        if c > absum-i: triplets.append([i, absum-i, c])
        i+=1
    c-=1

pythagorean = []
for t in triplets:
    if t[0]**2 + t[1]**2 == t[2]**2:
        pythagorean.append(t)

print(pythagorean)