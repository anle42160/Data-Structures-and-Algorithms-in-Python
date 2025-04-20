#R-1.6 Write a short Python function that takes a positive integer n and returns
#      the sum of the squares of all the odd positive integers smaller than n

# Programmer: Anna Le

def sumOfSqauredOdds(n):
    sum = 0

    if n < 0:
        return "This number is not positive, please enter a new number"
    
    n -= 1
    while n > 0:
        if n % 2 != 0:
            sum = sum + n*n
        n -= 1
    return sum        

#Test
print (sumOfSqauredOdds(-1))
print (sumOfSqauredOdds(4))
print (sumOfSqauredOdds(0))
print (sumOfSqauredOdds(5))
print (sumOfSqauredOdds(10))