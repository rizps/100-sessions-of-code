import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(20)

screen.listen()
screen.onkey(key="space", fun=move_forwards)




screen.exitonclick()