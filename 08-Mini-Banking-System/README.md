# Mini Banking System

A comprehensive command-line banking application with multiple accounts, file persistence, and transaction history tracking. Perfect for learning Object-Oriented Programming concepts!

## How to Run
```bash
python mini_banking_system.py
```

## Current Features ✅
✅ **Multiple Accounts** - Create and manage multiple bank accounts
✅ **Unique Account Numbers** - Auto-generated 9-digit account numbers
✅ **Deposit** - Add money to your account
✅ **Withdraw** - Remove money with balance verification
✅ **Check Balance** - View current account balance
✅ **Transfer Between Accounts** - Send money from one account to another
✅ **File Persistence** - Accounts automatically saved to individual files
✅ **Transaction History** - Track all transactions with timestamps
✅ **Auto-Load Accounts** - Previously created accounts load on startup
✅ **Input Validation** - Validates all monetary amounts
✅ **Error Handling** - Graceful error handling throughout

## How It Works

### Main Menu
```
Mini Banking System
1. Deposit
2. Withdraw
3. Check Balance
4. Create Account
5. Transfer Between Accounts
6. View Transaction History
7. Exit
```

### Features Explained

#### 1. Deposit
- Enter account number
- Enter amount to deposit
- Amount must be positive
- Balance updates immediately
- Transaction recorded with timestamp
- Account saved to file

#### 2. Withdraw
- Enter account number
- Enter amount to withdraw
- Amount must be positive
- Balance checked (prevents overdraft)
- Transaction recorded with timestamp
- Account saved to file

#### 3. Check Balance
- Enter account number
- Displays current balance

#### 4. Create Account
- Auto-generates unique 9-digit account number
- Enter account holder name
- Account created and immediately saved to file
- Ready for transactions

#### 5. Transfer Between Accounts
- Enter source account number
- Enter target account number
- Enter transfer amount
- Both accounts updated
- Transaction recorded for both accounts
- Both accounts saved to file

#### 6. View Transaction History
- Enter account number
- Displays all transactions with:
  - Timestamp (YYYY-MM-DD HH:MM:SS)
  - Transaction type
  - Amount
  - Balance after transaction

#### 7. Exit
- Safely exit the application

## Example Usage

### Creating an Account
```
Enter your choice: 4
Enter account holder name: Alice Johnson
Account created for Alice Johnson with account number 456789123.
```

### Depositing Money
```
Enter your choice: 1
Enter amount to deposit: 5000
Enter account number: 456789123
Deposited $5000.0. New balance: $5000.0
```

### Withdrawing Money
```
Enter your choice: 2
Enter amount to withdraw: 1000
Enter account number: 456789123
Withdrew $1000.0. New balance: $4000.0
```

### Transferring Between Accounts
```
Enter your choice: 5
Enter source account number: 123456789
Enter target account number: 456789123
Enter amount to transfer: 2000
Transferred $2000 to account 456789123
```

### Viewing Transaction History
```
Enter your choice: 6
Enter account number to view history: 456789123

Transaction History for Account 456789123 (Alice Johnson):
2026-02-16 12:30:45 - Account Created: $0 (Balance: $5000.0)
2026-02-16 12:31:10 - Deposit: $5000.0 (Balance: $5000.0)
2026-02-16 12:32:20 - Withdrawal: $1000.0 (Balance: $4000.0)
2026-02-16 12:33:45 - Transfer In from 123456789: $2000.0 (Balance: $6000.0)
```

## File Structure
```
08-Mini-Banking-System/
├── mini_banking_system.py       # Main application
├── 123456789_account.txt        # John Doe's account (auto-created)
├── 987654321_account.txt        # Jane Smith's account (auto-created)
├── 456789123_account.txt        # Example new account file
└── README.md                    # This file
```

## Account Data Files

Each account is stored in a separate file: `{account_number}_account.txt`

