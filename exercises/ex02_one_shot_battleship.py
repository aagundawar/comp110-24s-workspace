"""EX02 - One Shot Battleship - Another step toward Battleship."""
 
__author__ = "730663390"

# Defining variables
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
result_box: str = ""
row_counter: int = 1

# Ensures users guess is on the grid
guess_row: int = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
guess_column: int = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Defining hit and miss emojis
if guess_row == secret_row and guess_column == secret_column:
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

# Printing grid response based on users guess
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

# Giving user hints based on guess
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_row != secret_row and guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")