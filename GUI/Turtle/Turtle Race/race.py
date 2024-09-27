from turtle import Turtle, Screen
from random import randint

#
screen = Screen()
winner = ""
# Get user input
colors = ["red", "green", "blue", '''yellow''', "black", "pink"]
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
Y_axis = -60
for num in range(6):
    tom_variants = Turtle(shape="turtle")
    tom_variants.penup()
    tom_variants.color(colors[num])
    tom_variants.setposition(-300, Y_axis)
    Y_axis += 40
    players.append(tom_variants)

#  Player  Moves
while race_start:
    for player in players:
        player.forward(randint(0, 10))
        #       Winner
        if player.xcor() >= 320:
            winner = player.color()[0]
            race_start = False

if winner == user_choice:
    print("You Win")
else:
    print("You Loss")
    print(f"The winner is {winner}")

#
screen.exitonclick()
