from math import floor, ceil

def palindrome(n):
    a = []
    for digit in str(n):
        a.append(digit)
    i = 0
    while i < ceil(len(a)/2):
        if a[i] != a[len(a)-i-1]: return False
        i += 1
    return True

a, highest = 999, 0
while len(str(a)) == 3:
    b = 999
    while len(str(b)) == 3:
        product = a*b
        if palindrome(product) and product > highest:
            highest = product
            print(f'{a} * {b} = {product}')
            break
        else: b-=1
    a-=1
