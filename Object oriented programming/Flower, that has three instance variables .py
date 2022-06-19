""" Write a Python class named Flower, that has three nonpublic attributes of type str,
int, and float, that respectively represent the name of the flower, its number of
petals, and its price. Include a constructor method that initializes each variable to an
appropriate value as well as methods for setting the value and retrieving the value of
each type. """


class Flower:
    def __init__(self):
        self.name = str('default')
        self.petals = int(0)
        self.price = float(0.0)

    def set_name(self, name):
        self.name = str(name)

    def set_petals(self, petals):
        self.petals = int(petals)

    def set_price(self, price):
        self.price =float(price)

    def get_name(self) -> str:
        return self.name

    def get_petals(self) -> int:
        return self.petals

    def get_price(self) -> float:
        return self.price


b1 = Flower()
b1.set_price(15.35)
b1.set_petals(10)
b1.set_name('rose')
print(b1.get_name())
print(b1.get_petals())
print(b1.get_price())