**File Format:**
```
Account Number: 456789123
Account Holder: Alice Johnson
Current Balance: $6000.0

Transaction History:
2026-02-16 12:30:45 - Account Created: $0 (Balance: $5000.0)
2026-02-16 12:31:10 - Deposit: $5000.0 (Balance: $5000.0)
2026-02-16 12:32:20 - Withdrawal: $1000.0 (Balance: $4000.0)
2026-02-16 12:33:45 - Transfer In from 123456789: $2000.0 (Balance: $6000.0)
```

## Technical Details

### Class: BankAccount
The `BankAccount` class represents a single bank account with:

**Attributes:**
- `account_number` - Unique 9-digit identifier
- `account_holder` - Name of the account owner
- `balance` - Current account balance
- `filename` - Filename for persistent storage
- `transactions` - List of transaction records

**Methods:**
- `deposit(amount)` - Add money to account
- `withdraw(amount)` - Remove money from account
- `check_balance()` - Display current balance
- `transfer_between_accounts(target_account, amount)` - Transfer to another account
- `record_transaction(type, amount, new_balance)` - Log transaction
- `save_to_file()` - Save account data to file
- `display_transaction_history()` - Show all transactions

### Key Functions
- `load_accounts()` - Load all existing accounts from files
- `main()` - Main menu loop

### Data Persistence
- Each account saved in separate file
- Files named: `{account_number}_account.txt`
- Accounts auto-load on program startup
- Every transaction immediately saved
- Transaction history preserved

### Account Number Generation
- Random 9-digit numbers (100000000 - 999999999)
- Checked for uniqueness
- Prevents duplicate account numbers

## Input Validation
- Amounts must be valid numbers (integer or decimal)
- Amounts must be positive (> 0)
- Withdrawals checked against balance
- Account numbers validated before operations
- Prevents overdraft transactions

## Error Handling
- Catches invalid number inputs (ValueError)
- Handles missing account numbers
- Validates file format when loading
- Graceful error messages
- Skips malformed account files

## Learning Concepts
- **Object-Oriented Programming (OOP)**
  - Classes and Objects
  - Instance variables and methods
  - Encapsulation
  
- **File I/O**
  - Reading and writing files
  - Data persistence
  - File parsing
  
- **Data Management**
  - Dictionaries for account storage
  - Lists for transaction history
  - Timestamp tracking
  
- **Exception Handling**
  - Try-except blocks
  - ValueError handling
  - File operations

- **Application Design**
  - Menu-driven interface
  - Input validation
  - Error handling

## Default Accounts
Two accounts are created automatically on first run:
- **John Doe** (Account: 123456789)
- **Jane Smith** (Account: 987654321)

You can add more accounts using option 4 in the menu.

## Workflow Example
```
1. Run program (accounts auto-load)
2. Create new account (auto-generates number)
3. Deposit money to account
4. Withdraw money from account
5. Transfer between accounts
6. View transaction history
7. Close program (data saved)
8. Run program again (accounts still there!)
```

## Future Enhancement Ideas
- [ ] PIN/Password protection for accounts
- [ ] Interest calculation on savings accounts
- [ ] Different account types (Checking, Savings, Credit)
- [ ] Overdraft protection options
- [ ] Monthly statements
- [ ] Account closure
- [ ] Customer database
- [ ] Database integration (instead of text files)

## Common Use Cases

### Scenario 1: New User
```
1. Run program
2. Option 4: Create Account
3. Enter name and receive account number
4. Option 1: Deposit initial amount
5. Option 6: View transaction history
```

### Scenario 2: Multiple Accounts
```
1. Create Account 1 (John)
2. Create Account 2 (Jane)
3. Deposit to John's account
4. Deposit to Jane's account
5. Transfer from John to Jane
6. Both accounts saved automatically
```

### Scenario 3: Program Restart
```
1. Close and reopen program
2. Previous accounts automatically loaded
3. All transaction history preserved
4. Continue where you left off
```

## Important Notes
- Data persists between program sessions
- Each account has its own file
- Transactions cannot be deleted (audit trail)
- Transfer updates both accounts atomically
- Files are auto-created and auto-updated