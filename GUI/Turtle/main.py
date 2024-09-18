from turtle import Turtle, Screen
print()
# Create Turtle object
tom = Turtle()
# Create Screen object
screen = Screen()
# Change Shape
tom.shape("turtle")
# Draw square
for _ in range(12):
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen.exitonclick()
