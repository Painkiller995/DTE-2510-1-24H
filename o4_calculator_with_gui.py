"""
This module represents a gui calculator implementation.

Dependencies:
    - tkinter
    o4_calculator.py available in the same repository on github.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import tkinter as tk
from o4_calculator import Calculator


class CalculatorGUI:
    """
    Represents a simple calculator GUI.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator GUI")

        width, height = 300, 400
        x = (self.root.winfo_screenwidth() - width) // 2
        y = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        self.calculator = Calculator()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
