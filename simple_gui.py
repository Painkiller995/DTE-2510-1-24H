"""
This module represents a simple GUI implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import tkinter
from tkinter import ttk


class SimpleGUI:
    """A simple GUI application."""

    def __init__(self):
        self._root = tkinter.Tk()

        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()

        window_size = min(screen_width, screen_height)

        window_size -= window_size // 4

        position_right = (screen_width // 2) - (window_size // 2)
        position_down = (screen_height // 2) - (window_size // 2)

        self._root.geometry(
            f"{window_size}x{window_size}+{position_right}+{position_down}"
        )

        self._button = ttk.Button(
            self._root, text="Click me!", command=self.process_button_click
        )

        self._button.pack(expand=True)

    def run(self):
        """Run the GUI."""
        self._root.mainloop()

    def process_button_click(self):
        """Process button click."""
        print("Button clicked!")


if __name__ == "__main__":
    app = SimpleGUI()
    app.run()
