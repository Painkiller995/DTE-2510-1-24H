"""
This module represents two movable vertices and their distance implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import math
import tkinter as tk


class Circle:
    """
    A class representing a circle.
    """

    def __init__(self, x: int, y: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, x: int, y: int) -> bool:
        """
        Check if a point is inside the circle.

        Args:
            x: The x coordinate.
            y: The y coordinate.

        Returns:
            True if the point is inside the circle, False otherwise.
        """
        return (self.x - x) ** 2 + (self.y - y) ** 2 <= self.radius**2

    def paint(self, canvas: tk.Canvas) -> None:
        """
        Draw the circle on the canvas.

        Args:
            canvas: The canvas to draw the circle on.
        """
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            outline="black",
            fill="red",
        )


class CircleDragApp(tk.Frame):
    """
    A class representing a circle drag application.
    """

    def __init__(self) -> None:
        self.root = tk.Tk()
        super().__init__(self.root)

        self.root.title("Two Circles")
        self.set_window_shape()

        self.canvas = tk.Canvas(
            self.root,
            width=self.root.winfo_screenwidth(),
            height=self.root.winfo_screenheight(),
        )

        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.mouse_moved)

        self.initialize_circles()
        self.draw_line()

        self.current_circle = None

    def set_window_shape(self, width: int = 400, height: int = 400) -> None:
        """
        Sets the window size and positions it in the center of the screen.

        Args:
            width: The width of the window.
            height: The height of the window.
        """
        position_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        position_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{position_x}+{position_y}")

        # Prevent resizing the window as required by the task.
        self.root.resizable(False, False)

    def initialize_circles(self) -> None:
        """
        Creates the circles for the application.
        """
        self.circle1 = Circle(100, 200, 25)
        self.circle1.paint(self.canvas)
        self.circle2 = Circle(300, 200, 25)
        self.circle2.paint(self.canvas)

    def mouse_moved(self, event: tk.Event) -> None:
        """
        Handle the mouse moved event.
        """
        x, y = event.x, event.y
        if self.circle1.is_inside(x, y) and self.can_move(self.circle1, x, y):
            self.move_circle(self.circle1, x, y)
        elif self.circle2.is_inside(x, y) and self.can_move(self.circle2, x, y):
            self.move_circle(self.circle2, x, y)

    def can_move(self, circle: Circle, x: int, y: int) -> bool:
        """
        Check if the circle can be moved to the new position.

        Args:
            circle: The circle to move.
            x: The x coordinate.
            y: The y coordinate.

        Returns:
            True if the circle can be moved, False otherwise.
        """
        other_circle = self.circle2 if circle == self.circle1 else self.circle1
        dist = (x - other_circle.x) ** 2 + (y - other_circle.y) ** 2
        min_dist = (circle.radius + other_circle.radius) ** 2
        return (
            x - circle.radius >= 0
            and x + circle.radius <= self.canvas.winfo_width()
            and y - circle.radius >= 0
            and y + circle.radius <= self.canvas.winfo_height()
            and dist >= min_dist
        )

    def move_circle(self, circle: Circle, x: int, y: int) -> None:
        """
        Move the circle to the new position.

        Args:
            circle: The circle to move.
            x: The x coordinate.
            y: The y coordinate.
        """
        circle.x = x
        circle.y = y
        self.canvas.delete("all")
        self.circle1.paint(self.canvas)
        self.circle2.paint(self.canvas)
        self.draw_line()

    def draw_line(self) -> None:
        """
        Draw the line between the circles and the distance between them.
        """

        self.canvas.create_line(
            self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y
        )

        distance = math.sqrt(
            (self.circle2.x - self.circle1.x) ** 2
            + (self.circle2.y - self.circle1.y) ** 2
        )

        mid_x = (self.circle1.x + self.circle2.x) / 2
        mid_y = (self.circle1.y + self.circle2.y) / 2

        self.canvas.create_text(mid_x, mid_y, text=f"{distance:.2f}")


if __name__ == "__main__":
    app = CircleDragApp()
    app.mainloop()
