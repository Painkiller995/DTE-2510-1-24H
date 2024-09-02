"""
This module convert binary numbers to decimal numbers.

This implementation could be improved in the future, please check GitHub for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H
"""


def get_binary_input() -> str:
    """
    Prompt the user for a binary input and validate the input.

    Returns:
        str: The validated binary input from the user.
    """
    while True:
        user_input = input(
            "Please enter the binary number you would like to convert to decimal: "
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input. Please enter a valid integer."
            )
            continue

        if not all(int(digit) in [0, 1] for digit in user_input):
            print(
                "Oops! 😅 It seems you entered an invalid input. Please enter a valid binary number."
            )
            continue

        print("-------------------------------------------------")

        return user_input


def binary_to_decimal(binary_str: str) -> int:
    """
    Convert a binary number to its decimal representation.

    Args:
        binary_str (str): The binary number in string format to convert.

    Returns:
        int: The decimal representation of the binary number.
    """

    decimal_value = 0
    position = len(binary_str) - 1

    for bit in binary_str:
        decimal_value += int(bit) * (2**position)
        position -= 1

    return decimal_value


user_input = get_binary_input()
result = binary_to_decimal(user_input)
print(
    f"The decimal representation of \033[91m {user_input} \033[0m is \033[92m {result} \033[0m."
)
print("-------------------------------------------------")
