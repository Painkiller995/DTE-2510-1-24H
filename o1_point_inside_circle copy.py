import turtle

# Constants for circle properties
RADIUS = 100
CENTER_X = 0
CENTER_Y = 0
POINT_X = 0
POINT_Y = 0


# Function to get valid user input for point coordinates
def get_user_point():
    while True:
        try:
            point_x = int(input("Please enter the x-coordinate of the point: \n"))
            point_y = int(input("Please enter the y-coordinate of the point: \n"))
            return point_x, point_y
        except ValueError:
            print(
                "Oops! 😅 It seems you entered an invalid input. Please enter a valid number. "
                "Try again.\n"
            )


# Draw a circle using turtle
def draw_circle():
    turtle.penup()
    turtle.goto(CENTER_X, CENTER_Y - RADIUS)  # Move to starting point
    turtle.pendown()
    turtle.circle(RADIUS)


# Draw the point on the canvas
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(3)  # Small circle to represent the point
    turtle.end_fill()


# Check if the point is inside the circle
def is_point_in_circle(px, py):
    distance = ((px - CENTER_X) ** 2 + (py - CENTER_Y) ** 2) ** 0.5
    return distance <= RADIUS


# Main code execution
def main():
    # Set world coordinates to zoom in or out
    # Set larger ranges for zooming out, smaller ranges for zooming in
    turtle.setworldcoordinates(
        -200, -200, 200, 200
    )  # Zooms in by making the canvas smaller

    POINT_X, POINT_Y = get_user_point()

    # Draw the circle and the point
    draw_circle()
    draw_point(POINT_X, POINT_Y)

    # Determine if the point is inside or outside the circle
    if is_point_in_circle(POINT_X, POINT_Y):
        print("The point is inside the circle.")
    else:
        print("The point is outside the circle.")

    turtle.done()


# Run the program
if __name__ == "__main__":
    main()
