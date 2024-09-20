"""
This module represents a monte carlo simulation implementation of the estimation of pi.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import math
import random


NUMBER_OF_POINTS: int = 1000000


def get_random_point() -> tuple:
    """
    Get a random point.

    Returns:
        A random point.
    """
    return random.uniform(-1, 1), random.uniform(-1, 1)


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

    return 4 * number_of_hits / NUMBER_OF_POINTS


if __name__ == "__main__":
    pi: float = monte_carlo_simulation()
    print(f"Pi is approximately {pi}")
