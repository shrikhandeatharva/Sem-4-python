import random

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        transaction_code = self.generate_transaction_code()
        print(f"Deposit of Rs.{amount} successful. Transaction Code: {transaction_code}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            transaction_code = self.generate_transaction_code()
            print(f"Withdrawal of Rs.{amount} successful. Transaction Code: {transaction_code}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account Balance: Rs.{self.balance}")

    @staticmethod
    def generate_transaction_code():
        return str(random.randint(1000, 9999))

# Usage example:
account_number = input("Enter the account number: ")
initial_balance = float(input("Enter the initial balance: "))
account = BankAccount(account_number, initial_balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
