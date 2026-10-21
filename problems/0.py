import math

def sumOddSquares(t):
    total = 0
    for n in range(t):
        square = (2*(n+1)-1)**2
        total += square

    return total


print(sumOddSquares(279000))