import random
import turtle as t
from random import randint

tim = t.Turtle()
screen = t.Screen()
tim.shape("turtle")

edge = 3
screen.colormode(255)
# while edge < 11:
#     degre = 360 / edge
#     tim.color((random.randint(0, 255), randint(0, 255), randint(0, 255)))
#     for i in range(edge):
#         tim.forward(100)
#         tim.right(degre)
#     edge += 1

# other way
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(random.choice(colours))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for _ in range(3, 11):
    draw_shape(_)


screen.exitonclick()
