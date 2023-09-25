import getter

# CONSTANTS
SENTINEL = "999999"
ACC_BALANCE_MIN = 0.00
ACC_BALANCE_MAX = 9999999.99
ACC_NUM_MIN = 100000
ACC_NUM_MAX = 999998


def main():
    # getting the prefix
    file_prefix = input("Enter a file prefix: ")
    old_filename = f"{file_prefix}_old.txt"
    new_filename = f"{file_prefix}_new.txt"

    # Handling file not found error
    try:
        old_file = open(old_filename, "r")
    except FileNotFoundError:
        print("The file doesn't exist")
    else:

        new_file = open(new_filename, "w")
        file_line = old_file.readline().strip("\n")

        while file_line != SENTINEL:
            # extracting account number, balance and holder info from each line
            acc_num = getter.get_number(file_line)
            acc_balance = getter.get_balance(file_line)
            acc_holder = getter.get_name(file_line)

            print("Verifying input: {:s} {:f} {:s}".format(acc_num, acc_balance, acc_holder))

            transaction_on = True
            while transaction_on:
                transaction_code = input("Enter transaction code (d,w,c,a):").lower()
                while transaction_code not in ("d", "w", "c", "a"):
                    transaction_code = input("Enter valid transaction code (d,w,c,a):").lower()

                # handling deposit
                if transaction_code == "d":
                    deposit_amount = input("Enter deposit amount: ")
                    while not (getter.input_validator(deposit_amount)):
                        print("INVALID INPUT: Please enter a numeric value. ")
                        deposit_amount = input("Enter deposit amount: ")
                    deposit_amount = float(deposit_amount)
                    while deposit_amount <= 0.00:
                        print("INVALID INPUT: Please enter a numeric value greater than 0.")
                        deposit_amount = float(input("Enter deposit amount: "))
                    if round(acc_balance + deposit_amount, 2) > ACC_BALANCE_MAX:
                        print("Max Account Balance exceeded, deposit failed!")
                    else:
                        acc_balance = round(acc_balance + deposit_amount, 2)

                # handling withdrawl
                elif transaction_code == "w":
                    withdraw_amount = input("Enter withdraw amount: ")
                    while not (getter.input_validator(withdraw_amount)):
                        print("INVALID INPUT: Please enter a numeric value.")
                        withdraw_amount = input("Enter withdraw amount: ")
                    withdraw_amount = float(withdraw_amount)
                    while withdraw_amount <= 0.00:
                        print("INVALID INPUT: Please enter a numeric value greater than 0.")
                        withdraw_amount = float(input("Enter withdraw amount: "))
                    if round(acc_balance - withdraw_amount, 2) < ACC_BALANCE_MIN:
                        print("Min Account Balance exceeded, withdrawl failed!")
                    else:
                        acc_balance = round(acc_balance - withdraw_amount, 2)

                # handling closing account
                elif transaction_code == "c":
                    if (acc_balance > 0):
                        print("Account not closed because money is still in it.")
                    else:
                        print("Account is closed")

                # handling advancing
                elif transaction_code == "a":
                    new_file_line = f"{acc_num} {acc_balance:10.2f} {acc_holder}"
                    print("New balance:{:s}".format(new_file_line))
                    new_file.write(f"{new_file_line}\n")
                    transaction_on = False
                else:
                    print("Invalid transaction code")

            # move to another line
            file_line = old_file.readline().strip("\n")

        new_file.write(SENTINEL)
        old_file.close()
        new_file.close()


main()


