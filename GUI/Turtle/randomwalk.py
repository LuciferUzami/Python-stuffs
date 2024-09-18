from random import choice, randint
from turtle import Turtle, Screen

# Assessing Object
tom = Turtle()
screen = Screen()
# Set color
screen.colormode(255)
screen.bgcolor("black")
# Pen Size
tom.pensize(width=10)


# Get color
def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return tom.pencolor(r, g, b)


#  Angels
turn = [90, 180, -90, -180, 360, -360, ]

while True:
    tom.speed("fastest")
    tom.forward(30)
    tom.right(choice(turn))
    colors()
