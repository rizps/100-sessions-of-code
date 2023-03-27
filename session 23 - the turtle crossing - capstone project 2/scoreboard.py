from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

# detect collision with food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def plus_points(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 250)
        self.write(f"Game Over", font=FONT)




