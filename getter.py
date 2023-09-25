
# given one line of the master file, return the account number
def get_number(file_line):
    ACCOUNT_NUMBER_TAIL = 6
    account_num = file_line[:ACCOUNT_NUMBER_TAIL]
    return account_num

# given one line, return the account balance (as a float)
def get_balance(file_line):
    ACCOUNT_BALANCE_HEAD = 7
    ACCOUNT_BALANCE_TAIL = 17
    account_balance = float(file_line[ACCOUNT_BALANCE_HEAD:ACCOUNT_BALANCE_TAIL])
    return account_balance

# given one line, return the account holder’s name (as a string)
def get_name(file_line):
    ACCOUNT_HOLDER_HEAD = 18
    account_name = file_line[ACCOUNT_HOLDER_HEAD:]
    return account_name

def input_validator(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
