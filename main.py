import turtle as t
import random

tim = t.Turtle()

#from https://trinket.io/docs/colors
colors = ["skyblue", "cadetblue", "lightskyblue", "lightseagreen", "steelblue", "mediumturquoise", "azure", "pink",
          "palevioletred", "rosybrown", "mistyrose", "DarkSeaGreen", "MediumSeaGreen", "MediumAquamarine", "PowderBlue","Lavender"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)
