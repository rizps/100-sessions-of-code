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


# tim.shape("turtle")
tim.penup()
tim.speed(15)
y = 0

# for _ in range(100):
#     if _ % 10 == 0 and _ != 0:
#         y += 50
#         tim.goto(0, y)
#     tim.color(random_color())
#     tim.dot(30)
#     tim.forward(50)

# other way
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(num_of_dots):
    if dot_count % 10 == 0 and dot_count != 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    tim.dot(30)
    tim.color(random_color())
    tim.forward(50)


screen.exitonclick()