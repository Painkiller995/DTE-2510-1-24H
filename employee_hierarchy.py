"""
This module represents implementation of employee hierarchy.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

from abc import abstractmethod


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

    @abstractmethod
    def calculate_payroll(self) -> float:
        """
        Calculate the payroll for the employee.

        Returns:
            The salary of the employee.
        """


class SalaryEmployee(Employee):
    """
    This class represents an employee that is paid a fixed monthly salary.
    """

    def __init__(self, name: str, emp_id: int, monthly_salary: float):
        super().__init__(name, emp_id)
        self._monthly_salary = monthly_salary

    @property
    def monthly_salary(self) -> float:
        """
        The monthly salary of the employee.

        Returns:
            The monthly salary of the employee.
        """
        return self._monthly_salary

    def calculate_payroll(self):
        """
        Calculate the payroll for the employee.

        Returns:
            The monthly salary of the employee.
        """
        self.add_salary(self._monthly_salary)
        return self._monthly_salary


class HourlyEmployee(Employee):
    """
    This class represents an employee that is paid by the hour.
    """

    def __init__(self, name: str, emp_id: int, hourly_rate: float):
        super().__init__(name, emp_id)
        self._hourly_rate = hourly_rate
        self._hours_worked = 0

    @property
    def hourly_rate(self) -> float:
        """
        The hourly rate of the employee.

        Returns:
            The hourly rate of the employee.
        """
        return self._hourly_rate

    @property
    def hours_worked(self) -> int:
        """
        The number of hours worked by the employee.

        Returns:
            The number of hours worked by the employee.
        """
        return self._hours_worked

    def add_hours(self, hours: int) -> None:
        """
        Add hours worked by the employee.

        Args:
            hours: The hours worked.
        """
        self._hours_worked = hours

    def calculate_payroll(self) -> float:
        """
        Calculate the payroll for the employee.

        Returns:
            The salary of the employee.
        """
        salary = self._hours_worked * self._hourly_rate
        self.add_salary(salary)
        return salary


class CommissionEmployee(Employee):
    """
    This class represents an employee that is paid a base salary plus commission.
    """

    def __init__(self, name: str, emp_id: int, base_salary: float, commission: float):
        super().__init__(name, emp_id)
        self._base_salary = base_salary
        self._commission = commission

    @property
    def base_salary(self):
        """
        The base salary of the employee.

        Returns:
            The base salary of the employee.
        """
        return self._base_salary

    @property
    def commission(self):
        """
        The commission of the employee.

        Returns:
            The commission of the employee.
        """
        return self._commission

    def calculate_payroll(self):
        """
        Calculate the payroll for the employee.

        Returns:
            The salary of the employee.
        """
        total_salary = self._base_salary + self._commission
        self.add_salary(total_salary)
        return total_salary


if __name__ == "__main__":
    salary_employee = SalaryEmployee("Alice", 1, 3000)
    hourly_employee = HourlyEmployee("Bob", 2, 20)
    commission_employee = CommissionEmployee("Charlie", 3, 2700, 500)

    for month in range(1, 4):
        print(f"Month {month}:")

        hourly_employee.add_hours(160)

        for employee in [salary_employee, hourly_employee, commission_employee]:
            payroll = employee.calculate_payroll()
            print(
                f"{employee.name} (ID: {employee.emp_id}) - Payroll: {payroll:.2f} NOK"
            )

        print()

    for employee in [salary_employee, hourly_employee, commission_employee]:
        employee.print_salaries()
