class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"

# Sample program to create and test a BankAccount instance
if __name__ == "__main__":
    # Create a bank account with initial balance of $1000
    account = BankAccount("123456", "John Doe", 1000)

    print(account.display_balance())  # Display initial balance
    print(account.deposit(500))        # Deposit $500
    print(account.withdraw(200))       # Withdraw $200
    print(account.withdraw(1500))      # Attempt to withdraw more than the balance
    print(account.display_balance())  # Display updated balance