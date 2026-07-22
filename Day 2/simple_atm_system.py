# Simple ATM System
# Basic banking operations: Check Balance, Deposit, Withdraw

def atm_system():
    balance = 1000.0  # Starting balance
    pin = "1234"      # Default PIN

    print("=" * 40)
    print("         WELCOME TO PYTHON BANK ATM")
    print("=" * 40)

    # Verify PIN
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin != pin:
        print("Incorrect PIN. Access denied.")
        return

    while True:
        print("\n" + "-" * 40)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("-" * 40)

        choice = input("Select an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    balance += amount
                    print(f"${amount:.2f} deposited successfully.")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > balance:
                    print("Insufficient funds.")
                elif amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    balance -= amount
                    print(f"${amount:.2f} withdrawn successfully.")
                    print(f"Remaining balance: ${balance:.2f}")
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "4":
            print("Thank you for using Python Bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    atm_system()
