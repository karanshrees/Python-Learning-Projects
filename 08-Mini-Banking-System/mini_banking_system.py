class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance}")
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a number.")



    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    print(f"Withdrew ${amount}. New balance: ${self.balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a number.")


    def check_balance(self):
        print(f"Current balance: ${self.balance}")


def main():
    account = BankAccount("123456789", "John Doe")

    while True:
        print("\nMini Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter amount to deposit: ")
            account.deposit(amount)
        elif choice == '2':
            amount = input("Enter amount to withdraw: ")
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

