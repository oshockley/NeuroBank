from Banking_Classes.banking import BankAccount
from Banking_Classes.checking import CheckingAccount
from Banking_Classes.savings import SavingsAccount
from Banking_Classes.validation import validate_account_number, validate_balance

def main():
    accounts = {}

    while True:
        print("Welcome to the Banking System")
        print("1. Create Checking Account")
        print("2. Create Savings Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display Account Information")
        print("6. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            if validate_account_number(account_number):
                accounts[account_number] = CheckingAccount(account_number)
                print("Checking account created successfully.")
            else:
                print("Invalid account number.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            if validate_account_number(account_number):
                accounts[account_number] = SavingsAccount(account_number)
                print("Savings account created successfully.")
            else:
                print("Invalid account number.")

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in accounts and validate_balance(amount):
                accounts[account_number].deposit(amount)
                print("Deposit successful.")
            else:
                print("Invalid account number or amount.")

        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in accounts and validate_balance(amount):
                if accounts[account_number].withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid account number or amount.")

        elif choice == '5':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account_info = accounts[account_number]
                print(f"Account Number: {account_info.account_number}, Balance: {account_info.balance}")
            else:
                print("Account not found.")

        elif choice == '6':
            print("Exiting the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()