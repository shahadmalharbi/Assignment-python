class User():
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def make_withdrawal(self, amount):
        self.amount -=amount

    def display_user_balance(self):
        print("User:",self.name,"Balance:",self.amount)
    
    def deposit(self, amount):
        self.amount += amount
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.amount += amount
        return self
    
# the first user make 3 deposits and 1 withdrawal and then display their balance:
user1 = User("Shahad",300)
user1.deposit(100)
user1.deposit(100)
user1.deposit(100)
user1.make_withdrawal(200)
user1.display_user_balance()
#the second user make 2 deposits and 2 withdrawals and then display their balance
user2 = User("Taif",200)
user2.deposit(200)
user2.deposit(100)
user2.make_withdrawal(50)
user2.make_withdrawal(100)
user2.display_user_balance()
#the third user make 1 deposits and 3 withdrawals and then display their balance
user3 = User("Ali", 100)
user3.deposit(300)
user3.make_withdrawal(50)
user3.make_withdrawal(150)
user3.make_withdrawal(50)
user3.display_user_balance()

user1.transfer_money(user3,50)
user1.display_user_balance()
user3.display_user_balance()


