"""
This module represents a simple point inside circle implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import turtle
from turtle import Turtle

ZOOM_OUT_LEVEL = 10
CENTER_X = 0
CENTER_Y = 0
CIRCLE_RADIUS = 10

LLX = CENTER_X - CIRCLE_RADIUS - ZOOM_OUT_LEVEL
LLY = CENTER_Y - CIRCLE_RADIUS - ZOOM_OUT_LEVEL
URX = CENTER_X + CIRCLE_RADIUS + ZOOM_OUT_LEVEL
URY = CENTER_Y + CIRCLE_RADIUS + ZOOM_OUT_LEVEL


def get_user_input(coordinate_name: str) -> int:
    """
    Get the user input and validate it.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(f"Please enter the {coordinate_name} of the point: \n")

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")
        return int(user_input)


def draw_circle(
    center_x: int,
    center_y: int,
    radius: int,
    color: str = "black",
) -> None:
    """
    Draw a circle on the turtle canvas.

    Args:
        center_x (int): X-coordinate of the circle's center.
        center_y (int): Y-coordinate of the circle's center.
        radius (int): Radius of the circle.
        color (str): Color of the circle outline.
    """
    turtle = Turtle()
    turtle.penup()
    turtle.goto(center_x, center_y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)


def draw_point(
    point_x: int,
    point_y: int,
    size: int = 1,
    color: str = "red",
) -> None:
    """
    Draw a point on the turtle canvas.

    Args:
        x (int): X-coordinate of the point.
        y (int): Y-coordinate of the point.
        size (int): Size of the point.
        color (str): Color of the point.
    """
    turtle = Turtle()
    turtle.penup()
    turtle.goto(point_x, point_y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    # turtle.dot(size, color)
    turtle.circle(size)
    turtle.end_fill()


def is_point_in_circle(
    circle_center_x: int,
    circle_center_y: int,
    radius: int,
    point_x: int,
    point_y: int,
) -> bool:
    """
    Check if the point is inside the circle.

    Args:
        circle_center_x (int): X-coordinate of the circle's center.
        circle_center_y (int): Y-coordinate of the circle's center.
        radius (int): Radius of the circle.
        point_x (int): X-coordinate of the point.
        point_y (int): Y-coordinate of the point.
    """

    distance = (
        (point_x - circle_center_x) ** 2 + (point_y - circle_center_y) ** 2
    ) ** 0.5

    if distance <= radius:
        return True

    return False


def write_text(
    text: str,
    color: str = "black",
    align: str = "center",
    font: tuple = ("Arial", 12, "normal"),
):
    """
    Write text on the turtle canvas.

    Args:
        text (str): The text to write.
        align (str): The alignment of the text.
        font (tuple): The font style of the text.
    """
    turtle = Turtle()
    turtle.color(color)
    turtle.write(text, align=align, font=font)


if __name__ == "__main__":
    point_x_coord = get_user_input("x-coordinate")
    point_y_coord = get_user_input("y-coordinate")

    turtle.setworldcoordinates(LLX, LLY, URX, URY)

    draw_circle(CENTER_X, CENTER_Y, CIRCLE_RADIUS)

    is_inside: bool = is_point_in_circle(
        CENTER_X, CENTER_Y, CIRCLE_RADIUS, point_x_coord, point_y_coord
    )

    draw_point(point_x_coord, point_y_coord, color="green" if is_inside else "red")

    write_text(
        f"Point: ({point_x_coord}, {point_y_coord}) is {'inside' if is_inside else 'outside'} the circle.",
        "green" if is_inside else "red",
    )

    turtle.done()
