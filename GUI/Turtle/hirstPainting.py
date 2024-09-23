from turtle import Turtle, Screen
from random import choice
from PIL import Image
import colorgram

#  Create the object for Turtle and Screen
tom = Turtle()
screen = Screen()

# Set colormode
screen.colormode(255)

#  Reduce the image size for program better performance
image_path = "./Media/Images/hirstpainting.jpg"
with Image.open(image_path) as img:
    img = img.resize((800, 600))
    img.save("./Media/Images/resize_painting.jpg")

#  Get the color from image
img_colors = colorgram.extract("./Media/Images/resize_painting.jpg", 50)
colors = [color.rgb for color in img_colors]


# For color function
def getColor():
    random_color = choice(colors)
    return random_color.r, random_color.g, random_color.b


# Constant value
starting_x = -300


# Function for painting
def hirstPainting(y_axis):
    tom.penup()
    tom.setposition(starting_x, y_axis)
    for x in range(-300, 301, 40):
        tom.pendown()
        tom.dot(30, getColor())
        tom.penup()
        tom.forward(40)


#
for y_ax in range(-250, 281, 40):
    hirstPainting(y_axis=y_ax)

#  Screen out
screen.exitonclick()
