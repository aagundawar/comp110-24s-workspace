"""EX03 - Functional Battleship - Another Step Towards Battleship!"""
 
__author__ = "730663390"

import random

"""Defining Emojis."""
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, guess_type: str) -> int:
    """Checking whether guess is within grid size."""
    assert guess_type == "row" or guess_type == "column"
    if guess_type == "row":
        guess_row: int = int(input("Guess a row: "))
        while guess_row > grid_size or guess_row < 1:
            guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return (guess_row)
    elif guess_type == "column":
        guess_column: int = int(input("Guess a column: "))
        while guess_column > grid_size or guess_column < 1:
            guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return (guess_column)


def print_grid(grid_size: int, guess_row: int, guess_column: int, correct_guess: bool) -> None:
    """Prints grid with emoji showing guess."""
    row_counter: int = 1
    result_box: str = ""
    if correct_guess is True:
        result_box = RED_BOX
    elif correct_guess is False:
        result_box = WHITE_BOX
    while row_counter <= grid_size:
        emoji: str = ""
        column_counter: int = 1
        if guess_row == row_counter:
            while column_counter <= grid_size:
                if guess_column == column_counter:
                    emoji = emoji + result_box
                else:
                    emoji = emoji + BLUE_BOX
                column_counter = column_counter + 1
        else:
            while column_counter <= grid_size:
                emoji = emoji + BLUE_BOX
                column_counter = column_counter + 1
        print(emoji)
        row_counter = row_counter + 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Checks whether guess is correct or not."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else: 
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Combines all 3 functions to create one complete function."""
    turn_counter: int = 1
    won = False
    while turn_counter <= 5 and won is False:
        print(f"=== Turn {turn_counter}/5 ===")

        row: int = input_guess(grid_size, "row")
        column: int = input_guess(grid_size, "column")

        if correct_guess(secret_row, secret_column, row, column):
            print_grid(grid_size, row, column, True)
        else:
            print_grid(grid_size, row, column, False)

        if correct_guess(secret_row, secret_column, row, column):
            print("Hit!")
            print(f"You won in {turn_counter}/5 turns!")
            won = True
            return None
        else:
            print("Miss!")
            turn_counter += 1

    if turn_counter > 5:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    """Creates a random board with random row & column."""
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))