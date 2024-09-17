"""
This module represents a bean machine game implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import random

CHOICES = ["L", "R"]


def get_user_input(input_title: str) -> int:
    """
    Get the user input and validate it.

    Args:
        input_title: The title of the input.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(input_title)

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number."
            )
            continue

        input_number: int = int(user_input)

        if input_number <= 0:
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number greater than 0."
            )
            continue

        print("-------------------------------------------------")
        return input_number


number_of_balls: int = get_user_input("Enter the number of balls to drop: ")
number_of_slots: int = get_user_input("Enter the number of slots in the bean machine: ")

slots: list[int] = [0] * number_of_slots

for _ in range(number_of_balls):
    position: int = 0

    for _ in range(number_of_slots - 1):
        position += 1 if random.choice(CHOICES) == "R" else 0

    slots[position] += 1

max_balls: int = max(slots)


print("\n Here is the bean machine game result: 😊 \n")

for i in range(max_balls, 0, -1):
    for j in range(number_of_slots):
        print(" * " if slots[j] >= i else "   ", end="")
    print()

print("---" * number_of_slots)
for j in range(number_of_slots):
    print(f" {j+1} ", end="")
print()
