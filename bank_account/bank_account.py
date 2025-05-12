class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

# Test the class
account = BankAccount("Saeideh", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
print("Final balance:", account.get_balance())

# Direct access to private variable (not recommended)
# print(account.__balance)  # This will raise an AttributeError
