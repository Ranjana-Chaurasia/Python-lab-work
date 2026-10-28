# Encapsulated Banking System with Inheritance Models
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs.{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: Rs.{amount}")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: Rs.{self.__balance}")

# Derived class 1
class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    # Method overriding
    def deposit(self, amount):
        print("Savings Account Transaction:")
        super().deposit(amount)

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        super().deposit(interest)
        print(f"Interest added: Rs.{interest:.2f}")

# Derived class 2
class CurrentAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    # Method overriding
    def withdraw(self, amount):
        if 0 < amount <= self.get_balance() + self.overdraft_limit:
            print("Current Account Transaction:")
            super().withdraw(amount) if amount <= self.get_balance() else self._overdraft_withdraw(amount)
        else:
            print("Overdraft limit exceeded!")

    def _overdraft_withdraw(self, amount):
        remaining = self.get_balance() - amount
        # Use the base class withdrawal when balance is sufficient.
        # Otherwise, report the overdraft without accessing private data.
        self._set_overdraft_balance(remaining)

    def _set_overdraft_balance(self, remaining):
        # Adjust balance through the inherited account interface.
        current = self.get_balance()
        if remaining < current:
            super().withdraw(current)
            print(f"Withdrawn: Rs.{current}")
            print(f"Overdraft used: Rs.{abs(remaining)}")

# Polymorphic interface
def account_details(account):
    account.display()
    print("-" * 30)

savings = SavingsAccount("Riya", 5000, 5)
current = CurrentAccount("Aman", 3000, 2000)

print("\n--- Savings Account ---")
savings.deposit(1000)
savings.add_interest()
savings.withdraw(500)
account_details(savings)

print("\n--- Current Account ---")
current.deposit(2000)
current.withdraw(4000)
account_details(current)