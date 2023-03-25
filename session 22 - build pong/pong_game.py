from turtle import Screen
from paddle import Paddle
from pong import Pong
import time
from pong_scoreboard import Scoreboard

# setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


pong = Pong()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()

    if pong.ycor() > 280 or pong.ycor() < -280 :
        pong.bounce_y()

    if pong.distance(l_paddle) < 40 and pong.xcor() < -320:
        pong.bounce_x()

    if pong.distance(r_paddle) < 40 and pong.xcor() > 320:
        pong.bounce_x()

    # detect R paddle miss
    if pong.xcor() > 380 :
        pong.reset_position()
        score.l_points()

    # detect L paddle miss
    if pong.xcor() < -380:
        pong.reset_position()
        score.r_points()


screen.exitonclick()

