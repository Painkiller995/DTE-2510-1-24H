"""
This module convert decimal numbers to binary numbers.

This implementation could be improved in the future, please check GitHub for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H
"""


def get_valid_integer_input(prompt_message: str) -> int:
    """
    Prompt the user for an integer input and validate the input.

    Args:
        prompt_message (str): The message to display when asking for input.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        user_input = input(f"{prompt_message}: ")

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input. Please enter a valid integer."
            )
            continue

        print("-------------------------------------------------")

        return int(user_input)


def decimal_to_binary(decimal_number: int) -> str:
    """
    Convert a decimal number to its binary representation.

    Args:
        decimal_number (int): The decimal number to convert.

    Returns:
        str: The binary representation of the decimal number.
    """
    if decimal_number == 0:
        return "0"

    binary_result = ""

    while decimal_number > 0:
        remainder = decimal_number % 2
        decimal_number = decimal_number // 2
        binary_result = str(remainder) + binary_result

    return binary_result


print("Welcome to the Decimal-Binary Converter! 😁")

number = get_valid_integer_input(
    "Please enter the decimal number you would like to convert to binary"
)

binary_representation = decimal_to_binary(number)

print(f"Binary representation: \033[92m {binary_representation} \033[0m")
print("-------------------------------------------------")
