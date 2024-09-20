from turtle import Turtle, Screen
from PIL import Image
import colorgram

#  Create the object for Turtle and Screen
tom = Turtle()
screen = Screen()

#  Reduce the image size for program better performance
image_path = "./Media/Images/hirstpainting.jpg"
with Image.open(image_path) as img:
    img = img.resize((800, 600))
    img.save("./Media/Images/resize_painting.jpg")

#  Get the color from image
img_colors = colorgram.extract("./Media/Images/resize_painting.jpg", 100)
colors = [ color.rgb for color in img_colors]

#  Tom position
starting_x = -300
starting_y = -250
tom.penup()
moveing = True
tom.setposition(starting_x, starting_y)
while moveing:
    if starting_x == 300:
        starting_y += 30
        tom.setposition(starting_x, starting_y)
    else:
        tom.pendown()
        tom.dot(20, "red")
        tom.penup()
        tom.forward(30)
        starting_x += 30


#  Screen out
screen.exitonclick()



