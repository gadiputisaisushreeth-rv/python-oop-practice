class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} — Balance: {self.balance}"  # Day 1 task!

    def get_balance(self):
        return self.balance

    def deposit(self, amount):        # ← take amount as parameter
        self.balance += amount
        return self.balance

    def withdraw(self, amount):       # ← take amount as parameter
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds 😂")
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        self.balance += (self.balance*self.interest_rate)
    def __repr__(self):                    # ← add this
        return f"SavingsAccount(owner='{self.owner}', balance={self.balance}, rate={self.interest_rate})"
if __name__ == "__main__":
    user1 = SavingsAccount("Jeff", 1500, 0.05)
    print(user1)

    choice = input("Enter operation (deposit/withdraw/Interest/balance): ")

    if choice == "deposit":
        amount = int(input("Enter deposit amount: "))
        user1.deposit(amount)
    elif choice == "withdraw":
        amount = int(input("Enter withdrawal amount: "))
        user1.withdraw(amount)
    elif choice == "interest":
        user1.add_interest()

    print(f"Your balance is: {user1.get_balance()}")

# Change the SAME line in branch-b:
print("Hello from branch B")