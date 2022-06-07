class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("deposit amount non-positive")
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= 0:
            print("Insufficient funds: Charging a $5 fee")
            self.amount-=5
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance:",self.balance,"$")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate / 100)
        return self

class User():
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print("The Remaining balance after withdrawal : ",self.account.balance)	

    def display_user_balance(self):
        print("User:",self.name)
        self.account.display_account_info()
    
    def deposit(self,amount):
    	self.account.deposit(amount)
    	print("The Remaining balance after deposit : ",self.account.balance)	
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.amount += amount
        return self


user1 = User("Shahad")
user1.deposit(100)
user1.deposit(100)
user1.deposit(100)
user1.make_withdrawal(200)
user1.display_user_balance()
    