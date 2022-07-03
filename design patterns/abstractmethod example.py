from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def number_of_sides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method

    def number_of_sides(self):
        return 3


class Pentagon(Polygon):
    # overriding abstract method

    def number_of_sides(self):
        return 5


class Hexagon(Polygon):
    # overriding abstract method

    def number_of_sides(self):
        return 6


print(Hexagon().number_of_sides())
print(Pentagon().number_of_sides())


def print_sides(p: Polygon):
    number = p.number_of_sides()
    print(f"I have {number} sides")


print_sides(Hexagon())
