# R-1.7 Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.

#Programmer: Anna Le

n = 10
print (sum(i*i for i in range (1, n) if i%2 !=0))