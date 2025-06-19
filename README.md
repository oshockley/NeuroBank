# Banking System

This project implements a simple banking system with classes for different types of bank accounts and functions for managing them.

## Project Structure

```
banking-system
├── Banking Classes
│   ├── banking.py
│   ├── checking.py
│   ├── savings.py
│   └── validation.py
├── Banking Functions
│   └── main.py
└── README.md
```

## Classes

### BankAccount (in `Banking Classes/banking.py`)
- **Properties**:
  - `account_number`: Unique identifier for the account.
  - `balance`: Current balance of the account.
- **Methods**:
  - `deposit(amount)`: Adds the specified amount to the account balance.
  - `withdraw(amount)`: Subtracts the specified amount from the account balance.

### CheckingAccount (in `Banking Classes/checking.py`)
- Inherits from `BankAccount`.
- **Methods**:
  - `write_check(amount)`: Allows the account holder to write a check for the specified amount.

### SavingsAccount (in `Banking Classes/savings.py`)
- Inherits from `BankAccount`.
- **Methods**:
  - `add_interest(rate)`: Adds interest to the account balance based on the specified rate.

### Validation Functions (in `Banking Classes/validation.py`)
- **Functions**:
  - `validate_account_number(account_number)`: Validates the format of the account number.
  - `validate_balance(balance)`: Ensures the balance is a valid amount.

## Banking Functions

### Main Entry Point (in `Banking Functions/main.py`)
This file contains the main logic for creating accounts, processing transactions, and displaying account information.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd banking-system
   ```
3. Install any required dependencies (if applicable).

## Usage Examples

- Create a checking account and perform transactions.
- Create a savings account and add interest.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.