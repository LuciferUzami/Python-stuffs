from turtle import Turtle, Screen
from random import choice

# Objects
tom = Turtle()
screen = Screen()

#
tom.pensize(width=5)
#

with open("colors.txt", "r") as file:
    colors = [color.strip() for color in file if color.strip()]


def shaper(sides, color):
    angle = (360 / sides)
    tom.pencolor(color)
    for _ in range(sides):
        tom.forward(50)
        tom.right(angle)


#
for side in range(3, 5):
    shaper(side, choice(colors))

#
screen.exitonclick()
