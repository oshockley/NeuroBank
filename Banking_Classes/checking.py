class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the balance.")

class CheckingAccount(BankAccount):
    def write_check(self, amount):
        self.withdraw(amount)  # Use the withdraw method from the base class to process the check.