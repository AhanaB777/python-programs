"""
2. Create a class BankAccount with:
• Data members: account_holder, balance
• A constructor to initialize values
• Member functions:
o deposit(amount) → adds money
o withdraw(amount) → deducts money (check sufficient balance)
o display_balance() → shows current balance
Create 2 or 3 account objects. Perform deposit and withdrawal operations. Display final balance
"""
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def display_balance(self):
        print("Account Holder: ",self.account_holder)
        print("Current Balance: ",self.balance)

a1=BankAccount("Moricia", 80000)
a1.display_balance()
a1.deposit(30000)
a1.display_balance()
a1.withdraw(1500)
a1.display_balance()

a2=BankAccount("Luna", 110000)
a2.display_balance()
a2.deposit(600000)
a2.display_balance()
a2.withdraw(40000)
a2.display_balance()