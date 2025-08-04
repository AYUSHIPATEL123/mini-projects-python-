class BalanceException(Exception):
    pass
class Main_Account():
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance=balance
        print(f"Account for {self.name} is created successfully.......👍🏼👍🏼👍🏼\n")
    def get_balance(self):
        print(f" {self.name}'s account has balance of {self.balance}\n")    

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}'s account has been credited with {amount} has balance of {self.balance} successfully.......🤑🤑🤑\n")

    def exception(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Insufficient balance in {self.name}'s Account\n")
        
    def withdrow(self,amount):
        try:
            self.exception(amount)
            self.balance -= amount
            print(f"{self.name}'s account has been debited with {amount} has balance of {self.balance} successfully.......👎👎👎\n")
        except Exception as error:
            print(f"withdrow innterrapted : {error} ❌❌❌\n")

    def transfer(self,amount,account):
        print("______beggining the transfer process......💸💸💸______\n")
        try:
            self.exception(amount) 
            self.withdrow(amount)
            account.deposit(amount)
            print(f"{self.name} has successfully transfer {amount} to {account.name}✔️ ✔️ ✔️") 
        except Exception as error:
            print(f"withdrow innterrapted : {error} ❌❌❌\n")

class InterestBonusAccount(Main_Account):       #inheritence  
    def deposit(self, amount):                  # polimorfizem
        self.balance += amount * 1.10
        print(f"{self.name}'s account has been credited with {amount} has balance of {self.balance}🤑🤑🤑\n")

class SavingsAccount(Main_Account):     #inheritence         
    fee=10
    def withdrow(self, amount):         # polimorfizem
        try:
            self.exception(amount+self.fee)
            self.balance -= (amount + self.fee)
            print(f"{self.name}'s account has been debited with {amount} has balance of {self.balance} successfully.......👎👎👎\n")
        except Exception as error:
            print(f"withdrow innterrapted : {error} ❌❌❌\n")