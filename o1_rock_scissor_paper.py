"""
This module represents a simple rock, scissor, paper game implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import random

START_RANGE: int = 0
END_RANGE: int = 2
OPTIONS: dict[int, str] = {0: "Scissor", 1: "Rock", 2: "Paper"}


def get_user_input() -> int:
    """
    Get the user input and validate it.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(
            f"Please enter a number between {START_RANGE} and {END_RANGE} (0 for Scissor, 1 for Rock, 2 for Paper): \n"
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        integer_value: int = int(user_input)

        if integer_value < START_RANGE or integer_value > END_RANGE:
            print(
                "Oops! 😅 It seems you entered a number that is not between "
                f"{START_RANGE} and {END_RANGE}, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")
        return integer_value


user_input = get_user_input()
device_input: int = random.randint(START_RANGE, END_RANGE)

print(f"You selected: {OPTIONS[user_input]}")
print(f"Device selected: {OPTIONS[device_input]}")

if user_input == device_input:
    print("It's a draw! 😅")
elif (
    (user_input == 0 and device_input == 2)
    or (user_input == 1 and device_input == 0)
    or (user_input == 2 and device_input == 1)
):
    print("You win! 😎")
else:
    print("You lose! 😔")
