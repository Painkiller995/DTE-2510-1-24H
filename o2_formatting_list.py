"""
This module represents formatting list implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


def format_items(items: list[str]) -> str:
    """
    Format the given items.

    Args:
        items: The items.

    Returns:
        The formatted items.
    """
    if not items:
        return ""
    elif len(items) == 1:
        return f"The item is {items[0]}."
    elif len(items) == 2:
        return f"The items are {items[0]} and {items[1]}."
    else:
        return f"The items are {', '.join(items[:-1])} and {items[-1]}."


def get_user_input() -> list[str]:
    """
    Get the user input and validate it.

    Returns:
        The user input as a list of strings.
    """
    items = []
    while True:
        item = input("Enter an item (blank to quit): ")
        if item == "":
            break
        items.append(item)
    return items


if __name__ == "__main__":
    user_items = get_user_input()
    print(format_items(user_items))
