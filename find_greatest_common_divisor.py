"""
This module contains finds the greatest common divisor of two numbers.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


def get_user_input(value_title: str) -> int:
    """
    Get the user input and validate it.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(
            f"Please enter the {value_title} you would like to use: "
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")

        return int(user_input)


first_number: int = get_user_input("first number")
second_number: int = get_user_input("second number")

current_gcd: int = 1  # The greatest common divisor
candidate_divisor: int = 2  # The current divisor candidate

while candidate_divisor <= first_number and candidate_divisor <= second_number:
    if first_number % candidate_divisor == 0 and second_number % candidate_divisor == 0:
        current_gcd = candidate_divisor

    candidate_divisor += 1


print(
    f"The greatest common divisor of {first_number} and {second_number} is: {current_gcd}"
)
