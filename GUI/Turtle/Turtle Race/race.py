from random import choice
from turtle import Turtle, Screen

# Player
colors = ["red", "green", "blue", '''Yellow''']
for num in range(4):
    tom_variants = Turtle()
    tom_variants.shape("turtle")
    tom_variants.color(colors[num])

#
screen = Screen()

# Get user input
user_choice = screen.textinput("Turtle Race Game", "Which color turtle you will choose?:")
print(user_choice)

# Set color



#
screen.exitonclick()