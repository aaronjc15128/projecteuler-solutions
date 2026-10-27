def check(n):
    for d in range(20):
        if d == 0: continue
        elif n % d != 0: return False
    return True

for i in range(99999999999):
    if i == 0: continue
    elif check(i):
        print(i, 'yes')
        break
    else:
        print(i, 'no')
    