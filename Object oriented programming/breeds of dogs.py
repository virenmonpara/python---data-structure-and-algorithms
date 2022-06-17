# examples of inheritence and polymorphism

class Dog():
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    def bark(self):
        return "Woof!"


class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "arf arf!"


class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def shedding_amount(self):
        return 0


class GoldRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7


class GoldenDoodle(Poodle, GoldRetriever):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return "A roooooo!"


# example of inheritance
sammy = Samoyed('sammy', 2, 10)
# print(sammy.name, sammy.age, sammy.friendliness)
# print(sammy.likes_walks())

goldie = GoldenDoodle('goldie', 1, 9)
# print(goldie.name, goldie.age, goldie.friendliness)
# print(goldie.likes_walks())
# print(goldie.fetch_ability())
# print(goldie.shedding_amount())

# examples of polymorphism
new_dog = Dog('gene', 10, 10)
print(goldie.bark())
print(sammy.bark())
print(new_dog.bark())
