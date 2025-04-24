""""
R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.

Programmer: Anna Le
"""

class Flower:

    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    #Getters
    def getName (self):
        return str(self.name)
    
    def getPetals (self):
        return int(self.petals)
    
    def getPrice (self):
        return float(self.price)

    #Setters
    def setName (self, name):  
        self.name = name
    
    def setPetals (self, petals):
        self.petals = petals

    def setPrice (self, price):
        self.price = price
    
    def information (self):
        return "The name of the flower is {}. It has {} petals. The price of this flower is ${}.".format(self.name, self.petals, self.price)
    
#Test
rose = Flower("Rose", 10, 20.0)
zinnia = Flower("Zinnia", 200, 5.75)

print (rose.name)
print (rose.petals)
print (rose.price)
rose.setPrice = 52.55
print ("${}".format(rose.price))

print ("{} petals".format(zinnia.getPetals()))

print (rose.information())