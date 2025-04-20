#R-1.4 Write a short Python function that takes a positive integer n and returns
#      the sum of the squares of all the positive integers smaller than n.

# Programmer: Anna Le

def sumOfSquares(n):
    sum = 0
    if n < 0:
        return "This number is not positive, please enter a new number"
    while n > 0:
        n -= 1
        sum = sum + n*n
    return sum

#Test
print (sumOfSquares(-1))
print (sumOfSquares(4))
print (sumOfSquares(0))
print (sumOfSquares(5))