"""
This module represents a calculator implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

from typing import Literal


class Calculator:
    """
    Represents a simple calculator that can perform basic arithmetic operations.
    """

    def __init__(self):
        self._log = []

    def calculate(
        self,
        operand1: float,
        operand2: float,
        operator: Literal["*", "/", "+", "-"],
    ) -> float | None:
        """
        Calculate the result of the operation.

        Args:
            operand1: The first operand.
            operand2: The second operand.
            operator: The operator to use for the operation.

        Returns:
            The result of the operation.
        """
        if operator not in ["*", "/", "+", "-"]:
            raise ValueError("Invalid operator provided, please use one of: *, /, +, -")

        if operand1 is None or operand2 is None:
            raise ValueError("Operands cannot be None")

        if operator == "/" and operand2 == 0:
            raise ValueError("Division by zero")

        result = None

        if operator == "*":
            result = operand1 * operand2
        elif operator == "/":
            result = operand1 / operand2
        elif operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2

        expression = f"{operand1} {operator} {operand2} = {result}"
        self.add_to_log(expression)

        return result

    def get_log(self) -> list[str]:
        """
        Get the log of calculations performed.

        Returns:
            The log of calculations performed.
        """
        return self._log

    def get_last_logged(self) -> str | None:
        """
        Get the last calculation performed.

        Returns:
            The last calculation performed.
        """
        if len(self._log) == 0:
            return "No calculations available"
        return self._log[-1]

    def add_to_log(self, expression: str) -> None:
        """
        Add a calculation to the log.

        Args:
            expression: The calculation to add to the log.
        """
        self._log.append(expression)

    def clear_log(self) -> None:
        """
        Clear the log of calculations.
        """
        self._log.clear()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculate(1, 2, "+")
    calculator.calculate(2, 2, "*")
    calculator.calculate(16, 2, "/")
    print(calculator.get_log())
    print(calculator.get_last_logged())
