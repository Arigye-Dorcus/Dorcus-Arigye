
print("=== Welcome to Secure ATM ===")
account_balance = 1000.00
correct_password = "1234" 
attempts_remaining = 3


while attempts_remaining > 0:
    entered_password = input("Please enter your 4-digit PIN: ")
    
    if entered_password == correct_password:
        print("PIN accepted. Access granted.")
        break
    else:
        attempts_remaining -= 1
        if attempts_remaining > 0:
            print(f"Incorrect PIN. {attempts_remaining} attempts remaining.")
        else:
            print("Too many incorrect attempts. Your card is temporarily blocked.")
            exit()


print(f"\nYour current balance: ${account_balance:.2f}")

try:
    withdrawal_amount = float(input("Enter amount to withdraw: $"))
    
    if withdrawal_amount <= 0:
        print("Invalid amount. Please enter a positive number.")
    elif withdrawal_amount > account_balance:
        print("Insufficient funds. Your current balance is ${:.2f}".format(account_balance))
    else:

        account_balance -= withdrawal_amount
        print("\nProcessing transaction...")
        print("Withdrawal successful! Please take your cash.")
        print("Remaining balance: ${:.2f}".format(account_balance))
        
except ValueError:
    print("Invalid input. Please enter a numeric value.")

print("\nThank you for using Secure ATM. Have a nice day!")