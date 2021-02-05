# Write a Python class, Flower, that has three instance variables of type str,
#int, and float, that respectively represent the name of the flower, its number
#of petals, and its price. Your class must include a constructor method
#that initializes each variable to an appropriate value, and your class should
#include methods for setting the value of each type, and retrieving the value
#of each type.

class Flower:
    
    def __init__(self, name, number_of_petals, price):
        self.name = name
        self.number_of_petals = number_of_petals
        self.price = price

    def _name(self):
        return self.name
    
    def _number(self):
        return self.number_of_petals

    
    def _price(self):
        return self.price



flowers = Flower('Hibiscus', 9, 8.00)
print(flowers._name())
print(flowers._price())

nice = Flower('Sunflower', 200, 40.00)
print(nice._name(), nice._price())

#print('{} is going for {} for {} pieces).format(nice._name)