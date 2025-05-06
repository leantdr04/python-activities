from turtle import Turtle

SCORE_PLACEMENT = (-280, 260)
ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(SCORE_PLACEMENT)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=20)
        self.write("GAME OVER", align="center", font= FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

