"""
This module represents an account and transactions implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

from datetime import datetime


class Account:
    """
    This class represents an account.

    Attributes:
        cust_id: The customer ID.
        account_no: The account number.
        balance: The account balance.
        interest: The account interest rate.

    Methods:
        deposit: Deposits money to the account.
        withdraw: Withdraws money from the account.

    """

    def __init__(
        self,
        cust_id: int,
        account_no: int,
        balance: float = 0.0,
        interest: float = 0.0,
    ):
        self._cust_id = cust_id
        self._account_no = account_no
        self._balance = balance
        self._interest = interest

        self._transactions: list[Transaction] = []

    @property
    def cust_id(self) -> int:
        """Read-only property for customer ID."""
        return self._cust_id

    @property
    def account_no(self) -> int:
        """Read-only property for account number."""
        return self._account_no

    @property
    def balance(self) -> float:
        """Read-only property for account balance."""
        return self._balance

    @property
    def interest(self) -> float:
        """Read-only property for account interest."""
        return self._interest

    def deposit(self, amount) -> None:
        """
        This method deposits money to the account.
        Args:
            amount: The amount to deposit.
        """
        self._transactions.append(Transaction(amount))
        self._balance += amount

    def withdraw(self, amount) -> bool:
        """
        This method withdraws money from the account.
        Args:
            amount: The amount to withdraw.
        Returns:
            True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and self._balance - amount >= 0:
            self._transactions.append(Transaction(-amount))
            self._balance -= amount
            return True
        return False

    def show_transactions(self) -> None:
        """This method shows all transactions."""
        for transaction in self._transactions:
            print(transaction)

    def __str__(self) -> str:
        return (
            f"Customer ID: {self._cust_id}, "
            f"Account No: {self._account_no}, "
            f"Balance: {self._balance:.2f}, "
            f"Interest Rate: {self._interest:.2f}%"
        )


class Transaction:
    """
    This class represents a transaction.

    Attributes:
        time: The transaction time.
        amount: The transaction amount.
    """

    def __init__(self, amount: float = 0.0):
        self._time: str = self._get_time_as_str()
        self._amount = amount

    @property
    def time(self) -> str:
        """Read-only property for transaction time."""
        return self._time

    @property
    def amount(self) -> float:
        """Read-only property for transaction amount."""
        return self._amount

    def _get_time_as_str(self) -> str:
        """
        This method returns the transaction time as a string.
        Returns:
            The transaction time as a string.
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"Time: {self._time}, Amount: {self._amount:.2f}"


if __name__ == "__main__":
    # Create an account
    account = Account(1, 1000, 50000.0, 7)
    print(f"Account created:\n{account}")

    # Deposit money
    account.deposit(500.0)
    print(f"New balance after depositing 500 is {account.balance}")

    # Withdraw money
    if account.withdraw(1000.0):
        print(f"New balance after withdrawal of 1000 is {account.balance}")
    else:
        print("Withdrawal failed.")

    print("Transactions:")
    account.show_transactions()
