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

        self.frame1 = ttk.Frame(self._root, padding=10)
        self.frame2 = ttk.Frame(self._root, padding=10)

        self.frame1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.frame2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

        self.button1 = ttk.Button(
            self.frame1, text="Frame 1 Button", command=self.process_button1_click
        )
        self.button1.pack(pady=20)

        self.button2 = ttk.Button(
            self.frame2, text="Frame 2 Button", command=self.process_button2_click
        )
        self.button2.pack(pady=20)

    def run(self):
        """Run the GUI."""
        self._root.mainloop()

    def process_button_click(self):
        """Process button click."""
        print("Button clicked!")

    def process_button1_click(self):
        """Process button 1 click."""
        print("Button 1 clicked!")

    def process_button2_click(self):
        """Process button 2 click."""
        print("Button 2 clicked!")


if __name__ == "__main__":
    app = SimpleGUI()
    app.run()
