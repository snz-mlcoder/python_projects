class BankAccount:
    def __init__(self, owner : str, balance : float =0) -> None:
        self.owner = owner
        self.__balance = balance  # Private variable
        self.__transaction = [] # private transaction list 
        self.__is_frozen = False #freez flag

    def deposit(self, amount : float ) -> None:
        if self.__is_frozen:
            print("Account is frozen. Operation denied.")
            return
        if amount > 0:
            self.__balance += amount
            self.__transaction.append(f"Deposited {amount}")

            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount : float) -> None:
        if self.__is_frozen:
            print("Account is frozen. Operation denied.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            self.__transaction.append(f"withdraw {amount}")
            print(f"{amount} withdrawn. New balance: {self.__balance}")

        

    def show_transactions(self) -> None:
        if not self.__transaction:
            print ('No transaction yet.')
        else:
            print ("transaction history:")
            for t in self.__transaction:
                print ("-",t)

    def freeze(self) -> None:
        self.__is_frozen = True
        print("account has been frozen")

    def unfreeze(self) -> None:
        self.__is_frozen = False
        print("account has been unfrozen")


    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        status = "frozen" if self.__is_frozen else "Active"
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

# Test the class
account = BankAccount("Saeideh", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
print("Final balance:", account.get_balance())

account.show_transactions()

# Freeze account and try to deposit/withdraw
print("\n--- Freezing the account ---")
account.freeze()

account.deposit(100)   # Should be denied
account.withdraw(50)   # Should be denied

# Unfreeze and try again
print("\n--- Unfreezing the account ---")
account.unfreeze()

account.deposit(100)   # Should succeed
account.withdraw(50)   # Should succeed

print("\nFinal account status:")
print(account)

account.show_transactions()


# Direct access to private variable (not recommended)
# print(account.__balance)  # This will raise an AttributeError
