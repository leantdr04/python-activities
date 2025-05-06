from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
LEFT_SCORE_PLACEMENT = (100, 200)
RIGHT_SCORE_PLACEMENT = (-100, 200)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE_PLACEMENT)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_PLACEMENT)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def left_scored(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_scored(self):
        self.r_score += 1
        self.update_scoreboard()
