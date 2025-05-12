# 🏦 Bank Account Manager (v1)

A simple Python class that simulates a basic bank account system.  
This project is part of my object-oriented programming (OOP) practice using encapsulation and private attributes.

---

## ✅ Features

- Create a bank account with an initial balance
- Deposit and withdraw money
- Print account details
- Access current balance via a method
- Demonstrates:
  - Private attributes (`__balance`)
  - Class methods
  - `__str__` method for readable output

---

## 🧪 Example Usage

```python
account = BankAccount("Saeideh", 1000)
print(account)

account.deposit(500)
account.withdraw(200)
print("Final balance:", account.get_balance())
