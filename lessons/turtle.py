"""TODO: Describe your scene program."""
 
__author__ = "730663015"
 
from turtle import Turtle, colormode, done
 
 
def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    bob: Turtle = Turtle()

    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    bob.fillcolor("orange")
    draw_square(bob, -300, 50, 400)
    draw_rectangle(bob, -210, -270, 80, 65, 2) 
    bob.begin_fill()
    draw_triangle(bob, -300, 50, 400)
    bob.end_fill()
    bob.pencolor("blue")
    draw_circle(bob, -120, 0, 100)
    bob.pencolor("pink")
    draw_open_cone(bob, -120, -50, 60)
    done()
 
# TODO: Define the procedures for other components in your scene here.


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, length: float, n: int) -> None: 
    """Draw a rectangle of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        if i % 2 == 0:
            a_turtle.forward(length)
        else:
            a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1
    if n > 1:
        draw_rectangle(a_turtle, x + 169, y, width, length, n - 1)


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i = i + 1


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle connecting to the square."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(60)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(120)
        i = i + 1
    a_turtle.forward(width)


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.circle(radius)


def draw_open_cone(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a 3d-looking cone with an open top."""
    for i in range(0, 10):
        a_turtle.penup()
        a_turtle.goto(x - 5 * i, y - 5 * i)
        a_turtle.pendown()
        a_turtle.circle(radius - 5 * i)
        

# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()