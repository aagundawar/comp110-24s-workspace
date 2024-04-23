"""EX08 - House next to a lake on a sunny day with stars.

Above and Beyond - Breaks up Complex Functions: Lines 70-104 (Breaks up the house function into a base and roof function)
Above and Beyond - Try something fun!: Lines 54 - 56 (Generate random x and y coordinates within a range of 20 units from the original position (x, y) for each star)

"""
 
__author__ = "730663390"
 
import random
from turtle import Turtle, done 
 
 
def main() -> None:
    """The entrypoint of my scene."""
    leo: Turtle = Turtle()
    draw_sun(leo, -200.0, 200.0, 30.0)
    draw_lake(leo, -100.0, -200.0)
    draw_star_recursive(leo, -100.0, 200.0, 10.0, 3)
    draw_house(leo, 100.0, 0.0, 100.0, 100.0)
    done()


# TODO: Define the procedures for other components in your scene here.
             
def draw_sun(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a sun of the given radius using a starting location of x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def draw_lake(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws a lake using a starting location of x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("blue")
    a_turtle.begin_fill()
    a_turtle.circle(100)
    a_turtle.end_fill()


def draw_star_recursive(a_turtle: Turtle, x: float, y: float, size: float, n: int) -> None:
    """Recursively draws n number of stars of a given size using a starting location of x, y."""
    if n == 0:
        return
    else:
        a_turtle.penup()
        random_x = random.uniform(x - 20, x + 20)
        random_y = random.uniform(y - 20, y + 20)
        a_turtle.goto(random_x, random_y)
        a_turtle.pendown()
        
        i: int = 0
        while i < 5:
            a_turtle.forward(size)
            a_turtle.right(144)
            i += 1

        draw_star_recursive(a_turtle, x - (size * 10), y - (size * 3), size, n - 1)
    a_turtle.end_fill()


def draw_house(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws a house of a given width and height using a starting location of x, y."""
    draw_house_base(a_turtle, x, y, width, height)
    draw_house_roof(a_turtle, x, y + height, width, height / 2)


def draw_house_base(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the base of the house."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()

    a_turtle.color("orange")
    a_turtle.begin_fill()
    i: int = 0
    while i < 4:
        if i % 2 == 0:
            a_turtle.forward(height)
        else:
            a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    a_turtle.end_fill()


def draw_house_roof(a_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws the roof of the house."""
    a_turtle.begin_fill()
    a_turtle.fillcolor("red")
    i: int = 0
    while i < 3:
        a_turtle.forward(width)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()


# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()