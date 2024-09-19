from turtle import Turtle, Screen
from mypackages import rgb

#
tom = Turtle()
screen = Screen()

# Set colormode
screen.colormode(255)

# Set speed and pensize
tom.speed(0)
tom.pensize(2)


# Draw Circle
def spiroGraph(gap_size):
    for _ in range(int(360 / gap_size)):
        color = rgb.colors()
        tom.pencolor(color)
        tom.circle(100)
        tom.setheading(tom.heading() + gap_size)


# Call function
spiroGraph(5)

#
screen.exitonclick()
