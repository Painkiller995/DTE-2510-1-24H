"""
This module represents a gui calculator implementation.

Dependencies:
    - tkinter
    o4_calculator.py available in the same repository on github.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import tkinter as tk
from tkinter import messagebox
from typing import Callable, Literal

from o4_calculator import Calculator


class CalculatorGUI(tk.Frame):
    """
    Represents a simple calculator GUI.
    """

    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)

        self.root.title("Calculator GUI")
        self.set_window_shape()

        self.initialize_inputs()
        self.initialize_buttons()
        self.initialize_output()

        self.calculator = Calculator()

    def set_window_shape(self, width=300, height=400) -> None:
        """
        Sets the window size and positions it in the center of the screen.

        Args:
            width: The width of the window.
            height: The height of the window.
        """
        position_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        position_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{position_x}+{position_y}")
        self.root.resizable(False, False)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def initialize_inputs(self) -> None:
        """
        Creates the input fields for the calculator
        """

        input_frame = tk.Frame(self.root)
        input_frame.grid(row=1, column=1, pady=10)

        operand_1 = tk.Label(input_frame, text="Operand 1:")
        operand_1.grid(column=0, row=0, pady=3, padx=3)

        operator = tk.Label(input_frame, text="Operator (+, -, *, /):")
        operator.grid(column=0, row=1, pady=3, padx=3)

        operand_2 = tk.Label(input_frame, text="Operand 2:")
        operand_2.grid(column=0, row=2, pady=3, padx=3)

        self.operand1_entry = self.create_valid_entry(
            input_frame, validator=self.validate_float
        )
        self.operand1_entry.grid(column=1, row=0, pady=3, padx=3)

        self.operator_entry = self.create_valid_entry(
            input_frame, validator=self.validate_operator
        )
        self.operator_entry.grid(column=1, row=1, pady=3, padx=3)

        self.operand2_entry = self.create_valid_entry(
            input_frame, validator=self.validate_float
        )
        self.operand2_entry.grid(column=1, row=2, pady=3, padx=3)

    def initialize_buttons(self) -> None:
        """
        Creates and centers the buttons for the calculator.
        """

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        tk.Button(button_frame, text="Calculate", command=self.calculate).grid(
            column=0, row=0, pady=3, padx=3
        )

        tk.Button(button_frame, text="Clear", command=self.clear).grid(
            column=1, row=0, pady=3, padx=3
        )

        tk.Button(
            button_frame, text="Clear log", command=lambda: self.clear(True)
        ).grid(column=2, row=0, pady=3, padx=3)

        tk.Button(button_frame, text="Quit", command=self.root.quit).grid(
            column=3, row=0, pady=3, padx=3
        )

    def initialize_output(self) -> None:
        """
        Creates the output field for the calculator.
        """

        output_frame = tk.Frame(self.root)
        output_frame.grid(row=3, column=1, pady=10)

        self.output_label = tk.Label(output_frame, text="Result:")
        self.output_label.grid(column=0, row=0, pady=3, padx=3)

        self.result_label = tk.Label(output_frame, text="")
        self.result_label.grid(column=1, row=0, pady=3, padx=3)

        self.logs = tk.Text(output_frame, height=10, width=30)
        self.logs.grid(column=0, row=1, columnspan=2, pady=3, padx=3)
        self.logs.config(state=tk.DISABLED)

    def create_valid_entry(self, parent: tk.Widget, validator: Callable) -> tk.Entry:
        """
        Creates an entry field with validation.

        Args:
            parent: The parent widget.
            validator: The validation function.

        Returns:
            The created entry field.
        """

        validate_cmd = (self.root.register(validator), "%P")
        entry = tk.Entry(parent, validate="key", validatecommand=validate_cmd)
        return entry

    def validate_operator(self, operator: str) -> bool:
        """
        Validates that the input in operator_entry is one of the allowed operators.
        """
        if operator in {"+", "-", "*", "/"} or operator == "":
            return True
        else:
            return False

    def validate_float(self, entry_value: str) -> bool:
        """
        Validates that the input in operand entries is a valid float.

        Args:
            entry_value: The value of the entry field.

        Returns:
            True if the input is a valid float, False otherwise
        """

        if entry_value == "":
            return True

        if " " in entry_value:
            return False

        try:
            float(entry_value)
            return True
        except ValueError:
            return False

    def calculate(self) -> None:
        """
        Calculates the result of the expression and adds it to the log.
        """
        try:
            operand1_str = self.operand1_entry.get()
            operand2_str = self.operand2_entry.get()
            operator = self.operator_entry.get()

            if not all([operand1_str, operand2_str, operator]):
                raise ValueError("Please fill in all fields before calculating")

            operand1, operand2 = float(operand1_str), float(operand2_str)

            result = self.calculator.calculate(operand1, operand2, operator)  # type: ignore
            self.result_label.config(text=str(result))
            self.update_log()

        except ValueError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def update_log(self) -> None:
        """
        Displays the calculation log.
        """
        logs = "\n".join(self.calculator.get_log()[::-1])
        self.logs.config(state="normal")
        self.logs.delete(1.0, tk.END)
        self.logs.insert(tk.END, logs)
        self.logs.config(state="disabled")

    def clear(self, include_log: bool = False) -> None:
        """
        Clears the input fields.
        """
        self.operand1_entry.delete(0, tk.END)
        self.operator_entry.delete(0, tk.END)
        self.operand2_entry.delete(0, tk.END)
        self.result_label.config(text="")

        if include_log:
            self.calculator.clear_log()
            self.update_log()


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
