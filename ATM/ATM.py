class BankAccount:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    @staticmethod
    def display_menu():
        print("\nATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def show_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            print(f"Deposit successful. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def transfer(self, amount, recipient_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient_account.user_id}")
            print(f"Transfer successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid transfer amount or insufficient funds.")


def authenticate_user():
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")
    # You might want to implement a more secure authentication mechanism in a real-world scenario.

    print(f"\nWelcome, {user_id}!")
    print("Available Choices:")
    print("1. Transactions History")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transfer")
    print("5. Quit")

    return user_id, pin


def main():
    print("Welcome to the ATM System!")
    user_id, pin = authenticate_user()

    # Assuming we have two accounts for demonstration purposes
    account1 = BankAccount("user1", "1234")
    account2 = BankAccount("user2", "5678")

    if user_id == account1.user_id and pin == account1.pin:
        current_account = account1
    elif user_id == account2.user_id and pin == account2.pin:
        current_account = account2
    else:
        print("Authentication failed. Exiting.")
        return

    while True:
        current_account.display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            current_account.show_transaction_history()
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            current_account.withdraw(amount)
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            current_account.deposit(amount)
        elif choice == "4":
            amount = float(input("Enter transfer amount: "))
            recipient_id = input("Enter recipient's user ID: ")
            recipient_account = account1 if recipient_id == account1.user_id else account2
            current_account.transfer(amount, recipient_account)
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
