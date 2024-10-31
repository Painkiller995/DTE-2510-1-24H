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


class CalculatorGUI(tk.Frame):
    """
    Represents a simple calculator GUI.
    """

    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)

        self.root.title("Calculator GUI")
        self.set_geometry()

        self.calculator = Calculator()

    def set_geometry(self, width=300, height=400) -> None:
        """
        Sets the window size and positions it in the center of the screen.

        Args:
            width: The width of the window.
            height: The height of the window.
        """
        position_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        position_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{position_x}+{position_y}")


if __name__ == "__main__":
    app = CalculatorGUI()
    app.mainloop()
