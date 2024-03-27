"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730663390"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

location: int = int(input("Pick a secret boat location between 1 and 4: "))
if location < 1:
    locationLow: str = f"Error! {location} too low!"
    print(locationLow)
    exit()
elif location > 4:
    locationHigh: str = f"Error! {location} too high!"
    print(locationHigh)
    exit()

guess: int = int(input("Guess a number between 1 and 4: "))
if guess < 1:
    guessLow: str = f"Error! {guess} too low!"
    print(guessLow)
    exit()
elif guess > 4:
    guessHigh: str = f"Error! {guess} too high!"
    print(guessHigh)
    exit()

if location == guess:
    result = RED_BOX
else:
    result = WHITE_BOX

if guess == 1:
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
elif guess == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
elif guess == 3:
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
elif guess == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)

if location == guess:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")