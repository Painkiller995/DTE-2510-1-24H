"""
This module gets input from the user and converts it to binary.

The allowed input is between 0 and 15.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


def get_user_input() -> int:
    """
    Get the user input and validate it.

    Returns:
        The user input as an integer.
    """
    while True:
        user_input: str = input(
            "Please enter a number between 0 and 15 to convert to binary: "
        )

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        if int(user_input) < 0 or int(user_input) > 15:
            print(
                "Oops! 😅 It seems you entered a number that is not between 0 and 15, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")
        return int(user_input)


user_input = get_user_input()

print("-------------------------------------------------")
print(f"The binary representation of {user_input} is: {bin(user_input)[2:]}")
print("-------------------------------------------------")
print("Thank you for using the binary converter! 😊")
