"""
This module represents a simple ISBN-10 calculation implementation.

The user should enter 9 digits and the program will calculate the last digit of the ISBN-10.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


def get_user_input() -> str:
    """
    Get the user input and validate it.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(
            "Please enter a 9 digit number to calculate the last digit of the ISBN-10: \n"
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        if len(user_input) != 9:
            print(
                "Oops! 😅 It seems you entered a number that is not 9 digits long, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")

        return user_input


def calculate_last_digit(isbn_digits: str) -> str:
    """
    Calculate the last digit of the ISBN-10.

    Args:
        isbn_digits: The first 9 digits of the ISBN-10.

    Returns:
        The last digit of the ISBN-10.
    """

    checksum_value: int = 0

    for position, digit in enumerate(isbn_digits):
        checksum_value += int(digit) * (position + 1)

    return "X" if checksum_value % 11 == 10 else str(checksum_value % 11)


if __name__ == "__main__":
    print("Welcome to the ISBN-10 calculator! 📚")
    print("-------------------------------------------------")

    user_input: str = get_user_input()
    last_digit_value: str = calculate_last_digit(user_input)

    print(f"The last digit of the ISBN-10 is: {last_digit_value}")
    print(f"The ISBN-10 is: {user_input + last_digit_value}")
    print("-------------------------------------------------")
    print("Thank you for using the ISBN-10 calculator! 😊")
    print("-------------------------------------------------")
