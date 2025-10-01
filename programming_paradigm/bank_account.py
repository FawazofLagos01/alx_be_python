class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specific amount"""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if Account balance is greater than or equal to withdrawal amount."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """print the current balance in a user-friendly format."""
        print(f"Current Balance: ${[self.account_balance]}")
    