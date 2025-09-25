class BankAccount:
    """
    Represents a bank account with basic functionalities like deposit, withdrawal,
    and balance inquiry.
    """

    def __init__(self, account_holder, initial_balance=0):
        """
        Initializes a new BankAccount object.

        Args:
            account_holder (str): The name of the account holder.
            initial_balance (float): The initial balance of the account.
                                     Defaults to 0.
        """
        self.__account_holder = account_holder  # Encapsulated attribute
        self.__balance = initial_balance      # Encapsulated attribute
        print(f"Account for {self.__account_holder} created with initial balance: ${self.__balance:.2f}")

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        return self.__balance

    def get_account_holder(self):
        """
        Returns the name of the account holder.

        Returns:
            str: The account holder's name.
        """
        return self.__account_holder

# --- Usage Example ---
if __name__ == "__main__":
    # Create account objects
    account1 = BankAccount("Alice Smith", 1000)
    account2 = BankAccount("Bob Johnson")

    # Perform operations on account1
    account1.deposit(500)
    account1.withdraw(200)
    print(f"Alice's current balance: ${account1.get_balance():.2f}")

    # Perform operations on account2
    account2.deposit(150)
    account2.withdraw(50)
    account2.withdraw(500) # Attempt to withdraw more than available
    print(f"Bob's current balance: ${account2.get_balance():.2f}")