from random import choice
from turtle import Turtle, Screen
from mypackages import rgb

# Assessing Object
tom = Turtle()
screen = Screen()
# Set color
screen.colormode(255)
screen.bgcolor("black")
# Pen Size
tom.pensize(width=10)

#  Angels
turn = [90, 180, -90, -180, 360, -360, ]

while True:
    tom.speed("fastest")
    tom.forward(30)
    tom.right(choice(turn))
    tom.pencolor(rgb.colors())
