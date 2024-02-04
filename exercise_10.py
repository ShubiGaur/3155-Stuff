'''
Create a BankAccount class which has an __init__ method which accepts an account name and starting balance to store as instance fields. 
The class should also have a method to deposit money, a method to withdraw money, 
and a method called "get_balance" which returns a string of the format "{account_name} has a balance of {balance}" 
(do not print this out from within the class, just return the string). 
In the same file, create an instance of the BankAccount class with a hardcoded name and starting balance. 
Deposit any amount to the account and withdraw any amount from the account (both can be hardcoded) and then print the result of calling the get_balance method on the instance.


'''

class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        return f"{self.account_name} has a balance of {self.balance}"

# Create an instance of the BankAccount class
account = BankAccount("Shubi's Account", 3000)  # Hardcoded name and starting balance

# Deposit and withdraw some amounts
account.deposit(500)  # Hardcoded deposit amount
account.withdraw(200)  # Hardcoded withdrawal amount

# Print the result of calling the get_balance method
print(account.get_balance())

# ext sources: https://www.w3schools.com/python/python_classes.asp
            #  https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/