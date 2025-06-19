def validate_account_number(account_number):
    if isinstance(account_number, str) and len(account_number) == 10 and account_number.isdigit():
        return True
    return False

def validate_balance(balance):
    if isinstance(balance, (int, float)) and balance >= 0:
        return True
    return False