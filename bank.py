#Step 1: Define BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdew {self.account_number} Balance: {self.balance}"
    
    def get_balance(self):
        return f"Account {self.account_number} Balance: {self.balance}"
    
    #Step 2: Define SavingsAccount class
class SavingsAccount(BankAccount):
        def __init__(self, account_number, balance=0, interest_rate=0.03):
            super().__init__(account_number, balance)
            self.interest_rate = interest_rate

        def calculate_interest(self):
            interest = self.balance * self.interest_rate
            return f"Interest Earned: {interest}"
        

#Step 3: Testing the classes
acc = SavingsAccount("1234", 5000)
print(acc.get_balance()) #check balance
print(acc.deposit(2000)) #deposit money
print(acc.withdraw(3000)) #withdraw money
print(acc.calculate_interest()) #interest calculation