class BankAccount:
    def __init__ (self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
        print(f"Account for {self.owner_name} created with balance ${self.balance}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}.")

class SavingsAccount (BankAccount):
    def __init__(self, owner_name, balance, interest_rate):
        super().__init__(owner_name, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New Balance: ${self.balance}.")
 

# --- Using the Class ---
# Create an Object (Instance) named 'account1'
account1 = BankAccount("Bruce Wayne", 1000)

# Call methods
account1.deposit(500)    # Output: Deposited $500. New Balance: $1500.
account1.withdraw(200)   # Output: Withdrew $200. New Balance: $1300.
account1.withdraw(2000)  # Output: Insufficient Funds.


# Create a Savings Account
saving_account = SavingsAccount("Tony Stark", 10000, 0.05)

# Call deposit(1000) (inherited from Parent).
saving_account.deposit(1000)

saving_account.add_interest()  # Child specific.