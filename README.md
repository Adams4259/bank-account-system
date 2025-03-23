# **🏦 Bank Account System (OOP in FinTech)**

## **📌 Project Overview**
This project demonstrates **Object-Oriented Programming (OOP)** principles in Python to build a **Bank Account System**. The system allows users to:
- Create **bank accounts**
- Perform **deposits** and **withdrawals**
- Check **account balances**
- Implement **interest calculations** for savings accounts

The project is designed for **FinTech applications**, providing a structured approach to managing bank transactions using **Python OOP**.

---

## **🚀 Features**
✅ Create a **Bank Account** with an account number and balance  
✅ Deposit and withdraw funds with balance validation  
✅ Implement **inheritance** for specialized accounts (e.g., **SavingsAccount**)  
✅ Calculate **interest earnings** on savings accounts  

---

## **🛠 Tech Stack**
- **Language:** Python 3  
- **Concepts Used:** OOP (Classes, Inheritance, Encapsulation, Polymorphism)  

---

## **📂 Project Structure**
```
📁 Bank-Account-System/
│── 📄 bank_account.py   # Core implementation of BankAccount & SavingsAccount
│── 📄 README.md         # Project documentation
│── 📄 requirements.txt  # Dependencies (if any)
│── 📄 test_bank.py      # Test cases for account operations (Optional)
```

---

## **💻 Installation & Setup**
### **1️⃣ Clone the repository**
```sh
git clone https://github.com/your-username/Bank-Account-System.git
cd Bank-Account-System
```

### **2️⃣ Run the script**
```sh
python bank_account.py
```

---

## **📜 Code Overview**

### **🔹 BankAccount Class**
```python
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
        return f"Withdrew {amount}. New Balance: {self.balance}"

    def get_balance(self):
        return f"Account {self.account_number} Balance: {self.balance}"
```

### **🔹 SavingsAccount Class (Inheritance)**
```python
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        return f"Interest Earned: {interest}"
```

### **🔹 Sample Usage**
```python
acc = SavingsAccount("12345", 5000)
print(acc.get_balance())  # Check balance
print(acc.deposit(2000))  # Deposit money
print(acc.withdraw(3000))  # Withdraw money
print(acc.calculate_interest())  # Interest calculation
```

---

## **📌 Example Output**
```
Account 12345 Balance: 5000
Deposited 2000. New Balance: 7000
Withdrew 3000. New Balance: 4000
Interest Earned: 120.0
```

---

## **🔧 Possible Improvements**
🔹 Add **Transaction History**  
🔹 Implement **Overdraft Accounts**  
🔹 Save data using **CSV or a Database**  
🔹 Build a **FastAPI/Django backend API** around the system  

---

## **📜 License**
This project is licensed under the **MIT License**. Feel free to modify and use it.  

---

## **👨‍💻 Author**
👤 **Adams Echwa**  
📧 *adamsechwa18@gmail.com*  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)  

---

🚀 **Happy Coding!** 🚀

