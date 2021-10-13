class user():
    def __init__ (self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show_details(self):
        print("Personal Details")
        print("Name:",self.name)
        print("Age:", self.age)
        print("Gender:",self.gender)
class bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def money_deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print("current balance:\n ₹" , self.balance)
    def withdra(self, amount):
        self.amount = amount
        if self.balance < amount :
            print("ensufficent fund")
        else:
            self.balance > amount
            self.balance = self.balance - amount
            print("current balance:\n ₹", self.balance)
    def view_balance(self):
        self.show_details()
        print("current balance:\n ₹", self.balance)
