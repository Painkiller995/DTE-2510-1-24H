"""
This module represents a path finder implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""

import random

GRID_SIZE = 10
GRADING_FACTOR = 10
TARGET_VALUE = 200


def initialize_grid(size: int, default_value: int = 0) -> list[list[int]]:
    """
    Initializes a 2D grid of the specified size with a given default value.

    Args:
        size: The size of the grid (size x size).
        default_value The value to initialize each cell in the grid. Defaults to 0.

    Returns:
        A 2D grid initialized with the default value.
    """
    return [[default_value for _ in range(size)] for _ in range(size)]


def get_random_position(size: int) -> tuple[int, int]:
    """
    Randomly selects a position within the grid boundaries.

    Args:
        size: The size of the grid.

    Returns:
        The coordinates of the randomly selected target position.
    """
    return random.randint(0, size - 1), random.randint(0, size - 1)


def populate_grid_with_distances(
    size: int, target_value: int
) -> tuple[list[list[int]], tuple[int, int]]:
    """
    Creates a 2D grid of the specified size, assigns values based on the Manhattan distance
    from a randomly selected target position, and returns the grid along with the target's coordinates.

    Args:
        size: The size of the grid (size x size).
        target_value: The value assigned to the target position (highest value in the grid).

    Returns:
        A 2D grid of integers where each value decreases with distance from the target,
        and the coordinates of the target position.
    """

    grid = initialize_grid(size)

    target_x, target_y = get_random_position(size)

    for x in range(size):
        for y in range(size):
            manhattan_distance = abs(target_x - x) + abs(target_y - y)
            grid[x][y] = max(target_value - manhattan_distance * GRADING_FACTOR, 0)

    grid[target_x][target_y] = target_value

    return grid, (target_x, target_y)


def find_path(
    grid: list[list[int]],
    start_position: tuple[int, int],
    target_position: tuple[int, int],
) -> list[tuple[int, int]]:
    """
    Finds a path from the start position to the target position in the grid.

    Args:
        grid: The grid of values.
        start_position: The starting position.
        target_position: The target position.
    Returns:
        A list of positions representing the path from start to target.
    """

    current_position = start_position

    result_path = []

    while current_position != target_position:
        x, y = current_position

        neighbors = []

        # Check left
        if x > 0:
            neighbors.append((x - 1, y))
        # Check right
        if x < len(grid) - 1:
            neighbors.append((x + 1, y))
        # Check up
        if y > 0:
            neighbors.append((x, y - 1))
        # Check down
        if y < len(grid) - 1:
            neighbors.append((x, y + 1))

        next_position = max(neighbors, key=lambda pos: grid[pos[0]][pos[1]])

        current_position = next_position

        result_path.append(current_position)

    return result_path


def print_grid(grid: list[list[int]]) -> None:
    """
    Prints the grid in a human-readable format.
    Args:
        grid: The grid to print
    """
    for row in grid:
        print(" ".join(f"{value:3}" for value in row))


if __name__ == "__main__":
    grid, target_position = populate_grid_with_distances(GRID_SIZE, TARGET_VALUE)

    start_x, start_y = get_random_position(GRID_SIZE)

    path = find_path(grid, (start_x, start_y), target_position)

    print_grid(grid)

    print(f"Start position: ({start_x}, {start_y})")

    print(f"Target position: {target_position}")

    print(f"Path: {path}")

    print(f"Path length: {len(path)}")
