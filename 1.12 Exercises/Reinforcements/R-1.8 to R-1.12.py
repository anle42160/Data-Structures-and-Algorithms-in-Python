# Programmer: Anna Le

#R-1.8 Python allows negative integers to be used as indices into a sequence,
#      such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
#      the same element?



# R-1.9 What parameters should be sent to the range constructor, to produce a
#       range with values 50, 60, 70, 80?

range(50, 90, 10) #start: 50, stop: 90 (10/one step before desired stop), step: 10

#R-1.10 What parameters should be sent to the range constructor, to produce a
#       range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

range(8,-10,-2)

#R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
#       the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

2*i*i for i in range(9)

#R-1.12 Python’s random module includes a function choice(data) that returns a
#       random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to
#       the built-in range function, that return a random choice from the given
#       range. Using only the randrange function, implement your own version
#       of the choice function.

from random import randrange
randrange (50, 90, 10)