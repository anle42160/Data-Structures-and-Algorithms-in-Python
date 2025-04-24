""""
R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.

Programmer: Anna Le
"""

#Program from Textbook
class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
    
    #Added Code
    def __radd__(self, other): #__radd__ is the method called when the left opperand doesn't know how to add the right opperand, this has to be the name of the method.
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = other[j] + self[j] #this is essentially the __add__ method, but the orientation is changed to allow a list to be added to a vector
        return result
    
#Test
u = Vector(5)
u[0] = 1
u[1] = 2
u[2] = 3
u[3] = 4
u[4] = 5

v = [5, 3, 10, -2, 1] + u

print (v)

"""
Before the revision, the Vector class only supported a vector added to a list with the way that the __add__ method is structured.
The __add__ method adds self[j] to other[j] which refers to the vector to a list.
However this does not include other[j] to self[f].
"""