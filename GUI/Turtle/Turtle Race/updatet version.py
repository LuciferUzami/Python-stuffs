from turtle import Turtle, Screen
from random import randint

# Set up the screen
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")

# Track setup
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
    track_turtle.goto(-250, 150 - (lane * 50))  # Move down to the next lane
track_turtle.hideturtle()

# Finish line
finish_line = Turtle()
finish_line.penup()
finish_line.goto(250, 150)
finish_line.right(90)
finish_line.pendown()
finish_line.pensize(3)
finish_line.forward(300)  # Drawing the finish line
finish_line.hideturtle()

# Winner variable
winner = ""

# Get user input
colors = ["red", "green", "blue", "yellow", "white", "pink"]
user_choice = screen.textinput("Turtle Race Game", "Which color turtle do you choose (red, green, blue, yellow, white, pink)?:").lower()

# Validate the user input
condition = True
race_start = False
while condition:
    if user_choice in colors:
        race_start = True
        condition = False
    else:
        user_choice = screen.textinput("ERROR", 'Please choose a valid color ("red", "green", "blue", "yellow", "white", "pink"):').lower()

# Set up players (turtles)
players = []
Y_axis = -80
for num in range(6):
    turtle_player = Turtle(shape="turtle")
    turtle_player.penup()
    turtle_player.color(colors[num])
    turtle_player.goto(-250, Y_axis)
    Y_axis += 50
    players.append(turtle_player)

# Player moves
while race_start:
    for player in players:
        player.forward(randint(0, 10))
        # Check for a winner
        if player.xcor() >= 250:  # Finish line
            winner = player.color()[0]
            race_start = False
            break

# Show result in a message box
if winner == user_choice:
    player_result = "You Win!"
else:
    player_result = "You Lost!"
    print(f"The winner is {winner} turtle.")

# Display the result on the screen
result_turtle = Turtle()
result_turtle.penup()
result_turtle.hideturtle()
result_turtle.color("white")
result_turtle.goto(0, 200)
result_turtle.write(f"The winner is the {winner} turtle! \n  {player_result}", align="center", font=("Arial", 16, "bold"))

# Keep the screen open
screen.exitonclick()
