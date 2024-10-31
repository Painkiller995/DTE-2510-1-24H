"""
This module represents implementation of employee hierarchy.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


class Employee:
    """
    This class represents an employee.
    """

    def __init__(self, name: str, emp_id: int):
        self._name = name
        self._emp_id = emp_id
        self._monthly_salaries: list[float] = []

    @property
    def name(self) -> str:
        """
        The name of the employee.

        Returns:
            The name of the employee.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the name of the employee.
        """
        self._name = value

    @property
    def emp_id(self) -> int:
        """
        The employee ID.

        Returns:
            The employee ID.
        """
        return self._emp_id

    @property
    def monthly_salaries(self) -> list[float]:
        """
        The monthly salaries of the employee.

        Returns:
            The monthly salaries of the employee.
        """
        return self._monthly_salaries

    def add_salary(self, salary: float) -> None:
        """
        Add a salary to the employee.

        Args:
            salary: The salary to add.
        """
        self._monthly_salaries.append(salary)

    def print_salaries(self) -> None:
        """
        Print the salaries of the employee.
        """
        print(
            f"Salaries for {self._name} (ID: {self._emp_id}): {self._monthly_salaries}"
        )
