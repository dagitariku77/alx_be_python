# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes a bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Displays the current balance in the account."""
        print(f"Current Balance: ${self.account_balance:.2f}")
