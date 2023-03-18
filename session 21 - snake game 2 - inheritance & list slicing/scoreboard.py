from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")

# detect collision with food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score_update()

    def score_calc(self):
        self.score += 1
        self.clear()
        self.score_update()

    def score_update(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)