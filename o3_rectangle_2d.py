"""
This module represents a rectangle implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


class Rectangle2D:
    """
    Represents a 2D rectangle with a center point and dimensions.
    """

    def __init__(
        self,
        center_x: float = 0.0,
        center_y: float = 0.0,
        width: float = 0.0,
        height: float = 0.0,
    ):
        self._center_x = center_x
        self._center_y = center_y
        self._width = width
        self._height = height

    @property
    def center(self) -> tuple[float, float]:
        """
        The center point of the rectangle.

        Returns:
            The center point as a tuple (x, y).
        """
        return self._center_x, self._center_y

    @center.setter
    def center(self, value: tuple[float, float]):
        self._center_x, self._center_y = value

    @property
    def width(self) -> float:
        """
        The width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        """
        The height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value

    def get_area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self._width * self._height

    def get_perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self._width + self._height)

    def contains_point(self, x: float, y: float) -> bool:
        """
        Determine if a given point (x, y) is inside the rectangle.

        The point is inside if its x-coordinate falls between the left and right edges of the rectangle,
        and its y-coordinate falls between the top and bottom edges.

        Args:
            x: The x-coordinate of the point to check.
            y: The y-coordinate of the point to check.

        Returns:
            True if the point is within the rectangle, False otherwise.
        """
        left = self._center_x - self._width / 2
        right = self._center_x + self._width / 2
        bottom = self._center_y - self._height / 2
        top = self._center_y + self._height / 2

        return left <= x <= right and bottom <= y <= top

    def contains_rectangle(self, other: "Rectangle2D") -> bool:
        """
        Determine if this rectangle completely contains another rectangle.

        This rectangle contains the other if all four corners of the other rectangle are within this rectangle.

        Args:
            other: The other Rectangle2D instance to check.

        Returns:
            True if this rectangle fully contains the other rectangle, False otherwise.
        """
        other_left = other._center_x - other._width / 2
        other_right = other._center_x + other._width / 2
        other_bottom = other._center_y - other._height / 2
        other_top = other._center_y + other._height / 2

        return self.contains_point(other_left, other_bottom) and self.contains_point(
            other_right, other_top
        )

    def overlaps_rectangle(self, other: "Rectangle2D") -> bool:
        """
        Check if this rectangle overlaps with another rectangle.

        Args:
            other: The other Rectangle2D instance to check.

        Returns:
            True if the rectangles overlap, False otherwise.
        """
        horizontal_distance = abs(self._center_x - other._center_x)
        vertical_distance = abs(self._center_y - other._center_y)

        total_half_widths = (self._width + other._width) / 2
        total_half_heights = (self._height + other._height) / 2

        return (
            horizontal_distance < total_half_widths
            and vertical_distance < total_half_heights
        )

    def __contains__(self, other: "Rectangle2D") -> bool:
        return self.contains_rectangle(other)

    def __eq__(self, other: "Rectangle2D") -> bool:
        return self.get_area() == other.get_area()

    def __lt__(self, other: "Rectangle2D") -> bool:
        return self.get_area() < other.get_area()

    def __le__(self, other: "Rectangle2D") -> bool:
        return self.get_area() <= other.get_area()

    def __gt__(self, other: "Rectangle2D") -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other: "Rectangle2D") -> bool:
        return self.get_area() >= other.get_area()

    def __ne__(self, other: "Rectangle2D") -> bool:
        return self.get_area() != other.get_area()


if __name__ == "__main__":
    rect1 = Rectangle2D(center_x=0, center_y=0, width=10, height=5)
    rect2 = Rectangle2D(center_x=5, center_y=0, width=5, height=5)

    print(f"rect1 center: {rect1.center}")  # Expected: (0, 0)
    print(f"rect1 width: {rect1.width}")  # Expected: 10
    print(f"rect1 height: {rect1.height}")  # Expected: 5
    print(f"rect1 area: {rect1.get_area()}")  # Expected: 50
    print(f"rect1 perimeter: {rect1.get_perimeter()}")  # Expected: 30

    print(f"rect2 center: {rect2.center}")  # Expected: (5, 0)
    print(f"rect2 width: {rect2.width}")  # Expected: 5
    print(f"rect2 height: {rect2.height}")  # Expected: 5
    print(f"rect2 area: {rect2.get_area()}")  # Expected: 25
    print(f"rect2 perimeter: {rect2.get_perimeter()}")  # Expected: 20

    print(
        f"rect1 contains point (2, 0): {rect1.contains_point(2, 0)}"
    )  # Expected: True
    print(
        f"rect1 contains point (10, 10): {rect1.contains_point(10, 10)}"
    )  # Expected: False

    print(f"rect1 contains rect2: {rect1.contains_rectangle(rect2)}")  # Expected: False

    print(
        f"rect1 overlaps with rect2: {rect1.overlaps_rectangle(rect2)}"
    )  # Expected: True

    print(f"rect1 == rect2: {rect1 == rect2}")  # Expected: False
    print(f"rect1 > rect2: {rect1 > rect2}")  # Expected: True
    print(f"rect1 < rect2: {rect1 < rect2}")  # Expected: False
