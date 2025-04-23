# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#       one or more numbers, and returns the smallest and largest numbers, in the
#       form of a tuple of length two. Do not use the built-in functions min or
#       max in implementing your solution.

# Programmer: Anna Le

def minmax(data):
    min = data[0]
    max = data[0]

    for i in data [1:]: #this loop is slicing through  the data, where it starts at the second element in the list and keeps looping to the unknown stop
        if min > i:
            min = i
        elif max < i:
            max = i
    i += 1
    return (min, max)

print (minmax([1,2,3,4,5,6]))
print (minmax([89, 101, 78, 47, 4]))