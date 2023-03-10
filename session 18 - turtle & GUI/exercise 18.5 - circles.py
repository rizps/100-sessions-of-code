import turtle as t
import random


tim = t.Turtle()
screen = t.Screen()
def random_color():
    t.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.shape("turtle")
tim.shapesize(5)
tim.speed(10.5)
tim.pensize(5)

def draw_spiro(total_circle):
    for _ in range(total_circle):
        tim.color(random_color())
        tim.circle(200)
        tim.left(int(360/total_circle))
# draw_spiro(5)


# other way
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)


screen.exitonclick()