from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")

# detect collision with food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("last_highscore.txt") as lhs:
            self.high_score = int(lhs.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"score: {self.score}, high score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.score_update()

    def score_calc(self):
        self.score += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"score: {self.score}, high score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("last_highscore.txt", mode='w') as highscore:
                highscore.write(str(self.high_score))
        self.score = 0
        self.score_update()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)