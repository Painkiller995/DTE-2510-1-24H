"""
This module represents seconds to hours, minutes and seconds implementation.

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
        user_input: str = input("Please enter the number of seconds: \n")

        if not user_input.isdigit():
            print(
                "Oops! 😅 It seems you entered an invalid input, please enter a valid number. "
            )
            continue

        print("-------------------------------------------------")
        return int(user_input)


def format_time(seconds: int) -> str:
    """
    Format the given seconds to hours, minutes and seconds.

    The hours are limited to 24.

    Args:
        seconds: The seconds.

    Returns:
        The formatted time.
    """

    hours = (seconds // 3600) % 24
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    user_input = get_user_input()
    print(f"The time is: {format_time(user_input)}")
