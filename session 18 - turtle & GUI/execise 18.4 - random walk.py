import turtle as t
import random
from random import randint

tim = t.Turtle()
screen = t.Screen()
tim.shape("turtle")
tim.pensize(10)

directions = [0, 90, 180, 270]
screen.colormode(255)
# for _ in range(50):
#     tim.color((random.randint(0, 255), randint(0, 255), randint(0, 255)))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# other way
# making random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(50):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



screen.exitonclick()

