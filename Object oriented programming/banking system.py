# Parent Class User
# Holds datials about an user
# Has function to show user details.
# Child Class Bank
# Stores details about the account balance
# stores details about the amount
# Allows for deposits,withdraw,view_balance

class user():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("user details")
        print("name :", self.name)
        print("age :", self.age)
        print("gender :", self.gender)

# child class


class bank(user):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount=amount
        self.balance += self.amount
        print("account balance has been updated : €", self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient funds , balance availabel : €", self.balance)
        else:
            self.balance-=self.amount
            print("account balance has been updated : €", self.balance)
    
    def view_balance(self):
        print("account balance : €", self.balance)



# viren1=user('viren',22,'male')
viren = bank('viren', 22, 'male')
# viren.show_details()
# viren1.show_details()
viren.deposit(500)
viren.deposit(300)
viren.withdraw(20)
viren.withdraw(80)

