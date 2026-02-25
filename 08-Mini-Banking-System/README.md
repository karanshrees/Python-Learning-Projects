# Mini Banking System

A command-line banking application with basic account management features. Future versions will include multiple accounts, account transfers, and file persistence.

## How to Run
```bash
python mini_banking_system.py
```

## Current Features
✅ **Create Account** - Create a bank account with account number and holder name
✅ **Deposit** - Add money to your account
✅ **Withdraw** - Remove money from your account (with balance check)
✅ **Check Balance** - View current account balance
✅ **Input Validation** - Validates all monetary amounts
✅ **Error Handling** - Handles invalid inputs gracefully

## Upcoming Features (Planned Enhancements)
🔄 **Multiple Accounts** - Manage multiple bank accounts
🔄 **Unique Account Numbers** - Auto-generate or validate unique account numbers
🔄 **Account Transfers** - Transfer money between accounts
🔄 **File Persistence** - Save accounts to file and load on startup
🔄 **Transaction History** - Track all transactions
🔄 **Account Interest** - Calculate interest on savings

## How It Works

### Main Menu
```
Mini Banking System
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
```

### Features Explained

#### 1. Deposit
- Enter the amount to deposit
- Amount must be positive
- Balance updates immediately
- Shows new balance after deposit

#### 2. Withdraw
- Enter the amount to withdraw
- Amount must be positive
- Checks if you have sufficient funds
- Prevents overdraft
- Shows new balance after withdrawal

#### 3. Check Balance
- Displays current account balance
- Shows formatted balance

#### 4. Exit
- Safely exit the application

## Example Usage

### Deposit Money
```
Mini Banking System
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter your choice: 1
Enter amount to deposit: 1000
Deposited $1000.0. New balance: $1000.0
```

### Withdraw Money
```
Enter your choice: 2
Enter amount to withdraw: 500
Withdrew $500.0. New balance: $500.0
```

### Check Balance
```
Enter your choice: 3
Current balance: $500.0
```

### Attempt to Withdraw More Than Balance
```
Enter your choice: 2
Enter amount to withdraw: 1000
Insufficient funds.
```

### Invalid Amount
```
Enter your choice: 1
Enter amount to deposit: abc
Invalid amount. Please enter a number.
```

## File Structure
```
08-Mini-Banking-System/
├── mini_banking_system.py    # Main application
└── README.md                 # This file
```

## Technical Details

### Class: BankAccount
The `BankAccount` class represents a single bank account with:

**Attributes:**
- `account_number` - Unique identifier for the account
- `account_holder` - Name of the account owner
- `balance` - Current account balance (default: 0)

**Methods:**
- `deposit(amount)` - Add money to account
- `withdraw(amount)` - Remove money from account
- `check_balance()` - Display current balance

### Input Validation
- Amounts must be valid numbers (integers or decimals)
- Amounts must be positive (> 0)
- Withdrawals checked against balance

### Error Handling
- Catches invalid number inputs (ValueError)
- Prevents negative amounts
- Prevents overdrafts
- Graceful error messages

## Learning Concepts
- Object-Oriented Programming (OOP)
- Classes and Objects
- Class methods
- Instance variables
- Exception handling (try-except)
- User input validation
- Menu-driven application design
- String formatting (f-strings)

## Current Limitations
- ❌ Only one account per session
- ❌ Account data not saved to file
- ❌ No transaction history
- ❌ No account transfers
- ❌ Data lost when program exits

## Future Enhancement Roadmap

### Version 2.0 (Planned)
- [ ] Support multiple accounts
- [ ] Generate unique account numbers
- [ ] Transfer between accounts
- [ ] Save accounts to file (JSON or CSV)
- [ ] Load accounts on startup

### Version 3.0 (Planned)
- [ ] Transaction history
- [ ] Interest calculation
- [ ] Account types (Savings, Checking, etc.)
- [ ] Pin/Password protection
- [ ] Better formatting and UI

## Example Workflow
```
1. Run program
2. Deposit initial amount (e.g., $1000)
3. Make a withdrawal (e.g., $200)
4. Check balance to verify
5. Repeat steps 2-4 as needed
6. Exit when done
```

## Notes
- Currently stores account in memory only
- Account data is lost when program exits
- Perfect starting point for learning OOP
- Ready for enhancement with file persistence

## How to Use in Future Versions

Once multiple accounts are added:
```
Mini Banking System
1. Create Account
2. Select Account
3. Deposit
4. Withdraw
5. Check Balance
6. View All Accounts
7. Transfer Between Accounts
8. Exit
```