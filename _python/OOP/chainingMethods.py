

class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self

    def make_withdrawal(self, amount):
        if amount < self.account_balance:
            self.account_balance = self.account_balance - amount
        else:
            print("Your balance is not enough for this operation")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def  transfer_money(self, other_user, amount):
        if amount < self.account_balance:
            self.account_balance = self.account_balance - amount
            other_user.account_balance = other_user.account_balance + amount
        else:
            print("Your balance is not enough for this operation")
        return self

Khalil = User('Khalil', '@axsos')
Dara = User('Dara', '@axsos')
Moath = User('Moath', '@axsos')

Khalil.make_deposit(10).make_deposit(20).make_deposit(30).make_withdrawal(15).display_user_balance()

Dara.make_deposit(10).make_deposit(20).make_withdrawal(5).make_withdrawal(10).display_user_balance()

Moath.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(20).display_user_balance()

Khalil.transfer_money(Moath, 30).display_user_balance()
Moath.display_user_balance()

# Khalil.make_withdrawal(100)
# Khalil.transfer_money(Moath, 100)

