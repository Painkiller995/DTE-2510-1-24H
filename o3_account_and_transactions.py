"""
This module represents an account and transactions implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


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
            self._balance -= amount
            return True
        return False

    def __str__(self) -> str:
        return (
            f"Customer ID: {self._cust_id}, "
            f"Account No: {self._account_no}, "
            f"Balance: {self._balance:.2f}, "
            f"Interest Rate: {self._interest:.2f}%"
        )
