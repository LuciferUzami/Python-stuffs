from turtle import Turtle, Screen

#
tom = Turtle()
screen = Screen()
screen.listen()

#  functions
def forward():
    tom.forward(20)
def backward():
    tom.back(20)
def right():
    tom.setheading(tom.heading() - 10)
def left():
    tom.setheading(tom.heading() + 10)
def eraseAll():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


# Call the function
screen.onkeypress(forward, "Up")
screen.onkeypress(backward, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")
screen.onkey(eraseAll, "c")

#
screen.exitonclick()

