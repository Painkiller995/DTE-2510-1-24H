"""
This module gets input from the user and checks if it is a palindrome.

Accepted input is a digits only.
Maximum length of the input is 3 digits.

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
            "Please enter a number to check if it is a palindrome: "
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number."
            )
            continue

        if len(user_input) > 3:
            print(
                "Oops! 😅 It seems you entered a number that is longer than 3 digits, please enter a valid number."
            )
            continue

        print("-------------------------------------------------")
        return user_input


def is_palindrome_manual(input_string: str) -> bool:
    """
    Check if the input string is a palindrome manually.

    Args:
        input_string: The string to check.

    Returns:
        True if the input string is a palindrome, False otherwise.
    """
    is_palindrome: bool = True

    start_index = 0
    end_index = len(input_string) - 1

    while end_index > start_index:
        if input_string[start_index] != input_string[end_index]:
            is_palindrome = False
            break

        start_index += 1
        end_index -= 1

    return is_palindrome


def is_palindrome_integer(input: int) -> bool:
    """
    Check if the input is a palindrome without converting the integer to a string.

    Args:
        input: The integer to check.

    Returns:
        True if the input is a palindrome, False otherwise.
    """
    original = input
    reversed_num = 0

    while input > 0:
        remainder = input % 10
        reversed_num = reversed_num * 10 + remainder
        input //= 10

    return original == reversed_num


def is_palindrome_pythonic(input_string: str) -> bool:
    """
    Check if the input is a palindrome using a pythonic way.

    Args:
        input_string: The input to check.

    Returns:
        True if the input is a palindrome, False otherwise.
    """
    return input_string == input_string[::-1]


print("-------------------------------------------------")
print("Welcome to the palindrome checker! 😊")
user_input = get_user_input()
print(
    f"The input {user_input} in {'' if is_palindrome_manual(user_input) else 'not '}a palindrome."
)
print(
    f"The input {user_input} in {'' if is_palindrome_integer(int(user_input)) else 'not '}a palindrome (integer)."
)
print(
    f"The input {user_input} in {'' if is_palindrome_pythonic(user_input) else 'not '}a palindrome (pythonic)."
)
print("Thank you for using the palindrome checker! 😊")
print("-------------------------------------------------")
