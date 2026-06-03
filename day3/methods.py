class BankAccount:
    interest_rate=0.05
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def show_balance(self):
        print(f"Balace:{self.balance}")

    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited {amount}.\nnew balance:{self.balance}")

    @classmethod
    def set_rate(cls,rate):
        cls.interest_rate=rate

    @staticmethod
    def is_valid_amount(amount):
        return amount>0
    
acc=BankAccount('yashu',1000)
acc.show_balance()
acc.deposit(100)
BankAccount.set_rate(0.07)
print(BankAccount.is_valid_amount(-100))