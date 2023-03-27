import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing")
screen.tracer(0)

screen.listen()

player = Player()
cars = CarManager()
score = Scoreboard()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(cars.sleep_time)
    screen.update()
    if player.is_at_finish():
        player.goto_start()
        cars.increase_speed()
        score.plus_points()
    score.update_scoreboard()

    for car in cars.all_cars:
        if car.distance(player) < 15:
            score.game_over()
            game_is_on = False

    cars.add_cars()
    cars.move_car()






screen.exitonclick()
