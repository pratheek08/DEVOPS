class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount! Please enter a positive number.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount! Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")

def main():
    atm = ATM()
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amt = float(input("Enter deposit amount: "))
                atm.deposit(amt)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "3":
            try:
                amt = float(input("Enter withdrawal amount: "))
                atm.withdraw(amt)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice! Try again.")
main()
