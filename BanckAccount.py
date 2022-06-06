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
            

#To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)       
account1 = BankAccount(3,300)
account1.deposit(200).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
#To the second account, make 2 deposits and 4 withdrawals, 
# then yield interest and display the account's info all in one line of code (i.e. chaining)
account2 = BankAccount(2,200)
account2.deposit(100).deposit(100).withdraw(100).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()