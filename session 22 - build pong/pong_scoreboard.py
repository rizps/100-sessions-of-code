from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")

# detect collision with food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"score: {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"score: {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()

