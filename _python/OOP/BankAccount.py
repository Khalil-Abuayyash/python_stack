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

N001 = BankAccount(0.01, 100)
N002 = BankAccount(0.05, 1000)

N001.deposit(10).deposit(15).deposit(30).withdraw(20).yield_interest().display_aaccount_info()
N002.deposit(20).deposit(40).withdraw(10).withdraw(10).withdraw(5).withdraw(8).yield_interest().display_aaccount_info()