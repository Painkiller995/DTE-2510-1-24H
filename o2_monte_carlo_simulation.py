"""
This module represents a monte carlo simulation implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import math
import random


NUMBER_OF_POINTS: int = 1000000


def get_pi(number_of_hits: int, number_of_points: int) -> float:
    """
    Get the value of pi.

    Args:
        number_of_hits: The number of hits.
        number_of_points: The number of points.

    Returns:
        The value of pi.
    """
    return 4 * number_of_hits / number_of_points


def get_random_point() -> tuple:
    """
    Get a random point.

    Returns:
        A random point.
    """
    x: float = random.uniform(-1, 1)
    y: float = random.uniform(-1, 1)
    return x, y


def monte_carlo_simulation() -> float:
    """
    Perform a monte carlo simulation.

    Returns:
        The value of pi.
    """
    number_of_hits: int = 0

    for _ in range(NUMBER_OF_POINTS):
        x, y = get_random_point()

        if math.sqrt(x**2 + y**2) < 1:
            number_of_hits += 1

    return get_pi(number_of_hits, NUMBER_OF_POINTS)


if __name__ == "__main__":
    pi: float = monte_carlo_simulation()
    print(pi)
