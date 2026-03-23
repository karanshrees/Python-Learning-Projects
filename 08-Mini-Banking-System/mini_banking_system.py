import random
import datetime
import os 
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, load=False):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        # determine the filename where this account will be saved
        self.filename = f"{self.account_number}_account.txt"
        # list to store transaction history
        self.transactions = []
        if not load:
            # record account creation
            self.record_transaction("Account Created", 0, balance)
            # save a new account immediately
            self.save_to_file()


    def record_transaction(self, transaction_type, amount, new_balance):
        """Record a transaction in the history."""
        transaction = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "balance": new_balance
        }
        self.transactions.append(transaction)


    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance}")
                # record the transaction
                self.record_transaction("Deposit", amount, self.balance)
                # save the updated balance
                self.save_to_file()
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
                    # record the transaction
                    self.record_transaction("Withdrawal", amount, self.balance)
                    # save the updated balance
                    self.save_to_file()
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a number.")


    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    
    def trasfer_between_accounts(self, target_account, amount):
        try:
            amount = float(amount)
            if amount > 0:
                if self.balance >= amount:
                    # directly update balances without double-saving in withdraw/deposit
                    self.balance -= amount
                    target_account.balance += amount
                    print(f"Transferred ${amount} to account {target_account.account_number}")
                    # record transactions for both accounts
                    self.record_transaction(f"Transfer Out to {target_account.account_number}", amount, self.balance)
                    target_account.record_transaction(f"Transfer In from {self.account_number}", amount, target_account.balance)
                    # save both accounts after transfer
                    self.save_to_file()
                    target_account.save_to_file()
                else:
                    print("Insufficient funds for transfer. Transfer failed.")
            else:
                print("Transfer amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def save_to_file(self, filename=None):
        """Write the account data and full transaction history to a file. If no filename is provided
        the instance's own filename (based on its account number) is used.
        """
        if filename is None:
            filename = self.filename
        with open(filename, "w") as f:
            f.write(f"Account Number: {self.account_number}\n")
            f.write(f"Account Holder: {self.account_holder}\n")
            f.write(f"Current Balance: ${self.balance}\n\n")
            f.write("Transaction History:\n")
            for transaction in self.transactions:
                f.write(f"{transaction['timestamp']} - {transaction['type']}: ${transaction['amount']} (Balance: ${transaction['balance']})\n")


    def display_transaction_history(self):
        """Print the transaction history to the console."""
        print(f"\nTransaction History for Account {self.account_number} ({self.account_holder}):")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(f"{transaction['timestamp']} - {transaction['type']}: ${transaction['amount']} (Balance: ${transaction['balance']})")

def load_accounts():
    """Load existing accounts from their saved files."""
    accounts = {}
    for filename in os.listdir('.'):
        if filename.endswith('_account.txt'):
            try:
                # Extract account number from filename (source of truth)
                account_number = filename.replace('_account.txt', '')
                
                with open(filename, 'r') as f:
                    lines = f.readlines()
                if len(lines) < 3:
                    continue
                
                # Parse data from file content
                file_account_number = lines[0].strip().split(': ')[1] if ': ' in lines[0] else None
                account_holder = lines[1].strip().split(': ')[1] if ': ' in lines[1] else "Unknown"
                balance_str = lines[2].strip().split(': $')[1] if ': $' in lines[2] else "0"
                balance = float(balance_str)
                
                # Validate: account number in content should match filename
                if file_account_number and file_account_number != account_number:
                    print(f"Warning: Account number mismatch in {filename}. Filename says {account_number}, content says {file_account_number}. Using {account_number} from filename.")
                
                account = BankAccount(account_number, account_holder, balance, load=True)
                # parse transactions
                account.transactions = []
                if len(lines) > 4 and lines[3].strip() == "Transaction History:":
                    for line in lines[4:]:
                        line = line.strip()
                        if line:
                            parts = line.split(' - ')
                            if len(parts) == 2:
                                timestamp = parts[0]
                                rest = parts[1].split(': $')
                                if len(rest) == 2:
                                    trans_type = rest[0]
                                    amount_balance = rest[1].split(' (Balance: $')
                                    if len(amount_balance) == 2:
                                        amount = float(amount_balance[0])
                                        balance_end = float(amount_balance[1].rstrip(')'))
                                        transaction = {
                                            "timestamp": timestamp,
                                            "type": trans_type,
                                            "amount": amount,
                                            "balance": balance_end
                                        }
                                        account.transactions.append(transaction)
                
                # If this account number already exists, warn about duplicate
                if account_number in accounts:
                    print(f"Warning: Duplicate account number {account_number} found. Keeping the one from {accounts[account_number].filename}.")
                    continue
                
                accounts[account_number] = account
                # Re-save with corrected account number in content
                account.save_to_file()
            except (ValueError, IndexError) as e:
                # skip malformed files
                print(f"Warning: Could not parse {filename}: {e}")
                continue
    return accounts

def main():
    accounts = load_accounts()
    # ensure default accounts exist if not loaded
    if "123456789" not in accounts:
        accounts["123456789"] = BankAccount("123456789", "John Doe")
    if "987654321" not in accounts:
        accounts["987654321"] = BankAccount("987654321", "Jane Smith")
    account_number = random.randint(100000000, 999999999)

    while True:
        print("\nMini Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Create Account")
        print("5. Transfer Between Accounts")
        print("6. View Transaction History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter amount to deposit: ")
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        elif choice == '2':
            amount = input("Enter amount to withdraw: ")
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")
        elif choice == '4':
            while str(account_number) in accounts:
                account_number = random.randint(100000000, 999999999)
            account_holder = input("Enter account holder name: ")
            if account_number in accounts:
                print("Account number already exists. Please chose a different number.")
            else:
                accounts[str(account_number)] = BankAccount(str(account_number), account_holder)
                print(f"Account created for {account_holder} with account number {account_number}.")
        elif choice == '5':
            source_account_number = input("Enter source account number: ")
            target_account_number = input("Enter target account number: ")
            amount = input("Enter amount to transfer: ")
            if source_account_number in accounts and target_account_number in accounts:
                accounts[source_account_number].trasfer_between_accounts(accounts[target_account_number], amount)
            else:
                print("One or both account numbers are invalid.")
        elif choice == '6':
            account_number = input("Enter account number to view history: ")
            if account_number in accounts:
                accounts[account_number].display_transaction_history()
            else:
                print("Account not found.")
        elif choice == '7':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

