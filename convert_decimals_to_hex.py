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


def decimal_to_hex(hex_number: int) -> str:
    """
    Convert a decimal number to its binary representation.

    Args:
        decimal_number (int): The decimal number to convert.

    Returns:
        str: The binary representation of the decimal number.
    """
    if hex_number == 0:
        return "0"

    hex_result = ""

    while hex_number > 0:
        remainder = hex_number % 16
        hex_number = hex_number // 16

        if remainder < 10:
            hex_result = str(remainder) + hex_result
        else:
            hex_result = chr((remainder - 10) + ord("A")) + hex_result

    return hex_result


print("Welcome to the Decimal to Hexadecimal Converter! 🎉")
print("-------------------------------------------------")

decimal_number = get_valid_integer_input("Enter a decimal number")

hex_value = decimal_to_hex(decimal_number)

print(
    f"The hexadecimal representation of {decimal_number} is: \033[92m {hex_value} \033[0m"
)
print("-------------------------------------------------")
print("Thank you for using the Decimal to Hexadecimal Converter! 😊")
