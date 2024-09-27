from turtle import Turtle, Screen
from random import randint

#
screen = Screen()
screen.setup(width=600, height=500)

# Set Window Black
screen.bgcolor("black")

# Track
track_turtle = Turtle()
track_turtle.pencolor("white")
track_turtle.speed(0)
track_turtle.penup()
track_turtle.goto(-250, 150)

# Draw 6 lanes for 6 turtles
for lane in range(7):
    track_turtle.pendown()
    track_turtle.forward(500)  # Length of the track
    track_turtle.penup()
    track_turtle.goto(-250, 150 - (lane * 50))  # Move down to next lane
track_turtle.hideturtle()

# Winner Empty var
winner = ""

# Get user input
colors = ["red", "green", "blue", '''yellow''', "white", "pink"]
user_choice = screen.textinput("Turtle Race Game", "Which color turtle you will choose?:")

#  condition
condition = True
race_start = False
while condition:
    if user_choice in colors:
        race_start = True
        condition = False
    else:
        user_choice = screen.textinput("ERROR",
                                       'Give only give colors ("red", "green", "blue", ''yellow'', "black", "pink"):')

# Player
players = []
Y_axis = -80
for num in range(6):
    tom_variants = Turtle(shape="turtle")
    tom_variants.penup()
    tom_variants.color(colors[num])
    tom_variants.goto(-250, Y_axis)
    Y_axis += 50
    players.append(tom_variants)

#  Player  Moves
while race_start:
    for player in players:
        player.forward(randint(0, 10))
        #       Winner
        if player.xcor() >= 260:
            winner = player.color()[0]
            race_start = False

if winner == user_choice:
    print("You Win")
else:
    print("You Loss")
    print(f"The winner is {winner}")

#
screen.exitonclick()
