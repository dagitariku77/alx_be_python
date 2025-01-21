# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Initialize account with a default starting balance of 100
    account = BankAccount(100)

    # Check if enough command-line arguments were provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform actions based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Please use: deposit, withdraw, or display.")

if __name__ == "__main__":
    main()
