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





