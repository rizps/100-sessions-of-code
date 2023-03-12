import random
import turtle as t


screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
is_race_on = False

for turtle_index in range (6):
    new_tim = t.Turtle(shape= "turtle")
    new_tim.color(colors[turtle_index])
    new_tim.penup()
    new_tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win, the winner is {winning_color}")
            else:
                print(f"you lost, the winner is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()