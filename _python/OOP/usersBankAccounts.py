class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_aaccount_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(int_rate=0.02, balance=0)]
    
    def makeAnotherAccount(self):
        self.accounts.append(BankAccount(int_rate=0.02, balance=0))
        return self
    
    def deleteAccount(self):
        self.accounts.pop()

    def deposit(self, amount, account_index):
        self.accounts[account_index].deposit(amount)
        return self
    
    def withdraw(self, amount,account_index):
        self.accounts[account_index].withdraw(amount)
        return self

    def display_aaccount_info(self,account_index):
        self.accounts[account_index].display_aaccount_info()
        return self

    def yield_interest(self,account_index):
        self.accounts[account_index].yield_interest()
        return self

