"""
This module represents an eight queens check implementation.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2510-1-24H

"""


class EQ:
    """
    This class represents an eight queens check.
    """

    def __init__(self, queens: list[int] | None = None):
        self.queens = queens if queens else [-1] * 8

    def get(self, index: int) -> int:
        """
        Get the queen at the specified index.

        Args:
            index: The index of the queen.

        Returns:
            The queen at the specified index.
        """
        return self.queens[index]

    def set(self, index: int, value: int) -> None:
        """
        Set the queen at the specified index.

        Args:
            index: The index of the queen.
            value: The value of the queen.
        """
        self.queens[index] = value

    def print_board(self) -> None:
        """
        Print the board.
        """
        for i in range(8):
            row = [" "] * 8
            if self.queens[i] != -1:
                row[self.queens[i]] = "X"
            print("|" + "|".join(row) + "|")

    def is_solved(self) -> bool:
        """
        Check if all queens are placed correctly on the board.
        No two queens should be able to attack each other.
        """

        for row_index in range(8):
            for next_row_index in range(row_index + 1, 8):
                if self.queens[row_index] == self.queens[next_row_index]:
                    print(
                        f"Queens are in the same column: {row_index} and {next_row_index}"
                    )
                    return False

                column_difference = abs(
                    self.queens[row_index] - self.queens[next_row_index]
                )
                row_difference = abs(row_index - next_row_index)

                if column_difference == row_difference:
                    print(
                        f"Queens are on the same diagonal: {row_index} and {next_row_index}"
                    )
                    return False

        return True


if __name__ == "__main__":
    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board 1 a correct eight queen placement?", board1.is_solved())

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.is_solved():
        print("Eight queens are placed correctly in board 2")

        board2.print_board()

    else:
        print("Eight queens are placed incorrectly in board 2")
