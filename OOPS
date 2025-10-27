# using classes,objects for banking systems
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance   # Encapsulated (private) attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount!")

    # Method to check balance
    def check_balance(self):
        print(f"Account Balance: ₹{self.__balance}")

# Derived Class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # Polymorphism example (method overriding)
    def withdraw(self, amount):
        if amount > 0:
            print(f"Processing savings account withdrawal...")
        super().withdraw(amount)

    # Additional method for savings account
    def add_interest(self):
        interest = self.interest_rate * self._BankAccount__balance
        self._BankAccount__balance += interest
        print(f"Interest ₹{interest:.2f} added. New Balance: ₹{self._BankAccount__balance:.2f}")

# Another Derived Class
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=5000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._BankAccount__balance + self.overdraft_limit:
            self._BankAccount__balance -= amount
            print(f"Withdrawn ₹{amount}. New Balance: ₹{self._BankAccount__balance}")
        else:
            print("Overdraft limit exceeded!")

# ---- Usage Example ----
# Creating accounts
savings = SavingsAccount("101", "Aarav", 10000)
current = CurrentAccount("102", "Maya", 5000)

# Performing operations
savings.deposit(2000)
savings.withdraw(1500)
savings.add_interest()

current.deposit(3000)
current.withdraw(9000)
current.check_balance()
